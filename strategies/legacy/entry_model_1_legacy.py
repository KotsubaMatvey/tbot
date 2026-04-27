"""
LEGACY MODEL.

This model is archived and disabled by default.
It is preserved only for baseline comparison.
New active ICT models live in strategies/ict_models/.
"""

from __future__ import annotations

from market_primitives.common import FairValueGap, LiquiditySweep, StructureBreak, zone_overlap

from config import REQUIRE_HTF_CONTEXT_FOR_ENTRY_MODELS
from strategies.htf_context import htf_allows_side, htf_metadata, htf_score_modifier
from strategies.risk_policy import model1_risk_plan, risk_metadata
from strategies.scoring import score_model_1
from strategies.setup_quality import build_score_components, objective_quality, poi_quality, risk_quality
from strategies.setup_utils import classify_zone_status, primitive_direction, sweep_label
from strategies.types import EntrySetup, PrimitiveSnapshot, StrategyContext, default_components


def detect_entry_model_1(context: StrategyContext) -> list[EntrySetup]:
    results: list[EntrySetup] = []
    results.extend(_detect_direction(context, side="long"))
    results.extend(_detect_direction(context, side="short"))
    return sorted(results, key=lambda item: item.timestamp, reverse=True)


def _detect_direction(context: StrategyContext, side: str) -> list[EntrySetup]:
    htf_mode = context.htf_mode if REQUIRE_HTF_CONTEXT_FOR_ENTRY_MODELS else "off"
    if REQUIRE_HTF_CONTEXT_FOR_ENTRY_MODELS and not htf_allows_side(context.htf_context, side, htf_mode):
        return []

    snapshot = context.primary
    direction = primitive_direction(side)  # type: ignore[arg-type]
    sweeps = sorted(
        [item for item in (snapshot.raids + snapshot.sweeps) if item.direction == direction],
        key=lambda item: item.timestamp,
        reverse=True,
    )
    structures = sorted(
        [item for item in snapshot.structure_breaks if item.direction == direction and item.strength >= 0.2],
        key=lambda item: item.timestamp,
    )
    fvgs = sorted(
        [item for item in snapshot.fvgs if item.direction == direction and not item.invalidated],
        key=lambda item: item.created_at,
    )

    for sweep in sweeps[:4]:
        structure = next(
            (
                item
                for item in structures
                if item.timestamp > sweep.timestamp and item.source_swing_index >= sweep.source_swing_index
            ),
            None,
        )
        if structure is None:
            continue
        if context.require_displacement and structure.displacement_grade not in {"valid", "strong"}:
            continue

        post_bos_fvg = next(
            (
                item
                for item in fvgs
                if item.created_at > structure.timestamp
            ),
            None,
        )
        if post_bos_fvg is None:
            continue

        setup = _build_setup(snapshot, side, sweep, structure, post_bos_fvg, context, htf_mode)
        if setup is not None:
            return [setup]
    return []


