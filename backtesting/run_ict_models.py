from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

from backtesting import Candle
from backtesting.accumulator import ReplaySnapshotCache
from backtesting.context import build_accumulated_strategy_context_for_replay
from backtesting.data import HistoricalDataError, load_history_for
from strategies.ict_models.registry import (
    ACTIVE_ICT_MODELS,
    LEGACY_MODELS,
    RESEARCH_ONLY_MODELS,
    resolve_models,
)
from strategies.types import EntrySetup
from timeframes import SUPPORTED_TIMEFRAMES, execution_htf_for

EVENT_FIELDS = [
    "model",
    "model_family",
    "direction",
    "symbol",
    "timeframe",
    "timestamp",
    "entry_mode",
    "stop_mode",
    "target_mode",
    "entry_price",
    "entry_low",
    "entry_high",
    "stop_loss",
    "invalidation",
    "target_hint",
    "risk",
    "risk_bps",
    "same_bar_policy",
    "same_bar_ambiguous",
    "session_window",
    "ny_time",
    "swept_level",
    "sweep_extreme",
    "fvg_low",
    "fvg_high",
    "fvg_ce",
    "ifvg_low",
    "ifvg_high",
    "ifvg_ce",
    "ob_low",
    "ob_high",
    "breaker_low",
    "breaker_high",
    "time_to_retest_bars",
    "target_distance_r",
    "metadata_json",
    "mfe_r",
    "mae_r",
    "invalidated",
    "target_hit",
    "target_before_invalidation",
]


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        models = resolve_models(args.models, include_legacy=args.include_legacy)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 2
    try:
        store = _load_store(Path(args.data_dir), args.symbols, args.timeframes, args.context_mode)
    except HistoricalDataError as exc:
        print(f"Error: {exc}")
        return 2

    events: list[dict[str, Any]] = []
    for symbol in args.symbols:
        events.extend(_run_symbol(symbol, args.timeframes, models, store, args))
    summaries = _summaries(events)
    _write_outputs(Path(args.out_dir), events, summaries, vars(args), [m.name for m in models])
    print(f"Backtest complete: events={len(events)} out_dir={args.out_dir}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline event-study backtest for new ICT models.")
    parser.add_argument("--data-dir", default="data/history")
    parser.add_argument("--symbols", nargs="+", required=True)
    parser.add_argument("--timeframes", nargs="+", required=True, choices=SUPPORTED_TIMEFRAMES)
    parser.add_argument("--models", nargs="+", choices=sorted(set(ACTIVE_ICT_MODELS) | set(RESEARCH_ONLY_MODELS) | set(LEGACY_MODELS) | {"model1", "model2", "model3"}), default=None)
    parser.add_argument("--include-legacy", action="store_true")
    parser.add_argument("--entry-mode", choices=["edge", "midpoint", "ce", "close", "retest"], default=None)
    parser.add_argument("--stop-mode", choices=["aggressive", "standard", "structural", "ce", "opposite_boundary", "mean_threshold", "block_extreme"], default=None)
    parser.add_argument("--target-mode", choices=["nearest_liquidity", "opposite_range", "fixed_r"], default=None)
    parser.add_argument("--same-bar-policy", choices=["conservative", "neutral", "optimistic"], default="conservative")
    parser.add_argument("--context-mode", choices=["off", "aligned_only", "strict"], default="off")
    parser.add_argument("--forward-bars", type=int, default=20)
    parser.add_argument("--warmup-bars", type=int, default=100)
    parser.add_argument("--out-dir", default="backtest_results/new_ict_models")
    return parser


def _load_store(data_dir: Path, symbols: list[str], timeframes: list[str], context_mode: str) -> dict[tuple[str, str], list[Candle]]:
    store: dict[tuple[str, str], list[Candle]] = {}
    required = {(symbol, tf) for symbol in symbols for tf in timeframes}
    optional = set()
    if context_mode != "off":
        optional = {(symbol, execution_htf_for(tf)) for symbol in symbols for tf in timeframes if execution_htf_for(tf)}
    for symbol, tf in sorted(required | optional):
        store[(symbol, tf)] = load_history_for(data_dir, symbol, tf, required=(symbol, tf) in required) or []
    return store


