from __future__ import annotations

from typing import Any

from market_primitives.displacement import evaluate_displacement
from market_primitives.fvg import detect_fvg

from .common import buffered_stop, closed_candles, fixed_r_target, nearest_liquidity_target, setup

IFVG_ENTRY_MODE = "edge"
IFVG_STOP_MODE = "ce"
MAX_IFVG_RETEST_BARS = 40
IFVG_REQUIRE_DISPLACEMENT = False


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if len(closed) < 5:
        return []
    entry_mode = str(cfg.get("entry_mode") or cfg.get("ifvg_entry_mode") or IFVG_ENTRY_MODE)
    if entry_mode not in {"edge", "ce"}:
        entry_mode = IFVG_ENTRY_MODE
    stop_mode = str(cfg.get("stop_mode") or cfg.get("ifvg_stop_mode") or IFVG_STOP_MODE)
    if stop_mode not in {"ce", "opposite_boundary"}:
        stop_mode = IFVG_STOP_MODE
    target_mode = str(cfg.get("target_mode") or "fixed_r")
    max_retest = int(cfg.get("max_ifvg_retest_bars") or MAX_IFVG_RETEST_BARS)
    require_displacement = bool(cfg.get("ifvg_require_displacement", IFVG_REQUIRE_DISPLACEMENT))
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    gaps = detect_fvg(candles, symbol, timeframe, scan_back=60)
    results = []

    for gap in reversed(gaps):
        breach_idx = _breach_index(closed, gap)
        if breach_idx is None:
            continue
        side = "long" if gap.direction == "bearish" else "short"
        direction = "bullish" if side == "long" else "bearish"
        disp = evaluate_displacement(
            closed,
            breach_idx,
            direction=direction,
            structure_level=gap.gap_high if side == "long" else gap.gap_low,
            created_fvg_after_break=False,
        )
        if require_displacement and not disp.has_displacement:
            continue
        retest_idx = _retest_index(closed, breach_idx, gap.gap_low, gap.gap_high, max_retest)
        if retest_idx is None:
            continue
        ce = (gap.gap_low + gap.gap_high) / 2
        entry = gap.gap_high if side == "long" and entry_mode == "edge" else gap.gap_low if side == "short" and entry_mode == "edge" else ce
        stop_ref = ce if stop_mode == "ce" else gap.gap_low if side == "long" else gap.gap_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        target = fixed_r_target(side, entry, stop) if target_mode == "fixed_r" else nearest_liquidity_target(closed, side, entry, stop)
        retest = closed[retest_idx]
        item = setup(
            model_name="ifvg_retest",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(closed[breach_idx]["time"]),
            score=3 if disp.displacement_grade == "weak" else 4,
            reason="Pure IFVG first retest without mandatory sweep",
            metadata={
                "entry_mode": entry_mode,
                "stop_mode": stop_mode,
                "target_mode": target_mode,
                "source_fvg_direction": gap.direction,
                "breach_time": closed[breach_idx]["time"],
                "breach_close": closed[breach_idx]["close"],
                "entry_time": int(retest["time"]),
                "retest_time": int(retest["time"]),
                "ifvg_low": gap.gap_low,
                "ifvg_high": gap.gap_high,
                "ifvg_ce": ce,
                "time_to_retest_bars": retest_idx - breach_idx,
                "retest_depth": _retest_depth(retest, gap.gap_low, gap.gap_high, side),
                "breach_displacement_grade": disp.displacement_grade,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _breach_index(candles: list[dict[str, float | int]], gap: object) -> int | None:
    for idx, candle in enumerate(candles):
        if int(candle["time"]) <= int(gap.created_at):
            continue
        if gap.direction == "bearish" and float(candle["close"]) > float(gap.gap_high):
            return idx
        if gap.direction == "bullish" and float(candle["close"]) < float(gap.gap_low):
            return idx
    return None


def _retest_index(candles: list[dict[str, float | int]], breach_idx: int, low: float, high: float, max_bars: int) -> int | None:
    for idx in range(breach_idx + 1, min(len(candles), breach_idx + 1 + max_bars)):
        candle = candles[idx]
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            return idx
    return None


def _retest_depth(candle: dict[str, float | int], low: float, high: float, side: str) -> float:
    width = max(high - low, 1e-9)
    return (high - float(candle["low"])) / width if side == "long" else (float(candle["high"]) - low) / width


__all__ = ["detect_setups"]
