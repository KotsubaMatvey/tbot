from __future__ import annotations

from typing import Any

from .common import buffered_stop, closed_candles, context_metadata, nearest_liquidity_target, setup

RECLAIMED_OB_MIN_PRIOR_REACTION_R = 0.5
RECLAIMED_OB_ENTRY_MODE = "body_edge"
RECLAIMED_OB_STOP_MODE = "mean_threshold"


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
        entry = block.zone_high if side == "long" else block.zone_low
        mean = block.mean_threshold or block.midpoint
        stop_ref = mean if stop_mode == "mean_threshold" else block.zone_low if side == "long" else block.zone_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        target = nearest_liquidity_target(closed_candles(candles), side, entry, stop)
        metadata = context_metadata(context, side, htf_mode, cfg)
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
                "entry_mode": RECLAIMED_OB_ENTRY_MODE,
                "stop_mode": stop_mode,
                "target_mode": "nearest_liquidity",
                "source_ob_time": block.origin_time,
                "entry_time": block.timestamp,
                "retest_time": block.timestamp,
                "prior_reaction_r": RECLAIMED_OB_MIN_PRIOR_REACTION_R,
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


__all__ = ["detect_setups"]
