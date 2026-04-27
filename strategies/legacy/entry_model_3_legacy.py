"""
LEGACY MODEL.

This model is archived and disabled by default.
It is preserved only for baseline comparison.
New active ICT models live in strategies/ict_models/.
"""

from __future__ import annotations

from dataclasses import dataclass

from market_primitives.common import FairValueGap, OrderBlock, StructureBreak

from config import MODEL3_FILL_THRESHOLD
from strategies.htf_context import htf_allows_side, htf_metadata, htf_score_modifier
from strategies.risk_policy import model3_risk_plan, risk_metadata
from strategies.scoring import score_model_3
from strategies.setup_quality import build_score_components, objective_quality, poi_quality, risk_quality
from strategies.setup_utils import classify_zone_status, current_price, primitive_direction
from strategies.types import EntrySetup, PrimitiveSnapshot, StrategyContext, default_components


@dataclass(slots=True)
class _SourceZone:
    zone_type: str
    direction: str
    low: float
    high: float
    origin_time: int
    fill_ratio: float
    fill_mode: str
    displacement_factor: float
    has_displacement: bool
    metadata: dict[str, object]


def detect_entry_model_3(context: StrategyContext) -> list[EntrySetup]:
    if context.htf_mode != "off" and context.htf_context is None:
        return []
    if context.higher_timeframe is None or context.lower_timeframe is None:
        return []

    results: list[EntrySetup] = []
    results.extend(_detect_direction(context, side="long"))
    results.extend(_detect_direction(context, side="short"))
    return sorted(results, key=lambda item: item.timestamp, reverse=True)


def _detect_direction(context: StrategyContext, side: str) -> list[EntrySetup]:
    htf = context.higher_timeframe
    ltf = context.lower_timeframe
    if htf is None or ltf is None:
        return []
    if not htf_allows_side(context.htf_context, side, context.htf_mode):
        return []

    direction = primitive_direction(side)  # type: ignore[arg-type]
    if context.htf_context is not None and context.htf_context.bias.direction not in {direction, "neutral"}:
        return []
    if context.htf_context is not None and context.htf_context.bias.direction == "neutral":
        return []
    if context.htf_context is not None:
        if not context.htf_context.objective_unreached:
            return []
        if side == "long" and context.htf_context.draw_direction != "up":
            return []
        if side == "short" and context.htf_context.draw_direction != "down":
            return []

    primary_structure = next(
        (
            item
            for item in sorted(context.primary.structure_breaks, key=lambda item: item.timestamp, reverse=True)
            if item.direction == direction and (item.displacement_grade in {"valid", "strong"} or not context.require_displacement)
        ),
        None,
    )
    if primary_structure is None:
        return []

    source_zone = _select_source_zone(context.primary, direction, primary_structure, context.model3_fill_threshold)
    if source_zone is None:
        return []
    if not _source_zone_allowed(source_zone.zone_type, source_zone.fill_mode, context.model3_source_zone):
        return []
    if _objective_reached_before_entry(context.primary, context.htf_context, side, source_zone.origin_time):
        return []

    touch_time = _first_touch_time(ltf, source_zone.low, source_zone.high, source_zone.origin_time)
    if touch_time is None:
        return []
    ltf_structure = next(
        (
            item
            for item in sorted(ltf.structure_breaks, key=lambda item: item.timestamp, reverse=True)
            if item.direction == direction
            and item.timestamp > touch_time
            and item.strength >= 0.2
            and (item.displacement_grade in {"valid", "strong"} or not context.require_displacement)
        ),
        None,
    )
    if ltf_structure is None:
        return []
    reaction_bars = _bars_between(ltf, touch_time, ltf_structure.timestamp)
    if reaction_bars is None or reaction_bars > context.model3_reaction_bars:
        return []

    ltf_fvg = next(
        (
            item
            for item in sorted(ltf.fvgs, key=lambda item: item.created_at, reverse=True)
            if item.direction == direction and item.created_at > ltf_structure.timestamp and not item.invalidated
        ),
        None,
    )

    setup = _build_setup(context, htf, ltf, side, primary_structure, source_zone, ltf_structure, ltf_fvg, touch_time, reaction_bars)
    return [setup] if setup is not None else []