def _run_symbol(symbol: str, timeframes: list[str], models: list[Any], store: dict[tuple[str, str], list[Candle]], args: argparse.Namespace) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cache = ReplaySnapshotCache(store)
    config = {k: v for k, v in vars(args).items() if v is not None}
    seen: set[tuple[Any, ...]] = set()
    for timeframe in timeframes:
        candles = store.get((symbol, timeframe), [])
        for idx in range(max(args.warmup_bars, 0), len(candles)):
            ts = int(candles[idx]["time"])
            visible = candles[: idx + 1]
            context = None
            if args.context_mode != "off":
                context = build_accumulated_strategy_context_for_replay(
                    symbol=symbol,
                    timeframe=timeframe,
                    current_timestamp=ts,
                    snapshot_cache=cache,
                    htf_mode="strict" if args.context_mode == "strict" else "soft",
                )
            for spec in models:
                setups = spec.detector(symbol, timeframe, visible, context, config)
                for setup in setups:
                    if args.context_mode == "aligned_only" and not _context_aligned(setup, context):
                        continue
                    key = (spec.name, symbol, timeframe, setup.direction, setup.timestamp, round(setup.entry_low, 8), round(setup.entry_high, 8))
                    if key in seen:
                        continue
                    seen.add(key)
                    future = candles[idx + 1 : idx + 1 + args.forward_bars]
                    rows.append(_event_row(setup, spec.name, spec.model_family, args.same_bar_policy, future))
    return rows


def _context_aligned(setup: EntrySetup, context: object | None) -> bool:
    htf = getattr(context, "htf_context", None)
    if htf is None:
        return False
    return (setup.direction == "long" and htf.allows_long) or (setup.direction == "short" and htf.allows_short)


def _event_row(setup: EntrySetup, model_name: str, model_family: str, same_bar_policy: str, future: list[Candle]) -> dict[str, Any]:
    metadata = dict(setup.metadata)
    entry = setup.entry_price if setup.entry_price is not None else (setup.entry_low + setup.entry_high) / 2
    stop = setup.stop_loss if setup.stop_loss is not None else setup.invalidation
    risk = abs(entry - stop) if stop is not None else None
    outcome = _evaluate(setup.direction, entry, stop, setup.target_hint, future, same_bar_policy)
    target_distance_r = abs(setup.target_hint - entry) / risk if setup.target_hint is not None and risk and risk > 0 else None
    row = {
        "model": model_name,
        "model_family": model_family,
        "direction": setup.direction,
        "symbol": setup.symbol,
        "timeframe": setup.timeframe,
        "timestamp": setup.timestamp,
        "entry_mode": metadata.get("entry_mode"),
        "stop_mode": metadata.get("stop_mode"),
        "target_mode": metadata.get("target_mode"),
        "entry_price": entry,
        "entry_low": setup.entry_low,
        "entry_high": setup.entry_high,
        "stop_loss": stop,
        "invalidation": setup.invalidation,
        "target_hint": setup.target_hint,
        "risk": risk,
        "risk_bps": metadata.get("risk_bps") or (risk / max(entry, 1e-9) * 10_000 if risk else None),
        "same_bar_policy": same_bar_policy,
        "same_bar_ambiguous": outcome["same_bar_ambiguous"],
        "target_distance_r": target_distance_r,
        "metadata_json": json.dumps(metadata, ensure_ascii=True, sort_keys=True, default=str),
        **{field: metadata.get(field) for field in EVENT_FIELDS if field not in {"model", "model_family", "direction", "symbol", "timeframe", "timestamp", "entry_mode", "stop_mode", "target_mode", "entry_price", "entry_low", "entry_high", "stop_loss", "invalidation", "target_hint", "risk", "risk_bps", "same_bar_policy", "same_bar_ambiguous", "target_distance_r", "metadata_json", "mfe_r", "mae_r", "invalidated", "target_hit", "target_before_invalidation"}},
        **outcome,
    }
    return row


def _evaluate(direction: str, entry: float, stop: float | None, target: float | None, future: list[Candle], policy: str) -> dict[str, Any]:
    if stop is None or target is None:
        return {"mfe_r": None, "mae_r": None, "invalidated": False, "target_hit": False, "target_before_invalidation": False, "same_bar_ambiguous": False}
    risk = abs(entry - stop)
    if risk <= 0:
        return {"mfe_r": None, "mae_r": None, "invalidated": False, "target_hit": False, "target_before_invalidation": False, "same_bar_ambiguous": False}
    highs = [float(c["high"]) for c in future]
    lows = [float(c["low"]) for c in future]
    if direction == "long":
        mfe = max([0.0] + [high - entry for high in highs])
        mae = max([0.0] + [entry - low for low in lows])
    else:
        mfe = max([0.0] + [entry - low for low in lows])
        mae = max([0.0] + [high - entry for high in highs])
    invalidated = False
    target_hit = False
    target_before = False
    ambiguous = False
    for candle in future:
        stop_hit = float(candle["low"]) <= stop if direction == "long" else float(candle["high"]) >= stop
        target_reached = float(candle["high"]) >= target if direction == "long" else float(candle["low"]) <= target
        if stop_hit and target_reached:
            ambiguous = True
            if policy == "optimistic":
                target_hit = True
                target_before = True
                break
            invalidated = True
            if policy == "neutral":
                target_hit = True
                target_before = False
            break
        if target_reached:
            target_hit = True
            target_before = True
            break
        if stop_hit:
            invalidated = True
            break
    return {
        "mfe_r": mfe / risk,
        "mae_r": mae / risk,
        "invalidated": invalidated,
        "target_hit": target_hit,
        "target_before_invalidation": target_before,
        "same_bar_ambiguous": ambiguous if policy == "neutral" else False,
    }


