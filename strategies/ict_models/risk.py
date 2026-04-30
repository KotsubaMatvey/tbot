from __future__ import annotations

from typing import Any


def enrich_risk_metadata(
    *,
    model_name: str,
    direction: str,
    entry: float,
    stop: float,
    target: float | None,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    risk = abs(entry - stop)
    enriched = dict(metadata)
    enriched["stop_model"] = _stop_model(model_name, str(enriched.get("stop_mode") or ""))
    enriched["target_model"] = _target_model(str(enriched.get("target_mode") or ""), enriched)
    logical_model, logical_price = _logical_invalidation(model_name, enriched)
    enriched["logical_invalidation_model"] = logical_model
    enriched["logical_invalidation_price"] = logical_price
    enriched["logical_invalidation_confirmation"] = "body_close"
    enriched["rr_to_target"] = _rr_to_target(direction, entry, stop, target)
    enriched["tp1_price"] = _tp1_price(direction, entry, risk, target)
    enriched["tp2_price"] = target
    enriched["final_target"] = _final_target(direction, target, enriched)
    enriched["partial_close_fraction"] = 0.5
    enriched["be_trigger_r"] = 1.0
    enriched.setdefault("moved_to_be", False)
    enriched.setdefault("exit_reason", None)
    return enriched


def _stop_model(model_name: str, stop_mode: str) -> str:
    if stop_mode in {"ce", "opposite_boundary"} or model_name in {"ifvg_retest"}:
        return "ce_fvg" if stop_mode == "ce" else "fvg_boundary"
    if stop_mode in {"mean_threshold", "MT"} or model_name == "breaker_block":
        return "mean_threshold"
    if stop_mode in {"wick_extreme"} or model_name == "rejection_block":
        return "wick_extreme"
    if stop_mode in {"sweep_extreme"} or model_name in {"turtle_soup", "ict2022_mss_fvg"}:
        return "sweep_extreme"
    if stop_mode in {"structural", "block_extreme"}:
        return "structural_swing"
    return stop_mode or "physical_stop"


def _target_model(target_mode: str, metadata: dict[str, Any]) -> str:
    if target_mode in {"htf_external_liquidity", "htf_draw"}:
        return "htf_draw"
    if target_mode in {"opposite_range", "nearest_liquidity"}:
        objective = metadata.get("htf_objective_type")
        if objective in {"equal_highs", "equal_lows", "swing_high", "swing_low"}:
            return "external_liq_bsl_ssl"
        return "internal_liq_fvg_ob" if target_mode == "nearest_liquidity" else "external_liq_bsl_ssl"
    if target_mode == "dol_hierarchy":
        target_type = str(metadata.get("dol_target_type") or "")
        if target_type in {"htf_external", "clean_level", "external_swing_high", "external_swing_low"}:
            return "external_liq_bsl_ssl"
        if target_type in {"htf_internal_fvg", "opposing_poi"}:
            return "internal_liq_fvg_ob"
        return "draw_on_liquidity"
    if target_mode == "fixed_r":
        return "fixed_r"
    return target_mode or "unknown"


def _logical_invalidation(model_name: str, metadata: dict[str, Any]) -> tuple[str | None, float | None]:
    if model_name == "silver_bullet" and not metadata.get("silver_bullet_use_ce_invalidation"):
        return None, None
    candidates = {
        "ifvg_retest": ("ce_fvg", metadata.get("ifvg_ce_invalidation") or metadata.get("ifvg_ce")),
        "ict2022_mss_fvg": ("ce_fvg", metadata.get("fvg_ce_invalidation") or metadata.get("fvg_ce")),
        "silver_bullet": ("ce_fvg", metadata.get("fvg_ce_invalidation") or metadata.get("fvg_ce")),
        "reclaimed_ob": ("mean_threshold", metadata.get("ob_mean_threshold")),
        "breaker_block": ("mean_threshold", metadata.get("breaker_mean_threshold")),
        "rejection_block": ("wick_extreme", metadata.get("rejection_wick_extreme")),
        "turtle_soup": ("sweep_extreme", metadata.get("sweep_extreme")),
    }
    model, price = candidates.get(model_name, (None, None))
    return model, float(price) if isinstance(price, (int, float)) else None


def _rr_to_target(direction: str, entry: float, stop: float, target: float | None) -> float | None:
    if target is None:
        return None
    risk = abs(entry - stop)
    reward = target - entry if direction == "long" else entry - target
    if risk <= 0 or reward <= 0:
        return None
    return reward / risk


def _tp1_price(direction: str, entry: float, risk: float, target: float | None) -> float | None:
    if risk <= 0:
        return None
    one_r = entry + risk if direction == "long" else entry - risk
    if target is None:
        return one_r
    if direction == "long" and target > entry:
        return min(one_r, target)
    if direction == "short" and target < entry:
        return max(one_r, target)
    return one_r


def _final_target(direction: str, target: float | None, metadata: dict[str, Any]) -> float | None:
    objective = metadata.get("htf_objective_level")
    draw = metadata.get("htf_draw_direction")
    if isinstance(objective, (int, float)):
        if direction == "long" and draw == "up":
            return float(objective)
        if direction == "short" and draw == "down":
            return float(objective)
    return target


__all__ = ["enrich_risk_metadata"]
