from __future__ import annotations

from collections import defaultdict
import json
from statistics import median
from typing import Any, Callable

from backtesting import BacktestResult

SummaryRow = dict[str, Any]
KeyFunc = Callable[[BacktestResult], tuple[Any, ...]]


def score_bucket(score: int | None) -> str:
    if score is None:
        return "unknown"
    if score <= 2:
        return "low"
    if score == 3:
        return "medium"
    return "high"


def build_all_summaries(results: list[BacktestResult]) -> dict[str, list[SummaryRow]]:
    return {
        "summary_by_model": summarize(results, lambda row: (row.event.model_name,), ("model",)),
        "summary_by_direction": summarize(
            results,
            lambda row: (row.event.model_name, row.event.direction),
            ("model", "direction"),
        ),
        "summary_by_timeframe": summarize(
            results,
            lambda row: (row.event.model_name, row.event.timeframe),
            ("model", "timeframe"),
        ),
        "summary_by_symbol": summarize(
            results,
            lambda row: (row.event.model_name, row.event.symbol),
            ("model", "symbol"),
        ),
        "summary_by_score": summarize(
            results,
            lambda row: (row.event.model_name, score_bucket(row.event.score)),
            ("model", "score_bucket"),
        ),
        "summary_by_htf_bias": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_bias or "none"),
            ("model", "htf_bias"),
        ),
        "summary_by_htf_zone": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_zone_type or "None"),
            ("model", "htf_zone_type"),
        ),
        "summary_by_htf_location": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_location or "unknown"),
            ("model", "htf_location"),
        ),
        "summary_by_model_htf_alignment": summarize(
            results,
            lambda row: (row.event.model_name, _htf_alignment(row)),
            ("model", "htf_alignment"),
        ),
        "summary_by_displacement": summarize(
            results,
            lambda row: (row.event.model_name, _displacement_bucket(row)),
            ("model", "displacement"),
        ),
        "summary_by_displacement_grade": summarize(
            results,
            lambda row: (row.event.model_name, row.event.displacement_grade or "unknown"),
            ("model", "displacement_grade"),
        ),
        "summary_by_body_ratio_bucket": summarize(
            results,
            lambda row: (row.event.model_name, _number_bucket(row.event.body_ratio, (0.5, 0.7), ("lt_0_50", "0_50_0_70", "gte_0_70"))),
            ("model", "body_ratio_bucket"),
        ),
        "summary_by_range_expansion_bucket": summarize(
            results,
            lambda row: (row.event.model_name, _number_bucket(row.event.range_expansion, (1.2, 1.5), ("lt_1_20", "1_20_1_50", "gte_1_50"))),
            ("model", "range_expansion_bucket"),
        ),
        "summary_by_created_fvg_after_break": summarize(
            results,
            lambda row: (row.event.model_name, row.event.created_fvg_after_break),
            ("model", "created_fvg_after_break"),
        ),
        "summary_by_stop_mode": summarize(
            results,
            lambda row: (row.event.model_name, row.event.stop_mode or "none"),
            ("model", "stop_mode"),
        ),
        "summary_by_model3_stop_mode": summarize(
            results,
            lambda row: (row.event.model_name, row.event.model3_stop_mode or "none"),
            ("model", "model3_stop_mode"),
        ),
        "summary_by_invalidation_source": summarize(
            results,
            lambda row: (row.event.model_name, row.event.invalidation_source or "unknown"),
            ("model", "invalidation_source"),
        ),
        "summary_by_risk_bps_bucket": summarize(
            results,
            lambda row: (row.event.model_name, _risk_bps_bucket(row.event.risk_bps)),
            ("model", "risk_bps_bucket"),
        ),
        "summary_by_htf_alignment": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_context_alignment or _htf_alignment(row)),
            ("model", "htf_alignment"),
        ),
        "summary_by_objective_reached": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_objective_reached),
            ("model", "objective_reached"),
        ),
        "summary_by_objective_unreached": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_objective_unreached),
            ("model", "objective_unreached"),
        ),
        "summary_by_draw_direction": summarize(
            results,
            lambda row: (row.event.model_name, row.event.htf_draw_direction or "none"),
            ("model", "draw_direction"),
        ),
        "summary_by_ifvg_grade": summarize(
            results,
            lambda row: (row.event.model_name, row.event.ifvg_grade or "none"),
            ("model", "ifvg_grade"),
        ),
        "summary_by_ifvg_retest_depth": summarize(
            results,
            lambda row: (row.event.model_name, _number_bucket(row.event.ifvg_retest_depth, (0.5, 1.0), ("lt_ce", "ce_to_full", "full_plus"))),
            ("model", "ifvg_retest_depth"),
        ),
        "summary_by_ifvg_time_to_retest": summarize(
            results,
            lambda row: (row.event.model_name, _bar_bucket(row.event.ifvg_time_to_retest_bars)),
            ("model", "ifvg_time_to_retest"),
        ),
        "summary_by_bars_sweep_to_breach": summarize(
            results,
            lambda row: (row.event.model_name, _bar_bucket(row.event.bars_sweep_to_breach)),
            ("model", "bars_sweep_to_breach"),
        ),
        "summary_by_rr_to_objective": summarize(
            results,
            lambda row: (row.event.model_name, _number_bucket(row.event.rr_to_objective, (1.5, 2.0), ("lt_1_5", "1_5_2_0", "gte_2_0"))),
            ("model", "rr_to_objective"),
        ),
        "summary_by_objective_quality": summarize(
            results,
            lambda row: (row.event.model_name, row.event.objective_quality or row.event.objective_liquidity_quality or "unknown"),
            ("model", "objective_quality"),
        ),
        "summary_by_poi_quality": summarize(
            results,
            lambda row: (row.event.model_name, row.event.poi_quality or "unknown"),
            ("model", "poi_quality"),
        ),
        "summary_by_risk_quality": summarize(
            results,
            lambda row: (row.event.model_name, row.event.risk_quality or "unknown"),
            ("model", "risk_quality"),
        ),
        "summary_by_score_component": summarize(
            results,
            lambda row: (row.event.model_name, _score_component_bucket(row)),
            ("model", "score_component"),
        ),
        "summary_by_sweep_swing_significance": summarize(
            results,
            lambda row: (row.event.model_name, row.event.sweep_swing_significance or "unknown"),
            ("model", "sweep_swing_significance"),
        ),
        "summary_by_structure_swing_significance": summarize(
            results,
            lambda row: (row.event.model_name, row.event.structure_swing_significance or "unknown"),
            ("model", "structure_swing_significance"),
        ),
        "summary_by_equal_liquidity": summarize(
            results,
            lambda row: (row.event.model_name, row.event.objective_is_equal_high_low),
            ("model", "objective_is_equal_high_low"),
        ),
        "summary_by_dealing_range_source": summarize(
            results,
            lambda row: (row.event.model_name, row.event.dealing_range_source or "unknown"),
            ("model", "dealing_range_source"),
        ),
        "summary_by_model3_fill_threshold": summarize(
            results,
            lambda row: (row.event.model_name, row.event.fill_mode or "none"),
            ("model", "fill_mode"),
        ),
        "summary_by_fvg_status": summarize(
            results,
            lambda row: (row.event.model_name, row.event.fvg_status or "unknown"),
            ("model", "fvg_status"),
        ),
    }


