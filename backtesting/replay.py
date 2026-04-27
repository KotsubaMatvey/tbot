from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass, fields, is_dataclass
from typing import Any, Callable

from backtesting import BacktestEvent, BacktestResult, Candle
from backtesting.accumulator import ReplaySnapshotCache
from backtesting.context import CandleStore, build_accumulated_strategy_context_for_replay
from backtesting.outcome import evaluate_forward_outcome
from strategies import detect_entry_model_1, detect_entry_model_2, detect_entry_model_3
from strategies.types import EntrySetup, StrategyContext

logger = logging.getLogger(__name__)

Detector = Callable[[StrategyContext], list[EntrySetup] | list[dict[str, Any]]]

MODEL_DETECTORS: dict[str, Detector] = {
    "model1": detect_entry_model_1,
    "model2": detect_entry_model_2,
    "model3": detect_entry_model_3,
}

MODEL_NAMES: dict[str, str] = {
    "model1": "Entry Model 1",
    "model2": "Entry Model 2",
    "model3": "Entry Model 3",
}


@dataclass(slots=True)
class ReplayConfig:
    symbol: str
    timeframe: str
    models: list[str]
    forward_bars: int = 20
    warmup_bars: int = 100
    cooldown_bars: int = 5
    price_precision: int = 4
    start_ms: int | None = None
    end_ms: int | None = None
    htf_mode: str = "strict"
    require_displacement: bool = True
    model3_fill_threshold: float = 0.5
    stop_mode: str = "structural"
    model3_stop_mode: str = "source_zone_extreme"
    stop_buffer_bps: float = 2.0
    invalidation_confirmation: str = "close"
    model3_reaction_bars: int = 10
    model3_min_rr_to_objective: float = 1.5
    model3_source_zone: str = "any"


@dataclass(slots=True)
class ReplayWarning:
    model_name: str
    symbol: str
    timeframe: str
    timestamp: int
    message: str


def normalize_model_key(model: str) -> str:
    key = model.strip().lower().replace("_", "").replace("-", "").replace(" ", "")
    aliases = {
        "1": "model1",
        "entrymodel1": "model1",
        "model1": "model1",
        "2": "model2",
        "entrymodel2": "model2",
        "model2": "model2",
        "3": "model3",
        "entrymodel3": "model3",
        "model3": "model3",
    }
    if key not in aliases:
        raise ValueError(f"unsupported model '{model}'. Use model1, model2, model3.")
    return aliases[key]


def replay_entry_models(
    *,
    candles: list[Candle],
    candle_store: CandleStore,
    config: ReplayConfig,
) -> tuple[list[BacktestResult], list[ReplayWarning]]:
    results: list[BacktestResult] = []
    warnings: list[ReplayWarning] = []
    seen_keys: set[tuple[Any, ...]] = set()
    recent_by_zone: dict[tuple[Any, ...], int] = {}
    snapshot_cache = ReplaySnapshotCache(candle_store)

    model_keys = [normalize_model_key(model) for model in config.models]
    start_index = max(0, config.warmup_bars)

    for index in range(start_index, len(candles)):
        current = candles[index]
        current_timestamp = int(current["time"])
        if config.start_ms is not None and current_timestamp < config.start_ms:
            continue
        if config.end_ms is not None and current_timestamp > config.end_ms:
            continue
        context = build_accumulated_strategy_context_for_replay(
            symbol=config.symbol,
            timeframe=config.timeframe,
            current_timestamp=current_timestamp,
            snapshot_cache=snapshot_cache,
            htf_mode=config.htf_mode,
            require_displacement=config.require_displacement,
            model3_fill_threshold=config.model3_fill_threshold,
            stop_mode=config.stop_mode,
            model3_stop_mode=config.model3_stop_mode,
            stop_buffer_bps=config.stop_buffer_bps,
            invalidation_confirmation=config.invalidation_confirmation,
            model3_reaction_bars=config.model3_reaction_bars,
            model3_min_rr_to_objective=config.model3_min_rr_to_objective,
            model3_source_zone=config.model3_source_zone,
        )
        if context is None:
            continue

        for model_key in model_keys:
            detector = MODEL_DETECTORS[model_key]
            model_name = MODEL_NAMES[model_key]
            try:
                setups = detector(context)
            except Exception as exc:
                message = f"{type(exc).__name__}: {exc}"
                logger.exception(
                    "Backtest detector failed: model=%s symbol=%s timeframe=%s timestamp=%s",
                    model_name,
                    config.symbol,
                    config.timeframe,
                    current_timestamp,
                )
                warnings.append(
                    ReplayWarning(
                        model_name=model_name,
                        symbol=config.symbol,
                        timeframe=config.timeframe,
                        timestamp=current_timestamp,
                        message=message,
                    )
                )
                continue

            for raw_setup in setups:
                setup = _normalize_setup(raw_setup)
                if setup.get("status") != "triggered":
                    continue

                event = _setup_to_event(
                    setup=setup,
                    model_name=model_name,
                    symbol=config.symbol,
                    timeframe=config.timeframe,
                    detected_at=current_timestamp,
                    price_precision=config.price_precision,
                )
                dedup_key = _dedup_key(setup, event, config.price_precision)
                cooldown_key = _cooldown_key(event, config.price_precision)
                previous_index = recent_by_zone.get(cooldown_key)
                if dedup_key in seen_keys:
                    continue
                if previous_index is not None and index - previous_index <= config.cooldown_bars:
                    continue

                seen_keys.add(dedup_key)
                recent_by_zone[cooldown_key] = index

                future = candles[index + 1 : index + 1 + config.forward_bars]
                outcome = evaluate_forward_outcome(event, future)
                results.append(BacktestResult(event=event, outcome=outcome))

    return results, warnings


