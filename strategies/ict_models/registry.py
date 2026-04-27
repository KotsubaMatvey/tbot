from __future__ import annotations

from typing import Any

from strategies.legacy import detect_legacy_model_1, detect_legacy_model_2, detect_legacy_model_3
from strategies.types import StrategyContext

from . import breaker_block, ict2022_mss_fvg, ifvg_retest, reclaimed_ob, rejection_block, silver_bullet, turtle_soup
from .types import ICTDetector, ICTModelSpec


def _legacy_adapter(detector) -> ICTDetector:
    def wrapped(
        symbol: str,
        timeframe: str,
        candles: list[dict[str, float | int]],
        context: object | None = None,
        config: dict[str, Any] | None = None,
    ) -> list:
        if isinstance(context, StrategyContext):
            return detector(context)
        from scanner.snapshots import build_primitive_snapshot

        return detector(StrategyContext(primary=build_primitive_snapshot(symbol, timeframe, candles), htf_mode="off"))

    return wrapped


ACTIVE_ICT_MODELS: dict[str, ICTModelSpec] = {
    "turtle_soup": ICTModelSpec("turtle_soup", "Turtle Soup", turtle_soup.detect_setups),
    "silver_bullet": ICTModelSpec("silver_bullet", "Silver Bullet", silver_bullet.detect_setups),
    "ifvg_retest": ICTModelSpec("ifvg_retest", "IFVG Retest", ifvg_retest.detect_setups),
    "ict2022_mss_fvg": ICTModelSpec("ict2022_mss_fvg", "ICT 2022 MSS + FVG", ict2022_mss_fvg.detect_setups),
    "breaker_block": ICTModelSpec("breaker_block", "Breaker Block", breaker_block.detect_setups),
    "reclaimed_ob": ICTModelSpec("reclaimed_ob", "Reclaimed OB", reclaimed_ob.detect_setups),
}

RESEARCH_ONLY_MODELS: dict[str, ICTModelSpec] = {
    "rejection_block": ICTModelSpec(
        "rejection_block",
        "Rejection Block",
        rejection_block.detect_setups,
        research_only=True,
    ),
}

LEGACY_MODELS: dict[str, ICTModelSpec] = {
    "legacy_model1": ICTModelSpec("legacy_model1", "Legacy Entry Model 1", _legacy_adapter(detect_legacy_model_1), "legacy", legacy=True),
    "legacy_model2": ICTModelSpec("legacy_model2", "Legacy Entry Model 2", _legacy_adapter(detect_legacy_model_2), "legacy", legacy=True),
    "legacy_model3": ICTModelSpec("legacy_model3", "Legacy Entry Model 3", _legacy_adapter(detect_legacy_model_3), "legacy", legacy=True),
}

DEFAULT_MODELS = ["turtle_soup", "silver_bullet", "ifvg_retest"]

_OLD_ALIASES = {"model1": "legacy_model1", "entry_model_1": "legacy_model1", "model2": "legacy_model2", "entry_model_2": "legacy_model2", "model3": "legacy_model3", "entry_model_3": "legacy_model3"}


def get_model(name: str) -> ICTModelSpec:
    resolved = name.strip().lower()
    if resolved in ACTIVE_ICT_MODELS:
        return ACTIVE_ICT_MODELS[resolved]
    if resolved in RESEARCH_ONLY_MODELS:
        return RESEARCH_ONLY_MODELS[resolved]
    if resolved in LEGACY_MODELS:
        return LEGACY_MODELS[resolved]
    raise ValueError(f"unknown ICT model '{name}'")


def get_default_models() -> list[ICTModelSpec]:
    return [ACTIVE_ICT_MODELS[name] for name in DEFAULT_MODELS]


def list_active_models() -> list[str]:
    return list(ACTIVE_ICT_MODELS)


def list_research_models() -> list[str]:
    return list(RESEARCH_ONLY_MODELS)


def list_legacy_models() -> list[str]:
    return list(LEGACY_MODELS)


def resolve_models(names: list[str] | None, include_legacy: bool = False) -> list[ICTModelSpec]:
    requested = names or DEFAULT_MODELS
    resolved: list[ICTModelSpec] = []
    for raw in requested:
        name = raw.strip().lower()
        if name in _OLD_ALIASES:
            if not include_legacy:
                raise ValueError(f"{raw} is archived. Use legacy names with --include-legacy; preferred active names are {', '.join(DEFAULT_MODELS)}.")
            name = _OLD_ALIASES[name]
        if name in LEGACY_MODELS and not include_legacy:
            raise ValueError(f"{name} is legacy-only and requires --include-legacy.")
        spec = get_model(name)
        if spec.legacy and not include_legacy:
            raise ValueError(f"{name} is legacy-only and requires --include-legacy.")
        if spec not in resolved:
            resolved.append(spec)
    return resolved


__all__ = [
    "ACTIVE_ICT_MODELS",
    "DEFAULT_MODELS",
    "LEGACY_MODELS",
    "RESEARCH_ONLY_MODELS",
    "get_default_models",
    "get_model",
    "list_active_models",
    "list_legacy_models",
    "list_research_models",
    "resolve_models",
]
