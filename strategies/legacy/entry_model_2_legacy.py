"""
LEGACY MODEL.

This model is archived and disabled by default.
It is preserved only for baseline comparison.
New active ICT models live in strategies/ict_models/.
"""

from __future__ import annotations

from dataclasses import dataclass

from market_primitives.common import BreakerBlock, InvertedFVG, LiquiditySweep, zone_overlap

from config import MAX_IFVG_RETEST_BARS, MAX_INVERSION_AGE_BARS, MAX_SWEEP_TO_IFVG_BARS, REQUIRE_HTF_CONTEXT_FOR_ENTRY_MODELS
from strategies.htf_context import htf_allows_side, htf_metadata, htf_score_modifier
from strategies.risk_policy import model2_risk_plan, risk_metadata
from strategies.scoring import score_model_2
from strategies.setup_quality import build_score_components, objective_quality, poi_quality, risk_quality
from strategies.setup_utils import classify_zone_status, is_recent_enough, primitive_direction, sweep_label
from strategies.types import EntrySetup, PrimitiveSnapshot, StrategyContext, default_components


@dataclass(slots=True)
class _InversionCandidate:
    kind: str
    direction: str
    zone_low: float
    zone_high: float
    armed_time: int
    timestamp: int
    confidence: float
    metadata: dict


def detect_entry_model_2(context: StrategyContext) -> list[EntrySetup]:
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
    candidates = sorted(_build_candidates(snapshot, direction), key=lambda item: item.armed_time)
    current_timestamp = int(snapshot.candles[-1]["time"]) if snapshot.candles else 0

    for sweep in sweeps[:4]:
        candidate = next(
            (
                item
                for item in candidates
                if item.armed_time > sweep.timestamp
                and item.timestamp > sweep.timestamp
                and is_recent_enough(current_timestamp, item.armed_time, snapshot.timeframe, MAX_INVERSION_AGE_BARS)
            ),
            None,
        )
        if candidate is None:
            continue
        setup = _build_setup(snapshot, side, sweep, candidate, context, htf_mode)
        if setup is not None:
            return [setup]
    return []


def _build_candidates(snapshot: PrimitiveSnapshot, direction: str) -> list[_InversionCandidate]:
    candidates: list[_InversionCandidate] = []
    for inversion in snapshot.ifvgs:
        if inversion.direction != direction:
            continue
        candidates.append(_from_ifvg(inversion))
    return candidates


def _from_ifvg(inversion: InvertedFVG) -> _InversionCandidate:
    return _InversionCandidate(
        kind="IFVG",
        direction=inversion.direction,
        zone_low=inversion.zone_low,
        zone_high=inversion.zone_high,
        armed_time=inversion.invalidated_at,
        timestamp=inversion.retest_at or inversion.invalidated_at,
        confidence=inversion.confidence,
        metadata={
            "source_direction": inversion.source_direction,
            "source_fvg_direction": inversion.source_direction,
            "source_fvg_time": inversion.source_fvg_time,
            "invalidated_at": inversion.invalidated_at,
            "breach_time": inversion.invalidated_at,
            "retest_at": inversion.retest_at,
            "breach_displacement_factor": inversion.breach_displacement_factor,
            "has_displacement": inversion.breach_displacement_factor > 0,
            "ifvg_mean_threshold": inversion.mean_threshold,
            "ifvg_grade": inversion.ifvg_grade,
            "ifvg_quality": inversion.ifvg_grade,
            "ifvg_ce_level": inversion.ifvg_ce_level,
            "ifvg_retest_depth": inversion.ifvg_retest_depth,
            "ifvg_retest_touched_ce": inversion.metadata.get("ifvg_retest_touched_ce"),
            "ifvg_retest_breached_ce_by_close": inversion.metadata.get("ifvg_retest_breached_ce_by_close"),
            "ifvg_breach_time": inversion.invalidated_at,
            "ifvg_retest_time": inversion.retest_at,
            "ifvg_time_to_retest_bars": inversion.ifvg_time_to_retest_bars,
            "breach_displacement_grade": inversion.breach_displacement_grade,
        },
    )