def _build_setup(
    snapshot: PrimitiveSnapshot,
    side: str,
    sweep: LiquiditySweep,
    structure: StructureBreak,
    fvg: FairValueGap,
    context: StrategyContext,
    htf_mode: str,
) -> EntrySetup | None:
    higher_snapshot = context.higher_timeframe
    entry_low = fvg.gap_low
    entry_high = fvg.gap_high
    armed_time = max(structure.timestamp, fvg.created_at)
    status_info = classify_zone_status(snapshot, zone_low=entry_low, zone_high=entry_high, armed_time=armed_time)
    if status_info is None:
        return None
    status, status_time = status_info
    if status != "watching" and status_time <= fvg.created_at:
        return None

    risk_plan = model1_risk_plan(
        side=side,
        entry_low=entry_low,
        entry_high=entry_high,
        sweep_extreme=sweep.wick_extreme,
        stop_mode=context.stop_mode,
        stop_buffer_bps=context.stop_buffer_bps,
        invalidation_confirmation=context.invalidation_confirmation,
    )
    if not risk_plan.risk_valid:
        return None
    direction = primitive_direction(side)  # type: ignore[arg-type]

    htf_alignment = 0.0
    if higher_snapshot is not None:
        htf_alignment = 0.3 if any(item.direction == structure.direction for item in higher_snapshot.structure_breaks) else -0.2
    messy_overlap = any(
        zone_overlap(entry_low, entry_high, order_block.zone_low, order_block.zone_high) > 0.8
        for order_block in (higher_snapshot.order_blocks if higher_snapshot is not None else [])
    )
    late_mitigation = bool(fvg.mitigated_at and (fvg.mitigated_at - fvg.created_at) > 6 * 60 * 60 * 1000)
    score = score_model_1(
        clean_sweep=sweep.clean,
        structure_strength=structure.strength,
        entry_low=entry_low,
        entry_high=entry_high,
        invalidation=risk_plan.stop_loss,
        context_alignment=htf_alignment,
        htf_modifier=htf_score_modifier(context.htf_context, side, htf_mode),
        messy_overlap=messy_overlap,
        late_mitigation=late_mitigation,
        displacement_factor=structure.displacement_factor,
        has_displacement=structure.has_displacement,
        displacement_grade=structure.displacement_grade,
    )
    htf_meta = htf_metadata(context.htf_context)
    quality_meta = {
        **htf_meta,
        "objective_unreached": htf_meta.get("htf_objective_unreached"),
        "risk_bps": risk_plan.risk_bps,
    }
    score_components = build_score_components(
        htf_aligned=bool(htf_meta.get("htf_context_alignment") == "aligned" or htf_meta.get("htf_bias") == direction),
        objective_unreached=bool(htf_meta.get("htf_objective_unreached")),
        risk_valid=risk_plan.risk_valid,
        displacement_grade=structure.displacement_grade,
        fvg_quality="medium" if not fvg.invalidated else "low",
        sweep_quality="high" if sweep.clean else "medium",
        risk_bps=risk_plan.risk_bps,
        poi_quality_value=poi_quality(quality_meta),
        objective_quality_value=objective_quality(quality_meta),
    )

    components = default_components()
    components["sweep_detected"] = True
    components["structure_shift_detected"] = True
    components["fvg_detected"] = True

    return EntrySetup(
        model_name="Entry Model 1",
        direction="long" if side == "long" else "short",
        symbol=snapshot.symbol,
        timeframe=snapshot.timeframe,
        status=status,
        entry_low=entry_low,
        entry_high=entry_high,
        invalidation=risk_plan.stop_loss,
        target_hint=_target_hint(side, sweep.liquidity_level, structure.broken_level, entry_low, entry_high),
        sweep_level=sweep.liquidity_level,
        structure_level=structure.broken_level,
        context_timeframe=context.htf_timeframe,
        score=score,
        reason=_reason(context, side, structure),
        components=components,
        timestamp=max(status_time, sweep.timestamp, structure.timestamp, fvg.created_at),
        metadata={
            "sweep_time": sweep.timestamp,
            "sweep_timestamp": sweep.timestamp,
            "swing_significance": sweep.source_swing_significance,
            "sweep_swing_significance": sweep.source_swing_significance,
            "sweep_liquidity_quality": sweep.metadata.get("sweep_liquidity_quality"),
            "structure_time": structure.timestamp,
            "structure_type": structure.break_type,
            "structure_swing_significance": structure.metadata.get("swing_significance"),
            "displacement_factor": round(structure.displacement_factor, 6),
            "has_displacement": structure.has_displacement,
            "displacement_grade": structure.displacement_grade,
            "body_ratio": round(structure.body_ratio, 6),
            "range_expansion": round(structure.range_expansion, 6),
            "close_beyond_structure": structure.close_beyond_structure,
            "created_fvg_after_break": structure.created_fvg_after_break,
            "bars_in_displacement": structure.bars_in_displacement,
            "fvg_created_at": fvg.created_at,
            "fvg_time": fvg.created_at,
            "fvg_status": fvg.status,
            "fvg_fill_percent": fvg.fill_percent,
            "fvg_mitigated_at": fvg.mitigated_at,
            "htf_alignment": htf_meta.get("htf_context_alignment"),
            "objective_unreached": htf_meta.get("htf_objective_unreached"),
            "objective_quality": objective_quality(quality_meta),
            "poi_quality": poi_quality(quality_meta),
            "fvg_quality": "medium" if not fvg.invalidated else "low",
            "sweep_quality": "high" if sweep.clean else "medium",
            "risk_quality": risk_quality(risk_plan.risk_bps),
            "score_components": score_components,
            **risk_metadata(risk_plan),
            **htf_meta,
        },
    )


def _reason(context: StrategyContext, side: str, structure: StructureBreak) -> str:
    htf = context.htf_context
    if htf is None:
        return f"{sweep_label(side)} sweep, {structure.break_type} confirmed, post-BOS FVG ready"
    return (
        f"HTF {htf.bias.direction} {htf.dealing_range.location}/{htf.zone.zone_type} context -> "
        f"LTF {sweep_label(side)} sweep, {structure.break_type}, post-BOS FVG retest"
    )


def _target_hint(side: str, sweep_level: float, structure_level: float, entry_low: float, entry_high: float) -> float:
    entry_mid = (entry_low + entry_high) / 2
    risk = abs(entry_mid - sweep_level)
    if side == "long":
        return max(structure_level, entry_high) + risk * 2
    return min(structure_level, entry_low) - risk * 2


__all__ = ["detect_entry_model_1"]
