from __future__ import annotations

from typing import Any

from market_primitives.common import collect_swings

from .common import buffered_stop, closed_candles, context_metadata, draw_on_liquidity_target, setup
from .sessions import LONDON_OPEN, NY_OPEN, in_ny_windows

ENABLED_BY_DEFAULT = False
RESEARCH_ONLY = True
REJECTION_ENTRY_MODE = "body_level"
REJECTION_STOP_MODE = "wick_extreme"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if len(closed) < 10:
        return []
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    require_killzone = bool(cfg.get("rejection_block_require_killzone", False))
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    scan = closed[-120:]
    current = scan[-1]
    if require_killzone and not in_ny_windows(int(current["time"]), [LONDON_OPEN, NY_OPEN]):
        return []
    highs, lows = collect_swings(scan[:-1], symbol, timeframe, left=1, right=1)
    results = []
    current_idx = len(scan) - 1

    high = next((item for item in reversed(highs) if item.body_level is not None and _short_retest_valid(scan, item.index, current_idx, float(item.body_level), float(item.level))), None)
    if high is not None:
        body_level = float(high.body_level)
        wick_extreme = float(high.level)
        entry = body_level
        stop = buffered_stop("short", wick_extreme, entry, stop_bps)
        metadata = context_metadata(context, "short", htf_mode, cfg)
        target, target_metadata = draw_on_liquidity_target(closed, "short", entry, stop, metadata)
        item = setup(
            model_name="rejection_block",
            direction="short",
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(high.timestamp),
            score=2,
            reason="Bearish rejection block limit retest at highest swing body",
            metadata={
                **metadata,
                **target_metadata,
                "entry_mode": REJECTION_ENTRY_MODE,
                "stop_mode": REJECTION_STOP_MODE,
                "target_mode": "dol_hierarchy",
                "session_filter": "london_or_ny_open" if require_killzone else "off",
                "entry_time": int(current["time"]),
                "rejection_body_level": body_level,
                "rejection_wick_extreme": wick_extreme,
                "current_wick_extreme": float(current["high"]),
                "source_swing_time": high.timestamp,
                "source_swing_significance": high.significance,
                "rejection_wick_fraction": _upper_wick_fraction(scan[high.index]),
            },
        )
        if item:
            results.append(item)

    low = next((item for item in reversed(lows) if item.body_level is not None and _long_retest_valid(scan, item.index, current_idx, float(item.body_level), float(item.level))), None)
    if low is not None:
        body_level = float(low.body_level)
        wick_extreme = float(low.level)
        entry = body_level
        stop = buffered_stop("long", wick_extreme, entry, stop_bps)
        metadata = context_metadata(context, "long", htf_mode, cfg)
        target, target_metadata = draw_on_liquidity_target(closed, "long", entry, stop, metadata)
        item = setup(
            model_name="rejection_block",
            direction="long",
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(low.timestamp),
            score=2,
            reason="Bullish rejection block limit retest at lowest swing body",
            metadata={
                **metadata,
                **target_metadata,
                "entry_mode": REJECTION_ENTRY_MODE,
                "stop_mode": REJECTION_STOP_MODE,
                "target_mode": "dol_hierarchy",
                "session_filter": "london_or_ny_open" if require_killzone else "off",
                "entry_time": int(current["time"]),
                "rejection_body_level": body_level,
                "rejection_wick_extreme": wick_extreme,
                "current_wick_extreme": float(current["low"]),
                "source_swing_time": low.timestamp,
                "source_swing_significance": low.significance,
                "rejection_wick_fraction": _lower_wick_fraction(scan[low.index]),
            },
        )
        if item:
            results.append(item)

    return results[:1]


def _short_retest_valid(candles: list[dict[str, float | int]], swing_idx: int, current_idx: int, body_level: float, wick_high: float) -> bool:
    if current_idx <= swing_idx:
        return False
    current = candles[current_idx]
    if float(current["high"]) < body_level:
        return False
    for candle in candles[swing_idx + 1 : current_idx + 1]:
        if float(candle["high"]) > wick_high or float(candle["close"]) > wick_high:
            return False
    return True


def _long_retest_valid(candles: list[dict[str, float | int]], swing_idx: int, current_idx: int, body_level: float, wick_low: float) -> bool:
    if current_idx <= swing_idx:
        return False
    current = candles[current_idx]
    if float(current["low"]) > body_level:
        return False
    for candle in candles[swing_idx + 1 : current_idx + 1]:
        if float(candle["low"]) < wick_low or float(candle["close"]) < wick_low:
            return False
    return True


def _upper_wick_fraction(candle: dict[str, float | int]) -> float:
    body_high = max(float(candle["open"]), float(candle["close"]))
    return max(0.0, float(candle["high"]) - body_high) / max(float(candle["high"]) - float(candle["low"]), 1e-9)


def _lower_wick_fraction(candle: dict[str, float | int]) -> float:
    body_low = min(float(candle["open"]), float(candle["close"]))
    return max(0.0, body_low - float(candle["low"])) / max(float(candle["high"]) - float(candle["low"]), 1e-9)


__all__ = ["ENABLED_BY_DEFAULT", "RESEARCH_ONLY", "detect_setups"]