def _summaries(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    specs = {
        "summary_by_model": ("model",),
        "summary_by_direction": ("model", "direction"),
        "summary_by_timeframe": ("model", "timeframe"),
        "summary_by_entry_mode": ("model", "entry_mode"),
        "summary_by_stop_mode": ("model", "stop_mode"),
        "summary_by_target_mode": ("model", "target_mode"),
        "summary_by_session_window": ("model", "session_window"),
        "summary_by_same_bar_policy": ("model", "same_bar_policy"),
        "summary_by_model_family": ("model_family",),
    }
    return {name: _group(events, fields) for name, fields in specs.items()}


def _group(events: list[dict[str, Any]], fields: tuple[str, ...]) -> list[dict[str, Any]]:
    buckets: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[tuple(event.get(field) or "none" for field in fields)].append(event)
    rows = []
    for key, group in sorted(buckets.items(), key=lambda item: tuple(str(v) for v in item[0])):
        mfes = [float(e["mfe_r"]) for e in group if e.get("mfe_r") is not None]
        row = {field: value for field, value in zip(fields, key)}
        row.update(
            {
                "count": len(group),
                "avg_mfe_r": round(sum(mfes) / len(mfes), 6) if mfes else None,
                "median_mfe_r": round(float(median(mfes)), 6) if mfes else None,
                "target_before_invalidation_rate": round(sum(1 for e in group if e.get("target_before_invalidation")) / len(group), 6) if group else None,
                "invalidation_rate": round(sum(1 for e in group if e.get("invalidated")) / len(group), 6) if group else None,
                "same_bar_ambiguous_count": sum(1 for e in group if e.get("same_bar_ambiguous")),
            }
        )
        rows.append(row)
    return rows


def _write_outputs(out_dir: Path, events: list[dict[str, Any]], summaries: dict[str, list[dict[str, Any]]], config: dict[str, Any], models: list[str]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "events.csv", events, EVENT_FIELDS)
    for name, rows in summaries.items():
        fields = list(rows[0]) if rows else []
        _write_csv(out_dir / f"{name}.csv", rows, fields)
    _write_report(out_dir / "report.md", events, summaries, config, models)


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fieldnames})


def _write_report(path: Path, events: list[dict[str, Any]], summaries: dict[str, list[dict[str, Any]]], config: dict[str, Any], models: list[str]) -> None:
    lines = [
        "# New ICT Models Backtest Report",
        "",
        "Event-study only. No profitability claim.",
        "",
        "## Migration Summary",
        "- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.",
        "- Old models are disabled by default.",
        "- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.",
        "",
        "## Backtest Config",
        f"- models: {', '.join(models)}",
        f"- symbols: {', '.join(config.get('symbols') or [])}",
        f"- timeframes: {', '.join(config.get('timeframes') or [])}",
        f"- same_bar_policy: {config.get('same_bar_policy')}",
        f"- context_mode: {config.get('context_mode')}",
        f"- forward_bars: {config.get('forward_bars')}",
        "",
        "## Overall Comparison",
        _markdown_table(summaries.get("summary_by_model", [])),
        "",
        "## Entry Mode Analysis",
        _markdown_table(summaries.get("summary_by_entry_mode", [])),
        "",
        "## Stop Mode Analysis",
        _markdown_table(summaries.get("summary_by_stop_mode", [])),
        "",
        "## Same-Bar Conservative Impact",
        _markdown_table(summaries.get("summary_by_same_bar_policy", [])),
        "",
        "## Model Family",
        _markdown_table(summaries.get("summary_by_model_family", [])),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    headers = list(rows[0])
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows[:20]:
        lines.append("| " + " | ".join(str(row.get(header) or "") for header in headers) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
