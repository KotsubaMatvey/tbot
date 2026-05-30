from __future__ import annotations

from typing import Any

from strategies.types import EntrySetup


def passes_model_filter(event: dict[str, Any], rules: dict[str, Any]) -> bool:
    if not rules:
        return True
    if rules.get("enabled") is False:
        return False
    min_rr = _float_or_none(rules.get("min_target_distance_r"))
    if min_rr is not None:
        rr = _float_or_none(event.get("target_distance_r"))
        if rr is None or rr < min_rr:
            return False
    max_rr = _float_or_none(rules.get("max_target_distance_r"))
    if max_rr is not None:
        rr = _float_or_none(event.get("target_distance_r"))
        if rr is None or rr > max_rr:
            return False
    min_risk_bps = _float_or_none(rules.get("min_risk_bps"))
    if min_risk_bps is not None:
        risk_bps = _float_or_none(event.get("risk_bps"))
        if risk_bps is None or risk_bps < min_risk_bps:
            return False
    max_risk_bps = _float_or_none(rules.get("max_risk_bps"))
    if max_risk_bps is not None:
        risk_bps = _float_or_none(event.get("risk_bps"))
        if risk_bps is None or risk_bps > max_risk_bps:
            return False
    max_execution_cost_r = _float_or_none(rules.get("max_execution_cost_r"))
    if max_execution_cost_r is not None:
        cost_r = _float_or_none(event.get("execution_cost_r"))
        if cost_r is None or cost_r > max_execution_cost_r:
            return False
    max_dol_priority = _float_or_none(rules.get("max_dol_priority"))
    if max_dol_priority is not None:
        priority = _float_or_none(event.get("dol_priority"))
        if priority is None or priority > max_dol_priority:
            return False
    max_failed_asian_sweeps = _float_or_none(rules.get("max_asian_failed_sweep_count_before_reclaim"))
    if max_failed_asian_sweeps is not None:
        failed_sweeps = _float_or_none(event.get("asian_failed_sweep_count_before_reclaim"))
        if failed_sweeps is None or failed_sweeps > max_failed_asian_sweeps:
            return False
    min_score = _float_or_none(rules.get("min_decision_score"))
    if min_score is not None:
        score = _float_or_none(event.get("decision_score"))
        if score is None or score < min_score:
            return False
    if rules.get("require_smt") and not _bool(event.get("has_smt_confirmation")):
        return False
    if rules.get("require_session_window") and not (event.get("session_window") or event.get("ny_time")):
        return False
    if rules.get("require_htf_draw") and not _has_htf_draw(event):
        return False
    if rules.get("require_bias_alignment") and not _bias_aligned(event):
        return False
    if rules.get("require_premium_discount_alignment") and not _premium_discount_aligned(event):
        return False
    if rules.get("require_htf_inside_poi") and not _bool(event.get("htf_inside_poi")):
        return False
    if not _field_allowed(event, rules, "symbol", "allowed_symbols"):
        return False
    if not _field_allowed(event, rules, "direction", "allowed_directions"):
        return False
    if not _field_allowed(event, rules, "timeframe", "allowed_timeframes"):
        return False
    if not _timeframe_direction_allowed(event, rules):
        return False
    if not _field_allowed(event, rules, "session_label", "allowed_session_labels"):
        return False
    if not _field_allowed(event, rules, "session_window", "allowed_session_windows"):
        return False
    if not _field_allowed(event, rules, "range_source", "allowed_range_sources"):
        return False
    if not _field_allowed(event, rules, "htf_location", "allowed_htf_locations"):
        return False
    if not _field_allowed(event, rules, "htf_zone_type", "allowed_htf_zone_types"):
        return False
    if not _field_allowed(event, rules, "htf_context_alignment", "allowed_htf_context_alignments"):
        return False
    if not _field_allowed(event, rules, "dol_target_type", "allowed_dol_target_types"):
        return False
    if not _field_allowed(event, rules, "dol_source", "allowed_dol_sources"):
        return False
    if not _field_allowed(event, rules, "target_model", "allowed_target_models"):
        return False
    if not _field_allowed(event, rules, "turtle_quality", "allowed_turtle_qualities"):
        return False
    if not _displacement_allowed(event, rules):
        return False
    excluded = set(rules.get("exclude_no_trade_reasons") or [])
    if excluded:
        reasons = {reason.strip() for reason in str(event.get("no_trade_reasons") or "").split(";") if reason.strip()}
        if reasons & excluded:
            return False
    return True


def setup_filter_event(setup: EntrySetup) -> dict[str, Any]:
    entry = setup.entry_price if setup.entry_price is not None else (setup.entry_low + setup.entry_high) / 2
    stop = setup.stop_loss if setup.stop_loss is not None else setup.invalidation
    risk = abs(entry - stop) if stop is not None else None
    target_distance_r = abs(setup.target_hint - entry) / risk if setup.target_hint is not None and risk and risk > 0 else None
    return {
        **setup.metadata,
        "model": setup.model_name,
        "direction": setup.direction,
        "symbol": setup.symbol,
        "timeframe": setup.timeframe,
        "score": setup.score,
        "target_distance_r": target_distance_r,
    }


def _field_allowed(event: dict[str, Any], rules: dict[str, Any], field: str, rule_name: str) -> bool:
    allowed = rules.get(rule_name)
    if not allowed:
        return True
    return str(event.get(field) or "none") in {str(item) for item in allowed}


def _timeframe_direction_allowed(event: dict[str, Any], rules: dict[str, Any]) -> bool:
    allowed = rules.get("allowed_timeframe_directions")
    if not allowed:
        return True
    timeframe = str(event.get("timeframe") or "none")
    direction = str(event.get("direction") or "none")
    return f"{timeframe}:{direction}" in {str(item) for item in allowed}


def _displacement_allowed(event: dict[str, Any], rules: dict[str, Any]) -> bool:
    allowed = rules.get("allowed_displacement_grades")
    if not allowed:
        return True
    values = {str(item) for item in allowed}
    grade = event.get("displacement_grade") or event.get("breach_displacement_grade")
    return str(grade or "none") in values


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _has_htf_draw(event: dict[str, Any]) -> bool:
    side = str(event.get("direction") or "")
    draw = str(event.get("htf_draw_direction") or event.get("htf_objective") or "none")
    objective_type = str(event.get("htf_objective_type") or "none")
    objective_unreached = _bool(event.get("htf_objective_unreached") or event.get("objective_unreached"))
    if side == "long" and draw != "up":
        return False
    if side == "short" and draw != "down":
        return False
    return side in {"long", "short"} and objective_type != "none" and objective_unreached


def _bias_aligned(event: dict[str, Any]) -> bool:
    side = str(event.get("direction") or "")
    bias = str(event.get("htf_bias") or "none")
    return (side == "long" and bias == "bullish") or (side == "short" and bias == "bearish")


def _premium_discount_aligned(event: dict[str, Any]) -> bool:
    side = str(event.get("direction") or "")
    location = str(event.get("htf_location") or event.get("is_in_p_d") or "unknown")
    return (side == "long" and location == "discount") or (side == "short" and location == "premium")


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = ["passes_model_filter", "setup_filter_event"]