def replay_entry_models_multi_timeframe(
    *,
    candle_store: CandleStore,
    symbol: str,
    timeframes: list[str],
    models: list[str],
    forward_bars: int = 20,
    warmup_bars: int = 100,
    cooldown_bars: int = 5,
    price_precision: int = 4,
    start_ms: int | None = None,
    end_ms: int | None = None,
    htf_mode: str = "strict",
    require_displacement: bool = True,
    model3_fill_threshold: float = 0.5,
    stop_mode: str = "structural",
    model3_stop_mode: str = "source_zone_extreme",
    stop_buffer_bps: float = 2.0,
    invalidation_confirmation: str = "close",
    model3_reaction_bars: int = 10,
    model3_min_rr_to_objective: float = 1.5,
    model3_source_zone: str = "any",
) -> tuple[list[BacktestResult], list[ReplayWarning]]:
    results: list[BacktestResult] = []
    warnings: list[ReplayWarning] = []
    snapshot_cache = ReplaySnapshotCache(candle_store)
    model_keys = [normalize_model_key(model) for model in models]
    seen_keys: set[tuple[Any, ...]] = set()
    recent_by_zone: dict[tuple[Any, ...], int] = {}

    replay_points: list[tuple[int, str, int]] = []
    for timeframe in timeframes:
        candles = candle_store.get((symbol, timeframe), [])
        for index in range(max(0, warmup_bars), len(candles)):
            timestamp = int(candles[index]["time"])
            if start_ms is not None and timestamp < start_ms:
                continue
            if end_ms is not None and timestamp > end_ms:
                continue
            replay_points.append((timestamp, timeframe, index))
    replay_points.sort(key=lambda item: (item[0], item[1], item[2]))

    for current_timestamp, timeframe, index in replay_points:
        candles = candle_store.get((symbol, timeframe), [])
        context = build_accumulated_strategy_context_for_replay(
            symbol=symbol,
            timeframe=timeframe,
            current_timestamp=current_timestamp,
            snapshot_cache=snapshot_cache,
            htf_mode=htf_mode,
            require_displacement=require_displacement,
            model3_fill_threshold=model3_fill_threshold,
            stop_mode=stop_mode,
            model3_stop_mode=model3_stop_mode,
            stop_buffer_bps=stop_buffer_bps,
            invalidation_confirmation=invalidation_confirmation,
            model3_reaction_bars=model3_reaction_bars,
            model3_min_rr_to_objective=model3_min_rr_to_objective,
            model3_source_zone=model3_source_zone,
        )
        if context is None:
            continue

        for model_key in model_keys:
            detector = MODEL_DETECTORS[model_key]
            model_name = MODEL_NAMES[model_key]
            try:
                setups = detector(context)
            except Exception as exc:
                message = f"{type(exc).__name__}: {exc}"
                logger.exception(
                    "Backtest detector failed: model=%s symbol=%s timeframe=%s timestamp=%s",
                    model_name,
                    symbol,
                    timeframe,
                    current_timestamp,
                )
                warnings.append(
                    ReplayWarning(
                        model_name=model_name,
                        symbol=symbol,
                        timeframe=timeframe,
                        timestamp=current_timestamp,
                        message=message,
                    )
                )
                continue

            for raw_setup in setups:
                setup = _normalize_setup(raw_setup)
                if setup.get("status") != "triggered":
                    continue

                event = _setup_to_event(
                    setup=setup,
                    model_name=model_name,
                    symbol=symbol,
                    timeframe=timeframe,
                    detected_at=current_timestamp,
                    price_precision=price_precision,
                )
                dedup_key = _dedup_key(setup, event, price_precision)
                cooldown_key = _cooldown_key(event, price_precision)
                recent_index_key = (*cooldown_key, timeframe)
                previous_index = recent_by_zone.get(recent_index_key)
                if dedup_key in seen_keys:
                    continue
                if previous_index is not None and index - previous_index <= cooldown_bars:
                    continue

                seen_keys.add(dedup_key)
                recent_by_zone[recent_index_key] = index

                future = candles[index + 1 : index + 1 + forward_bars]
                outcome = evaluate_forward_outcome(event, future)
                results.append(BacktestResult(event=event, outcome=outcome))

    return results, warnings


