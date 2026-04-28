from __future__ import annotations

from math import sqrt

from .common import Candle, SMTDivergence, collect_swings

SMT_LOOKBACK_BARS = 50
SMT_MAX_TIME_DELTA_BARS = 10
SMT_MIN_DIVERGENCE_BPS = 5.0
SMT_MIN_CORRELATION = 0.7


def detect_smt(
    candles_a: list[Candle],
    candles_b: list[Candle],
    symbol_a: str,
    symbol_b: str,
    timeframe: str,
    *,
    lookback_bars: int = SMT_LOOKBACK_BARS,
    max_time_delta_bars: int = SMT_MAX_TIME_DELTA_BARS,
    min_divergence_bps: float = SMT_MIN_DIVERGENCE_BPS,
    min_correlation: float = SMT_MIN_CORRELATION,
) -> list[SMTDivergence]:
    aligned_a, aligned_b = _aligned(candles_a, candles_b, lookback_bars)
    if len(aligned_a) < 10:
        return []
    correlation = _return_correlation(aligned_a, aligned_b)
    if correlation is not None and correlation < min_correlation:
        return []

    swing_highs_a, swing_lows_a = collect_swings(aligned_a, symbol_a, timeframe, left=1, right=1)
    swing_highs_b, swing_lows_b = collect_swings(aligned_b, symbol_b, timeframe, left=1, right=1)
    results: list[SMTDivergence] = []

    bullish = _bullish_smt(
        swing_lows_a,
        swing_lows_b,
        max_time_delta_bars,
        min_divergence_bps,
    )
    if bullish is not None:
        primary, secondary, strength = bullish
        results.append(
            SMTDivergence(
                symbol=symbol_a,
                timeframe=timeframe,
                direction="bullish",
                timestamp=primary.timestamp,
                primary_level=primary.level,
                secondary_symbol=symbol_b,
                secondary_level=secondary.level,
                strength=strength,
                metadata={
                    "primary_role": "benchmark",
                    "secondary_role": "confirmation",
                    "smt_pair": f"{symbol_a}:{symbol_b}",
                    "correlation": correlation,
                    "min_divergence_bps": min_divergence_bps,
                    "max_time_delta_bars": max_time_delta_bars,
                },
            )
        )

    bearish = _bearish_smt(
        swing_highs_a,
        swing_highs_b,
        max_time_delta_bars,
        min_divergence_bps,
    )
    if bearish is not None:
        primary, secondary, strength = bearish
        results.append(
            SMTDivergence(
                symbol=symbol_a,
                timeframe=timeframe,
                direction="bearish",
                timestamp=primary.timestamp,
                primary_level=primary.level,
                secondary_symbol=symbol_b,
                secondary_level=secondary.level,
                strength=strength,
                metadata={
                    "primary_role": "benchmark",
                    "secondary_role": "confirmation",
                    "smt_pair": f"{symbol_a}:{symbol_b}",
                    "correlation": correlation,
                    "min_divergence_bps": min_divergence_bps,
                    "max_time_delta_bars": max_time_delta_bars,
                },
            )
        )
    return results


def _aligned(candles_a: list[Candle], candles_b: list[Candle], lookback_bars: int) -> tuple[list[Candle], list[Candle]]:
    candles_b_by_time = {int(c["time"]): c for c in candles_b[-lookback_bars:]}
    aligned_a: list[Candle] = []
    aligned_b: list[Candle] = []
    for candle in candles_a[-lookback_bars:]:
        other = candles_b_by_time.get(int(candle["time"]))
        if other is not None:
            aligned_a.append(candle)
            aligned_b.append(other)
    return aligned_a, aligned_b


def _bullish_smt(lows_a, lows_b, max_delta: int, min_bps: float):
    if len(lows_a) < 2 or len(lows_b) < 2:
        return None
    prev_a, current_a = lows_a[-2], lows_a[-1]
    prev_b, current_b = lows_b[-2], lows_b[-1]
    if abs(current_a.index - current_b.index) > max_delta:
        return None
    primary_move = _bps(prev_a.level, current_a.level)
    secondary_move = _bps(prev_b.level, current_b.level)
    if current_a.level < prev_a.level and current_b.level > prev_b.level and primary_move >= min_bps and secondary_move >= min_bps:
        return current_a, current_b, _strength(primary_move, secondary_move)
    return None


def _bearish_smt(highs_a, highs_b, max_delta: int, min_bps: float):
    if len(highs_a) < 2 or len(highs_b) < 2:
        return None
    prev_a, current_a = highs_a[-2], highs_a[-1]
    prev_b, current_b = highs_b[-2], highs_b[-1]
    if abs(current_a.index - current_b.index) > max_delta:
        return None
    primary_move = _bps(prev_a.level, current_a.level)
    secondary_move = _bps(prev_b.level, current_b.level)
    if current_a.level > prev_a.level and current_b.level < prev_b.level and primary_move >= min_bps and secondary_move >= min_bps:
        return current_a, current_b, _strength(primary_move, secondary_move)
    return None


def _bps(first: float, second: float) -> float:
    return abs(second - first) / max(abs(first), 1e-9) * 10_000


def _strength(primary_bps: float, secondary_bps: float) -> float:
    return min(1.0, (primary_bps + secondary_bps) / 100.0)


def _return_correlation(candles_a: list[Candle], candles_b: list[Candle]) -> float | None:
    if len(candles_a) < 3 or len(candles_a) != len(candles_b):
        return None
    returns_a = _returns(candles_a)
    returns_b = _returns(candles_b)
    if len(returns_a) < 2:
        return None
    mean_a = sum(returns_a) / len(returns_a)
    mean_b = sum(returns_b) / len(returns_b)
    num = sum((a - mean_a) * (b - mean_b) for a, b in zip(returns_a, returns_b))
    den_a = sqrt(sum((a - mean_a) ** 2 for a in returns_a))
    den_b = sqrt(sum((b - mean_b) ** 2 for b in returns_b))
    if den_a <= 0 or den_b <= 0:
        return None
    return num / (den_a * den_b)


def _returns(candles: list[Candle]) -> list[float]:
    values = [float(c["close"]) for c in candles]
    return [(values[idx] - values[idx - 1]) / max(values[idx - 1], 1e-9) for idx in range(1, len(values))]


__all__ = ["detect_smt"]