def _build_setup(
    context: StrategyContext,
    htf: PrimitiveSnapshot,
    ltf: PrimitiveSnapshot,
    side: str,
    primary_structure: StructureBreak,
    source_zone: _SourceZone,
    ltf_structure: StructureBreak,
    ltf_fvg: FairValueGap | None,
    touch_time: int,
    reaction_bars: int,
) -> EntrySetup | None:
    entry_low = ltf_fvg.gap_low if ltf_fvg is not None else source_zone.low
    entry_high = ltf_fvg.gap_high if ltf_fvg is not None else source_zone.high
    armed_time = max(ltf_structure.timestamp, ltf_fvg.created_at if ltf_fvg is not None else source_zone.origin_time)
    status_info = classify_zone_status(
        ltf,
        zone_low=entry_low,
        zone_high=entry_high,
        armed_time=armed_time,
    )
    if status_info is None:
        return None
    status, status_time = status_info

    ltf_protected = ltf_structure.broken_level
    htf_ob_low, htf_ob_high = _nearest_htf_ob_extreme(htf, side)
    risk_plan = model3_risk_plan(
        side=side,
        entry_low=entry_low,
        entry_high=entry_high,
        ltf_protected_swing=ltf_protected,
        source_zone_low=source_zone.low,
        source_zone_high=source_zone.high,
        htf_ob_low=htf_ob_low,
        htf_ob_high=htf_ob_high,
        model3_stop_mode=context.model3_stop_mode,
        stop_buffer_bps=context.stop_buffer_bps,
        invalidation_confirmation=context.invalidation_confirmation,
    )
    price = current_price(ltf)
    entry_mid = (entry_low + entry_high) / 2
    if not risk_plan.risk_valid:
        return None
    distance_to_objective = _distance_to_objective(context, side, entry_mid)
    rr_to_objective = distance_to_objective / max(abs(entry_mid - risk_plan.stop_loss), 1e-9) if distance_to_objective is not None else None
    if rr_to_objective is None or rr_to_objective < context.model3_min_rr_to_objective:
        return None
    zone_width = max(abs(entry_high - entry_low), entry_mid * 0.0005)
    if price is not None:
        distance = 0.0 if entry_low <= price <= entry_high else min(abs(price - entry_low), abs(price - entry_high))
        if distance > max(zone_width * 2.0, price * 0.004):
            return None

    score = score_model_3(
        htf_alignment=0.8 if primary_structure.break_type in {"BOS", "CHOCH", "MSS"} else 0.5,
        ltf_strength=min(1.0, ltf_structure.strength + 0.15),
        entry_low=entry_low,
        entry_high=entry_high,
        invalidation=risk_plan.stop_loss,
        missed_primary_penalty=0.3,
        htf_modifier=htf_score_modifier(context.htf_context, side, context.htf_mode),
        fill_quality=source_zone.fill_ratio,
        has_displacement=primary_structure.has_displacement or ltf_structure.has_displacement,
        displacement_grade=_max_grade(primary_structure.displacement_grade, ltf_structure.displacement_grade),
        rr_to_objective=rr_to_objective,
    )
    htf_meta = htf_metadata(context.htf_context)
    quality_meta = {
        **htf_meta,
        "objective_unreached": htf_meta.get("htf_objective_unreached"),
        "risk_bps": risk_plan.risk_bps,
    }
    score_components = build_score_components(
        htf_aligned=bool(htf_meta.get("htf_context_alignment") == "aligned"),
        objective_unreached=True,
        risk_valid=risk_plan.risk_valid,
        displacement_grade=_max_grade(primary_structure.displacement_grade, ltf_structure.displacement_grade),
        fvg_quality="medium" if source_zone.zone_type == "FVG" else None,
        risk_bps=risk_plan.risk_bps,
        rr_to_objective=rr_to_objective,
        poi_quality_value=poi_quality(quality_meta),
        objective_quality_value=objective_quality(quality_meta),
    )

    components = default_components()
    components["structure_shift_detected"] = True
    components["fvg_detected"] = True
    components["ltf_refinement_detected"] = True

    return EntrySetup(
        model_name="Entry Model 3",
        direction="long" if side == "long" else "short",
        symbol=context.primary.symbol,
        timeframe=ltf.timeframe,
        status=status,
        entry_low=entry_low,
        entry_high=entry_high,
        invalidation=risk_plan.stop_loss,
        target_hint=_target_hint(side, entry_low, entry_high, risk_plan.stop_loss),
        sweep_level=None,
        structure_level=ltf_structure.broken_level,
        context_timeframe=htf.timeframe,
        score=score,
        reason=_reason(context, side, source_zone, ltf_fvg),
        components=components,
        timestamp=max(status_time, primary_structure.timestamp, ltf_structure.timestamp, armed_time),
        metadata={
            "primary_timeframe": context.primary.timeframe,
            "htf_timeframe": htf.timeframe,
            "ltf_timeframe": ltf.timeframe,
            "primary_structure_time": primary_structure.timestamp,
            "primary_structure_type": primary_structure.break_type,
            "structure_swing_significance": primary_structure.metadata.get("swing_significance"),
            "displacement_factor": round(max(primary_structure.displacement_factor, ltf_structure.displacement_factor), 6),
            "has_displacement": primary_structure.has_displacement or ltf_structure.has_displacement,
            "displacement_grade": _max_grade(primary_structure.displacement_grade, ltf_structure.displacement_grade),
            "ltf_reaction_displacement_grade": ltf_structure.displacement_grade,
            "ltf_structure_type": ltf_structure.break_type,
            "ltf_mss_time": ltf_structure.timestamp,
            "ltf_reaction_bars": reaction_bars,
            "reaction_speed": reaction_bars,
            "time_to_fill": _bars_between(context.primary, source_zone.origin_time, touch_time),
            "source_zone_type": source_zone.zone_type,
            "source_zone_time": source_zone.origin_time,
            "source_zone_low": source_zone.low,
            "source_zone_high": source_zone.high,
            "source_zone_valid": True,
            "source_zone_invalidation_level": risk_plan.structural_invalidation,
            "original_entry_zone_low": source_zone.low,
            "original_entry_zone_high": source_zone.high,
            "missed_entry_distance": _missed_entry_distance(context.primary, source_zone),
            "objective_reached_before_entry": False,
            "objective_unreached": True,
            "objective_quality": objective_quality(quality_meta),
            "poi_quality": poi_quality(quality_meta),
            "risk_quality": risk_quality(risk_plan.risk_bps),
            "distance_to_objective": distance_to_objective,
            "rr_to_objective": round(rr_to_objective, 6) if rr_to_objective is not None else None,
            "score_components": score_components,
            "fill_percent": round(source_zone.fill_ratio * 100, 4),
            "fvg_fill_percent": round(source_zone.fill_ratio * 100, 4),
            "fill_mode": source_zone.fill_mode,
            "ltf_entry_zone_low": entry_low,
            "ltf_entry_zone_high": entry_high,
            **source_zone.metadata,
            **risk_metadata(risk_plan, model3_stop_mode=context.model3_stop_mode),
            **htf_meta,
        },
    )


