from __future__ import annotations

from typing import Any

from market_primitives.common import Candle, average_range, cluster_levels, collect_swings
from strategies.htf_context import htf_metadata, htf_score_modifier
from strategies.risk_policy import price_buffer
from strategies.types import EntrySetup, default_components

from .risk import enrich_risk_metadata


def closed_candles(candles: list[Candle]) -> list[Candle]:
    return candles[:-1] if len(candles) > 1 else list(candles)


def setup(
    *,
    model_name: str,
    direction: str,
    symbol: str,
    timeframe: str,
    entry_low: float,
    entry_high: float,
    entry_price: float | None = None,
    stop_loss: float,
    target_hint: float | None,
    timestamp: int,
    score: int,
    reason: str,
    metadata: dict[str, Any],
) -> EntrySetup | None:
    resolved_entry = entry_price if entry_price is not None else (entry_low + entry_high) / 2
    risk = resolved_entry - stop_loss if direction == "long" else stop_loss - resolved_entry
    if risk <= 0:
        return None
    components = default_components()
    risk_metadata = enrich_risk_metadata(
        model_name=model_name,
        direction=direction,
        entry=resolved_entry,
        stop=stop_loss,
        target=target_hint,
        metadata=metadata,
    )
    return EntrySetup(
        model_name=model_name,
        model_family="ict",
        direction="long" if direction == "long" else "short",
        symbol=symbol,
        timeframe=timeframe,
        status="triggered",
        entry_low=entry_low,
        entry_high=entry_high,
        entry_price=resolved_entry,
        stop_loss=stop_loss,
        invalidation=stop_loss,
        target_hint=target_hint,
        sweep_level=metadata.get("swept_level") or metadata.get("sweep_level"),
        structure_level=metadata.get("structure_level"),
        context_timeframe=None,
        score=score,
        reason=reason,
        components=components,
        timestamp=timestamp,
        metadata={
            "model_family": "ict",
            "entry_price": resolved_entry,
            "stop_loss": stop_loss,
            "risk": risk,
            "risk_bps": risk / max(resolved_entry, 1e-9) * 10_000,
            **risk_metadata,
        },
    )


def buffered_stop(side: str, ref: float, price: float, bps: float) -> float:
    buffer = price_buffer(price, stop_buffer_bps=bps)
    return ref - buffer if side == "long" else ref + buffer


def fixed_r_target(side: str, entry: float, stop: float, multiple: float = 2.0) -> float:
    risk = abs(entry - stop)
    return entry + risk * multiple if side == "long" else entry - risk * multiple


def nearest_liquidity_target(candles: list[Candle], side: str, entry: float, fallback_stop: float) -> float:
    target, _ = draw_on_liquidity_target(candles, side, entry, fallback_stop)
    return target


def draw_on_liquidity_target(
    candles: list[Candle],
    side: str,
    entry: float,
    fallback_stop: float,
    metadata: dict[str, Any] | None = None,
) -> tuple[float, dict[str, object]]:
    target = _htf_objective_target(side, entry, metadata or {})
    if target is not None:
        return target

    scan = closed_candles(candles)[-80:]
    highs, lows = collect_swings(scan, "", "")
    if side == "long":
        equal_highs = _nearest_equal_level([s.level for s in highs if s.level > entry], higher=True)
        if equal_highs is not None:
            return equal_highs, {"dol_priority": 2, "dol_target_type": "clean_equal_highs", "dol_source": "local_eqh"}
        candidates = [s.level for s in highs if s.level > entry]
        if candidates:
            return min(candidates), {"dol_priority": 1, "dol_target_type": "external_swing_high", "dol_source": "local_swing"}
        fallback = fixed_r_target(side, entry, fallback_stop)
        return fallback, {"dol_priority": 99, "dol_target_type": "fixed_r_fallback", "dol_source": "fallback"}

    equal_lows = _nearest_equal_level([s.level for s in lows if s.level < entry], higher=False)
    if equal_lows is not None:
        return equal_lows, {"dol_priority": 2, "dol_target_type": "clean_equal_lows", "dol_source": "local_eql"}
    candidates = [s.level for s in lows if s.level < entry]
    if candidates:
        return max(candidates), {"dol_priority": 1, "dol_target_type": "external_swing_low", "dol_source": "local_swing"}
    fallback = fixed_r_target(side, entry, fallback_stop)
    return fallback, {"dol_priority": 99, "dol_target_type": "fixed_r_fallback", "dol_source": "fallback"}


