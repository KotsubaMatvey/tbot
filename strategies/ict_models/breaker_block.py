from __future__ import annotations

from typing import Any

from .common import buffered_stop, closed_candles, context_metadata, nearest_liquidity_target, setup
from .sessions import LONDON_TO_NY, in_ny_windows

BREAKER_ENTRY_MODE = "edge"
BREAKER_STOP_MODE = "mean_threshold"
BREAKER_REQUIRE_SWEEP = True
BREAKER_REQUIRE_DISPLACEMENT = True
BREAKER_MAX_RETEST_COUNT = 0


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    entry_mode = str(cfg.get("entry_mode") or BREAKER_ENTRY_MODE)
    stop_mode = str(cfg.get("stop_mode") or BREAKER_STOP_MODE)
    require_sweep = bool(cfg.get("breaker_require_sweep", BREAKER_REQUIRE_SWEEP))
    require_displacement = bool(cfg.get("breaker_require_displacement", BREAKER_REQUIRE_DISPLACEMENT))
    require_killzone = bool(cfg.get("breaker_block_require_killzone", False))
    max_trigger_to_retest = cfg.get("breaker_max_trigger_to_retest_bars")
    max_trigger_to_retest = int(max_trigger_to_retest) if max_trigger_to_retest is not None else None
    max_retest_count = int(cfg.get("breaker_max_retest_count", BREAKER_MAX_RETEST_COUNT))
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    snapshot = getattr(context, "primary", None) if context is not None else None
    if snapshot is None:
        from scanner.snapshots import build_primitive_snapshot

        snapshot = build_primitive_snapshot(symbol, timeframe, candles)
    results = []
    for block in sorted(snapshot.breaker_blocks, key=lambda item: item.timestamp, reverse=True):
        if not block.retested:
            continue
        if require_sweep and block.sweep_time is None:
            continue
        trigger_to_retest = _bars_between(snapshot.candles, block.trigger_time, block.timestamp)
        if max_trigger_to_retest is not None and trigger_to_retest is not None and trigger_to_retest > max_trigger_to_retest:
            continue
        retest_count = _retest_count(snapshot.candles, block)
        if max_retest_count > 0 and retest_count > max_retest_count:
            continue
        displacement = _breaker_displacement(block)
        if require_displacement and displacement["grade"] not in {"valid", "strong"}:
            continue
        if require_killzone and not in_ny_windows(block.trigger_time, LONDON_TO_NY):
            continue
        side = "long" if block.direction == "bullish" else "short"
        entry = block.zone_high if side == "long" and entry_mode == "edge" else block.zone_low if side == "short" and entry_mode == "edge" else (block.zone_low + block.zone_high) / 2
        mean = (block.zone_low + block.zone_high) / 2
        stop_ref = mean if stop_mode == "mean_threshold" else block.zone_low if side == "long" else block.zone_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        target = nearest_liquidity_target(closed_candles(candles), side, entry, stop)
        metadata = context_metadata(context, side, htf_mode, cfg)
        item = setup(
            model_name="breaker_block",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=block.trigger_time,
            score=3,
            reason="Failed order block retested as breaker",
            metadata={
                **metadata,
                "entry_mode": entry_mode,
                "stop_mode": stop_mode,
                "target_mode": "nearest_liquidity",
                "session_filter": "london_to_ny" if require_killzone else "off",
                "source_ob_time": block.source_order_block_time or block.origin_time,
                "source_ob_direction": block.source_order_block_direction,
                "breaker_low": block.zone_low,
                "breaker_high": block.zone_high,
                "breaker_mean_threshold": mean,
                "break_time": block.trigger_time,
                "retest_time": block.timestamp,
                "trigger_to_retest_bars": trigger_to_retest,
                "poi_retest_count": retest_count,
                "displacement_grade": displacement["grade"],
                "displacement_factor": displacement["factor"],
                "body_ratio": displacement["body_ratio"],
                "range_expansion": displacement["range_expansion"],
                "created_fvg_after_break": displacement["created_fvg_after_break"],
                "entry_time": block.timestamp,
                "sweep_time": block.sweep_time,
                "failed_ob_confirmed": block.failed_ob_confirmed,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _bars_between(candles: list[dict[str, float | int]], start: int, end: int) -> int | None:
    start_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == start), None)
    end_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == end), None)
    if start_idx is None or end_idx is None:
        return None
    return max(0, end_idx - start_idx)


def _retest_count(candles: list[dict[str, float | int]], block: object) -> int:
    touches = 0
    low, high = sorted((float(block.zone_low), float(block.zone_high)))
    for candle in candles:
        timestamp = int(candle["time"])
        if timestamp <= int(block.trigger_time):
            continue
        if timestamp > int(block.timestamp):
            break
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            touches += 1
    return touches


def _breaker_displacement(block: object) -> dict[str, object]:
    metadata = getattr(block, "metadata", {}) if isinstance(getattr(block, "metadata", None), dict) else {}
    return {
        "grade": metadata.get("displacement_grade") or "weak",
        "factor": metadata.get("displacement_factor") or 0.0,
        "body_ratio": metadata.get("body_ratio") or 0.0,
        "range_expansion": metadata.get("range_expansion") or 0.0,
        "created_fvg_after_break": bool(metadata.get("created_fvg_after_break")),
    }


__all__ = ["detect_setups"]
