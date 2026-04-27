from __future__ import annotations

from typing import Any

from market_primitives.common import collect_swings

from .common import buffered_stop, closed_candles, opposite_range_target, setup, wick_extension_bps

TURTLE_LOOKBACK_BARS = 50
TURTLE_MIN_SWING_AGE = 5
TURTLE_ENTRY_MODE = "close"
TURTLE_TARGET_MODE = "opposite_range"
TURTLE_STOP_BUFFER_BPS = 2


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
    if len(closed) < min_age + 5:
        return []

    scan = closed[-lookback:]
    sweep = scan[-1]
    highs, lows = collect_swings(scan[:-1], symbol, timeframe, left=1, right=1)
    results = []
    low = next((s for s in reversed(lows) if len(scan) - 1 - s.index >= min_age and sweep["low"] < s.level < sweep["close"]), None)
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
            },
        )
        if item:
            results.append(item)

    high = next((s for s in reversed(highs) if len(scan) - 1 - s.index >= min_age and sweep["high"] > s.level > sweep["close"]), None)
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
            },
        )
        if item:
            results.append(item)
    return results


__all__ = ["detect_setups"]