def summarize(results: list[BacktestResult], key_func: KeyFunc, key_names: tuple[str, ...]) -> list[SummaryRow]:
    grouped: dict[tuple[Any, ...], list[BacktestResult]] = defaultdict(list)
    for result in results:
        grouped[key_func(result)].append(result)

    rows: list[SummaryRow] = []
    for key, group in sorted(grouped.items(), key=lambda item: tuple(str(part) for part in item[0])):
        row: SummaryRow = {name: value for name, value in zip(key_names, key)}
        row.update(_metrics_for(group))
        rows.append(row)
    return rows


def _metrics_for(group: list[BacktestResult]) -> SummaryRow:
    count = len(group)
    valid_r = [item for item in group if item.event.skipped_reason is None and item.outcome.mfe_r is not None]
    skipped_outcomes = [item for item in group if item not in valid_r]
    mfe_r = [item.outcome.mfe_r for item in valid_r if item.outcome.mfe_r is not None]
    mae_r = [item.outcome.mae_r for item in valid_r if item.outcome.mae_r is not None]
    scores = [item.event.score for item in group if item.event.score is not None]

    return {
        "count": count,
        "valid_outcome_count": len(valid_r),
        "skipped_outcome_count": len(skipped_outcomes),
        "invalid_risk_count": sum(1 for item in group if item.event.skipped_reason == "invalid risk" or item.event.risk_valid is False),
        "long_count": sum(1 for item in group if item.event.direction == "long"),
        "short_count": sum(1 for item in group if item.event.direction == "short"),
        "avg_mfe_r": _avg(mfe_r),
        "median_mfe_r": _median(mfe_r),
        "avg_mae_r": _avg(mae_r),
        "median_mae_r": _median(mae_r),
        "hit_0_5r_rate": _rate(valid_r, lambda item: item.outcome.hit_0_5r),
        "hit_1r_rate": _rate(valid_r, lambda item: item.outcome.hit_1r),
        "hit_2r_rate": _rate(valid_r, lambda item: item.outcome.hit_2r),
        "invalidation_rate": _rate(group, lambda item: item.outcome.invalidated),
        "hit_1r_before_invalidation_rate": _rate(valid_r, lambda item: item.outcome.hit_1r_before_invalidation),
        "hit_2r_before_invalidation_rate": _rate(valid_r, lambda item: item.outcome.hit_2r_before_invalidation),
        "avg_score": _avg(scores),
        "best_symbol": _best_dimension(group, "symbol"),
        "best_timeframe": _best_dimension(group, "timeframe"),
    }