def _htf_objective_target(side: str, entry: float, metadata: dict[str, Any]) -> tuple[float, dict[str, object]] | None:
    target = metadata.get("htf_objective_level")
    draw = metadata.get("htf_draw_direction")
    if not isinstance(target, (int, float)):
        return None
    if side == "long" and (draw != "up" or float(target) <= entry):
        return None
    if side == "short" and (draw != "down" or float(target) >= entry):
        return None
    objective_type = str(metadata.get("htf_objective_type") or "")
    if objective_type in {"swing_high", "swing_low"}:
        return float(target), {"dol_priority": 1, "dol_target_type": "htf_external", "dol_source": objective_type}
    if objective_type in {"equal_highs", "equal_lows"}:
        return float(target), {"dol_priority": 2, "dol_target_type": "clean_level", "dol_source": objective_type}
    if "fvg" in objective_type.lower():
        return float(target), {"dol_priority": 3, "dol_target_type": "htf_internal_fvg", "dol_source": objective_type}
    if objective_type in {"pdh", "pdl", "session_high", "session_low"}:
        return float(target), {"dol_priority": 4, "dol_target_type": "session_daily_extreme", "dol_source": objective_type}
    if objective_type in {"order_block", "breaker_block", "opposing_poi"}:
        return float(target), {"dol_priority": 5, "dol_target_type": "opposing_poi", "dol_source": objective_type}
    return float(target), {"dol_priority": 1, "dol_target_type": "htf_external", "dol_source": objective_type or "htf_objective"}


def _nearest_equal_level(levels: list[float], *, higher: bool) -> float | None:
    clusters = [cluster for cluster in cluster_levels(levels) if len(cluster) >= 2]
    if not clusters:
        return None
    values = [sum(cluster) / len(cluster) for cluster in clusters]
    return min(values) if higher else max(values)


def opposite_range_target(candles: list[Candle], side: str, entry: float, stop: float, lookback: int = 50) -> float:
    scan = closed_candles(candles)[-lookback:]
    if not scan:
        return fixed_r_target(side, entry, stop)
    return max(float(c["high"]) for c in scan) if side == "long" else min(float(c["low"]) for c in scan)


def wick_extension_bps(level: float, extreme: float) -> float:
    return abs(extreme - level) / max(level, 1e-9) * 10_000


def avg_range(candles: list[Candle], lookback: int = 20) -> float:
    return average_range(closed_candles(candles)[-lookback:])


def context_metadata(context: object | None, side: str, htf_mode: str, config: dict[str, Any] | None = None) -> dict[str, object]:
    htf = getattr(context, "htf_context", None) if context is not None else None
    metadata = htf_metadata(htf)
    metadata["htf_mode"] = htf_mode
    metadata["htf_score_modifier"] = round(htf_score_modifier(htf, side, htf_mode), 4)
    metadata["bias_alignment"] = metadata.get("htf_context_alignment")
    metadata["is_in_p_d"] = metadata.get("htf_location")
    smt = _smt_for_side(config or {}, side)
    metadata["has_smt_confirmation"] = smt is not None
    metadata["smt_detected"] = smt is not None
    if smt is not None:
        metadata["smt_direction"] = smt.direction
        metadata["smt_pair"] = smt.metadata.get("smt_pair")
        metadata["smt_primary_symbol"] = smt.symbol
        metadata["smt_secondary_symbol"] = smt.secondary_symbol
        metadata["smt_strength"] = round(float(smt.strength), 6)
        metadata["smt_timestamp"] = smt.timestamp
    return metadata


def _smt_for_side(config: dict[str, Any], side: str) -> Any | None:
    expected = "bullish" if side == "long" else "bearish"
    divergences = config.get("smt_divergences") or []
    return next((item for item in reversed(divergences) if getattr(item, "direction", None) == expected), None)


__all__ = [
    "avg_range",
    "buffered_stop",
    "closed_candles",
    "draw_on_liquidity_target",
    "context_metadata",
    "fixed_r_target",
    "nearest_liquidity_target",
    "opposite_range_target",
    "setup",
    "wick_extension_bps",
]
