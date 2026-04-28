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
    "setup_timestamp",
    "detected_at",
    "entry_time",
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
    "activated_trade",
    "invalidated_before_entry",
    "session_window",
    "ny_time",
    "swept_level",
    "sweep_extreme",
    "sweep_liquidity_quality",
    "sweep_level_age_bars",
    "turtle_quality",
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
    "retest_time",
    "target_distance_r",
    "time_to_entry_bars",
    "bars_to_invalidation",
    "bars_to_1r",
    "bars_to_2r",
    "metadata_json",
    "mfe_r",
    "mae_r",
    "invalidated",
    "target_hit",
    "target_before_invalidation",
    "hit_1r_before_invalidation",
    "hit_2r_before_invalidation",
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
    parser.add_argument("--turtle-soup-min-wick-fraction", type=float, default=None)
    parser.add_argument("--turtle-soup-min-wick-atr-ratio", type=float, default=None)
    parser.add_argument("--turtle-soup-min-close-back-fraction", type=float, default=None)
    parser.add_argument("--turtle-soup-min-level-age-bars", type=int, default=None)
    parser.add_argument("--turtle-soup-max-confirmation-bars", type=int, default=None)
    parser.add_argument("--turtle-soup-require-killzone", action="store_true")
    parser.add_argument("--turtle-soup-require-smt", action="store_true")
    parser.add_argument("--silver-bullet-windows", default=None, help="Comma-separated NY windows, e.g. 10:00-11:00,14:00-15:00.")
    parser.add_argument("--silver-bullet-retest-must-occur-within-window", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--silver-bullet-max-retest-bars", type=int, default=None)
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
    if args.turtle_soup_min_level_age_bars is not None:
        config["turtle_min_swing_age"] = args.turtle_soup_min_level_age_bars
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
                    event_idx = _index_at_or_before(candles, setup.timestamp)
                    if event_idx is None:
                        continue
                    event_window = candles[event_idx + 1 : event_idx + 1 + args.forward_bars]
                    rows.append(_event_row(setup, spec.name, spec.model_family, args.same_bar_policy, event_window, detected_at=ts))
    return rows


def _context_aligned(setup: EntrySetup, context: object | None) -> bool:
    htf = getattr(context, "htf_context", None)
    if htf is None:
        return False
    return (setup.direction == "long" and htf.allows_long) or (setup.direction == "short" and htf.allows_short)


def _index_at_or_before(candles: list[Candle], timestamp: int) -> int | None:
    match = None
    for idx, candle in enumerate(candles):
        if int(candle["time"]) <= timestamp:
            match = idx
        else:
            break
    return match


def _event_row(setup: EntrySetup, model_name: str, model_family: str, same_bar_policy: str, future: list[Candle], *, detected_at: int | None = None) -> dict[str, Any]:
    metadata = dict(setup.metadata)
    entry = setup.entry_price if setup.entry_price is not None else (setup.entry_low + setup.entry_high) / 2
    stop = setup.stop_loss if setup.stop_loss is not None else setup.invalidation
    risk = abs(entry - stop) if stop is not None else None
    entry_time = int(metadata.get("entry_time") or setup.timestamp)
    outcome = _evaluate(setup.direction, entry, stop, setup.target_hint, future, same_bar_policy, entry_time=entry_time)
    target_distance_r = abs(setup.target_hint - entry) / risk if setup.target_hint is not None and risk and risk > 0 else None
    row = {
        "model": model_name,
        "model_family": model_family,
        "direction": setup.direction,
        "symbol": setup.symbol,
        "timeframe": setup.timeframe,
        "timestamp": setup.timestamp,
        "setup_timestamp": setup.timestamp,
        "detected_at": detected_at,
        "entry_time": entry_time,
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
        "invalidated_before_entry": outcome["invalidated_before_entry"],
        "target_distance_r": target_distance_r,
        "time_to_entry_bars": outcome["time_to_entry_bars"],
        "metadata_json": json.dumps(metadata, ensure_ascii=True, sort_keys=True, default=str),
        **{field: metadata.get(field) for field in EVENT_FIELDS if field not in {"model", "model_family", "direction", "symbol", "timeframe", "timestamp", "setup_timestamp", "detected_at", "entry_time", "entry_mode", "stop_mode", "target_mode", "entry_price", "entry_low", "entry_high", "stop_loss", "invalidation", "target_hint", "risk", "risk_bps", "same_bar_policy", "same_bar_ambiguous", "invalidated_before_entry", "target_distance_r", "time_to_entry_bars", "bars_to_invalidation", "bars_to_1r", "bars_to_2r", "metadata_json", "mfe_r", "mae_r", "invalidated", "target_hit", "target_before_invalidation", "hit_1r_before_invalidation", "hit_2r_before_invalidation"}},
        **outcome,
    }
    return row


def _empty_outcome() -> dict[str, Any]:
    return {
        "mfe_r": None,
        "mae_r": None,
        "invalidated": False,
        "target_hit": False,
        "target_before_invalidation": False,
        "hit_1r_before_invalidation": False,
        "hit_2r_before_invalidation": False,
        "same_bar_ambiguous": False,
        "invalidated_before_entry": False,
        "activated_trade": False,
        "time_to_entry_bars": None,
        "bars_to_invalidation": None,
        "bars_to_1r": None,
        "bars_to_2r": None,
    }


def _evaluate(direction: str, entry: float, stop: float | None, target: float | None, future: list[Candle], policy: str, entry_time: int | None = None) -> dict[str, Any]:
    if stop is None or target is None:
        return _empty_outcome()
    risk = abs(entry - stop)
    if risk <= 0:
        return _empty_outcome()
    entry_time = int(entry_time or (future[0]["time"] if future else 0))
    invalidated_before_entry = any(_stop_hit(direction, candle, stop) for candle in future if int(candle["time"]) < entry_time)
    active = [candle for candle in future if int(candle["time"]) >= entry_time]
    if invalidated_before_entry or not active:
        outcome = _empty_outcome()
        outcome["invalidated_before_entry"] = invalidated_before_entry
        outcome["time_to_entry_bars"] = _bars_until_or_none(future, entry_time)
        return outcome
    highs = [float(c["high"]) for c in active]
    lows = [float(c["low"]) for c in active]
    if direction == "long":
        mfe = max([0.0] + [high - entry for high in highs])
        mae = max([0.0] + [entry - low for low in lows])
    else:
        mfe = max([0.0] + [entry - low for low in lows])
        mae = max([0.0] + [high - entry for high in highs])
    invalidated = False
    target_hit = False
    target_before = False
    hit_1r = False
    hit_2r = False
    bars_to_1r = None
    bars_to_2r = None
    bars_to_invalidation = None
    ambiguous = False
    target_1r = entry + risk if direction == "long" else entry - risk
    target_2r = entry + risk * 2 if direction == "long" else entry - risk * 2
    for offset, candle in enumerate(active, start=1):
        stop_hit = _stop_hit(direction, candle, stop)
        target_reached = _target_hit(direction, candle, target)
        hit_1r_now = _target_hit(direction, candle, target_1r)
        hit_2r_now = _target_hit(direction, candle, target_2r)
        any_target = target_reached or hit_1r_now or hit_2r_now
        if stop_hit and any_target:
            ambiguous = True
            if policy == "optimistic":
                target_hit = True
                target_before = True
                hit_1r = hit_1r or hit_1r_now
                hit_2r = hit_2r or hit_2r_now
                bars_to_1r = bars_to_1r or (offset if hit_1r_now else None)
                bars_to_2r = bars_to_2r or (offset if hit_2r_now else None)
                break
            invalidated = True
            bars_to_invalidation = offset
            if policy == "neutral":
                target_hit = True
                target_before = False
            break
        if hit_1r_now and bars_to_1r is None:
            hit_1r = True
            bars_to_1r = offset
        if hit_2r_now and bars_to_2r is None:
            hit_2r = True
            bars_to_2r = offset
        if target_reached:
            target_hit = True
            target_before = True
            break
        if stop_hit:
            invalidated = True
            bars_to_invalidation = offset
            break
    return {
        "mfe_r": mfe / risk,
        "mae_r": mae / risk,
        "invalidated": invalidated,
        "target_hit": target_hit,
        "target_before_invalidation": target_before,
        "hit_1r_before_invalidation": hit_1r,
        "hit_2r_before_invalidation": hit_2r,
        "same_bar_ambiguous": ambiguous if policy == "neutral" else False,
        "invalidated_before_entry": invalidated_before_entry,
        "activated_trade": True,
        "time_to_entry_bars": _bars_until_or_none(future, entry_time),
        "bars_to_invalidation": bars_to_invalidation,
        "bars_to_1r": bars_to_1r,
        "bars_to_2r": bars_to_2r,
    }


def _stop_hit(direction: str, candle: Candle, stop: float) -> bool:
    return float(candle["low"]) <= stop if direction == "long" else float(candle["high"]) >= stop


def _target_hit(direction: str, candle: Candle, target: float) -> bool:
    return float(candle["high"]) >= target if direction == "long" else float(candle["low"]) <= target


def _bars_until_or_none(candles: list[Candle], timestamp: int) -> int | None:
    for idx, candle in enumerate(candles, start=1):
        if int(candle["time"]) >= timestamp:
            return idx
    return None


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
        "summary_by_turtle_quality": ("model", "turtle_quality"),
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
                "total_setups": len(group),
                "activated_trades": sum(1 for e in group if e.get("activated_trade")),
                "invalidated_before_entry": sum(1 for e in group if e.get("invalidated_before_entry")),
                "avg_mfe_r": round(sum(mfes) / len(mfes), 6) if mfes else None,
                "median_mfe_r": round(float(median(mfes)), 6) if mfes else None,
                "win_rate": round(sum(1 for e in group if e.get("target_before_invalidation")) / len(group), 6) if group else None,
                "avg_rr": _avg_field(group, "target_distance_r"),
                "expectancy": _expectancy(group),
                "target_before_invalidation_rate": round(sum(1 for e in group if e.get("target_before_invalidation")) / len(group), 6) if group else None,
                "hit_1r_before_invalidation_rate": round(sum(1 for e in group if e.get("hit_1r_before_invalidation")) / len(group), 6) if group else None,
                "hit_2r_before_invalidation_rate": round(sum(1 for e in group if e.get("hit_2r_before_invalidation")) / len(group), 6) if group else None,
                "invalidation_rate": round(sum(1 for e in group if e.get("invalidated")) / len(group), 6) if group else None,
                "avg_time_to_entry": _avg_field(group, "time_to_entry_bars"),
                "avg_time_to_invalidation": _avg_field(group, "bars_to_invalidation"),
                "avg_time_to_1r": _avg_field(group, "bars_to_1r"),
                "avg_time_to_2r": _avg_field(group, "bars_to_2r"),
                "same_bar_ambiguous_count": sum(1 for e in group if e.get("same_bar_ambiguous")),
            }
        )
        rows.append(row)
    return rows


def _avg_field(group: list[dict[str, Any]], field: str) -> float | None:
    values = [float(item[field]) for item in group if item.get(field) is not None]
    return round(sum(values) / len(values), 6) if values else None


def _expectancy(group: list[dict[str, Any]]) -> float | None:
    outcomes = []
    for event in group:
        if event.get("invalidated_before_entry"):
            continue
        if event.get("target_before_invalidation") and event.get("target_distance_r") is not None:
            outcomes.append(float(event["target_distance_r"]))
        elif event.get("invalidated"):
            outcomes.append(-1.0)
        elif event.get("mfe_r") is not None:
            outcomes.append(float(event["mfe_r"]))
    return round(sum(outcomes) / len(outcomes), 6) if outcomes else None


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
        "- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.",
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
