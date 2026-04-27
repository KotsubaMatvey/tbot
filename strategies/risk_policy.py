from __future__ import annotations

from dataclasses import dataclass

from config import INVALIDATION_CONFIRMATION, MIN_RISK_BPS, STOP_BUFFER_BPS


@dataclass(slots=True)
class RiskPlan:
    stop_loss: float
    structural_invalidation: float
    invalidation_source: str
    stop_mode: str
    risk_bps: float
    risk_valid: bool
    stop_buffer_bps: float
    invalidation_confirmation: str
    stop_hit_policy: str = "wick"


def price_buffer(price: float, *, stop_buffer_bps: float = STOP_BUFFER_BPS, atr: float | None = None) -> float:
    atr_buffer = (atr or 0.0) * 0.05
    bps_buffer = price * stop_buffer_bps / 10_000
    return max(bps_buffer, atr_buffer)


def build_risk_plan(
    *,
    side: str,
    entry_low: float,
    entry_high: float,
    stop_loss: float,
    structural_invalidation: float,
    invalidation_source: str,
    stop_mode: str,
    stop_buffer_bps: float = STOP_BUFFER_BPS,
    invalidation_confirmation: str = INVALIDATION_CONFIRMATION,
    stop_hit_policy: str = "wick",
) -> RiskPlan:
    entry_mid = (entry_low + entry_high) / 2
    risk = _risk(side, entry_mid, stop_loss)
    risk_bps = (risk / entry_mid * 10_000) if entry_mid > 0 and risk is not None else 0.0
    return RiskPlan(
        stop_loss=stop_loss,
        structural_invalidation=structural_invalidation,
        invalidation_source=invalidation_source,
        stop_mode=stop_mode,
        risk_bps=round(risk_bps, 6),
        risk_valid=bool(risk is not None and risk > 0 and risk_bps >= MIN_RISK_BPS),
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
        stop_hit_policy=stop_hit_policy,
    )


def risk_metadata(plan: RiskPlan, *, model3_stop_mode: str | None = None) -> dict[str, object]:
    payload: dict[str, object] = {
        "stop_loss": plan.stop_loss,
        "structural_invalidation": plan.structural_invalidation,
        "invalidation_source": plan.invalidation_source,
        "stop_mode": plan.stop_mode,
        "risk_bps": plan.risk_bps,
        "risk_valid": plan.risk_valid,
        "stop_buffer_bps": plan.stop_buffer_bps,
        "invalidation_confirmation": plan.invalidation_confirmation,
        "stop_hit_policy": plan.stop_hit_policy,
    }
    if model3_stop_mode is not None:
        payload["model3_stop_mode"] = model3_stop_mode
    return payload


def model1_risk_plan(
    *,
    side: str,
    entry_low: float,
    entry_high: float,
    sweep_extreme: float,
    stop_mode: str,
    stop_buffer_bps: float,
    invalidation_confirmation: str,
) -> RiskPlan:
    mode = _mode(stop_mode, {"aggressive", "standard", "structural"}, "structural")
    ce = (entry_low + entry_high) / 2
    ref = {
        "aggressive": entry_low if side == "long" else entry_high,
        "standard": ce,
        "structural": sweep_extreme,
    }[mode]
    stop = _buffered(side, ref, entry_low, entry_high, stop_buffer_bps)
    structural = _buffered(side, sweep_extreme, entry_low, entry_high, stop_buffer_bps)
    return build_risk_plan(
        side=side,
        entry_low=entry_low,
        entry_high=entry_high,
        stop_loss=stop,
        structural_invalidation=structural,
        invalidation_source="sweep_extreme" if mode == "structural" else f"fvg_{mode}",
        stop_mode=mode,
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
    )


def model2_risk_plan(
    *,
    side: str,
    zone_low: float,
    zone_high: float,
    sweep_extreme: float,
    stop_mode: str,
    stop_buffer_bps: float,
    invalidation_confirmation: str,
) -> RiskPlan:
    mode = _mode(stop_mode, {"aggressive", "standard", "structural"}, "standard")
    ce = (zone_low + zone_high) / 2
    ref = {
        "aggressive": zone_low if side == "long" else zone_high,
        "standard": ce,
        "structural": zone_low if side == "long" else zone_high,
    }[mode]
    stop = _buffered(side, ref, zone_low, zone_high, stop_buffer_bps)
    structural_ref = zone_low if side == "long" else zone_high
    structural = _buffered(side, structural_ref, zone_low, zone_high, stop_buffer_bps)
    return build_risk_plan(
        side=side,
        entry_low=zone_low,
        entry_high=zone_high,
        stop_loss=stop,
        structural_invalidation=structural,
        invalidation_source="ifvg_ce" if mode == "standard" else "ifvg_boundary",
        stop_mode=mode,
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
    )


def model3_risk_plan(
    *,
    side: str,
    entry_low: float,
    entry_high: float,
    ltf_protected_swing: float,
    source_zone_low: float,
    source_zone_high: float,
    htf_ob_low: float | None,
    htf_ob_high: float | None,
    model3_stop_mode: str,
    stop_buffer_bps: float,
    invalidation_confirmation: str,
) -> RiskPlan:
    mode = _mode(model3_stop_mode, {"ltf_mss", "source_zone_extreme", "htf_ob_extreme"}, "source_zone_extreme")
    if mode == "ltf_mss":
        ref = ltf_protected_swing
        source = "ltf_mss_protected_swing"
    elif mode == "htf_ob_extreme" and htf_ob_low is not None and htf_ob_high is not None:
        ref = htf_ob_low if side == "long" else htf_ob_high
        source = "htf_ob_extreme"
    else:
        ref = source_zone_low if side == "long" else source_zone_high
        source = "source_zone_extreme"
        mode = "source_zone_extreme" if mode == "htf_ob_extreme" else mode
    stop = _buffered(side, ref, entry_low, entry_high, stop_buffer_bps)
    structural_ref = source_zone_low if side == "long" else source_zone_high
    structural = _buffered(side, structural_ref, entry_low, entry_high, stop_buffer_bps)
    return build_risk_plan(
        side=side,
        entry_low=entry_low,
        entry_high=entry_high,
        stop_loss=stop,
        structural_invalidation=structural,
        invalidation_source=source,
        stop_mode=mode,
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
    )


def _buffered(side: str, ref: float, entry_low: float, entry_high: float, stop_buffer_bps: float) -> float:
    price = (entry_low + entry_high) / 2
    buffer = price_buffer(price, stop_buffer_bps=stop_buffer_bps)
    return ref - buffer if side == "long" else ref + buffer


def _risk(side: str, entry: float, stop: float) -> float | None:
    if side == "long":
        return entry - stop
    if side == "short":
        return stop - entry
    return None


def _mode(value: str, allowed: set[str], default: str) -> str:
    text = (value or default).strip().lower()
    return text if text in allowed else default


__all__ = [
    "RiskPlan",
    "build_risk_plan",
    "model1_risk_plan",
    "model2_risk_plan",
    "model3_risk_plan",
    "price_buffer",
    "risk_metadata",
]
