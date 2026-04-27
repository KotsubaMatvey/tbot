from __future__ import annotations

from typing import Any

from market_primitives.common import Candle, average_range, collect_swings
from strategies.risk_policy import price_buffer
from strategies.types import EntrySetup, default_components


def closed_candles(candles: list[Candle]) -> list[Candle]:
    return candles[:-1] if len(candles) > 1 else list(candles)


def setup(
    *,
    model_name: str,
    direction: str,
    symbol: str,
    timeframe: str,
    entry_low: float,
    entry_high: float,
    stop_loss: float,
    target_hint: float | None,
    timestamp: int,
    score: int,
    reason: str,
    metadata: dict[str, Any],
) -> EntrySetup | None:
    entry_price = (entry_low + entry_high) / 2
    risk = entry_price - stop_loss if direction == "long" else stop_loss - entry_price
    if risk <= 0:
        return None
    components = default_components()
    return EntrySetup(
        model_name=model_name,
        model_family="ict",
        direction="long" if direction == "long" else "short",
        symbol=symbol,
        timeframe=timeframe,
        status="triggered",
        entry_low=entry_low,
        entry_high=entry_high,
        entry_price=entry_price,
        stop_loss=stop_loss,
        invalidation=stop_loss,
        target_hint=target_hint,
        sweep_level=metadata.get("swept_level") or metadata.get("sweep_level"),
        structure_level=metadata.get("structure_level"),
        context_timeframe=None,
        score=score,
        reason=reason,
        components=components,
        timestamp=timestamp,
        metadata={
            "model_family": "ict",
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "risk": risk,
            "risk_bps": risk / max(entry_price, 1e-9) * 10_000,
            **metadata,
        },
    )


def buffered_stop(side: str, ref: float, price: float, bps: float) -> float:
    buffer = price_buffer(price, stop_buffer_bps=bps)
    return ref - buffer if side == "long" else ref + buffer


def fixed_r_target(side: str, entry: float, stop: float, multiple: float = 2.0) -> float:
    risk = abs(entry - stop)
    return entry + risk * multiple if side == "long" else entry - risk * multiple


def nearest_liquidity_target(candles: list[Candle], side: str, entry: float, fallback_stop: float) -> float:
    scan = closed_candles(candles)[-80:]
    highs, lows = collect_swings(scan, "", "")
    if side == "long":
        candidates = [s.level for s in highs if s.level > entry]
        return min(candidates) if candidates else fixed_r_target(side, entry, fallback_stop)
    candidates = [s.level for s in lows if s.level < entry]
    return max(candidates) if candidates else fixed_r_target(side, entry, fallback_stop)


def opposite_range_target(candles: list[Candle], side: str, entry: float, stop: float, lookback: int = 50) -> float:
    scan = closed_candles(candles)[-lookback:]
    if not scan:
        return fixed_r_target(side, entry, stop)
    return max(float(c["high"]) for c in scan) if side == "long" else min(float(c["low"]) for c in scan)


def wick_extension_bps(level: float, extreme: float) -> float:
    return abs(extreme - level) / max(level, 1e-9) * 10_000


def avg_range(candles: list[Candle], lookback: int = 20) -> float:
    return average_range(closed_candles(candles)[-lookback:])


__all__ = [
    "avg_range",
    "buffered_stop",
    "closed_candles",
    "fixed_r_target",
    "nearest_liquidity_target",
    "opposite_range_target",
    "setup",
    "wick_extension_bps",
]
