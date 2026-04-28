from __future__ import annotations

from typing import Any

from strategies.types import EntrySetup


def passes_model_filter(event: dict[str, Any], rules: dict[str, Any]) -> bool:
    if not rules:
        return True
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
    min_score = _float_or_none(rules.get("min_decision_score"))
    if min_score is not None:
        score = _float_or_none(event.get("decision_score"))
        if score is None or score < min_score:
            return False
    if rules.get("require_smt") and not _bool(event.get("has_smt_confirmation")):
        return False
    if rules.get("require_session_window") and not (event.get("session_window") or event.get("ny_time")):
        return False
    if not _field_allowed(event, rules, "htf_location", "allowed_htf_locations"):
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
        "score": setup.score,
        "target_distance_r": target_distance_r,
    }


def _field_allowed(event: dict[str, Any], rules: dict[str, Any], field: str, rule_name: str) -> bool:
    allowed = rules.get(rule_name)
    if not allowed:
        return True
    return str(event.get(field) or "none") in {str(item) for item in allowed}


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


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = ["passes_model_filter", "setup_filter_event"]