def _select_source_zone(
    snapshot: PrimitiveSnapshot,
    direction: str,
    structure: StructureBreak,
    fill_threshold: float,
) -> _SourceZone | None:
    zones: list[_SourceZone] = []
    for fvg in snapshot.fvgs:
        if fvg.direction != direction or fvg.invalidated or fvg.created_at < structure.timestamp:
            continue
        if fvg.fill_ratio < fill_threshold:
            continue
        zones.append(
            _SourceZone(
                zone_type="FVG",
                direction=fvg.direction,
                low=fvg.gap_low,
                high=fvg.gap_high,
                origin_time=fvg.created_at,
                fill_ratio=fvg.fill_ratio,
                fill_mode=_fill_mode(fill_threshold),
                displacement_factor=structure.displacement_factor,
                has_displacement=structure.has_displacement,
                metadata={
                    "source_fvg_status": fvg.status,
                    "source_fvg_fill_percent": fvg.fill_percent,
                    "source_zone_low": fvg.gap_low,
                    "source_zone_high": fvg.gap_high,
                    "ote_retracement_level": None,
                },
            )
        )
    for block in snapshot.order_blocks:
        if block.direction != direction or block.invalidated or block.origin_time < structure.timestamp:
            continue
        if not block.mitigated:
            continue
        zones.append(
            _SourceZone(
                zone_type="OB",
                direction=block.direction,
                low=block.zone_low,
                high=block.zone_high,
                origin_time=block.origin_time,
                fill_ratio=1.0,
                fill_mode="ob_retest",
                displacement_factor=structure.displacement_factor,
                has_displacement=structure.has_displacement,
                metadata={
                    "ifvg_mean_threshold": block.mean_threshold,
                    "source_zone_low": block.zone_low,
                    "source_zone_high": block.zone_high,
                    "ote_retracement_level": None,
                },
            )
        )
    return next(iter(sorted(zones, key=lambda item: item.origin_time, reverse=True)), None)


