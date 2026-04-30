from __future__ import annotations

from typing import Any

from strategies.types import EntrySetup


def classify_setup_lifecycle(setup: EntrySetup, candles: list[dict[str, float | int]]) -> dict[str, Any]:
    if not candles:
        return {"status": "setup_formed"}
    entry_low = min(float(setup.entry_low), float(setup.entry_high))
    entry_high = max(float(setup.entry_low), float(setup.entry_high))
    entry_time = int(setup.metadata.get("entry_time") or setup.timestamp)
    active = [candle for candle in candles if int(candle["time"]) >= setup.timestamp]
    pre_entry = [candle for candle in active if int(candle["time"]) < entry_time]
    post_entry = [candle for candle in active if int(candle["time"]) >= entry_time]

    if _target_hit(setup, pre_entry, "tp1_price") or _target_hit(setup, pre_entry):
        return {"status": "cancelled", "lifecycle_reason": "target_reached_before_entry"}
    if _stop_hit(setup, pre_entry) or _logical_invalidation_hit(setup, pre_entry):
        return {"status": "cancelled", "lifecycle_reason": "invalidated_before_entry"}

    fill_idx = _first_entry_index(post_entry, entry_low, entry_high)
    if fill_idx is None:
        return {"status": "limit_pending", "lifecycle_reason": "waiting_for_entry_retest"}

    filled = post_entry[fill_idx + 1 :]
    for offset, candle in enumerate(filled, start=1):
        stop_hit = _stop_hit(setup, [candle])
        logical_hit = _logical_invalidation_hit(setup, [candle])
        target_hit = _target_hit(setup, [candle])
        tp1_hit = _target_hit(setup, [candle], "tp1_price")
        if (stop_hit or logical_hit) and target_hit:
            return {"status": "sl_hit", "lifecycle_reason": "same_bar_stop_and_target_conservative", "bars_after_entry": offset}
        if logical_hit:
            return {
                "status": "invalidated",
                "lifecycle_reason": "logical_invalidation_body_close",
                "exit_reason": _logical_exit_reason(setup),
                "bars_after_entry": offset,
            }
        if stop_hit:
            return {"status": "sl_hit", "lifecycle_reason": "physical_stop_hit", "exit_reason": "sl_hit", "bars_after_entry": offset}
        if target_hit:
            return {"status": "tp_hit", "lifecycle_reason": "target_hit", "exit_reason": "tp_hit", "bars_after_entry": offset}
        if tp1_hit:
            return {
                "status": "tp1_hit",
                "lifecycle_reason": "partial_close_move_sl_to_be",
                "moved_to_be": True,
                "bars_after_entry": offset,
            }
    return {"status": "entry_filled", "lifecycle_reason": "entry_touched_no_exit_yet"}


def _first_entry_index(candles: list[dict[str, float | int]], entry_low: float, entry_high: float) -> int | None:
    for idx, candle in enumerate(candles):
        if float(candle["low"]) <= entry_high and float(candle["high"]) >= entry_low:
            return idx
    return None


def _stop_hit(setup: EntrySetup, candles: list[dict[str, float | int]]) -> bool:
    stop = setup.stop_loss if setup.stop_loss is not None else setup.invalidation
    if stop is None:
        return False
    return any(float(candle["low"]) <= stop if setup.direction == "long" else float(candle["high"]) >= stop for candle in candles)


def _target_hit(setup: EntrySetup, candles: list[dict[str, float | int]], metadata_key: str = "target_hint") -> bool:
    target = setup.target_hint if metadata_key == "target_hint" else setup.metadata.get(metadata_key)
    if target is None:
        return False
    return any(
        float(candle["high"]) >= float(target) if setup.direction == "long" else float(candle["low"]) <= float(target)
        for candle in candles
    )


def _logical_invalidation_hit(setup: EntrySetup, candles: list[dict[str, float | int]]) -> bool:
    price = setup.metadata.get("logical_invalidation_price")
    if price is None:
        return False
    level = float(price)
    return any(
        float(candle["close"]) <= level if setup.direction == "long" else float(candle["close"]) >= level
        for candle in candles
    )


def _logical_exit_reason(setup: EntrySetup) -> str:
    model = setup.metadata.get("logical_invalidation_model")
    if model == "ce_fvg":
        return "ce_violation"
    if model == "mean_threshold":
        return "mt_violation"
    if model in {"sweep_level", "sweep_extreme"}:
        return "sweep_bos"
    if model == "body_level":
        return "body_level_violation"
    return "logical_invalidation"


__all__ = ["classify_setup_lifecycle"]