def _normalize_setup(setup: EntrySetup | dict[str, Any]) -> dict[str, Any]:
    if isinstance(setup, dict):
        return dict(setup)
    if is_dataclass(setup):
        return {field.name: getattr(setup, field.name) for field in fields(setup)}
    raise TypeError(f"unsupported setup type: {type(setup).__name__}")


def _setup_to_event(
    *,
    setup: dict[str, Any],
    model_name: str,
    symbol: str,
    timeframe: str,
    detected_at: int,
    price_precision: int,
) -> BacktestEvent:
    direction = str(setup.get("direction") or "").lower()
    level = _optional_float(setup.get("level"))
    entry_low = _optional_float(setup.get("entry_low"))
    entry_high = _optional_float(setup.get("entry_high"))
    if entry_low is None and entry_high is None and level is not None:
        entry_low = level
    entry_price = _entry_price(entry_low, entry_high)
    metadata = setup.get("metadata") or {}
    stop_loss = _optional_float(metadata.get("stop_loss")) or _optional_float(setup.get("stop_loss"))
    invalidation = stop_loss or _optional_float(setup.get("invalidation"))
    warning = None
    skipped_reason = None

    if invalidation is None:
        sweep_extreme = _optional_float(setup.get("sweep_extreme"))
        sweep_level = _optional_float(setup.get("sweep_level"))
        invalidation = _fallback_invalidation(direction, entry_low, entry_high, sweep_extreme or sweep_level)
        warning = "invalidation fallback used"

    risk = _risk(direction, entry_price, invalidation)
    if entry_price is None:
        skipped_reason = "missing entry"
    elif risk is None or risk <= 0:
        skipped_reason = "invalid risk"
        warning = "risk is not positive; R metrics are skipped"
        risk = None

    components = {
        "components": setup.get("components") or {},
        "metadata": setup.get("metadata") or {},
        "raw_model_name": setup.get("model_name"),
        "raw_timeframe": setup.get("timeframe"),
        "raw_timestamp": setup.get("timestamp"),
    }
    event_id = _event_id(
        model_name=model_name,
        symbol=symbol,
        timeframe=timeframe,
        direction=direction,
        detected_at=detected_at,
        entry_low=entry_low,
        entry_high=entry_high,
        price_precision=price_precision,
    )

    return BacktestEvent(
        event_id=event_id,
        model_name=model_name,
        symbol=symbol,
        timeframe=timeframe,
        direction=direction,
        detected_at=detected_at,
        status="skipped_outcome" if skipped_reason else str(setup.get("status") or ""),
        entry_low=entry_low,
        entry_high=entry_high,
        entry_price=entry_price,
        invalidation=invalidation,
        risk=risk,
        stop_loss=stop_loss or invalidation,
        structural_invalidation=_optional_float(metadata.get("structural_invalidation")),
        invalidation_source=_optional_str(metadata.get("invalidation_source")),
        stop_mode=_optional_str(metadata.get("stop_mode")),
        model3_stop_mode=_optional_str(metadata.get("model3_stop_mode")),
        risk_bps=_optional_float(metadata.get("risk_bps")),
        risk_valid=_optional_bool(metadata.get("risk_valid")),
        stop_buffer_bps=_optional_float(metadata.get("stop_buffer_bps")),
        invalidation_confirmation=_optional_str(metadata.get("invalidation_confirmation")),
        stop_hit_policy=_optional_str(metadata.get("stop_hit_policy")),
        score=_optional_int(setup.get("score")),
        reason=str(setup.get("reason") or ""),
        components_json=json.dumps(components, ensure_ascii=True, sort_keys=True, default=str),
        warning=warning,
        skipped_reason=skipped_reason,
        htf_bias=_optional_str(metadata.get("htf_bias")),
        htf_confidence=_optional_float(metadata.get("htf_confidence")),
        htf_zone_type=_optional_str(metadata.get("htf_zone_type")),
        htf_zone_low=_optional_float(metadata.get("htf_zone_low")),
        htf_zone_high=_optional_float(metadata.get("htf_zone_high")),
        htf_location=_optional_str(metadata.get("htf_location")),
        htf_allows_long=_optional_bool(metadata.get("htf_allows_long")),
        htf_allows_short=_optional_bool(metadata.get("htf_allows_short")),
        htf_objective_type=_optional_str(metadata.get("htf_objective_type")),
        htf_objective_level=_optional_float(metadata.get("htf_objective_level")),
        htf_structure_bias=_optional_str(metadata.get("htf_structure_bias")),
        htf_draw_direction=_optional_str(metadata.get("htf_draw_direction")),
        htf_objective_reached=_optional_bool(metadata.get("htf_objective_reached")),
        htf_objective_unreached=_optional_bool(metadata.get("htf_objective_unreached")),
        htf_context_alignment=_optional_str(metadata.get("htf_context_alignment") or metadata.get("htf_alignment")),
        htf_poi_direction=_optional_str(metadata.get("htf_poi_direction")),
        displacement_factor=_optional_float(metadata.get("displacement_factor")),
        has_displacement=_optional_bool(metadata.get("has_displacement")),
        displacement_grade=_optional_str(metadata.get("displacement_grade")),
        body_ratio=_optional_float(metadata.get("body_ratio")),
        range_expansion=_optional_float(metadata.get("range_expansion")),
        close_beyond_structure=_optional_bool(metadata.get("close_beyond_structure")),
        created_fvg_after_break=_optional_bool(metadata.get("created_fvg_after_break")),
        bars_in_displacement=_optional_int(metadata.get("bars_in_displacement")),
        swing_significance=_optional_str(metadata.get("swing_significance")),
        sweep_swing_significance=_optional_str(metadata.get("sweep_swing_significance") or metadata.get("swing_significance")),
        sweep_liquidity_quality=_optional_str(metadata.get("sweep_liquidity_quality")),
        structure_swing_significance=_optional_str(metadata.get("structure_swing_significance")),
        objective_liquidity_quality=_optional_str(metadata.get("objective_liquidity_quality") or metadata.get("objective_quality")),
        objective_type=_optional_str(metadata.get("objective_type") or metadata.get("htf_objective_type")),
        objective_age_bars=_optional_int(metadata.get("objective_age_bars")),
        objective_is_equal_high_low=_optional_bool(metadata.get("objective_is_equal_high_low")),
        dealing_range_source=_optional_str(metadata.get("dealing_range_source")),
        fvg_status=_optional_str(metadata.get("fvg_status") or metadata.get("source_fvg_status")),
        fvg_fill_percent=_optional_float(metadata.get("fvg_fill_percent") or metadata.get("source_fvg_fill_percent")),
        fvg_quality=_optional_str(metadata.get("fvg_quality")),
        source_fvg_direction=_optional_str(metadata.get("source_fvg_direction")),
        source_fvg_time=_optional_int(metadata.get("source_fvg_time")),
        breach_time=_optional_int(metadata.get("breach_time")),
        breach_displacement_factor=_optional_float(metadata.get("breach_displacement_factor")),
        breach_displacement_grade=_optional_str(metadata.get("breach_displacement_grade")),
        ifvg_mean_threshold=_optional_float(metadata.get("ifvg_mean_threshold")),
        ifvg_grade=_optional_str(metadata.get("ifvg_grade")),
        ifvg_quality=_optional_str(metadata.get("ifvg_quality")),
        ifvg_ce_level=_optional_float(metadata.get("ifvg_ce_level")),
        ifvg_retest_depth=_optional_float(metadata.get("ifvg_retest_depth")),
        ifvg_breach_time=_optional_int(metadata.get("ifvg_breach_time")),
        ifvg_retest_time=_optional_int(metadata.get("ifvg_retest_time")),
        ifvg_time_to_retest_bars=_optional_int(metadata.get("ifvg_time_to_retest_bars")),
        bars_sweep_to_breach=_optional_int(metadata.get("bars_sweep_to_breach")),
        rr_to_objective=_optional_float(metadata.get("rr_to_objective")),
        source_zone_type=_optional_str(metadata.get("source_zone_type")),
        source_zone_time=_optional_int(metadata.get("source_zone_time")),
        source_zone_low=_optional_float(metadata.get("source_zone_low")),
        source_zone_high=_optional_float(metadata.get("source_zone_high")),
        source_zone_valid=_optional_bool(metadata.get("source_zone_valid")),
        source_zone_invalidation_level=_optional_float(metadata.get("source_zone_invalidation_level")),
        missed_entry_distance=_optional_float(metadata.get("missed_entry_distance")),
        original_entry_zone_low=_optional_float(metadata.get("original_entry_zone_low")),
        original_entry_zone_high=_optional_float(metadata.get("original_entry_zone_high")),
        objective_reached_before_entry=_optional_bool(metadata.get("objective_reached_before_entry")),
        distance_to_objective=_optional_float(metadata.get("distance_to_objective")),
        fill_percent=_optional_float(metadata.get("fill_percent")),
        fill_mode=_optional_str(metadata.get("fill_mode")),
        time_to_fill=_optional_int(metadata.get("time_to_fill")),
        reaction_speed=_optional_int(metadata.get("reaction_speed")),
        ltf_mss_time=_optional_int(metadata.get("ltf_mss_time")),
        ltf_reaction_bars=_optional_int(metadata.get("ltf_reaction_bars")),
        ltf_reaction_displacement_grade=_optional_str(metadata.get("ltf_reaction_displacement_grade")),
        objective_quality=_optional_str(metadata.get("objective_quality")),
        poi_quality=_optional_str(metadata.get("poi_quality")),
        risk_quality=_optional_str(metadata.get("risk_quality")),
    )