def _fill_mode(threshold: float) -> str:
    if threshold >= 1.0:
        return "100"
    if threshold >= 0.5:
        return "50"
    return "25"


def _reason(context: StrategyContext, side: str, source_zone: _SourceZone, ltf_fvg: FairValueGap | None) -> str:
    htf = context.htf_context
    pullback = f"{source_zone.fill_mode}% FF FVG" if source_zone.zone_type == "FVG" else "OB retracement"
    entry = "LTF FVG pickup" if ltf_fvg is not None else "LTF MSS pickup"
    if htf is None:
        return f"Missed entry pullback: {pullback} -> {entry}"
    return (
        f"HTF {htf.bias.direction} {htf.dealing_range.location}/{htf.zone.zone_type} context -> "
        f"{pullback}, {entry}"
    )


def _target_hint(side: str, entry_low: float, entry_high: float, invalidation: float) -> float:
    entry_mid = (entry_low + entry_high) / 2
    risk = abs(entry_mid - invalidation)
    if side == "long":
        return entry_high + risk * 2
    return entry_low - risk * 2


def _source_zone_allowed(zone_type: str, fill_mode: str, requested: str) -> bool:
    if requested == "any":
        return True
    if requested == "ob":
        return zone_type == "OB"
    if requested == "fvg_ce":
        return zone_type == "FVG" and fill_mode in {"50", "100"}
    if requested == "fvg_full":
        return zone_type == "FVG" and fill_mode == "100"
    return True


def _objective_reached_before_entry(
    snapshot: PrimitiveSnapshot,
    htf_context: object,
    side: str,
    start_time: int,
) -> bool:
    objective = getattr(htf_context, "objective", None)
    target = getattr(objective, "target_level", None)
    if target is None:
        return True
    for candle in snapshot.candles:
        if int(candle["time"]) <= start_time:
            continue
        if side == "long" and float(candle["high"]) >= float(target):
            return True
        if side == "short" and float(candle["low"]) <= float(target):
            return True
    return False


def _first_touch_time(snapshot: PrimitiveSnapshot, low: float, high: float, start_time: int) -> int | None:
    for candle in snapshot.candles:
        if int(candle["time"]) <= start_time:
            continue
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            return int(candle["time"])
    return None


def _bars_between(snapshot: PrimitiveSnapshot, start_time: int, end_time: int) -> int | None:
    ordered = [int(candle["time"]) for candle in snapshot.candles]
    try:
        start_idx = next(idx for idx, value in enumerate(ordered) if value >= start_time)
        end_idx = next(idx for idx, value in enumerate(ordered) if value >= end_time)
    except StopIteration:
        return None
    return max(0, end_idx - start_idx)


def _distance_to_objective(context: StrategyContext, side: str, entry_mid: float) -> float | None:
    if context.htf_context is None or context.htf_context.objective.target_level is None:
        return None
    target = float(context.htf_context.objective.target_level)
    if side == "long":
        return max(0.0, target - entry_mid)
    return max(0.0, entry_mid - target)


def _nearest_htf_ob_extreme(snapshot: PrimitiveSnapshot, side: str) -> tuple[float | None, float | None]:
    direction = "bullish" if side == "long" else "bearish"
    block = next((item for item in sorted(snapshot.order_blocks, key=lambda item: item.origin_time, reverse=True) if item.direction == direction), None)
    if block is None:
        return None, None
    return block.zone_low, block.zone_high


def _missed_entry_distance(snapshot: PrimitiveSnapshot, source_zone: _SourceZone) -> float | None:
    price = current_price(snapshot)
    if price is None:
        return None
    if source_zone.low <= price <= source_zone.high:
        return 0.0
    return min(abs(price - source_zone.low), abs(price - source_zone.high))


def _max_grade(left: str, right: str) -> str:
    order = {"weak": 0, "valid": 1, "strong": 2}
    return left if order.get(left, 0) >= order.get(right, 0) else right


__all__ = ["detect_entry_model_3"]
