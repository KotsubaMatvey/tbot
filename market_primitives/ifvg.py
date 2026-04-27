from __future__ import annotations

from .common import Candle, InvertedFVG, in_zone
from .displacement import evaluate_displacement
from .fvg import detect_fvg


def detect_ifvg(candles: list[Candle], symbol: str, timeframe: str) -> list[InvertedFVG]:
    if len(candles) < 5:
        return []

    closed = candles[:-1] if len(candles) > 1 else candles
    gaps = detect_fvg(candles, symbol, timeframe)
    results: list[InvertedFVG] = []

    for gap in gaps:
        if not gap.invalidated or gap.invalidated_at is None:
            continue

        breach_idx = next((idx for idx, candle in enumerate(closed) if candle["time"] == gap.invalidated_at), None)
        if breach_idx is None:
            continue
        breach_candle = closed[breach_idx]
        if gap.direction == "bearish":
            body_breached = float(breach_candle["close"]) > gap.gap_high
            direction = "bullish"
        else:
            body_breached = float(breach_candle["close"]) < gap.gap_low
            direction = "bearish"
        if not body_breached:
            continue

        displacement = evaluate_displacement(
            closed,
            breach_idx,
            direction=direction,
            structure_level=gap.gap_high if direction == "bullish" else gap.gap_low,
            created_fvg_after_break=True,
        )
        if not displacement.has_displacement:
            continue

        retest_at = None
        retest_depth = None
        time_to_retest_bars = None
        for candle in closed[breach_idx + 1 :]:
            if in_zone(candle, gap.gap_low, gap.gap_high):
                retest_at = candle["time"]
                time_to_retest_bars = closed.index(candle) - breach_idx
                retest_depth = _retest_depth(candle, gap.gap_low, gap.gap_high, direction)
                break

        mean_threshold = (gap.gap_low + gap.gap_high) / 2
        grade = "strong" if displacement.displacement_grade == "strong" and retest_at is not None else "valid"
        confidence = 0.55 + min(0.25, displacement.displacement_factor * 0.25) + min(0.15, (gap.fill_ratio or 0.0) * 0.2)
        results.append(
            InvertedFVG(
                symbol=symbol,
                timeframe=timeframe,
                direction=direction,  # type: ignore[arg-type]
                timestamp=retest_at or gap.invalidated_at,
                source_direction=gap.direction,
                zone_low=gap.gap_low,
                zone_high=gap.gap_high,
                invalidated_at=gap.invalidated_at,
                retest_at=retest_at,
                confidence=min(confidence, 0.95),
                source_fvg_time=gap.created_at,
                breach_displacement_factor=displacement.displacement_factor,
                mean_threshold=mean_threshold,
                ifvg_grade=grade,
                ifvg_ce_level=mean_threshold,
                ifvg_retest_depth=retest_depth,
                ifvg_time_to_retest_bars=time_to_retest_bars,
                breach_displacement_grade=displacement.displacement_grade,
                metadata={
                    "created_at": gap.created_at,
                    "source_fvg_time": gap.created_at,
                    "source_fvg_direction": gap.direction,
                    "fill_ratio": gap.fill_ratio,
                    "fill_percent": gap.fill_percent,
                    "breach_time": gap.invalidated_at,
                    "breach_displacement_factor": displacement.displacement_factor,
                    "breach_displacement_grade": displacement.displacement_grade,
                    "body_ratio": displacement.body_ratio,
                    "range_expansion": displacement.range_expansion,
                    "close_beyond_structure": displacement.close_beyond_structure,
                    "created_fvg_after_break": displacement.created_fvg_after_break,
                    "bars_in_displacement": displacement.bars_count,
                    "mean_threshold": mean_threshold,
                    "ifvg_grade": grade,
                    "ifvg_ce_level": mean_threshold,
                    "ifvg_retest_depth": retest_depth,
                    "ifvg_retest_touched_ce": bool(retest_depth is not None and retest_depth >= 0.5),
                    "ifvg_retest_breached_ce_by_close": _ce_breached_by_close(
                        closed[breach_idx + time_to_retest_bars] if time_to_retest_bars else None,
                        mean_threshold,
                        direction,
                    ),
                    "ifvg_breach_time": gap.invalidated_at,
                    "ifvg_retest_time": retest_at,
                    "ifvg_time_to_retest_bars": time_to_retest_bars,
                },
            )
        )

    return results


__all__ = ["detect_ifvg"]


def _retest_depth(candle: Candle, low: float, high: float, direction: str) -> float:
    width = max(high - low, 1e-9)
    if direction == "bullish":
        return max(0.0, min(1.0, (high - float(candle["low"])) / width))
    return max(0.0, min(1.0, (float(candle["high"]) - low) / width))


def _ce_breached_by_close(candle: Candle | None, ce: float, direction: str) -> bool:
    if candle is None:
        return False
    if direction == "bullish":
        return float(candle["close"]) < ce
    return float(candle["close"]) > ce
