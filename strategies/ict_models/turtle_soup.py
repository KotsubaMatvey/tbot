from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import Any
from zoneinfo import ZoneInfo

from market_primitives.common import collect_swings
from market_primitives.structure import detect_structure_breaks

from .common import avg_range, buffered_stop, closed_candles, context_metadata, draw_on_liquidity_target, fixed_r_target, opposite_range_target, setup, wick_extension_bps
from .sessions import LONDON_OPEN, NY_OPEN, NY_PM_SESSION, NY_TZ, in_ny_windows

TURTLE_LOOKBACK_BARS = 50
TURTLE_MIN_SWING_AGE = 5
TURTLE_ENTRY_MODE = "close"
TURTLE_TARGET_MODE = "opposite_range"
TURTLE_STOP_BUFFER_BPS = 2
TURTLE_MIN_WICK_FRACTION = 0.10
TURTLE_MIN_WICK_ATR_RATIO = 0.0
TURTLE_MIN_CLOSE_BACK_FRACTION = 0.05
TURTLE_MAX_CONFIRMATION_BARS = 1
TURTLE_REQUIRE_MSS_CONFIRMATION = False


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if str(cfg.get("turtle_soup_range_source") or "").strip().lower() == "asian_range":
        return _asian_range_setups(symbol, timeframe, candles, closed, context, cfg)
    entry_mode = str(cfg.get("entry_mode") or cfg.get("turtle_entry_mode") or TURTLE_ENTRY_MODE)
    if entry_mode not in {"close", "retest"}:
        entry_mode = TURTLE_ENTRY_MODE
    target_mode = str(cfg.get("target_mode") or TURTLE_TARGET_MODE)
    if target_mode not in {"opposite_range", "nearest_liquidity", "dol_hierarchy", "fixed_r"}:
        target_mode = TURTLE_TARGET_MODE
    stop_bps = float(cfg.get("stop_buffer_bps") or cfg.get("turtle_stop_buffer_bps") or TURTLE_STOP_BUFFER_BPS)
    lookback = int(cfg.get("turtle_lookback_bars") or TURTLE_LOOKBACK_BARS)
    min_age = int(cfg.get("turtle_min_swing_age") or TURTLE_MIN_SWING_AGE)
    min_wick_fraction = float(cfg.get("turtle_soup_min_wick_fraction") or TURTLE_MIN_WICK_FRACTION)
    min_wick_atr_ratio = float(cfg.get("turtle_soup_min_wick_atr_ratio") or TURTLE_MIN_WICK_ATR_RATIO)
    min_close_back_fraction = float(cfg.get("turtle_soup_min_close_back_fraction") or TURTLE_MIN_CLOSE_BACK_FRACTION)
    max_confirmation_bars = int(cfg.get("turtle_soup_max_confirmation_bars") or TURTLE_MAX_CONFIRMATION_BARS)
    require_killzone = bool(cfg.get("turtle_soup_require_killzone", False))
    require_smt = bool(cfg.get("turtle_soup_require_smt", False))
    require_smt_on_sweep = bool(cfg.get("turtle_soup_require_smt_on_sweep", False))
    require_mss_confirmation = bool(cfg.get("turtle_soup_require_mss_confirmation", TURTLE_REQUIRE_MSS_CONFIRMATION))
    require_confirmation_fvg = bool(cfg.get("turtle_soup_require_confirmation_fvg", True))
    allowed_significances = set(cfg.get("turtle_soup_allowed_swing_significances") or [])
    session_windows = _window_list(cfg.get("turtle_soup_session_windows") or cfg.get("turtle_soup_killzone_windows") or _default_session_windows())
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    if len(closed) < min_age + 5:
        return []

    scan = closed[-lookback:]
    if require_mss_confirmation:
        return _confirmed_setups(
            symbol,
            timeframe,
            candles,
            scan,
            cfg,
            entry_mode,
            target_mode,
            stop_bps,
            min_age,
            min_wick_fraction,
            min_wick_atr_ratio,
            min_close_back_fraction,
            max_confirmation_bars,
            context,
            htf_mode,
            session_windows,
            require_killzone,
            require_smt,
            require_confirmation_fvg,
            allowed_significances,
        )

    sweep = scan[-1]
    highs, lows = collect_swings(scan[:-1], symbol, timeframe, left=1, right=1)
    results = []
    if max_confirmation_bars < 1 or require_killzone or require_smt:
        if max_confirmation_bars < 1:
            return []
        session_window = _matching_window(int(sweep["time"]), session_windows)
        if require_killzone and session_window is None:
            return []
        if require_smt and not _has_smt_confirmation(cfg):
            return []
    else:
        session_window = _matching_window(int(sweep["time"]), session_windows)

    average_true_range = avg_range(scan[:-1])
    low = next(
        (
            s
            for s in reversed(lows)
            if len(scan) - 1 - s.index >= min_age
            and (not allowed_significances or s.significance in allowed_significances)
            and sweep["low"] < s.level < sweep["close"]
        ),
        None,
    )
    if low is not None:
        quality = _quality("long", sweep, low.level, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
        if not quality["passed"]:
            low = None
    if low is not None and require_smt and not _has_smt_confirmation(cfg, "long", int(sweep["time"]) if require_smt_on_sweep else None):
        low = None
    if low is not None:
        entry = float(sweep["close"] if entry_mode == "close" else low.level)
        stop = buffered_stop("long", float(sweep["low"]), entry, stop_bps)
        stop, min_stop_applied = _apply_min_stop_distance("long", entry, stop, cfg)
        metadata = context_metadata(context, "long", htf_mode, cfg)
        target, target_metadata = _target_for(closed, "long", entry, stop, target_mode, metadata)
        item = setup(
            model_name="turtle_soup",
            direction="long",
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(sweep["time"]),
            score=3,
            reason="Bullish Turtle Soup sweep and close back above liquidity",
            metadata={
                **metadata,
                **target_metadata,
                **_session_metadata(int(sweep["time"]), session_window),
                "entry_mode": entry_mode,
                "stop_mode": "sweep_extreme",
                "turtle_soup_min_stop_applied": min_stop_applied,
                "turtle_soup_min_stop_bps": cfg.get("turtle_soup_min_stop_bps"),
                "target_mode": target_mode,
                "swept_level": low.level,
                "sweep_extreme": sweep["low"],
                "wick_extension_bps": wick_extension_bps(low.level, float(sweep["low"])),
                "close_back_distance_bps": wick_extension_bps(low.level, float(sweep["close"])),
                "sweep_swing_significance": low.significance,
                "sweep_liquidity_quality": low.quality,
                "sweep_level_age_bars": len(scan) - 1 - low.index,
                "turtle_quality": quality["quality"],
                "turtle_quality_filters": quality,
            },
        )
        if item:
            results.append(item)

    high = next(
        (
            s
            for s in reversed(highs)
            if len(scan) - 1 - s.index >= min_age
            and (not allowed_significances or s.significance in allowed_significances)
            and sweep["high"] > s.level > sweep["close"]
        ),
        None,
    )
    if high is not None:
        quality = _quality("short", sweep, high.level, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
        if not quality["passed"]:
            high = None
    if high is not None and require_smt and not _has_smt_confirmation(cfg, "short", int(sweep["time"]) if require_smt_on_sweep else None):
        high = None
    if high is not None:
        entry = float(sweep["close"] if entry_mode == "close" else high.level)
        stop = buffered_stop("short", float(sweep["high"]), entry, stop_bps)
        stop, min_stop_applied = _apply_min_stop_distance("short", entry, stop, cfg)
        metadata = context_metadata(context, "short", htf_mode, cfg)
        target, target_metadata = _target_for(closed, "short", entry, stop, target_mode, metadata)
        item = setup(
            model_name="turtle_soup",
            direction="short",
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(sweep["time"]),
            score=3,
            reason="Bearish Turtle Soup sweep and close back below liquidity",
            metadata={
                **metadata,
                **target_metadata,
                **_session_metadata(int(sweep["time"]), session_window),
                "entry_mode": entry_mode,
                "stop_mode": "sweep_extreme",
                "turtle_soup_min_stop_applied": min_stop_applied,
                "turtle_soup_min_stop_bps": cfg.get("turtle_soup_min_stop_bps"),
                "target_mode": target_mode,
                "swept_level": high.level,
                "sweep_extreme": sweep["high"],
                "wick_extension_bps": wick_extension_bps(high.level, float(sweep["high"])),
                "close_back_distance_bps": wick_extension_bps(high.level, float(sweep["close"])),
                "sweep_swing_significance": high.significance,
                "sweep_liquidity_quality": high.quality,
                "sweep_level_age_bars": len(scan) - 1 - high.index,
                "turtle_quality": quality["quality"],
                "turtle_quality_filters": quality,
            },
        )
        if item:
            results.append(item)
    return results


def _confirmed_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    scan: list[dict[str, float | int]],
    cfg: dict[str, Any],
    entry_mode: str,
    target_mode: str,
    stop_bps: float,
    min_age: int,
    min_wick_fraction: float,
    min_wick_atr_ratio: float,
    min_close_back_fraction: float,
    max_confirmation_bars: int,
    context: object | None,
    htf_mode: str,
    session_windows: list[str],
    require_killzone: bool,
    require_smt: bool,
    require_confirmation_fvg: bool,
    allowed_significances: set[str],
) -> list:
    if max_confirmation_bars < 1:
        return []
    if require_smt and not _has_smt_confirmation(cfg):
        return []
    current = scan[-1]
    structures = [
        item
        for item in detect_structure_breaks(candles, symbol, timeframe)
        if item.timestamp == int(current["time"])
        and item.displacement_grade in {"valid", "strong"}
        and (item.created_fvg_after_break or not require_confirmation_fvg)
    ]
    if not structures:
        return []

    highs, lows = collect_swings(scan[:-1], symbol, timeframe, left=1, right=1)
    results = []
    for structure in structures:
        side = "long" if structure.direction == "bullish" else "short"
        sweep_match = _find_confirmed_sweep(
            side,
            scan,
            highs,
            lows,
            current,
            min_age,
            max_confirmation_bars,
            min_wick_fraction,
            min_wick_atr_ratio,
            min_close_back_fraction,
            allowed_significances,
        )
        if sweep_match is None:
            continue
        swing, sweep_idx, quality = sweep_match
        sweep = scan[sweep_idx]
        if require_smt and not _has_smt_confirmation(
            cfg,
            side,
            int(sweep["time"]) if cfg.get("turtle_soup_require_smt_on_sweep", False) else None,
        ):
            continue
        session_window = _matching_window(int(sweep["time"]), session_windows)
        if require_killzone and session_window is None:
            continue
        if _closed_beyond_sweep_extreme(side, scan[sweep_idx + 1 :], float(sweep["low"] if side == "long" else sweep["high"])):
            continue
        entry = float(current["close"] if entry_mode == "close" else swing.level)
        stop = buffered_stop(side, float(sweep["low"] if side == "long" else sweep["high"]), entry, stop_bps)
        stop, min_stop_applied = _apply_min_stop_distance(side, entry, stop, cfg)
        metadata = context_metadata(context, side, htf_mode, cfg)
        target, target_metadata = _target_for(candles, side, entry, stop, target_mode, metadata)
        item = setup(
            model_name="turtle_soup",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(current["time"]),
            score=4 if structure.displacement_grade == "strong" else 3,
            reason=f"{side.title()} Turtle Soup sweep, close-back, displacement MSS/FVG confirmation",
            metadata={
                **metadata,
                **target_metadata,
                **_session_metadata(int(sweep["time"]), session_window),
                "entry_mode": entry_mode,
                "stop_mode": "sweep_extreme",
                "turtle_soup_min_stop_applied": min_stop_applied,
                "turtle_soup_min_stop_bps": cfg.get("turtle_soup_min_stop_bps"),
                "target_mode": target_mode,
                "swept_level": swing.level,
                "sweep_extreme": sweep["low"] if side == "long" else sweep["high"],
                "sweep_time": int(sweep["time"]),
                "entry_time": int(current["time"]),
                "mss_time": structure.timestamp,
                "structure_level": structure.broken_level,
                "displacement_grade": structure.displacement_grade,
                "displacement_factor": structure.displacement_factor,
                "body_ratio": structure.body_ratio,
                "range_expansion": structure.range_expansion,
                "created_fvg_after_break": structure.created_fvg_after_break,
                "wick_extension_bps": wick_extension_bps(swing.level, float(sweep["low"] if side == "long" else sweep["high"])),
                "close_back_distance_bps": wick_extension_bps(swing.level, float(sweep["close"])),
                "sweep_swing_significance": swing.significance,
                "sweep_liquidity_quality": swing.quality,
                "sweep_level_age_bars": sweep_idx - swing.index,
                "time_to_confirmation_bars": len(scan) - 1 - sweep_idx,
                "turtle_quality": quality["quality"],
                "turtle_quality_filters": quality,
                "ltf_trigger_type": "mss_displacement_fvg" if structure.created_fvg_after_break else "mss_displacement",
            },
        )
        if item:
            results.append(item)
    return results


def _find_confirmed_sweep(
    side: str,
    scan: list[dict[str, float | int]],
    highs: list,
    lows: list,
    current: dict[str, float | int],
    min_age: int,
    max_confirmation_bars: int,
    min_wick_fraction: float,
    min_wick_atr_ratio: float,
    min_close_back_fraction: float,
    allowed_significances: set[str],
) -> tuple[Any, int, dict[str, Any]] | None:
    latest_idx = len(scan) - 1
    earliest_idx = max(0, latest_idx - max_confirmation_bars)
    swings = lows if side == "long" else highs
    for sweep_idx in range(latest_idx - 1, earliest_idx - 1, -1):
        sweep = scan[sweep_idx]
        average_true_range = avg_range(scan[max(0, sweep_idx - 20) : sweep_idx])
        for swing in reversed(swings):
            if swing.index >= sweep_idx or sweep_idx - swing.index < min_age:
                continue
            if allowed_significances and swing.significance not in allowed_significances:
                continue
            swept = float(sweep["low"]) < swing.level < float(sweep["close"]) if side == "long" else float(sweep["high"]) > swing.level > float(sweep["close"])
            if not swept:
                continue
            quality = _quality(side, sweep, swing.level, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
            if quality["passed"]:
                return swing, sweep_idx, quality
    return None


def _closed_beyond_sweep_extreme(side: str, candles: list[dict[str, float | int]], extreme: float) -> bool:
    if side == "long":
        return any(float(candle["close"]) < extreme for candle in candles)
    return any(float(candle["close"]) > extreme for candle in candles)


def _quality(
    side: str,
    candle: dict[str, float | int],
    level: float,
    atr: float,
    min_wick_fraction: float,
    min_wick_atr_ratio: float,
    min_close_back_fraction: float,
) -> dict[str, Any]:
    high = float(candle["high"])
    low = float(candle["low"])
    close = float(candle["close"])
    candle_range = max(high - low, 1e-9)
    if side == "long":
        wick_extension = max(level - low, 0.0)
        close_back = max(close - level, 0.0)
    else:
        wick_extension = max(high - level, 0.0)
        close_back = max(level - close, 0.0)
    wick_fraction = wick_extension / candle_range
    wick_atr_ratio = wick_extension / max(atr, 1e-9) if atr > 0 else None
    close_back_fraction = close_back / candle_range
    passed_wick_fraction = wick_fraction >= min_wick_fraction
    passed_wick_atr = True if min_wick_atr_ratio <= 0 else bool(wick_atr_ratio is not None and wick_atr_ratio >= min_wick_atr_ratio)
    passed_close_back = close_back_fraction >= min_close_back_fraction
    passed = passed_wick_fraction and passed_wick_atr and passed_close_back
    strong = passed and wick_fraction >= max(min_wick_fraction * 2, 0.25) and close_back_fraction >= max(min_close_back_fraction * 2, 0.12)
    return {
        "passed": passed,
        "quality": "strong" if strong else "valid" if passed else "weak",
        "wick_extension": wick_extension,
        "wick_fraction": round(wick_fraction, 6),
        "wick_atr_ratio": round(wick_atr_ratio, 6) if wick_atr_ratio is not None else None,
        "close_back_fraction": round(close_back_fraction, 6),
        "min_wick_fraction": min_wick_fraction,
        "min_wick_atr_ratio": min_wick_atr_ratio,
        "min_close_back_fraction": min_close_back_fraction,
    }


def _has_smt_confirmation(cfg: dict[str, Any], side: str | None = None, sweep_timestamp: int | None = None) -> bool:
    divergences = cfg.get("smt_divergences") or []
    if side is None:
        return bool(cfg.get("has_smt_confirmation") or divergences)
    expected = "bullish" if side == "long" else "bearish"
    return any(
        getattr(item, "direction", None) == expected
        and (sweep_timestamp is None or int(getattr(item, "timestamp", -1)) == sweep_timestamp)
        for item in divergences
    )


def _target_for(
    candles: list[dict[str, float | int]],
    side: str,
    entry: float,
    stop: float,
    target_mode: str,
    metadata: dict[str, object],
) -> tuple[float, dict[str, object]]:
    if target_mode == "fixed_r":
        return fixed_r_target(side, entry, stop), {"dol_priority": 99, "dol_target_type": "fixed_r", "dol_source": "fixed_r"}
    if target_mode in {"nearest_liquidity", "dol_hierarchy"}:
        return draw_on_liquidity_target(candles, side, entry, stop, metadata)
    return opposite_range_target(candles, side, entry, stop), {}


def _asian_range_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    closed: list[dict[str, float | int]],
    context: object | None,
    cfg: dict[str, Any],
) -> list:
    if len(closed) < 4:
        return []
    current = closed[-1]
    session_windows = _window_list(cfg.get("turtle_soup_session_windows") or [NY_OPEN, NY_PM_SESSION])
    session_window = _matching_window(int(current["time"]), session_windows)
    require_killzone = bool(cfg.get("turtle_soup_require_killzone", True))
    if require_killzone and session_window is None:
        return []
    require_smt = bool(cfg.get("turtle_soup_require_smt", False))
    require_smt_on_sweep = bool(cfg.get("turtle_soup_require_smt_on_sweep", False))
    if require_smt and not _has_smt_confirmation(cfg):
        return []

    range_window = str(cfg.get("turtle_soup_asian_range_window") or "00:00-08:00")
    range_tz = str(cfg.get("turtle_soup_asian_range_tz") or "UTC")
    range_candles, range_start, range_end, range_date = _range_candles_before(
        closed[:-1],
        int(current["time"]),
        range_window,
        range_tz,
    )
    if len(range_candles) < int(cfg.get("turtle_soup_asian_min_range_bars") or 2):
        return []
    range_high = max(float(candle["high"]) for candle in range_candles)
    range_low = min(float(candle["low"]) for candle in range_candles)
    range_mid = (range_high + range_low) / 2
    range_width = range_high - range_low
    if range_width <= 0:
        return []
    range_width_bps = range_width / max(range_mid, 1e-9) * 10_000
    min_range_bps = float(cfg.get("turtle_soup_asian_min_range_bps") or 0.0)
    if range_width_bps < min_range_bps:
        return []

    entry_mode = str(cfg.get("entry_mode") or cfg.get("turtle_entry_mode") or TURTLE_ENTRY_MODE)
    if entry_mode not in {"close", "retest"}:
        entry_mode = TURTLE_ENTRY_MODE
    target_mode = str(cfg.get("target_mode") or TURTLE_TARGET_MODE)
    if target_mode not in {"opposite_range", "nearest_liquidity", "dol_hierarchy", "fixed_r"}:
        target_mode = TURTLE_TARGET_MODE
    stop_bps = float(cfg.get("stop_buffer_bps") or cfg.get("turtle_stop_buffer_bps") or TURTLE_STOP_BUFFER_BPS)
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    min_wick_fraction = float(cfg.get("turtle_soup_min_wick_fraction") or TURTLE_MIN_WICK_FRACTION)
    min_wick_atr_ratio = float(cfg.get("turtle_soup_min_wick_atr_ratio") or TURTLE_MIN_WICK_ATR_RATIO)
    min_close_back_fraction = float(cfg.get("turtle_soup_min_close_back_fraction") or TURTLE_MIN_CLOSE_BACK_FRACTION)
    min_breach_bps = float(cfg.get("turtle_soup_asian_min_breach_bps") or 0.0)
    first_signal_only = bool(cfg.get("turtle_soup_asian_first_signal_only", True))
    reject_prior_failed_sweep = bool(cfg.get("turtle_soup_asian_reject_prior_failed_sweep", False))
    average_true_range = avg_range(closed[:-1])
    results = []

    if float(current["low"]) < range_low < float(current["close"]) and (
        not require_smt or _has_smt_confirmation(cfg, "long", int(current["time"]) if require_smt_on_sweep else None)
    ):
        breach_bps = wick_extension_bps(range_low, float(current["low"]))
        failed_sweep_count = _prior_failed_asian_sweep_count(closed[:-1], range_end, int(current["time"]), "long", range_low)
        if (
            breach_bps >= min_breach_bps
            and not (reject_prior_failed_sweep and failed_sweep_count)
            and not _prior_asian_reclaim(closed[:-1], range_end, int(current["time"]), "long", range_low, first_signal_only)
        ):
            quality = _quality("long", current, range_low, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
            if quality["passed"]:
                entry = float(current["close"] if entry_mode == "close" else range_low)
                stop = buffered_stop("long", float(current["low"]), entry, stop_bps)
                stop, min_stop_applied = _apply_min_stop_distance("long", entry, stop, cfg)
                metadata = context_metadata(context, "long", htf_mode, cfg)
                target, target_metadata = _target_for(candles, "long", entry, stop, target_mode, metadata)
                item = setup(
                    model_name="turtle_soup",
                    direction="long",
                    symbol=symbol,
                    timeframe=timeframe,
                    entry_low=entry,
                    entry_high=entry,
                    entry_price=entry,
                    stop_loss=stop,
                    target_hint=target,
                    timestamp=int(current["time"]),
                    score=3,
                    reason="Bullish Asian range Turtle Soup sweep and reclaim",
                    metadata={
                        **metadata,
                        **target_metadata,
                        **_session_metadata(int(current["time"]), session_window),
                        **_asian_metadata(range_window, range_tz, range_date, range_start, range_end, range_high, range_low, range_width_bps, breach_bps, first_signal_only),
                        "entry_mode": entry_mode,
                        "stop_mode": "asian_sweep_extreme",
                        "turtle_soup_min_stop_applied": min_stop_applied,
                        "turtle_soup_min_stop_bps": cfg.get("turtle_soup_min_stop_bps"),
                        "target_mode": target_mode,
                        "swept_level": range_low,
                        "sweep_extreme": current["low"],
                        "sweep_time": int(current["time"]),
                        "entry_time": int(current["time"]),
                        "asian_failed_sweep_count_before_reclaim": failed_sweep_count,
                        "asian_reject_prior_failed_sweep": reject_prior_failed_sweep,
                        "wick_extension_bps": breach_bps,
                        "close_back_distance_bps": wick_extension_bps(range_low, float(current["close"])),
                        "turtle_quality": quality["quality"],
                        "turtle_quality_filters": quality,
                        "ltf_trigger_type": "asian_range_reclaim",
                    },
                )
                if item:
                    results.append(item)

    if float(current["high"]) > range_high > float(current["close"]) and (
        not require_smt or _has_smt_confirmation(cfg, "short", int(current["time"]) if require_smt_on_sweep else None)
    ):
        breach_bps = wick_extension_bps(range_high, float(current["high"]))
        failed_sweep_count = _prior_failed_asian_sweep_count(closed[:-1], range_end, int(current["time"]), "short", range_high)
        if (
            breach_bps >= min_breach_bps
            and not (reject_prior_failed_sweep and failed_sweep_count)
            and not _prior_asian_reclaim(closed[:-1], range_end, int(current["time"]), "short", range_high, first_signal_only)
        ):
            quality = _quality("short", current, range_high, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
            if quality["passed"]:
                entry = float(current["close"] if entry_mode == "close" else range_high)
                stop = buffered_stop("short", float(current["high"]), entry, stop_bps)
                stop, min_stop_applied = _apply_min_stop_distance("short", entry, stop, cfg)
                metadata = context_metadata(context, "short", htf_mode, cfg)
                target, target_metadata = _target_for(candles, "short", entry, stop, target_mode, metadata)
                item = setup(
                    model_name="turtle_soup",
                    direction="short",
                    symbol=symbol,
                    timeframe=timeframe,
                    entry_low=entry,
                    entry_high=entry,
                    entry_price=entry,
                    stop_loss=stop,
                    target_hint=target,
                    timestamp=int(current["time"]),
                    score=3,
                    reason="Bearish Asian range Turtle Soup sweep and reclaim",
                    metadata={
                        **metadata,
                        **target_metadata,
                        **_session_metadata(int(current["time"]), session_window),
                        **_asian_metadata(range_window, range_tz, range_date, range_start, range_end, range_high, range_low, range_width_bps, breach_bps, first_signal_only),
                        "entry_mode": entry_mode,
                        "stop_mode": "asian_sweep_extreme",
                        "turtle_soup_min_stop_applied": min_stop_applied,
                        "turtle_soup_min_stop_bps": cfg.get("turtle_soup_min_stop_bps"),
                        "target_mode": target_mode,
                        "swept_level": range_high,
                        "sweep_extreme": current["high"],
                        "sweep_time": int(current["time"]),
                        "entry_time": int(current["time"]),
                        "asian_failed_sweep_count_before_reclaim": failed_sweep_count,
                        "asian_reject_prior_failed_sweep": reject_prior_failed_sweep,
                        "wick_extension_bps": breach_bps,
                        "close_back_distance_bps": wick_extension_bps(range_high, float(current["close"])),
                        "turtle_quality": quality["quality"],
                        "turtle_quality_filters": quality,
                        "ltf_trigger_type": "asian_range_reclaim",
                    },
                )
                if item:
                    results.append(item)
    return results


def _range_candles_before(
    candles: list[dict[str, float | int]],
    current_timestamp: int,
    window: str,
    tz_name: str,
) -> tuple[list[dict[str, float | int]], int, int, str]:
    zone = ZoneInfo(tz_name)
    current_dt = datetime.fromtimestamp(current_timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(zone)
    start_time, end_time = (_parse_time(part) for part in window.split("-", 1))
    end_date = current_dt.date()
    if end_time <= start_time:
        range_date = end_date - timedelta(days=1)
    else:
        if current_dt.time() <= end_time:
            end_date -= timedelta(days=1)
        range_date = end_date
    start_dt = datetime.combine(range_date, start_time, tzinfo=zone)
    end_dt = datetime.combine(end_date, end_time, tzinfo=zone)
    start_ms = int(start_dt.astimezone(ZoneInfo("UTC")).timestamp() * 1000)
    end_ms = int(end_dt.astimezone(ZoneInfo("UTC")).timestamp() * 1000)
    return [candle for candle in candles if start_ms <= int(candle["time"]) <= end_ms], start_ms, end_ms, range_date.isoformat()


def _prior_asian_reclaim(
    candles: list[dict[str, float | int]],
    after_timestamp: int,
    before_timestamp: int,
    side: str,
    level: float,
    first_signal_only: bool,
) -> bool:
    if not first_signal_only:
        return False
    for candle in candles:
        ts = int(candle["time"])
        if ts <= after_timestamp or ts >= before_timestamp:
            continue
        if side == "long" and float(candle["low"]) < level < float(candle["close"]):
            return True
        if side == "short" and float(candle["high"]) > level > float(candle["close"]):
            return True
    return False


def _prior_failed_asian_sweep_count(
    candles: list[dict[str, float | int]],
    after_timestamp: int,
    before_timestamp: int,
    side: str,
    level: float,
) -> int:
    failed = 0
    for candle in candles:
        ts = int(candle["time"])
        if ts <= after_timestamp or ts >= before_timestamp:
            continue
        if side == "long" and float(candle["low"]) < level and float(candle["close"]) <= level:
            failed += 1
        if side == "short" and float(candle["high"]) > level and float(candle["close"]) >= level:
            failed += 1
    return failed


def _apply_min_stop_distance(side: str, entry: float, stop: float, cfg: dict[str, Any]) -> tuple[float, bool]:
    min_stop_bps = float(cfg.get("turtle_soup_min_stop_bps") or 0.0)
    if min_stop_bps <= 0:
        return stop, False
    min_risk = entry * min_stop_bps / 10_000.0
    current_risk = abs(entry - stop)
    if current_risk >= min_risk:
        return stop, False
    if side == "long":
        return entry - min_risk, True
    return entry + min_risk, True


def _asian_metadata(
    range_window: str,
    range_tz: str,
    range_date: str,
    range_start: int,
    range_end: int,
    range_high: float,
    range_low: float,
    range_width_bps: float,
    breach_bps: float,
    first_signal_only: bool,
) -> dict[str, object]:
    return {
        "range_source": "asian_range",
        "asian_range_window": range_window,
        "asian_range_tz": range_tz,
        "asian_range_date": range_date,
        "asian_range_start": range_start,
        "asian_range_end": range_end,
        "asian_range_high": range_high,
        "asian_range_low": range_low,
        "asian_range_width_bps": round(range_width_bps, 6),
        "asian_sweep_breach_bps": round(breach_bps, 6),
        "asian_first_signal_only": first_signal_only,
    }


def _default_session_windows() -> list[str]:
    return [LONDON_OPEN, NY_OPEN, NY_PM_SESSION]


def _window_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return [str(item).strip() for item in value if str(item).strip()]


def _matching_window(timestamp: int, windows: list[str]) -> str | None:
    return next((window for window in windows if in_ny_windows(timestamp, window)), None)


def _session_metadata(timestamp: int, window: str | None) -> dict[str, object]:
    if window is None:
        return {}
    dt = datetime.fromtimestamp(timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(ZoneInfo(NY_TZ))
    return {
        "session_window": window,
        "session_date": dt.strftime("%Y-%m-%d"),
        "session_label": _session_label(window),
        "ny_time": dt.strftime("%Y-%m-%d %H:%M"),
        "session_filter": "configured",
    }


def _session_label(window: str) -> str:
    start = _parse_time(window.split("-", 1)[0])
    if start < time(5, 0):
        return "london_open"
    if start < time(10, 0):
        return "ny_open"
    if start < time(12, 0):
        return "ny_am"
    if start >= time(13, 30) and start < time(16, 0):
        return "ny_pm"
    return "custom"


def _parse_time(value: str) -> time:
    hour, minute = value.split(":", 1)
    return time(int(hour), int(minute))


__all__ = ["detect_setups"]
