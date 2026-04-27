from __future__ import annotations

from config import EQ_ATR_MULT, EQ_TOLERANCE_BPS, MIN_EQ_TOUCHES

from .common import Candle, EqualLiquidityLevel, KeyLevel, average_range, cluster_levels, collect_swings


def detect_eqh(candles: list[Candle], symbol: str, timeframe: str, tolerance: float | None = None) -> list[EqualLiquidityLevel]:
    if len(candles) < 20:
        return []
    current = candles[-1]
    swing_highs, _ = collect_swings(candles[-50:-1], symbol, timeframe)
    tol = _tolerance(current["high"], candles, tolerance)
    groups = _equal_level_groups([swing.level for swing in swing_highs], tol)
    results: list[EqualLiquidityLevel] = []
    for group in groups:
        level = sum(group) / len(group)
        proximity = abs(current["high"] - level) / level
        if current["high"] <= level and proximity <= max(0.002, tol):
            results.append(
                EqualLiquidityLevel(
                    symbol=symbol,
                    timeframe=timeframe,
                    direction="bearish",
                    timestamp=current["time"],
                    level=level,
                    touches=len(group),
                    tolerance=tol,
                    metadata={"objective_liquidity_quality": "strong", "objective_is_equal_high_low": True},
                )
            )
    return results


def detect_eql(candles: list[Candle], symbol: str, timeframe: str, tolerance: float | None = None) -> list[EqualLiquidityLevel]:
    if len(candles) < 20:
        return []
    current = candles[-1]
    _, swing_lows = collect_swings(candles[-50:-1], symbol, timeframe)
    tol = _tolerance(current["low"], candles, tolerance)
    groups = _equal_level_groups([swing.level for swing in swing_lows], tol)
    results: list[EqualLiquidityLevel] = []
    for group in groups:
        level = sum(group) / len(group)
        proximity = abs(current["low"] - level) / level
        if current["low"] >= level and proximity <= max(0.002, tol):
            results.append(
                EqualLiquidityLevel(
                    symbol=symbol,
                    timeframe=timeframe,
                    direction="bullish",
                    timestamp=current["time"],
                    level=level,
                    touches=len(group),
                    tolerance=tol,
                    metadata={"objective_liquidity_quality": "strong", "objective_is_equal_high_low": True},
                )
            )
    return results


def detect_key_levels(candles: list[Candle], symbol: str, timeframe: str) -> list[KeyLevel]:
    if len(candles) < 35:
        return []
    closed = candles[:-1]
    swing_highs, swing_lows = collect_swings(closed[-60:], symbol, timeframe)
    levels = [item.level for item in swing_highs] + [item.level for item in swing_lows]
    clusters = cluster_levels(levels, tolerance=0.0025)
    current = closed[-1]
    results: list[KeyLevel] = []
    for cluster in clusters:
        if len(cluster) < 2:
            continue
        level = sum(cluster) / len(cluster)
        proximity = abs(current["close"] - level) / level
        if proximity > 0.0035:
            continue
        direction = "bullish" if current["close"] >= level else "bearish"
        bias = "support" if direction == "bullish" else "resistance"
        results.append(
            KeyLevel(
                symbol=symbol,
                timeframe=timeframe,
                direction=direction,
                timestamp=current["time"],
                level=level,
                touches=len(cluster),
                bias=bias,
            )
        )
    return sorted(results, key=lambda item: (-item.touches, abs(current["close"] - item.level)))


def _equal_level_groups(levels: list[float], tolerance: float) -> list[list[float]]:
    groups: list[list[float]] = []
    consumed: set[int] = set()
    for index, level in enumerate(levels):
        if index in consumed:
            continue
        group = [level]
        for other_index in range(index + 1, len(levels)):
            other = levels[other_index]
            if level > 0 and abs(other - level) / level <= tolerance:
                consumed.add(other_index)
                group.append(other)
        if len(group) >= MIN_EQ_TOUCHES:
            groups.append(group)
    return groups


def _tolerance(price: float, candles: list[Candle], override: float | None) -> float:
    if override is not None:
        return override
    atr = average_range(candles[-20:]) if candles else 0.0
    absolute = max(price * EQ_TOLERANCE_BPS / 10_000, atr * EQ_ATR_MULT)
    return absolute / max(price, 1e-9)


__all__ = ["detect_eqh", "detect_eql", "detect_key_levels"]