def _from_breaker(breaker: BreakerBlock) -> _InversionCandidate:
    return _InversionCandidate(
        kind="Breaker",
        direction=breaker.direction,
        zone_low=breaker.zone_low,
        zone_high=breaker.zone_high,
        armed_time=breaker.trigger_time,
        timestamp=breaker.timestamp,
        confidence=0.7 if breaker.retested else 0.58,
        metadata={
            "origin_time": breaker.origin_time,
            "trigger_time": breaker.trigger_time,
            "retested": breaker.retested,
        },
    )


def _build_setup(
    snapshot: PrimitiveSnapshot,
    side: str,
    sweep: LiquiditySweep,
    candidate: _InversionCandidate,
    context: StrategyContext,
    htf_mode: str,
) -> EntrySetup | None:
    higher_snapshot = context.higher_timeframe
    status_info = classify_zone_status(
        snapshot,
        zone_low=candidate.zone_low,
        zone_high=candidate.zone_high,
        armed_time=candidate.armed_time,
    )
    if status_info is None:
        return None
    status, status_time = status_info
    if status != "watching" and status_time <= candidate.armed_time:
        return None
    if context.require_displacement and candidate.metadata.get("has_displacement") is False:
        return None
    if candidate.metadata.get("ifvg_grade") == "weak":
        return None
    time_to_retest = candidate.metadata.get("ifvg_time_to_retest_bars")
    if isinstance(time_to_retest, int) and time_to_retest > MAX_IFVG_RETEST_BARS:
        return None
    bars_sweep_to_breach = _bars_between(snapshot, sweep.timestamp, int(candidate.armed_time))
    if bars_sweep_to_breach is not None and bars_sweep_to_breach > MAX_SWEEP_TO_IFVG_BARS:
        return None

    risk_plan = model2_risk_plan(
        side=side,
        zone_low=candidate.zone_low,
        zone_high=candidate.zone_high,
        sweep_extreme=sweep.wick_extreme,
        stop_mode=context.stop_mode,
        stop_buffer_bps=context.stop_buffer_bps,
        invalidation_confirmation=context.invalidation_confirmation,
    )
    if not risk_plan.risk_valid:
        return None
    direction = primitive_direction(side)  # type: ignore[arg-type]

    messy_overlap = any(
        zone_overlap(candidate.zone_low, candidate.zone_high, block.zone_low, block.zone_high) > 0.9
        for block in (higher_snapshot.breaker_blocks if higher_snapshot else [])
    )
    score = score_model_2(
        clean_sweep=sweep.clean,
        inversion_confidence=candidate.confidence,
        entry_low=candidate.zone_low,
        entry_high=candidate.zone_high,
        invalidation=risk_plan.stop_loss,
        htf_modifier=htf_score_modifier(context.htf_context, side, htf_mode),
        messy_overlap=messy_overlap,
        breach_displacement_factor=float(candidate.metadata.get("breach_displacement_factor") or 0.0),
        has_displacement=bool(candidate.metadata.get("has_displacement")),
        ifvg_grade=str(candidate.metadata.get("ifvg_grade") or "weak"),
        displacement_grade=str(candidate.metadata.get("breach_displacement_grade") or "weak"),
    )
    htf_meta = htf_metadata(context.htf_context)
    rr_to_objective = _rr_to_objective(context, side, (candidate.zone_low + candidate.zone_high) / 2, risk_plan.stop_loss)
    quality_meta = {
        **htf_meta,
        "objective_unreached": htf_meta.get("htf_objective_unreached"),
        "risk_bps": risk_plan.risk_bps,
    }
    score_components = build_score_components(
        htf_aligned=bool(htf_meta.get("htf_context_alignment") == "aligned" or htf_meta.get("htf_bias") == direction),
        objective_unreached=bool(htf_meta.get("htf_objective_unreached")),
        risk_valid=risk_plan.risk_valid,
        displacement_grade=str(candidate.metadata.get("breach_displacement_grade") or "weak"),
        ifvg_grade=str(candidate.metadata.get("ifvg_grade") or "weak"),
        sweep_quality="high" if sweep.clean else "medium",
        risk_bps=risk_plan.risk_bps,
        rr_to_objective=rr_to_objective,
        poi_quality_value=poi_quality(quality_meta),
        objective_quality_value=objective_quality(quality_meta),
    )

    components = default_components()
    components["sweep_detected"] = True
    components["inversion_detected"] = True

    return EntrySetup(
        model_name="Entry Model 2",
        direction="long" if side == "long" else "short",
        symbol=snapshot.symbol,
        timeframe=snapshot.timeframe,
        status=status,
        entry_low=candidate.zone_low,
        entry_high=candidate.zone_high,
        invalidation=risk_plan.stop_loss,
        target_hint=_target_hint(side, candidate.zone_low, candidate.zone_high, sweep.wick_extreme),
        sweep_level=sweep.liquidity_level,
        structure_level=None,
        context_timeframe=context.htf_timeframe,
        score=score,
        reason=_reason(context, side, candidate),
        components=components,
        timestamp=max(status_time, sweep.timestamp, candidate.timestamp),
        metadata={
            "candidate_kind": candidate.kind,
            "sweep_time": sweep.timestamp,
            "preceding_sweep": True,
            "swing_significance": sweep.source_swing_significance,
            "sweep_swing_significance": sweep.source_swing_significance,
            "sweep_liquidity_quality": sweep.metadata.get("sweep_liquidity_quality"),
            "sweep_level": sweep.liquidity_level,
            "bars_sweep_to_breach": bars_sweep_to_breach,
            "rr_to_objective": rr_to_objective,
            "has_htf_confluence": htf_meta.get("htf_context_alignment") == "aligned",
            "htf_alignment": htf_meta.get("htf_context_alignment"),
            "objective_unreached": htf_meta.get("htf_objective_unreached"),
            "objective_quality": objective_quality(quality_meta),
            "poi_quality": poi_quality(quality_meta),
            "ifvg_quality": candidate.metadata.get("ifvg_grade"),
            "sweep_quality": "high" if sweep.clean else "medium",
            "risk_quality": risk_quality(risk_plan.risk_bps),
            "score_components": score_components,
            **candidate.metadata,
            **risk_metadata(risk_plan),
            **htf_meta,
        },
    )


