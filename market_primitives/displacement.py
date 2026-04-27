from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from config import (
    DISPLACEMENT_FVG_BONUS,
    DISPLACEMENT_STRONG_BODY_RATIO,
    DISPLACEMENT_STRONG_RANGE_EXPANSION,
    DISPLACEMENT_VALID_BODY_RATIO,
    DISPLACEMENT_VALID_RANGE_EXPANSION,
)

from .common import Candle, average_range, candle_range


@dataclass(slots=True)
class DisplacementQuality:
    body_ratio: float
    range_expansion: float
    displacement_factor: float
    has_displacement: bool
    displacement_grade: Literal["weak", "valid", "strong"] = "weak"
    close_beyond_structure: bool = False
    created_fvg_after_break: bool = False
    bars_count: int = 1
    impulse_direction: str = "unknown"


def evaluate_displacement(
    candles: list[Candle],
    index: int,
    *,
    direction: str,
    structure_level: float | None = None,
    created_fvg_after_break: bool = False,
    lookback: int = 20,
) -> DisplacementQuality:
    if index < 0 or index >= len(candles):
        return DisplacementQuality(0.0, 0.0, 0.0, False)

    candle = candles[index]
    current_range = candle_range(candle)
    body = abs(float(candle["close"]) - float(candle["open"]))
    body_ratio = body / max(current_range, 1e-9)
    start = max(0, index - lookback)
    avg_range = average_range(candles[start:index])
    range_expansion = current_range / max(avg_range, 1e-9) if avg_range else 1.0
    close_beyond = True
    if structure_level is not None:
        if direction == "bullish":
            close_beyond = float(candle["close"]) > structure_level
        elif direction == "bearish":
            close_beyond = float(candle["close"]) < structure_level

    factor = min(1.0, body_ratio * 0.55 + min(range_expansion / 2.0, 1.0) * 0.45)
    if created_fvg_after_break:
        factor = min(1.0, factor + DISPLACEMENT_FVG_BONUS)
    grade: Literal["weak", "valid", "strong"] = "weak"
    if (
        close_beyond
        and created_fvg_after_break
        and body_ratio >= DISPLACEMENT_STRONG_BODY_RATIO
        and range_expansion >= DISPLACEMENT_STRONG_RANGE_EXPANSION
    ):
        grade = "strong"
    elif (
        close_beyond
        and created_fvg_after_break
        and body_ratio >= DISPLACEMENT_VALID_BODY_RATIO
        and range_expansion >= DISPLACEMENT_VALID_RANGE_EXPANSION
    ):
        grade = "valid"
    has_displacement = grade in {"valid", "strong"}
    return DisplacementQuality(
        body_ratio=body_ratio,
        range_expansion=range_expansion,
        displacement_factor=factor,
        has_displacement=has_displacement,
        displacement_grade=grade,
        close_beyond_structure=close_beyond,
        created_fvg_after_break=created_fvg_after_break,
        bars_count=1,
        impulse_direction=direction,
    )


__all__ = ["DisplacementQuality", "evaluate_displacement"]
