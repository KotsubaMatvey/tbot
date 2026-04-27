from __future__ import annotations

from typing import Any

from .common import buffered_stop, closed_candles, nearest_liquidity_target, setup

BREAKER_ENTRY_MODE = "edge"
BREAKER_STOP_MODE = "mean_threshold"
BREAKER_REQUIRE_SWEEP = True


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
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    snapshot = getattr(context, "primary", None) if context is not None else None
    if snapshot is None:
        from scanner.snapshots import build_primitive_snapshot

        snapshot = build_primitive_snapshot(symbol, timeframe, candles)
    results = []
    for block in sorted(snapshot.breaker_blocks, key=lambda item: item.timestamp, reverse=True):
        if not block.retested:
            continue
        side = "long" if block.direction == "bullish" else "short"
        entry = block.zone_high if side == "long" and entry_mode == "edge" else block.zone_low if side == "short" and entry_mode == "edge" else (block.zone_low + block.zone_high) / 2
        mean = (block.zone_low + block.zone_high) / 2
        stop_ref = mean if stop_mode == "mean_threshold" else block.zone_low if side == "long" else block.zone_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        target = nearest_liquidity_target(closed_candles(candles), side, entry, stop)
        item = setup(
            model_name="breaker_block",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=block.timestamp,
            score=3,
            reason="Failed order block retested as breaker",
            metadata={
                "entry_mode": entry_mode,
                "stop_mode": stop_mode,
                "target_mode": "nearest_liquidity",
                "source_ob_time": block.source_order_block_time or block.origin_time,
                "breaker_low": block.zone_low,
                "breaker_high": block.zone_high,
                "breaker_mean_threshold": mean,
                "break_time": block.trigger_time,
                "retest_time": block.timestamp,
                "failed_ob_confirmed": block.failed_ob_confirmed,
            },
        )
        if item:
            results.append(item)
            break
    return results


__all__ = ["detect_setups"]
