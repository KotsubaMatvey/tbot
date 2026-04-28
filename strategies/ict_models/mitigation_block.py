from __future__ import annotations

from typing import Any

from market_primitives.common import Candle, collect_swings

from .common import buffered_stop, closed_candles, context_metadata, nearest_liquidity_target, setup
from .sessions import LONDON_OPEN, NY_OPEN, in_ny_windows

ENABLED_BY_DEFAULT = False
RESEARCH_ONLY = True
MITIGATION_ENTRY_MODE = "body_zone_retest"
MITIGATION_STOP_MODE = "block_extreme"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if len(closed) < 20:
        return []
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    require_killzone = bool(cfg.get("mitigation_block_require_killzone", False))
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    scan = closed[-100:]
    current = scan[-1]
    if require_killzone and not in_ny_windows(int(current["time"]), [LONDON_OPEN, NY_OPEN]):
        return []
    highs, lows = collect_swings(scan[:-1], symbol, timeframe)

    short_setup = _bearish_failure(symbol, timeframe, scan, current, highs, stop_bps, context, htf_mode, cfg)
    if short_setup is not None:
        return [short_setup]
    long_setup = _bullish_failure(symbol, timeframe, scan, current, lows, stop_bps, context, htf_mode, cfg)
    return [long_setup] if long_setup is not None else []


def _bearish_failure(
    symbol: str,
    timeframe: str,
    candles: list[Candle],
    current: Candle,
    highs: list,
    stop_bps: float,
    context: object | None,
    htf_mode: str,
    cfg: dict[str, Any],
):
    if len(highs) < 2:
        return None
    first, second = highs[-2], highs[-1]
    if second.level >= first.level:
        return None
    pivot_low = min(float(candle["low"]) for candle in candles[first.index : second.index + 1])
    break_idx = next((idx for idx in range(second.index + 1, len(candles) - 1) if float(candles[idx]["close"]) < pivot_low), None)
    if break_idx is None:
        return None
    block = _last_opposite_candle(candles[first.index : break_idx + 1], bullish=False)
    if block is None:
        return None
    low, high = _body_zone(block)
    if not _touches_zone(current, low, high):
        return None
    entry = low
    stop = buffered_stop("short", float(block["high"]), entry, stop_bps)
    metadata = context_metadata(context, "short", htf_mode, cfg)
    return setup(
        model_name="mitigation_block",
        direction="short",
        symbol=symbol,
        timeframe=timeframe,
        entry_low=low,
        entry_high=high,
        entry_price=entry,
        stop_loss=stop,
        target_hint=nearest_liquidity_target(candles, "short", entry, stop),
        timestamp=int(current["time"]),
        score=2,
        reason="Bearish mitigation block after failure swing and MSS",
        metadata={
            **metadata,
            "entry_mode": MITIGATION_ENTRY_MODE,
            "stop_mode": MITIGATION_STOP_MODE,
            "target_mode": "nearest_liquidity",
            "mitigation_low": low,
            "mitigation_high": high,
            "mitigation_block_time": int(block["time"]),
            "failure_swing_time": second.timestamp,
            "mss_time": int(candles[break_idx]["time"]),
            "entry_time": int(current["time"]),
        },
    )


def _bullish_failure(
    symbol: str,
    timeframe: str,
    candles: list[Candle],
    current: Candle,
    lows: list,
    stop_bps: float,
    context: object | None,
    htf_mode: str,
    cfg: dict[str, Any],
):
    if len(lows) < 2:
        return None
    first, second = lows[-2], lows[-1]
    if second.level <= first.level:
        return None
    pivot_high = max(float(candle["high"]) for candle in candles[first.index : second.index + 1])
    break_idx = next((idx for idx in range(second.index + 1, len(candles) - 1) if float(candles[idx]["close"]) > pivot_high), None)
    if break_idx is None:
        return None
    block = _last_opposite_candle(candles[first.index : break_idx + 1], bullish=True)
    if block is None:
        return None
    low, high = _body_zone(block)
    if not _touches_zone(current, low, high):
        return None
    entry = high
    stop = buffered_stop("long", float(block["low"]), entry, stop_bps)
    metadata = context_metadata(context, "long", htf_mode, cfg)
    return setup(
        model_name="mitigation_block",
        direction="long",
        symbol=symbol,
        timeframe=timeframe,
        entry_low=low,
        entry_high=high,
        entry_price=entry,
        stop_loss=stop,
        target_hint=nearest_liquidity_target(candles, "long", entry, stop),
        timestamp=int(current["time"]),
        score=2,
        reason="Bullish mitigation block after failure swing and MSS",
        metadata={
            **metadata,
            "entry_mode": MITIGATION_ENTRY_MODE,
            "stop_mode": MITIGATION_STOP_MODE,
            "target_mode": "nearest_liquidity",
            "mitigation_low": low,
            "mitigation_high": high,
            "mitigation_block_time": int(block["time"]),
            "failure_swing_time": second.timestamp,
            "mss_time": int(candles[break_idx]["time"]),
            "entry_time": int(current["time"]),
        },
    )


def _last_opposite_candle(candles: list[Candle], *, bullish: bool) -> Candle | None:
    for candle in reversed(candles):
        is_bullish = float(candle["close"]) > float(candle["open"])
        if is_bullish == bullish:
            return candle
    return None


def _body_zone(candle: Candle) -> tuple[float, float]:
    return sorted((float(candle["open"]), float(candle["close"])))


def _touches_zone(candle: Candle, low: float, high: float) -> bool:
    return float(candle["low"]) <= high and float(candle["high"]) >= low


__all__ = ["ENABLED_BY_DEFAULT", "RESEARCH_ONLY", "detect_setups"]