def _reason(context: StrategyContext, side: str, candidate: _InversionCandidate) -> str:
    htf = context.htf_context
    if htf is None:
        return f"{sweep_label(side)} sweep, {candidate.kind} inversion armed"
    return (
        f"HTF {htf.bias.direction} {htf.dealing_range.location}/{htf.zone.zone_type} context -> "
        f"LTF {sweep_label(side)} sweep, {candidate.kind} inversion retest"
    )


def _target_hint(side: str, entry_low: float, entry_high: float, invalidation: float) -> float:
    entry_mid = (entry_low + entry_high) / 2
    risk = abs(entry_mid - invalidation)
    if side == "long":
        return entry_high + risk * 2.5
    return entry_low - risk * 2.5


def _bars_between(snapshot: PrimitiveSnapshot, start_time: int, end_time: int) -> int | None:
    ordered = [int(candle["time"]) for candle in snapshot.candles]
    try:
        start_idx = next(idx for idx, value in enumerate(ordered) if value >= start_time)
        end_idx = next(idx for idx, value in enumerate(ordered) if value >= end_time)
    except StopIteration:
        return None
    return max(0, end_idx - start_idx)


def _rr_to_objective(context: StrategyContext, side: str, entry_mid: float, stop_loss: float) -> float | None:
    if context.htf_context is None or context.htf_context.objective.target_level is None:
        return None
    target = float(context.htf_context.objective.target_level)
    distance = max(0.0, target - entry_mid) if side == "long" else max(0.0, entry_mid - target)
    risk = abs(entry_mid - stop_loss)
    if risk <= 0:
        return None
    return round(distance / risk, 6)


__all__ = ["detect_entry_model_2"]