def _avg(values: list[float | int]) -> float | None:
    if not values:
        return None
    return round(sum(float(value) for value in values) / len(values), 6)


def _median(values: list[float | int]) -> float | None:
    if not values:
        return None
    return round(float(median(float(value) for value in values)), 6)


def _rate(group: list[BacktestResult], predicate: Callable[[BacktestResult], bool]) -> float | None:
    if not group:
        return None
    return round(sum(1 for item in group if predicate(item)) / len(group), 6)


def _best_dimension(group: list[BacktestResult], attr: str) -> str | None:
    by_value: dict[str, list[float]] = defaultdict(list)
    for item in group:
        value = str(getattr(item.event, attr))
        if item.outcome.mfe_r is not None:
            by_value[value].append(item.outcome.mfe_r)
    if not by_value:
        return None
    best = max(by_value.items(), key=lambda item: sum(item[1]) / len(item[1]))
    return best[0]


def _htf_alignment(result: BacktestResult) -> str:
    bias = result.event.htf_bias
    if not bias or bias == "none":
        return "no_htf"
    if bias == "neutral":
        return "neutral"
    if (result.event.direction == "long" and bias == "bullish") or (
        result.event.direction == "short" and bias == "bearish"
    ):
        return "aligned"
    return "opposed"


def _displacement_bucket(result: BacktestResult) -> str:
    if result.event.has_displacement is True:
        return "has_displacement"
    if result.event.has_displacement is False:
        return "weak_or_none"
    return "unknown"


def _risk_bps_bucket(value: float | None) -> str:
    return _number_bucket(value, (10, 25, 50), ("lt_10", "10_25", "25_50", "gte_50"))


def _number_bucket(value: float | None, thresholds: tuple[float, ...], labels: tuple[str, ...]) -> str:
    if value is None:
        return "unknown"
    for threshold, label in zip(thresholds, labels):
        if value < threshold:
            return label
    return labels[-1]


def _bar_bucket(value: int | None) -> str:
    if value is None:
        return "unknown"
    if value <= 5:
        return "0_5"
    if value <= 15:
        return "6_15"
    if value <= 40:
        return "16_40"
    return "gt_40"


def _score_component_bucket(result: BacktestResult) -> str:
    try:
        payload = json.loads(result.event.components_json)
    except (TypeError, json.JSONDecodeError):
        return "unknown"
    metadata = payload.get("metadata") or {}
    components = metadata.get("score_components") or {}
    gates = components.get("gates") or {}
    if gates and not all(bool(value) for value in gates.values()):
        failed = [key for key, value in gates.items() if not value]
        return f"failed_{failed[0]}" if failed else "failed_gate"
    risk = components.get("risk") or {}
    quality = components.get("quality") or {}
    return str(risk.get("risk_quality") or quality.get("displacement_grade") or "unknown")


__all__ = ["SummaryRow", "build_all_summaries", "score_bucket", "summarize"]
