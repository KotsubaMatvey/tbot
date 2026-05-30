from __future__ import annotations

import argparse
import csv
import json
from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

from backtesting import Candle
from backtesting.accumulator import ReplaySnapshotCache
from backtesting.context import build_accumulated_strategy_context_for_replay
from backtesting.data import HistoricalDataError, load_funding_for, load_history_for
from market_primitives.smt import detect_smt
from strategies.ict_models.sessions import in_ny_windows
from strategies.ict_models.registry import (
    ACTIVE_ICT_MODELS,
    DEFAULT_MODELS,
    LEGACY_MODELS,
    RESEARCH_ONLY_MODELS,
    resolve_models,
)
from strategies.pre_model_filter import evaluate_pre_model_filter, merge_pre_model_metadata, setup_passes_pre_model_filter
from strategies.types import EntrySetup
from timeframes import SUPPORTED_TIMEFRAMES, execution_htf_for

DEFAULT_DATA_DIR = "data/history_2025-05-01_2025-10-31"
DETECTOR_CANDLE_WINDOW = 1500

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
    "exit_time",
    "entry_mode",
    "stop_mode",
    "stop_model",
    "target_mode",
    "target_model",
    "dol_priority",
    "dol_target_type",
    "dol_source",
    "entry_price",
    "entry_low",
    "entry_high",
    "stop_loss",
    "invalidation",
    "target_hint",
    "tp1_price",
    "tp2_price",
    "final_target",
    "rr_to_target",
    "logical_invalidation_model",
    "logical_invalidation_price",
    "partial_close_fraction",
    "be_trigger_r",
    "moved_to_be",
    "tp1_time",
    "exit_reason",
    "risk",
    "risk_bps",
    "commission_bps",
    "slippage_bps",
    "round_trip_cost_bps",
    "commission_points",
    "slippage_points",
    "round_trip_cost_points",
    "execution_cost_r",
    "funding_rows",
    "funding_rate_sum",
    "funding_cost_r",
    "funding_notional_price_mode",
    "total_cost_r",
    "gross_managed_outcome_r",
    "net_managed_outcome_r",
    "same_bar_policy",
    "same_bar_ambiguous",
    "activated_trade",
    "invalidated_before_entry",
    "target_reached_before_entry",
    "session_window",
    "session_date",
    "session_label",
    "session_type",
    "ny_time",
    "htf_mode",
    "htf_bias",
    "htf_location",
    "htf_zone_type",
    "htf_objective_type",
    "htf_objective_level",
    "htf_draw_direction",
    "htf_objective_unreached",
    "htf_context_alignment",
    "bias_alignment",
    "htf_score_modifier",
    "pd_array_type",
    "pd_array_age_bars",
    "p_d_value",
    "is_in_p_d",
    "has_smt_confirmation",
    "smt_detected",
    "smt_direction",
    "smt_pair",
    "smt_strength",
    "smt_timestamp",
    "decision_score",
    "score_bucket",
    "htf_alignment_score",
    "draw_score",
    "pd_location_score",
    "poi_score",
    "displacement_score",
    "smt_score",
    "killzone_score",
    "target_rr_score",
    "no_trade_reasons",
    "pre_model_filter_pass",
    "pre_model_allowed_directions",
    "pre_model_reasons",
    "htf_inside_poi",
    "htf_approaching_poi",
    "swept_level",
    "sweep_extreme",
    "sweep_liquidity_quality",
    "sweep_level_age_bars",
    "range_source",
    "asian_range_window",
    "asian_range_tz",
    "asian_range_date",
    "asian_range_start",
    "asian_range_end",
    "asian_range_high",
    "asian_range_low",
    "asian_range_width_bps",
    "asian_sweep_breach_bps",
    "asian_first_signal_only",
    "displacement_grade",
    "displacement_factor",
    "body_ratio",
    "range_expansion",
    "breach_displacement_grade",
    "turtle_quality",
    "turtle_soup_min_stop_applied",
    "turtle_soup_min_stop_bps",
    "asian_failed_sweep_count_before_reclaim",
    "asian_reject_prior_failed_sweep",
    "time_to_confirmation_bars",
    "ltf_trigger_type",
    "fvg_low",
    "fvg_high",
    "fvg_ce",
    "fvg_fill_depth",
    "ifvg_low",
    "ifvg_high",
    "ifvg_ce",
    "ifvg_fill_depth",
    "ifvg_min_retest_depth",
    "source_fvg_age_bars",
    "source_fvg_touches_before_inversion",
    "silver_bullet_min_retest_depth",
    "ob_low",
    "ob_high",
    "breaker_low",
    "breaker_high",
    "poi_retest_count",
    "trigger_to_retest_bars",
    "rejection_body_level",
    "rejection_wick_extreme",
    "current_wick_extreme",
    "rejection_zone_low",
    "rejection_zone_high",
    "rejection_body_sweep_bps",
    "rejection_min_wick_fraction",
    "body_liquidity_sweep",
    "mitigation_low",
    "mitigation_high",
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
    "invalidated_at",
    "target_hit",
    "tp1_hit",
    "tp2_hit",
    "final_target_hit",
    "logical_invalidated",
    "tp1_r",
    "managed_outcome_r",
    "managed_exit_reason",
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
        store = _load_store(Path(args.data_dir), args.symbols, args.timeframes, args.context_mode, args.smt_pairs)
        funding_store = _load_funding_store(Path(args.funding_data_dir), args.symbols) if args.funding_data_dir else {}
    except HistoricalDataError as exc:
        print(f"Error: {exc}")
        return 2

    events: list[dict[str, Any]] = []
    for symbol in args.symbols:
        events.extend(_run_symbol(symbol, args.timeframes, models, store, funding_store, args))
    summaries = _summaries(events)
    _write_outputs(Path(args.out_dir), events, summaries, vars(args), [m.name for m in models])
    print(f"Backtest complete: events={len(events)} out_dir={args.out_dir}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline event-study backtest for new ICT models.")
    parser.add_argument("--data-dir", default=DEFAULT_DATA_DIR)
    parser.add_argument("--symbols", nargs="+", required=True)
    parser.add_argument("--timeframes", nargs="+", required=True, choices=SUPPORTED_TIMEFRAMES)
    parser.add_argument("--models", nargs="+", choices=sorted(set(ACTIVE_ICT_MODELS) | set(RESEARCH_ONLY_MODELS) | set(LEGACY_MODELS) | {"model1", "model2", "model3"}), default=None)
    parser.add_argument("--include-legacy", action="store_true")
    parser.add_argument("--entry-mode", choices=["edge", "midpoint", "ce", "close", "retest"], default=None)
    parser.add_argument("--stop-mode", choices=["aggressive", "standard", "structural", "ce", "opposite_boundary", "mean_threshold", "block_extreme"], default=None)
    parser.add_argument("--target-mode", choices=["nearest_liquidity", "opposite_range", "fixed_r", "dol_hierarchy"], default=None)
    parser.add_argument("--same-bar-policy", choices=["conservative", "neutral", "optimistic"], default="conservative")
    parser.add_argument("--start-date", default=None, help="YYYY-MM-DD inclusive UTC date to start scanning.")
    parser.add_argument("--end-date", default=None, help="YYYY-MM-DD inclusive UTC date to stop scanning.")
    parser.add_argument("--tp1-r", type=float, default=1.0)
    parser.add_argument("--partial-close-fraction", type=float, default=0.5)
    parser.add_argument("--move-to-be-after-tp1", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--commission-bps", type=float, default=0.0, help="Per-side commission in basis points.")
    parser.add_argument("--slippage-bps", type=float, default=0.0, help="Per-side slippage/spread estimate in basis points.")
    parser.add_argument("--commission-points", type=float, default=0.0, help="Per-side fixed execution commission expressed in instrument price points.")
    parser.add_argument("--slippage-points", type=float, default=0.0, help="Per-side slippage/spread estimate expressed in instrument price points.")
    parser.add_argument("--funding-data-dir", default=None, help="Directory containing SYMBOL_funding.csv hourly funding history.")
    parser.add_argument("--context-mode", choices=["off", "aligned_only", "strict"], default="off")
    parser.add_argument("--forward-bars", type=int, default=20)
    parser.add_argument("--warmup-bars", type=int, default=100)
    parser.add_argument("--turtle-soup-min-wick-fraction", type=float, default=None)
    parser.add_argument("--turtle-soup-min-wick-atr-ratio", type=float, default=None)
    parser.add_argument("--turtle-soup-min-close-back-fraction", type=float, default=None)
    parser.add_argument("--turtle-soup-min-level-age-bars", type=int, default=None)
    parser.add_argument("--turtle-soup-max-confirmation-bars", type=int, default=None)
    parser.add_argument("--turtle-soup-min-stop-bps", type=float, default=None)
    parser.add_argument("--turtle-soup-allowed-swing-significances", nargs="*", default=None)
    parser.add_argument("--turtle-soup-session-windows", default=None)
    parser.add_argument("--turtle-soup-range-source", default=None)
    parser.add_argument("--turtle-soup-asian-range-window", default=None)
    parser.add_argument("--turtle-soup-asian-range-tz", default=None)
    parser.add_argument("--turtle-soup-asian-min-range-bps", type=float, default=None)
    parser.add_argument("--turtle-soup-asian-min-breach-bps", type=float, default=None)
    parser.add_argument("--turtle-soup-asian-first-signal-only", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--turtle-soup-asian-reject-prior-failed-sweep", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--turtle-soup-require-killzone", action="store_true")
    parser.add_argument("--turtle-soup-require-smt", action="store_true")
    parser.add_argument("--turtle-soup-require-smt-on-sweep", action="store_true")
    parser.add_argument("--turtle-soup-require-mss-confirmation", action="store_true")
    parser.add_argument("--turtle-soup-require-confirmation-fvg", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--max-ifvg-retest-bars", type=int, default=None)
    parser.add_argument("--min-ifvg-retest-bars", type=int, default=None)
    parser.add_argument("--ifvg-entry-mode", choices=["edge", "ce"], default=None)
    parser.add_argument("--ifvg-stop-mode", choices=["ce", "opposite_boundary"], default=None)
    parser.add_argument("--ifvg-min-retest-depth", type=float, default=None)
    parser.add_argument("--ifvg-max-source-touches-before-inversion", type=int, default=None)
    parser.add_argument("--ifvg-max-source-age-bars", type=int, default=None)
    parser.add_argument("--ict2022-max-fvg-retest-bars", type=int, default=None)
    parser.add_argument("--ict2022-session-windows", default=None)
    parser.add_argument("--ict2022-require-strong-displacement", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--ict2022-retest-must-occur-within-session", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--breaker-max-trigger-to-retest-bars", type=int, default=None)
    parser.add_argument("--breaker-max-retest-count", type=int, default=None)
    parser.add_argument("--breaker-require-displacement", action="store_true")
    parser.add_argument("--rejection-block-min-wick-fraction", type=float, default=None)
    parser.add_argument("--smt-pairs", nargs="*", default=["BTCUSDT:ETHUSDT", "ETHUSDT:SOLUSDT"])
    parser.add_argument("--smt-lookback-bars", type=int, default=50)
    parser.add_argument("--smt-max-time-delta-bars", type=int, default=10)
    parser.add_argument("--smt-min-divergence-bps", type=float, default=5.0)
    parser.add_argument("--smt-min-correlation", type=float, default=0.7)
    parser.add_argument("--silver-bullet-windows", default=None, help="Comma-separated NY windows, e.g. 10:00-11:00,14:00-15:00.")
    parser.add_argument("--silver-bullet-retest-must-occur-within-window", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--silver-bullet-max-retest-bars", type=int, default=None)
    parser.add_argument("--silver-bullet-min-retest-depth", type=float, default=None)
    parser.add_argument("--silver-bullet-use-ce-invalidation", action=argparse.BooleanOptionalAction, default=None)
    parser.add_argument("--pre-model-filter", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--pre-model-allow-neutral-htf", action="store_true")
    parser.add_argument("--pre-model-allow-equilibrium", action="store_true")
    parser.add_argument("--pre-model-require-smt", action="store_true")
    parser.add_argument("--pre-model-require-killzone", action="store_true")
    parser.add_argument("--pre-model-require-htf-poi", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--pre-model-killzone-windows", default=None)
    parser.add_argument("--scan-session-windows", default=None, help="NY windows to scan, e.g. 02:30-02:30,10:45-11:00.")
    parser.add_argument("--scan-session-lag-bars", type=int, default=1, help="Also scan bars whose prior N bars were inside the scan window.")
    parser.add_argument("--out-dir", default="backtest_results/new_ict_models")
    return parser


def _load_store(data_dir: Path, symbols: list[str], timeframes: list[str], context_mode: str, smt_pairs: list[str]) -> dict[tuple[str, str], list[Candle]]:
    store: dict[tuple[str, str], list[Candle]] = {}
    required = {(symbol, tf) for symbol in symbols for tf in timeframes}
    smt_symbols = _symbols_from_smt_pairs(smt_pairs, set(symbols))
    required |= {(symbol, tf) for symbol in smt_symbols for tf in timeframes}
    optional = set()
    if context_mode != "off":
        optional = {(symbol, execution_htf_for(tf)) for symbol in symbols for tf in timeframes if execution_htf_for(tf)}
    for symbol, tf in sorted(required | optional):
        store[(symbol, tf)] = load_history_for(data_dir, symbol, tf, required=(symbol, tf) in required) or []
    return store


def _load_funding_store(data_dir: Path, symbols: list[str]) -> dict[str, list[dict[str, float | int]]]:
    return {symbol: load_funding_for(data_dir, symbol) or [] for symbol in symbols}


def _symbols_from_smt_pairs(raw_pairs: list[str], requested: set[str]) -> set[str]:
    symbols: set[str] = set()
    for raw in raw_pairs or []:
        if ":" not in raw:
            continue
        first, second = raw.split(":", 1)
        pair = {first.strip().upper(), second.strip().upper()}
        if pair & requested:
            symbols |= pair
    return symbols


def _window_list(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return [str(item).strip() for item in value if str(item).strip()]


def _scan_session_window_matches(candles: list[Candle], idx: int, windows: list[str], lag_bars: int = 1) -> bool:
    max_lag = max(0, int(lag_bars))
    for offset in range(max_lag + 1):
        check_idx = idx - offset
        if check_idx < 0:
            break
        if in_ny_windows(int(candles[check_idx]["time"]), windows):
            return True
    return False


def _run_symbol(
    symbol: str,
    timeframes: list[str],
    models: list[Any],
    store: dict[tuple[str, str], list[Candle]],
    funding_store: dict[str, list[dict[str, float | int]]],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cache = ReplaySnapshotCache(store)
    seen: set[tuple[Any, ...]] = set()
    accumulate_primary = _models_need_accumulated_primary(models)
    for timeframe in timeframes:
        candles = store.get((symbol, timeframe), [])
        scan_windows = _window_list(args.scan_session_windows)
        start_idx, end_idx = _date_scan_bounds(candles, args.warmup_bars, args.start_date, args.end_date)
        for idx in range(start_idx, end_idx):
            ts = int(candles[idx]["time"])
            if scan_windows and not _scan_session_window_matches(candles, idx, scan_windows, args.scan_session_lag_bars):
                continue
            visible = candles[max(0, idx + 1 - DETECTOR_CANDLE_WINDOW) : idx + 1]
            config = {k: v for k, v in vars(args).items() if v is not None}
            if args.turtle_soup_min_level_age_bars is not None:
                config["turtle_min_swing_age"] = args.turtle_soup_min_level_age_bars
            config["smt_divergences"] = []
            config["has_smt_confirmation"] = False
            if args.pre_model_require_smt:
                smt = _smt_divergences(symbol, timeframe, visible, store, args, ts)
                config["smt_divergences"] = smt
                config["has_smt_confirmation"] = bool(smt)
            context = None
            if args.context_mode != "off":
                context = build_accumulated_strategy_context_for_replay(
                    symbol=symbol,
                    timeframe=timeframe,
                    current_timestamp=ts,
                    snapshot_cache=cache,
                    primary_visible=visible,
                    accumulate_primary=accumulate_primary,
                    htf_mode="strict" if args.context_mode == "strict" else "soft",
                )
            pre_model = evaluate_pre_model_filter(context, config)
            if not pre_model.passed:
                continue
            if not args.pre_model_require_smt:
                smt = _smt_divergences(symbol, timeframe, visible, store, args, ts)
                config["smt_divergences"] = smt
                config["has_smt_confirmation"] = bool(smt)
            for spec in models:
                setups = spec.detector(symbol, timeframe, visible, context, config)
                for setup in setups:
                    if not setup_passes_pre_model_filter(setup, pre_model):
                        continue
                    merge_pre_model_metadata(setup, pre_model)
                    if args.context_mode in {"aligned_only", "strict"} and not _context_aligned(
                        setup,
                        context,
                        require_htf_poi=args.pre_model_require_htf_poi,
                    ):
                        continue
                    key = (spec.name, symbol, timeframe, setup.direction, setup.timestamp, round(setup.entry_low, 8), round(setup.entry_high, 8))
                    if key in seen:
                        continue
                    seen.add(key)
                    event_idx = _index_at_or_before(candles, setup.timestamp)
                    if event_idx is None:
                        continue
                    event_window = candles[event_idx + 1 : event_idx + 1 + args.forward_bars]
                    rows.append(
                        _event_row(
                            setup,
                            spec.name,
                            spec.model_family,
                            args.same_bar_policy,
                            event_window,
                            detected_at=ts,
                            args=args,
                            funding_rates=funding_store.get(symbol, []),
                        )
                    )
    return rows


def _models_need_accumulated_primary(models: list[Any]) -> bool:
    return any(getattr(spec, "name", None) != "silver_bullet" for spec in models)


def _context_aligned(setup: EntrySetup, context: object | None, *, require_htf_poi: bool = True) -> bool:
    htf = getattr(context, "htf_context", None)
    if htf is None:
        return False
    if not require_htf_poi:
        objective_unreached = bool(htf.objective_unreached or htf.objective.objective_unreached)
        if (
            setup.direction == "long"
            and htf.bias.direction == "bullish"
            and htf.objective.direction == "up"
            and objective_unreached
            and htf.dealing_range.location == "discount"
        ):
            return True
        if (
            setup.direction == "short"
            and htf.bias.direction == "bearish"
            and htf.objective.direction == "down"
            and objective_unreached
            and htf.dealing_range.location == "premium"
        ):
            return True
        return False
    return (setup.direction == "long" and htf.allows_long) or (setup.direction == "short" and htf.allows_short)


def _smt_divergences(symbol: str, timeframe: str, visible: list[Candle], store: dict[tuple[str, str], list[Candle]], args: argparse.Namespace, timestamp: int) -> list[Any]:
    results = []
    smt_window = max(args.smt_lookback_bars + args.smt_max_time_delta_bars + 2, args.smt_lookback_bars)
    for raw in args.smt_pairs or []:
        if ":" not in raw:
            continue
        primary, secondary = (part.strip().upper() for part in raw.split(":", 1))
        if symbol != primary:
            continue
        primary_candles = visible[-smt_window:]
        secondary_candles = _candles_until(store.get((secondary, timeframe), []), timestamp, smt_window)
        if not primary_candles or not secondary_candles:
            continue
        results.extend(
            detect_smt(
                primary_candles,
                secondary_candles,
                primary,
                secondary,
                timeframe,
                lookback_bars=args.smt_lookback_bars,
                max_time_delta_bars=args.smt_max_time_delta_bars,
                min_divergence_bps=args.smt_min_divergence_bps,
                min_correlation=args.smt_min_correlation,
            )
        )
    return results


def _candles_until(candles: list[Candle], timestamp: int, limit: int | None = None) -> list[Candle]:
    visible = [candle for candle in candles if int(candle["time"]) <= timestamp]
    return visible[-limit:] if limit is not None else visible


def _index_at_or_before(candles: list[Candle], timestamp: int) -> int | None:
    match = None
    for idx, candle in enumerate(candles):
        if int(candle["time"]) <= timestamp:
            match = idx
        else:
            break
    return match


def _timestamp_in_date_range(timestamp: int, start_date: str | None, end_date: str | None) -> bool:
    if start_date and timestamp < _date_to_ms(start_date):
        return False
    if end_date and timestamp > _date_to_ms(end_date, end_of_day=True):
        return False
    return True


def _date_scan_bounds(candles: list[Candle], warmup_bars: int, start_date: str | None, end_date: str | None) -> tuple[int, int]:
    start_idx = max(warmup_bars, 0)
    end_idx = len(candles)
    if not candles:
        return start_idx, end_idx

    timestamps = [int(candle["time"]) for candle in candles]
    if start_date:
        start_idx = max(start_idx, bisect_left(timestamps, _date_to_ms(start_date)))
    if end_date:
        end_idx = bisect_right(timestamps, _date_to_ms(end_date, end_of_day=True))
    return start_idx, end_idx


def _date_to_ms(value: str, *, end_of_day: bool = False) -> int:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    if end_of_day and len(value) == 10:
        dt = dt.replace(hour=23, minute=59, second=59, microsecond=999000)
    return int(dt.timestamp() * 1000)


def _event_row(
    setup: EntrySetup,
    model_name: str,
    model_family: str,
    same_bar_policy: str,
    future: list[Candle],
    *,
    detected_at: int | None = None,
    args: argparse.Namespace | None = None,
    funding_rates: list[dict[str, float | int]] | None = None,
) -> dict[str, Any]:
    metadata = dict(setup.metadata)
    entry = setup.entry_price if setup.entry_price is not None else (setup.entry_low + setup.entry_high) / 2
    stop = setup.stop_loss if setup.stop_loss is not None else setup.invalidation
    risk = abs(entry - stop) if stop is not None else None
    entry_time = int(metadata.get("entry_time") or setup.timestamp)
    outcome = _evaluate(
        setup.direction,
        entry,
        stop,
        setup.target_hint,
        future,
        same_bar_policy,
        entry_time=entry_time,
        tp1=metadata.get("tp1_price"),
        logical_invalidation=metadata.get("logical_invalidation_price"),
        final_target=metadata.get("final_target"),
        cancel_on_pre_entry_tp1=True,
        tp1_r=float(getattr(args, "tp1_r", 1.0) if args is not None else 1.0),
        partial_close_fraction=float(getattr(args, "partial_close_fraction", 0.5) if args is not None else 0.5),
        move_to_be_after_tp1=bool(getattr(args, "move_to_be_after_tp1", True) if args is not None else True),
    )
    execution = _execution_costs(entry, risk, outcome, args)
    funding = _funding_costs(setup.direction, entry, risk, entry_time, outcome, funding_rates or [])
    costs = {
        **execution,
        **funding,
        "total_cost_r": round(float(execution["execution_cost_r"]) + float(funding["funding_cost_r"]), 6),
    }
    outcome = _with_execution_costs(outcome, costs)
    target_distance_r = abs(setup.target_hint - entry) / risk if setup.target_hint is not None and risk and risk > 0 else None
    decision = _decision_score(setup.direction, model_name, metadata, target_distance_r)
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
        "exit_time": outcome.get("exit_time"),
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
        **costs,
        "same_bar_policy": same_bar_policy,
        "same_bar_ambiguous": outcome["same_bar_ambiguous"],
        "invalidated_before_entry": outcome["invalidated_before_entry"],
        "target_distance_r": target_distance_r,
        "time_to_entry_bars": outcome["time_to_entry_bars"],
        "metadata_json": json.dumps(metadata, ensure_ascii=True, sort_keys=True, default=str),
        **{field: metadata.get(field) for field in EVENT_FIELDS if field not in {"model", "model_family", "direction", "symbol", "timeframe", "timestamp", "setup_timestamp", "detected_at", "entry_time", "exit_time", "entry_mode", "stop_mode", "target_mode", "entry_price", "entry_low", "entry_high", "stop_loss", "invalidation", "target_hint", "risk", "risk_bps", "commission_bps", "slippage_bps", "round_trip_cost_bps", "commission_points", "slippage_points", "round_trip_cost_points", "execution_cost_r", "funding_rows", "funding_rate_sum", "funding_cost_r", "funding_notional_price_mode", "total_cost_r", "gross_managed_outcome_r", "net_managed_outcome_r", "same_bar_policy", "same_bar_ambiguous", "invalidated_before_entry", "target_reached_before_entry", "target_distance_r", "time_to_entry_bars", "bars_to_invalidation", "bars_to_1r", "bars_to_2r", "metadata_json", "mfe_r", "mae_r", "invalidated", "target_hit", "tp1_hit", "tp1_time", "tp2_hit", "final_target_hit", "logical_invalidated", "managed_outcome_r", "managed_exit_reason", "target_before_invalidation", "hit_1r_before_invalidation", "hit_2r_before_invalidation"}},
        **decision,
        **outcome,
    }
    return row


def _execution_costs(
    entry: float,
    risk: float | None,
    outcome: dict[str, Any],
    args: argparse.Namespace | None,
) -> dict[str, Any]:
    commission_bps = float(getattr(args, "commission_bps", 0.0) if args is not None else 0.0)
    slippage_bps = float(getattr(args, "slippage_bps", 0.0) if args is not None else 0.0)
    commission_points = float(getattr(args, "commission_points", 0.0) if args is not None else 0.0)
    slippage_points = float(getattr(args, "slippage_points", 0.0) if args is not None else 0.0)
    round_trip_bps = max(0.0, 2.0 * (commission_bps + slippage_bps))
    round_trip_points = max(0.0, 2.0 * (commission_points + slippage_points))
    if not outcome.get("activated_trade") or risk is None or risk <= 0:
        execution_cost_r = 0.0
    else:
        execution_cost_r = ((entry * round_trip_bps / 10_000.0) + round_trip_points) / risk
    return {
        "commission_bps": commission_bps,
        "slippage_bps": slippage_bps,
        "round_trip_cost_bps": round_trip_bps,
        "commission_points": commission_points,
        "slippage_points": slippage_points,
        "round_trip_cost_points": round_trip_points,
        "execution_cost_r": round(execution_cost_r, 6),
    }


def _funding_costs(
    direction: str,
    entry: float,
    risk: float | None,
    entry_time: int,
    outcome: dict[str, Any],
    funding_rates: list[dict[str, float | int]],
) -> dict[str, Any]:
    exit_time = outcome.get("exit_time")
    if not outcome.get("activated_trade") or risk is None or risk <= 0 or not isinstance(exit_time, int):
        return {
            "funding_rows": 0,
            "funding_rate_sum": 0.0,
            "funding_cost_r": 0.0,
            "funding_notional_price_mode": "entry_proxy",
        }
    tp1_time = outcome.get("tp1_time")
    partial = float(outcome.get("partial_close_fraction") or 0.0)
    signed_rate_sum = 0.0
    signed_payment_points = 0.0
    matched_rows = 0
    mark_price_rows = 0
    for row in funding_rates:
        timestamp = int(row["time"])
        if timestamp <= entry_time or timestamp > exit_time:
            continue
        remaining = 1.0
        if isinstance(tp1_time, int) and timestamp > tp1_time:
            remaining = 1.0 - partial
        rate = float(row["funding_rate"]) * remaining
        direction_rate = rate if direction == "long" else -rate
        notional_price = float(row.get("mark_price", entry))
        if "mark_price" in row:
            mark_price_rows += 1
        signed_rate_sum += direction_rate
        signed_payment_points += notional_price * direction_rate
        matched_rows += 1
    funding_cost_r = signed_payment_points / risk
    price_mode = (
        "settlement_mark_price"
        if matched_rows and mark_price_rows == matched_rows
        else "mixed_mark_and_entry_proxy"
        if mark_price_rows
        else "entry_proxy"
    )
    return {
        "funding_rows": matched_rows,
        "funding_rate_sum": round(signed_rate_sum, 10),
        "funding_cost_r": round(funding_cost_r, 6),
        "funding_notional_price_mode": price_mode,
    }


def _with_execution_costs(outcome: dict[str, Any], execution: dict[str, Any]) -> dict[str, Any]:
    gross = outcome.get("managed_outcome_r")
    if gross is None:
        outcome["gross_managed_outcome_r"] = None
        outcome["net_managed_outcome_r"] = None
        return outcome
    cost_r = float(execution.get("total_cost_r", execution.get("execution_cost_r", 0.0)) or 0.0)
    outcome["gross_managed_outcome_r"] = gross
    outcome["net_managed_outcome_r"] = round(float(gross) - cost_r, 6)
    return outcome


def _decision_score(direction: str, model_name: str, metadata: dict[str, Any], target_distance_r: float | None) -> dict[str, Any]:
    reasons: list[str] = []
    htf_score = _htf_alignment_score(direction, metadata, reasons)
    draw_score = _draw_score(metadata)
    pd_score = _pd_location_score(direction, metadata, reasons)
    poi_score = _poi_score(metadata)
    displacement_score = _displacement_score(model_name, metadata, reasons)
    smt_score = 20 if metadata.get("has_smt_confirmation") else 0
    killzone_score = _killzone_score(model_name, metadata, reasons)
    target_rr_score = _target_rr_score(model_name, target_distance_r, reasons)
    total = min(
        100,
        htf_score
        + draw_score
        + pd_score
        + poi_score
        + displacement_score
        + smt_score
        + killzone_score
        + target_rr_score,
    )
    return {
        "decision_score": total,
        "score_bucket": "high" if total >= 70 else "medium" if total >= 50 else "low",
        "htf_alignment_score": htf_score,
        "draw_score": draw_score,
        "pd_location_score": pd_score,
        "poi_score": poi_score,
        "displacement_score": displacement_score,
        "smt_score": smt_score,
        "killzone_score": killzone_score,
        "target_rr_score": target_rr_score,
        "no_trade_reasons": ";".join(reasons),
    }


def _htf_alignment_score(direction: str, metadata: dict[str, Any], reasons: list[str]) -> int:
    bias = metadata.get("htf_bias")
    mode = metadata.get("htf_mode")
    if mode == "off" or bias in {None, "none"}:
        return 20
    expected = "bullish" if direction == "long" else "bearish"
    if bias == expected:
        return 40
    if bias == "neutral":
        reasons.append("neutral_htf_bias")
        return 10
    reasons.append("against_htf_flow")
    return 0


def _draw_score(metadata: dict[str, Any]) -> int:
    objective = metadata.get("htf_objective_type")
    if objective in {"equal_highs", "equal_lows"}:
        return 20
    if objective in {"swing_high", "swing_low"}:
        return 12
    return 5


def _pd_location_score(direction: str, metadata: dict[str, Any], reasons: list[str]) -> int:
    location = metadata.get("htf_location")
    if location in {None, "unknown"}:
        return 5
    if direction == "long" and location == "discount":
        return 15
    if direction == "short" and location == "premium":
        return 15
    if location == "equilibrium":
        reasons.append("equilibrium")
        return 0
    reasons.append("poor_pd_location")
    return 0


def _poi_score(metadata: dict[str, Any]) -> int:
    if metadata.get("htf_zone_type") in {"OB", "FVG", "IFVG", "Breaker", "PD"}:
        return 10
    if any(metadata.get(key) is not None for key in ("fvg_low", "ifvg_low", "ob_low", "breaker_low", "rejection_body_level", "mitigation_low")):
        return 8
    return 0


def _displacement_score(model_name: str, metadata: dict[str, Any], reasons: list[str]) -> int:
    grade = metadata.get("displacement_grade") or metadata.get("breach_displacement_grade")
    if grade == "strong":
        return 20
    if grade == "valid":
        return 15
    if model_name in {"ict2022_mss_fvg", "ifvg_retest", "breaker_block"}:
        reasons.append("insufficient_displacement")
    return 0


def _killzone_score(model_name: str, metadata: dict[str, Any], reasons: list[str]) -> int:
    has_window = bool(metadata.get("session_window") or metadata.get("ny_time"))
    session_filter = metadata.get("session_filter")
    if has_window or (session_filter not in {None, "off"}):
        return 20
    if model_name in {"ict2022_mss_fvg", "silver_bullet"}:
        reasons.append("missing_required_killzone")
    return 0


def _target_rr_score(model_name: str, target_distance_r: float | None, reasons: list[str]) -> int:
    if target_distance_r is None:
        reasons.append("missing_target_rr")
        return 0
    if model_name == "silver_bullet":
        if target_distance_r >= 2:
            return 20
        reasons.append("target_rr_below_2")
        return 0
    if target_distance_r >= 3:
        return 20
    if target_distance_r >= 2:
        reasons.append("target_rr_below_3")
        return 10
    reasons.append("target_rr_below_2")
    return 0


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
        "target_reached_before_entry": False,
        "activated_trade": False,
        "exit_time": None,
        "time_to_entry_bars": None,
        "bars_to_invalidation": None,
        "bars_to_1r": None,
        "bars_to_2r": None,
        "tp1_hit": False,
        "tp1_time": None,
        "tp2_hit": False,
        "final_target_hit": False,
        "logical_invalidated": False,
        "moved_to_be": False,
        "tp1_r": None,
        "partial_close_fraction": None,
        "managed_outcome_r": None,
        "managed_exit_reason": None,
        "exit_reason": None,
    }


def _evaluate(
    direction: str,
    entry: float,
    stop: float | None,
    target: float | None,
    future: list[Candle],
    policy: str,
    entry_time: int | None = None,
    *,
    tp1: float | None = None,
    logical_invalidation: float | None = None,
    final_target: float | None = None,
    cancel_on_pre_entry_tp1: bool = False,
    tp1_r: float = 1.0,
    partial_close_fraction: float = 0.5,
    move_to_be_after_tp1: bool = True,
) -> dict[str, Any]:
    if stop is None or target is None:
        return _empty_outcome()
    risk = abs(entry - stop)
    if risk <= 0:
        return _empty_outcome()
    entry_time = int(entry_time or (future[0]["time"] if future else 0))
    tp1_cancel = entry + risk * tp1_r if direction == "long" else entry - risk * tp1_r
    before_entry = [candle for candle in future if int(candle["time"]) < entry_time]
    invalidated_before_entry = any(
        _stop_hit(direction, candle, stop) or _logical_hit(direction, candle, logical_invalidation)
        for candle in before_entry
    )
    target_reached_before_entry = bool(
        cancel_on_pre_entry_tp1
        and any(_target_hit(direction, candle, tp1_cancel) for candle in before_entry)
    )
    active = [candle for candle in future if int(candle["time"]) >= entry_time]
    if invalidated_before_entry or target_reached_before_entry or not active:
        outcome = _empty_outcome()
        outcome["invalidated_before_entry"] = invalidated_before_entry
        outcome["target_reached_before_entry"] = target_reached_before_entry
        outcome["exit_reason"] = "target_reached_before_entry" if target_reached_before_entry else "invalidated_before_entry" if invalidated_before_entry else None
        outcome["managed_exit_reason"] = outcome["exit_reason"]
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
    tp1_hit = False
    tp1_time = None
    tp2_hit = False
    final_target_hit = False
    logical_invalidated = False
    moved_to_be = False
    managed_outcome: float | None = None
    managed_exit_reason = None
    exit_reason = None
    exit_time = None
    bars_to_1r = None
    bars_to_2r = None
    bars_to_invalidation = None
    ambiguous = False
    target_1r = entry + risk if direction == "long" else entry - risk
    target_2r = entry + risk * 2 if direction == "long" else entry - risk * 2
    tp1_target = entry + risk * tp1_r if direction == "long" else entry - risk * tp1_r
    if tp1 is not None and abs(float(tp1) - tp1_target) < risk * 0.01:
        tp1_target = float(tp1)
    tp2_target = target
    final_target = float(final_target) if isinstance(final_target, (int, float)) else target
    partial = min(max(partial_close_fraction, 0.0), 1.0)
    for offset, candle in enumerate(active, start=1):
        effective_stop = entry if moved_to_be and move_to_be_after_tp1 else stop
        stop_hit = _stop_hit(direction, candle, effective_stop)
        logical_hit = _logical_hit(direction, candle, logical_invalidation)
        target_reached = _target_hit(direction, candle, target)
        tp1_reached = _target_hit(direction, candle, tp1_target)
        tp2_reached = _target_hit(direction, candle, tp2_target) if tp2_target is not None else False
        final_reached = _target_hit(direction, candle, final_target) if final_target is not None else False
        hit_1r_now = _target_hit(direction, candle, target_1r)
        hit_2r_now = _target_hit(direction, candle, target_2r)
        any_target = target_reached or hit_1r_now or hit_2r_now
        if (stop_hit or logical_hit) and any_target:
            ambiguous = True
            if policy == "optimistic":
                target_rr = abs(target - entry) / risk
                target_hit = True
                target_before = True
                hit_1r = hit_1r or hit_1r_now
                hit_2r = hit_2r or hit_2r_now
                tp1_hit = tp1_hit or tp1_reached
                tp1_time = int(candle["time"]) if tp1_reached else tp1_time
                tp2_hit = tp2_hit or tp2_reached
                final_target_hit = final_target_hit or final_reached
                exit_reason = "tp_hit"
                managed_outcome = partial * tp1_r + (1.0 - partial) * target_rr if tp1_reached else target_rr
                managed_exit_reason = "final_target_hit"
                exit_time = int(candle["time"])
                bars_to_1r = bars_to_1r or (offset if hit_1r_now else None)
                bars_to_2r = bars_to_2r or (offset if hit_2r_now else None)
                break
            invalidated = True
            logical_invalidated = logical_hit
            exit_reason = "logical_invalidation" if logical_hit else "sl_hit"
            managed_outcome = partial * tp1_r if moved_to_be else -1.0
            managed_exit_reason = "be_after_tp1" if moved_to_be and not logical_hit else exit_reason
            bars_to_invalidation = offset
            exit_time = int(candle["time"])
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
        if tp1_reached:
            if not tp1_hit:
                tp1_time = int(candle["time"])
            tp1_hit = True
            moved_to_be = True
        if tp2_reached:
            tp2_hit = True
        if final_reached:
            final_target_hit = True
        if target_reached:
            target_hit = True
            target_before = True
            exit_reason = "tp_hit"
            target_rr = abs(target - entry) / risk
            managed_outcome = partial * tp1_r + (1.0 - partial) * target_rr if tp1_hit else target_rr
            managed_exit_reason = "final_target_hit"
            exit_time = int(candle["time"])
            break
        if logical_hit:
            invalidated = True
            logical_invalidated = True
            exit_reason = "logical_invalidation"
            managed_outcome = partial * tp1_r if moved_to_be else -1.0
            managed_exit_reason = "logical_invalidation_after_tp1" if moved_to_be else "logical_invalidation"
            bars_to_invalidation = offset
            exit_time = int(candle["time"])
            break
        if stop_hit:
            invalidated = True
            exit_reason = "sl_hit"
            managed_outcome = partial * tp1_r if moved_to_be else -1.0
            managed_exit_reason = "be_after_tp1" if moved_to_be and move_to_be_after_tp1 else "sl_hit"
            bars_to_invalidation = offset
            exit_time = int(candle["time"])
            break
    if managed_outcome is None:
        close_r = _close_outcome_r(direction, active[-1], entry, risk)
        if tp1_hit:
            managed_outcome = partial * tp1_r + (1.0 - partial) * close_r
            managed_exit_reason = "horizon_close_after_tp1"
        else:
            managed_outcome = close_r
            managed_exit_reason = "horizon_close"
        exit_reason = "horizon_close"
        exit_time = int(active[-1]["time"])
    return {
        "mfe_r": mfe / risk,
        "mae_r": mae / risk,
        "invalidated": invalidated,
        "target_hit": target_hit,
        "target_before_invalidation": target_before,
        "hit_1r_before_invalidation": hit_1r,
        "hit_2r_before_invalidation": hit_2r,
        "same_bar_ambiguous": ambiguous,
        "invalidated_before_entry": invalidated_before_entry,
        "target_reached_before_entry": target_reached_before_entry,
        "activated_trade": True,
        "exit_time": exit_time,
        "time_to_entry_bars": _bars_until_or_none(future, entry_time),
        "bars_to_invalidation": bars_to_invalidation,
        "bars_to_1r": bars_to_1r,
        "bars_to_2r": bars_to_2r,
        "tp1_hit": tp1_hit,
        "tp1_time": tp1_time,
        "tp2_hit": tp2_hit,
        "final_target_hit": final_target_hit,
        "logical_invalidated": logical_invalidated,
        "moved_to_be": moved_to_be,
        "tp1_r": tp1_r,
        "partial_close_fraction": partial,
        "managed_outcome_r": managed_outcome,
        "managed_exit_reason": managed_exit_reason,
        "exit_reason": exit_reason,
    }


def _stop_hit(direction: str, candle: Candle, stop: float) -> bool:
    return float(candle["low"]) <= stop if direction == "long" else float(candle["high"]) >= stop


def _target_hit(direction: str, candle: Candle, target: float) -> bool:
    return float(candle["high"]) >= target if direction == "long" else float(candle["low"]) <= target


def _logical_hit(direction: str, candle: Candle, level: float | None) -> bool:
    if level is None:
        return False
    return float(candle["close"]) <= level if direction == "long" else float(candle["close"]) >= level


def _close_outcome_r(direction: str, candle: Candle, entry: float, risk: float) -> float:
    close = float(candle["close"])
    if direction == "long":
        return (close - entry) / risk
    return (entry - close) / risk


def _bars_until_or_none(candles: list[Candle], timestamp: int) -> int | None:
    for idx, candle in enumerate(candles, start=1):
        if int(candle["time"]) >= timestamp:
            return idx
    return None


def _summaries(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    specs = {
        "summary_by_model": ("model",),
        "summary_by_symbol": ("model", "symbol"),
        "summary_by_direction": ("model", "direction"),
        "summary_by_timeframe": ("model", "timeframe"),
        "summary_by_entry_mode": ("model", "entry_mode"),
        "summary_by_stop_mode": ("model", "stop_mode"),
        "summary_by_target_mode": ("model", "target_mode"),
        "summary_by_session_window": ("model", "session_window"),
        "summary_by_session_day": ("model", "session_date", "session_window"),
        "summary_by_session_label": ("model", "session_label"),
        "summary_by_same_bar_policy": ("model", "same_bar_policy"),
        "summary_by_model_family": ("model_family",),
        "summary_by_turtle_quality": ("model", "turtle_quality"),
        "summary_by_asian_failed_sweep_count": ("model", "asian_failed_sweep_count_before_reclaim"),
        "summary_by_htf_location": ("model", "htf_location"),
        "summary_by_htf_zone": ("model", "htf_zone_type"),
        "summary_by_displacement": ("model", "displacement_grade"),
        "summary_by_score_bucket": ("model", "score_bucket"),
        "summary_by_no_trade_reasons": ("model", "no_trade_reasons"),
    }
    return {name: _group(events, fields) for name, fields in specs.items()}


def _group(events: list[dict[str, Any]], fields: tuple[str, ...]) -> list[dict[str, Any]]:
    buckets: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[tuple(_group_value(event.get(field)) for field in fields)].append(event)
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
                "avg_decision_score": _avg_field(group, "decision_score"),
                "expectancy": _expectancy(group),
                "gross_managed_expectancy": _avg_field(group, "gross_managed_outcome_r"),
                "managed_expectancy": _avg_managed_outcome(group),
                "avg_managed_outcome_r": _avg_managed_outcome(group),
                "avg_execution_cost_r": _avg_field(group, "execution_cost_r"),
                "avg_funding_cost_r": _avg_field(group, "funding_cost_r"),
                "avg_total_cost_r": _avg_field(group, "total_cost_r"),
                "target_before_invalidation_rate": round(sum(1 for e in group if e.get("target_before_invalidation")) / len(group), 6) if group else None,
                "hit_1r_before_invalidation_rate": round(sum(1 for e in group if e.get("hit_1r_before_invalidation")) / len(group), 6) if group else None,
                "hit_2r_before_invalidation_rate": round(sum(1 for e in group if e.get("hit_2r_before_invalidation")) / len(group), 6) if group else None,
                "invalidation_rate": round(sum(1 for e in group if e.get("invalidated")) / len(group), 6) if group else None,
                "avg_time_to_entry": _avg_field(group, "time_to_entry_bars"),
                "avg_time_to_invalidation": _avg_field(group, "bars_to_invalidation"),
                "avg_time_to_1r": _avg_field(group, "bars_to_1r"),
                "avg_time_to_2r": _avg_field(group, "bars_to_2r"),
                "same_bar_ambiguous_count": sum(1 for e in group if e.get("same_bar_ambiguous")),
                "no_trade_reason_count": sum(1 for e in group if e.get("no_trade_reasons")),
            }
        )
        rows.append(row)
    return rows


def _group_value(value: Any) -> Any:
    if value is None or value == "":
        return "none"
    return value


def _avg_field(group: list[dict[str, Any]], field: str) -> float | None:
    values = [float(item[field]) for item in group if item.get(field) is not None]
    return round(sum(values) / len(values), 6) if values else None


def _avg_managed_outcome(group: list[dict[str, Any]]) -> float | None:
    values = []
    for item in group:
        value = item.get("net_managed_outcome_r")
        if value is None:
            value = item.get("managed_outcome_r")
        if value is not None:
            values.append(float(value))
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
        f"- New registry default models are `{', '.join(DEFAULT_MODELS)}`.",
        "",
        "## Backtest Config",
        f"- data_dir: {config.get('data_dir')}",
        f"- models: {', '.join(models)}",
        f"- symbols: {', '.join(config.get('symbols') or [])}",
        f"- timeframes: {', '.join(config.get('timeframes') or [])}",
        f"- same_bar_policy: {config.get('same_bar_policy')}",
        f"- context_mode: {config.get('context_mode')}",
        f"- forward_bars: {config.get('forward_bars')}",
        f"- commission_bps: {config.get('commission_bps')}",
        f"- slippage_bps: {config.get('slippage_bps')}",
        f"- commission_points: {config.get('commission_points')}",
        f"- slippage_points: {config.get('slippage_points')}",
        f"- funding_data_dir: {config.get('funding_data_dir')}",
        "- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.",
        "",
        "## Overall Comparison",
        _markdown_table(summaries.get("summary_by_model", [])),
        "",
        "## Symbol Analysis",
        _markdown_table(summaries.get("summary_by_symbol", [])),
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
        "",
        "## Turtle Quality",
        _markdown_table(summaries.get("summary_by_turtle_quality", [])),
        "",
        "## Asian Failed Sweep Count",
        _markdown_table(summaries.get("summary_by_asian_failed_sweep_count", [])),
        "",
        "## HTF Location",
        _markdown_table(summaries.get("summary_by_htf_location", [])),
        "",
        "## Displacement",
        _markdown_table(summaries.get("summary_by_displacement", [])),
        "",
        "## Decision Score Buckets",
        _markdown_table(summaries.get("summary_by_score_bucket", [])),
        "",
        "## No-Trade Reasons",
        _markdown_table(summaries.get("summary_by_no_trade_reasons", [])),
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
