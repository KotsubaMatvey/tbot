from __future__ import annotations

from typing import Any

from market_primitives.common import collect_swings

from .common import avg_range, buffered_stop, closed_candles, opposite_range_target, setup, wick_extension_bps

TURTLE_LOOKBACK_BARS = 50
TURTLE_MIN_SWING_AGE = 5
TURTLE_ENTRY_MODE = "close"
TURTLE_TARGET_MODE = "opposite_range"
TURTLE_STOP_BUFFER_BPS = 2
TURTLE_MIN_WICK_FRACTION = 0.10
TURTLE_MIN_WICK_ATR_RATIO = 0.0
TURTLE_MIN_CLOSE_BACK_FRACTION = 0.05
TURTLE_MAX_CONFIRMATION_BARS = 1


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    entry_mode = str(cfg.get("entry_mode") or cfg.get("turtle_entry_mode") or TURTLE_ENTRY_MODE)
    if entry_mode not in {"close", "retest"}:
        entry_mode = TURTLE_ENTRY_MODE
    target_mode = str(cfg.get("target_mode") or TURTLE_TARGET_MODE)
    stop_bps = float(cfg.get("stop_buffer_bps") or cfg.get("turtle_stop_buffer_bps") or TURTLE_STOP_BUFFER_BPS)
    lookback = int(cfg.get("turtle_lookback_bars") or TURTLE_LOOKBACK_BARS)
    min_age = int(cfg.get("turtle_min_swing_age") or TURTLE_MIN_SWING_AGE)
    min_wick_fraction = float(cfg.get("turtle_soup_min_wick_fraction") or TURTLE_MIN_WICK_FRACTION)
    min_wick_atr_ratio = float(cfg.get("turtle_soup_min_wick_atr_ratio") or TURTLE_MIN_WICK_ATR_RATIO)
    min_close_back_fraction = float(cfg.get("turtle_soup_min_close_back_fraction") or TURTLE_MIN_CLOSE_BACK_FRACTION)
    max_confirmation_bars = int(cfg.get("turtle_soup_max_confirmation_bars") or TURTLE_MAX_CONFIRMATION_BARS)
    require_killzone = bool(cfg.get("turtle_soup_require_killzone", False))
    require_smt = bool(cfg.get("turtle_soup_require_smt", False))
    if len(closed) < min_age + 5:
        return []

    scan = closed[-lookback:]
    sweep = scan[-1]
    highs, lows = collect_swings(scan[:-1], symbol, timeframe, left=1, right=1)
    results = []
    if max_confirmation_bars < 1 or require_killzone or require_smt:
        if max_confirmation_bars < 1:
            return []
        if require_killzone and not _in_default_killzone(int(sweep["time"])):
            return []
        if require_smt and not bool(getattr(context, "has_smt_confirmation", False)):
            return []

    average_true_range = avg_range(scan[:-1])
    low = next((s for s in reversed(lows) if len(scan) - 1 - s.index >= min_age and sweep["low"] < s.level < sweep["close"]), None)
    if low is not None:
        quality = _quality("long", sweep, low.level, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
        if not quality["passed"]:
            low = None
    if low is not None:
        entry = float(sweep["close"] if entry_mode == "close" else low.level)
        stop = buffered_stop("long", float(sweep["low"]), entry, stop_bps)
        target = opposite_range_target(scan, "long", entry, stop) if target_mode == "opposite_range" else None
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
                "entry_mode": entry_mode,
                "stop_mode": "sweep_extreme",
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

    high = next((s for s in reversed(highs) if len(scan) - 1 - s.index >= min_age and sweep["high"] > s.level > sweep["close"]), None)
    if high is not None:
        quality = _quality("short", sweep, high.level, average_true_range, min_wick_fraction, min_wick_atr_ratio, min_close_back_fraction)
        if not quality["passed"]:
            high = None
    if high is not None:
        entry = float(sweep["close"] if entry_mode == "close" else high.level)
        stop = buffered_stop("short", float(sweep["high"]), entry, stop_bps)
        target = opposite_range_target(scan, "short", entry, stop) if target_mode == "opposite_range" else None
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
                "entry_mode": entry_mode,
                "stop_mode": "sweep_extreme",
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


def _in_default_killzone(timestamp: int) -> bool:
    from datetime import datetime
    from zoneinfo import ZoneInfo

    value = datetime.fromtimestamp(timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(ZoneInfo("America/New_York")).time()
    return (8 <= value.hour < 11) or (13 <= value.hour < 16)


__all__ = ["detect_setups"]
