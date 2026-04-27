from __future__ import annotations

from dataclasses import dataclass

Candle = dict[str, float | int]


@dataclass(slots=True)
class BacktestEvent:
    event_id: str
    model_name: str
    symbol: str
    timeframe: str
    direction: str
    detected_at: int
    status: str
    entry_low: float | None
    entry_high: float | None
    entry_price: float | None
    invalidation: float | None
    risk: float | None
    stop_loss: float | None = None
    structural_invalidation: float | None = None
    invalidation_source: str | None = None
    stop_mode: str | None = None
    model3_stop_mode: str | None = None
    risk_bps: float | None = None
    risk_valid: bool | None = None
    stop_buffer_bps: float | None = None
    invalidation_confirmation: str | None = None
    stop_hit_policy: str | None = None
    score: int | None = None
    reason: str = ""
    components_json: str = ""
    warning: str | None = None
    skipped_reason: str | None = None
    htf_bias: str | None = None
    htf_confidence: float | None = None
    htf_zone_type: str | None = None
    htf_zone_low: float | None = None
    htf_zone_high: float | None = None
    htf_location: str | None = None
    htf_allows_long: bool | None = None
    htf_allows_short: bool | None = None
    htf_objective_type: str | None = None
    htf_objective_level: float | None = None
    htf_structure_bias: str | None = None
    htf_draw_direction: str | None = None
    htf_objective_reached: bool | None = None
    htf_objective_unreached: bool | None = None
    htf_context_alignment: str | None = None
    htf_poi_direction: str | None = None
    displacement_factor: float | None = None
    has_displacement: bool | None = None
    displacement_grade: str | None = None
    body_ratio: float | None = None
    range_expansion: float | None = None
    close_beyond_structure: bool | None = None
    created_fvg_after_break: bool | None = None
    bars_in_displacement: int | None = None
    swing_significance: str | None = None
    sweep_swing_significance: str | None = None
    sweep_liquidity_quality: str | None = None
    structure_swing_significance: str | None = None
    objective_liquidity_quality: str | None = None
    objective_type: str | None = None
    objective_age_bars: int | None = None
    objective_is_equal_high_low: bool | None = None
    dealing_range_source: str | None = None
    fvg_status: str | None = None
    fvg_fill_percent: float | None = None
    fvg_quality: str | None = None
    source_fvg_direction: str | None = None
    source_fvg_time: int | None = None
    breach_time: int | None = None
    breach_displacement_factor: float | None = None
    breach_displacement_grade: str | None = None
    ifvg_mean_threshold: float | None = None
    ifvg_grade: str | None = None
    ifvg_quality: str | None = None
    ifvg_ce_level: float | None = None
    ifvg_retest_depth: float | None = None
    ifvg_breach_time: int | None = None
    ifvg_retest_time: int | None = None
    ifvg_time_to_retest_bars: int | None = None
    bars_sweep_to_breach: int | None = None
    rr_to_objective: float | None = None
    source_zone_type: str | None = None
    source_zone_time: int | None = None
    source_zone_low: float | None = None
    source_zone_high: float | None = None
    source_zone_valid: bool | None = None
    source_zone_invalidation_level: float | None = None
    missed_entry_distance: float | None = None
    original_entry_zone_low: float | None = None
    original_entry_zone_high: float | None = None
    objective_reached_before_entry: bool | None = None
    distance_to_objective: float | None = None
    fill_percent: float | None = None
    fill_mode: str | None = None
    time_to_fill: int | None = None
    reaction_speed: int | None = None
    ltf_mss_time: int | None = None
    ltf_reaction_bars: int | None = None
    ltf_reaction_displacement_grade: str | None = None
    objective_quality: str | None = None
    poi_quality: str | None = None
    risk_quality: str | None = None


@dataclass(slots=True)
class BacktestOutcome:
    event_id: str
    forward_bars: int
    mfe: float | None
    mae: float | None
    mfe_r: float | None
    mae_r: float | None
    hit_0_5r: bool
    hit_1r: bool
    hit_2r: bool
    invalidated: bool
    bars_to_0_5r: int | None
    bars_to_1r: int | None
    bars_to_2r: int | None
    bars_to_invalidation: int | None
    future_high: float | None
    future_low: float | None
    hit_1r_before_invalidation: bool
    hit_2r_before_invalidation: bool


@dataclass(slots=True)
class BacktestResult:
    event: BacktestEvent
    outcome: BacktestOutcome


__all__ = [
    "BacktestEvent",
    "BacktestOutcome",
    "BacktestResult",
    "Candle",
]