def _entry_price(entry_low: float | None, entry_high: float | None) -> float | None:
    if entry_low is not None and entry_high is not None:
        return (entry_low + entry_high) / 2
    if entry_low is not None:
        return entry_low
    if entry_high is not None:
        return entry_high
    return None


def _fallback_invalidation(
    direction: str,
    entry_low: float | None,
    entry_high: float | None,
    sweep_level: float | None,
) -> float | None:
    if sweep_level is not None:
        return sweep_level
    if entry_low is None or entry_high is None:
        return None
    width = max(abs(entry_high - entry_low), 1e-9)
    if direction == "long":
        return entry_low - width
    if direction == "short":
        return entry_high + width
    return None


def _risk(direction: str, entry_price: float | None, invalidation: float | None) -> float | None:
    if entry_price is None or invalidation is None:
        return None
    if direction == "long":
        return entry_price - invalidation
    if direction == "short":
        return invalidation - entry_price
    return None


def _dedup_key(setup: dict[str, Any], event: BacktestEvent, price_precision: int) -> tuple[Any, ...]:
    return (
        event.model_name,
        event.symbol,
        event.timeframe,
        event.direction,
        setup.get("timestamp"),
        _rounded(event.entry_low, price_precision),
        _rounded(event.entry_high, price_precision),
    )


def _cooldown_key(event: BacktestEvent, price_precision: int) -> tuple[Any, ...]:
    return (
        event.model_name,
        event.symbol,
        event.timeframe,
        event.direction,
        _rounded(event.entry_low, price_precision),
        _rounded(event.entry_high, price_precision),
    )


def _event_id(**payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha1(encoded).hexdigest()[:16]


def _rounded(value: float | None, precision: int) -> float | None:
    return round(value, precision) if value is not None else None


def _optional_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def _optional_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    return int(value)


def _optional_str(value: Any) -> str | None:
    if value is None or value == "":
        return None
    return str(value)


def _optional_bool(value: Any) -> bool | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


__all__ = [
    "MODEL_DETECTORS",
    "MODEL_NAMES",
    "ReplayConfig",
    "ReplayWarning",
    "normalize_model_key",
    "replay_entry_models",
    "replay_entry_models_multi_timeframe",
]
