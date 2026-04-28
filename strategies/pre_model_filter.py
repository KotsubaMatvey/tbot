from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from strategies.ict_models.sessions import LONDON_OPEN, NY_OPEN, in_ny_windows


@dataclass(slots=True)
class PreModelDecision:
    passed: bool
    allowed_directions: set[str]
    reasons: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


def evaluate_pre_model_filter(context: object | None, config: dict[str, Any] | None = None) -> PreModelDecision:
    cfg = config or {}
    if not _bool(cfg.get("pre_model_filter", cfg.get("pre_model_filter_enabled", True))):
        return _decision({"long", "short"}, [], enabled=False)

    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    if htf_mode == "off":
        return _decision({"long", "short"}, [], htf_mode=htf_mode)

    htf = getattr(context, "htf_context", None) if context is not None else None
    if htf is None:
        return _decision(set(), ["missing_htf_context"], htf_mode=htf_mode)

    reasons: list[str] = []
    bias = htf.bias.direction
    location = htf.dealing_range.location
    objective = htf.objective.direction
    objective_unreached = bool(htf.objective_unreached or htf.objective.objective_unreached)

    if bias == "neutral" and not _bool(cfg.get("pre_model_allow_neutral_htf", False)):
        reasons.append("neutral_htf_bias")
    if location == "equilibrium" and not _bool(cfg.get("pre_model_allow_equilibrium", False)):
        reasons.append("equilibrium")
    if htf.objective.target_type == "none" or objective == "none":
        reasons.append("missing_draw")
    elif not objective_unreached:
        reasons.append("draw_already_reached")
    if cfg.get("pre_model_require_htf_poi", True) and not (htf.inside_zone or htf.approaching_zone):
        reasons.append("not_in_htf_poi")

    allowed = _allowed_by_context(htf, objective_unreached)
    if cfg.get("pre_model_require_smt"):
        allowed &= _allowed_by_smt(cfg)
        if not allowed:
            reasons.append("missing_smt_confirmation")

    if cfg.get("pre_model_require_killzone"):
        timestamp = _current_timestamp(context)
        windows = _window_list(cfg.get("pre_model_killzone_windows") or [LONDON_OPEN, NY_OPEN])
        if timestamp is None or not in_ny_windows(timestamp, windows):
            allowed.clear()
            reasons.append("outside_killzone")

    return _decision(
        allowed if not reasons else set(),
        reasons,
        htf_mode=htf_mode,
        htf_bias=bias,
        htf_location=location,
        htf_objective=objective,
        htf_inside_poi=htf.inside_zone,
        htf_approaching_poi=htf.approaching_zone,
    )


def merge_pre_model_metadata(setup: Any, decision: PreModelDecision) -> None:
    setup.metadata.update(decision.metadata)


def setup_passes_pre_model_filter(setup: Any, decision: PreModelDecision) -> bool:
    return decision.passed and setup.direction in decision.allowed_directions


def _allowed_by_context(htf: Any, objective_unreached: bool) -> set[str]:
    allowed: set[str] = set()
    if htf.allows_long or (
        htf.bias.direction == "bullish"
        and htf.objective.direction == "up"
        and objective_unreached
        and htf.dealing_range.location != "premium"
    ):
        allowed.add("long")
    if htf.allows_short or (
        htf.bias.direction == "bearish"
        and htf.objective.direction == "down"
        and objective_unreached
        and htf.dealing_range.location != "discount"
    ):
        allowed.add("short")
    return allowed


def _allowed_by_smt(config: dict[str, Any]) -> set[str]:
    allowed: set[str] = set()
    for item in config.get("smt_divergences") or []:
        direction = getattr(item, "direction", None)
        if direction == "bullish":
            allowed.add("long")
        elif direction == "bearish":
            allowed.add("short")
    return allowed


def _current_timestamp(context: object | None) -> int | None:
    primary = getattr(context, "primary", None)
    candles = getattr(primary, "candles", None)
    if not candles:
        return None
    return int(candles[-1]["time"])


def _window_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return [str(item) for item in value]


def _decision(allowed: set[str], reasons: list[str], **metadata: Any) -> PreModelDecision:
    payload = {
        "pre_model_filter_pass": not reasons and bool(allowed),
        "pre_model_allowed_directions": ",".join(sorted(allowed)),
        "pre_model_reasons": ";".join(reasons),
        **metadata,
    }
    return PreModelDecision(
        passed=bool(payload["pre_model_filter_pass"]),
        allowed_directions=allowed,
        reasons=reasons,
        metadata=payload,
    )


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


__all__ = [
    "PreModelDecision",
    "evaluate_pre_model_filter",
    "merge_pre_model_metadata",
    "setup_passes_pre_model_filter",
]
