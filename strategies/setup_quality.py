from __future__ import annotations

from typing import Any


def grade_points(grade: str | None) -> float:
    return {"strong": 0.6, "valid": 0.3, "medium": 0.2, "weak": -0.4}.get(str(grade or "weak"), 0.0)


def risk_quality(risk_bps: float | None) -> str:
    if risk_bps is None or risk_bps <= 0:
        return "invalid"
    if risk_bps <= 20:
        return "high"
    if risk_bps <= 50:
        return "medium"
    return "low"


def rr_quality(rr_to_objective: float | None) -> str:
    if rr_to_objective is None:
        return "unknown"
    if rr_to_objective >= 2.0:
        return "high"
    if rr_to_objective >= 1.5:
        return "medium"
    return "low"


def objective_quality(metadata: dict[str, Any]) -> str:
    if metadata.get("objective_unreached") is False or metadata.get("htf_objective_unreached") is False:
        return "invalid"
    objective_type = str(metadata.get("htf_objective_type") or metadata.get("objective_type") or "none")
    if objective_type in {"equal_highs", "equal_lows"}:
        return "high"
    if objective_type in {"swing_high", "swing_low"}:
        return "medium"
    return "unknown"


def poi_quality(metadata: dict[str, Any]) -> str:
    zone_type = str(metadata.get("htf_zone_type") or "None")
    if zone_type in {"OB", "IFVG", "Breaker"}:
        return "high"
    if zone_type in {"FVG", "PD"}:
        return "medium"
    return "low"


def build_score_components(
    *,
    htf_aligned: bool,
    objective_unreached: bool,
    risk_valid: bool,
    displacement_grade: str | None = None,
    ifvg_grade: str | None = None,
    fvg_quality: str | None = None,
    sweep_quality: str | None = None,
    risk_bps: float | None = None,
    rr_to_objective: float | None = None,
    poi_quality_value: str | None = None,
    objective_quality_value: str | None = None,
) -> dict[str, Any]:
    return {
        "gates": {
            "htf_aligned": htf_aligned,
            "objective_unreached": objective_unreached,
            "risk_valid": risk_valid,
        },
        "quality": {
            "displacement_grade": displacement_grade or "weak",
            "ifvg_grade": ifvg_grade,
            "fvg_quality": fvg_quality,
            "sweep_quality": sweep_quality,
            "poi_quality": poi_quality_value,
            "objective_quality": objective_quality_value,
        },
        "risk": {
            "risk_bps": risk_bps,
            "risk_quality": risk_quality(risk_bps),
            "rr_to_objective": rr_to_objective,
            "rr_quality": rr_quality(rr_to_objective),
        },
    }


__all__ = [
    "build_score_components",
    "grade_points",
    "objective_quality",
    "poi_quality",
    "risk_quality",
    "rr_quality",
]
