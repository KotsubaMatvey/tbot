from __future__ import annotations

from typing import Any

from market_primitives.common import Candle, in_zone

from .common import buffered_stop, closed_candles, context_metadata, draw_on_liquidity_target, setup

RECLAIMED_OB_MIN_PRIOR_REACTION_R = 0.5
RECLAIMED_OB_ENTRY_MODE = "body_edge"
RECLAIMED_OB_STOP_MODE = "block_extreme"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    stop_mode = str(cfg.get("stop_mode") or RECLAIMED_OB_STOP_MODE)
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    snapshot = getattr(context, "primary", None) if context is not None else None
    if snapshot is None:
        from scanner.snapshots import build_primitive_snapshot

        snapshot = build_primitive_snapshot(symbol, timeframe, candles)
    results = []
    for block in sorted(snapshot.order_blocks, key=lambda item: item.timestamp, reverse=True):
        if block.invalidated or not block.validated or not block.mitigated:
            continue
        side = "long" if block.direction == "bullish" else "short"
        reclaim = _reclaimed_sequence(
            block=block,
            candles=getattr(snapshot, "candles", candles),
            side=side,
            min_prior_reaction_r=float(cfg.get("reclaimed_ob_min_prior_reaction_r") or RECLAIMED_OB_MIN_PRIOR_REACTION_R),
        )
        if reclaim is None:
            continue
        entry = block.zone_high if side == "long" else block.zone_low
        mean = block.mean_threshold or block.midpoint
        stop_ref = mean if stop_mode == "mean_threshold" else block.zone_low if side == "long" else block.zone_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        metadata = context_metadata(context, side, htf_mode, cfg)
        target, target_metadata = draw_on_liquidity_target(closed_candles(candles), side, entry, stop, metadata)
        item = setup(
            model_name="reclaimed_ob",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=block.validation_time or block.origin_time,
            score=3,
            reason="Validated order block reclaimed for continuation retest",
            metadata={
                **metadata,
                **target_metadata,
                "entry_mode": RECLAIMED_OB_ENTRY_MODE,
                "stop_mode": stop_mode,
                "target_mode": "dol_hierarchy",
                "source_ob_time": block.origin_time,
                "entry_time": block.timestamp,
                "retest_time": block.timestamp,
                "prior_reaction_r": reclaim["prior_reaction_r"],
                "prior_reaction_time": reclaim["prior_reaction_time"],
                "reclaim_structure_level": reclaim["reclaim_structure_level"],
                "reclaim_structure_break_time": reclaim["reclaim_structure_break_time"],
                "ob_low": block.zone_low,
                "ob_high": block.zone_high,
                "ob_mean_threshold": mean,
                "retest_count": 1,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _reclaimed_sequence(
    *,
    block: Any,
    candles: list[Candle],
    side: str,
    min_prior_reaction_r: float,
) -> dict[str, float | int] | None:
    origin_idx = _index_by_time(candles, int(block.origin_time))
    current_idx = _index_by_time(candles, int(block.timestamp))
    validation_time = block.validation_time or block.origin_time
    validation_idx = _index_by_time(candles, int(validation_time))
    if origin_idx is None or current_idx is None or validation_idx is None or not (origin_idx < validation_idx < current_idx):
        return None

    zone_low = float(block.zone_low)
    zone_high = float(block.zone_high)
    current = candles[current_idx]
    if not in_zone(current, zone_low, zone_high):
        return None

    mean = float(block.mean_threshold or block.midpoint)
    if _invalidated_between(candles[validation_idx + 1 : current_idx + 1], side, mean):
        return None

    structure_break = _validation_break(block, candles[validation_idx], side, zone_low, zone_high)
    if structure_break is None:
        return None
    reaction_r = _reaction_from_origin_r(candles, origin_idx, current_idx, side, zone_low, zone_high)
    if reaction_r < min_prior_reaction_r:
        return None
    prior_touch = next(
        (idx for idx in range(validation_idx + 1, current_idx) if in_zone(candles[idx], zone_low, zone_high)),
        None,
    )
    level, break_time = structure_break
    return {
        "prior_reaction_r": round(reaction_r, 4),
        "prior_reaction_time": int(candles[prior_touch]["time"]) if prior_touch is not None else int(block.origin_time),
        "reclaim_structure_level": level,
        "reclaim_structure_break_time": break_time,
    }


def _index_by_time(candles: list[Candle], timestamp: int) -> int | None:
    return next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == timestamp), None)


def _invalidated_between(candles: list[Candle], side: str, mean_threshold: float) -> bool:
    if side == "long":
        return any(float(candle["close"]) < mean_threshold for candle in candles)
    return any(float(candle["close"]) > mean_threshold for candle in candles)


def _reaction_from_origin_r(candles: list[Candle], origin_idx: int, current_idx: int, side: str, zone_low: float, zone_high: float) -> float:
    move_away = candles[origin_idx + 1 : current_idx]
    if not move_away:
        return 0.0
    zone_width = max(abs(zone_high - zone_low), ((zone_high + zone_low) / 2) * 0.0001, 1e-9)
    if side == "long":
        move = max(float(candle["high"]) for candle in move_away) - zone_high
    else:
        move = zone_low - min(float(candle["low"]) for candle in move_away)
    return max(0.0, move / zone_width)


def _validation_break(block: Any, candle: Candle, side: str, zone_low: float, zone_high: float) -> tuple[float, int] | None:
    metadata_level = getattr(block, "metadata", {}).get("broken_level")
    if isinstance(metadata_level, (int, float)):
        level = float(metadata_level)
    else:
        level = zone_high if side == "long" else zone_low
    if side == "long":
        broke = float(candle["close"]) > level
    else:
        broke = float(candle["close"]) < level
    if not broke:
        return None
    return level, int(candle["time"])


__all__ = ["detect_setups"]
