from __future__ import annotations

from typing import Any

from config import (
    DISPLACEMENT_STRONG_BODY_RATIO,
    DISPLACEMENT_STRONG_RANGE_EXPANSION,
    DISPLACEMENT_VALID_BODY_RATIO,
    DISPLACEMENT_VALID_RANGE_EXPANSION,
    MAX_IFVG_RETEST_BARS,
    MIN_IFVG_RETEST_BARS,
)
from market_primitives.displacement import evaluate_displacement
from market_primitives.fvg import detect_fvg

from .common import buffered_stop, closed_candles, context_metadata, draw_on_liquidity_target, fixed_r_target, setup

IFVG_ENTRY_MODE = "edge"
IFVG_STOP_MODE = "ce"
IFVG_REQUIRE_DISPLACEMENT = True
IFVG_MIN_RETEST_DEPTH = 0.15


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
    target_mode = str(cfg.get("target_mode") or "nearest_liquidity")
    min_retest = int(cfg.get("min_ifvg_retest_bars") or MIN_IFVG_RETEST_BARS)
    max_retest = int(cfg.get("max_ifvg_retest_bars") or MAX_IFVG_RETEST_BARS)
    require_displacement = bool(cfg.get("ifvg_require_displacement", IFVG_REQUIRE_DISPLACEMENT))
    reject_retest_close_beyond_ce = bool(cfg.get("ifvg_reject_retest_close_beyond_ce", True))
    min_retest_depth = float(cfg.get("ifvg_min_retest_depth", IFVG_MIN_RETEST_DEPTH))
    max_source_touches = int(cfg.get("ifvg_max_source_touches_before_inversion", 12))
    max_source_age = int(cfg.get("ifvg_max_source_age_bars", 100))
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    gaps = detect_fvg(candles, symbol, timeframe, scan_back=60)
    candle_index = {int(candle["time"]): idx for idx, candle in enumerate(closed)}
    results = []

    for gap in reversed(gaps):
        source_idx = candle_index.get(int(gap.created_at))
        if source_idx is None:
            continue
        breach_idx = _breach_index(closed, gap, source_idx)
        if breach_idx is None:
            continue
        source_age = breach_idx - source_idx
        if source_age > max_source_age:
            continue
        source_touches = _source_touches_before_breach(closed, gap, source_idx, breach_idx)
        if source_touches > max_source_touches:
            continue
        side = "long" if gap.direction == "bearish" else "short"
        direction = "bullish" if side == "long" else "bearish"
        created_fvg = _created_fvg_after_break(closed, breach_idx, direction)
        disp = evaluate_displacement(
            closed,
            breach_idx,
            direction=direction,
            structure_level=gap.gap_high if side == "long" else gap.gap_low,
            created_fvg_after_break=created_fvg,
        )
        displacement_grade = _ifvg_displacement_grade(disp)
        if require_displacement and displacement_grade == "weak":
            continue
        retest_idx = _retest_index(closed, breach_idx, gap.gap_low, gap.gap_high, min_retest, max_retest, side, min_retest_depth)
        if retest_idx is None:
            continue
        ce = (gap.gap_low + gap.gap_high) / 2
        if reject_retest_close_beyond_ce and _ce_breached_by_close(closed[retest_idx], ce, side):
            continue
        entry = gap.gap_high if side == "long" and entry_mode == "edge" else gap.gap_low if side == "short" and entry_mode == "edge" else ce
        stop_ref = ce if stop_mode == "ce" else gap.gap_low if side == "long" else gap.gap_high
        stop = buffered_stop(side, stop_ref, entry, stop_bps)
        retest = closed[retest_idx]
        metadata = context_metadata(context, side, htf_mode, cfg)
        if _context_target_reached_before_retest(closed, breach_idx, retest_idx, side, metadata):
            continue
        if target_mode == "fixed_r":
            target = fixed_r_target(side, entry, stop)
            target_metadata = {"dol_priority": 99, "dol_target_type": "fixed_r", "dol_source": "fixed_r"}
        else:
            target, target_metadata = draw_on_liquidity_target(closed, side, entry, stop, metadata)
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
            score=3 if displacement_grade == "weak" else 4,
            reason="Pure IFVG first retest without mandatory sweep",
            metadata={
                **metadata,
                **target_metadata,
                "entry_mode": entry_mode,
                "stop_mode": stop_mode,
                "target_mode": target_mode,
                "source_fvg_time": gap.created_at,
                "source_fvg_age_bars": source_age,
                "source_fvg_direction": gap.direction,
                "breach_time": closed[breach_idx]["time"],
                "breach_close": closed[breach_idx]["close"],
                "entry_time": int(retest["time"]),
                "retest_time": int(retest["time"]),
                "ifvg_low": gap.gap_low,
                "ifvg_high": gap.gap_high,
                "ifvg_ce": ce,
                "ifvg_ce_invalidation": ce,
                "ifvg_ce_breached_by_retest_close": _ce_breached_by_close(retest, ce, side),
                "ifvg_min_retest_bars": min_retest,
                "ifvg_max_retest_bars": max_retest,
                "ifvg_min_retest_depth": min_retest_depth,
                "source_fvg_touches_before_inversion": source_touches,
                "time_to_retest_bars": retest_idx - breach_idx,
                "retest_depth": _retest_depth(retest, gap.gap_low, gap.gap_high, side),
                "ifvg_fill_depth": _retest_depth(retest, gap.gap_low, gap.gap_high, side),
                "displacement_grade": displacement_grade,
                "breach_displacement_factor": disp.displacement_factor,
                "breach_displacement_grade": displacement_grade,
                "body_ratio": disp.body_ratio,
                "range_expansion": disp.range_expansion,
                "close_beyond_structure": disp.close_beyond_structure,
                "created_fvg_after_break": disp.created_fvg_after_break,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _ifvg_displacement_grade(disp: object) -> str:
    if not getattr(disp, "created_fvg_after_break", False):
        return "weak"
    if getattr(disp, "displacement_grade", "weak") in {"valid", "strong"}:
        return str(getattr(disp, "displacement_grade"))
    if not getattr(disp, "close_beyond_structure", False):
        return "weak"
    body_ratio = float(getattr(disp, "body_ratio", 0.0))
    range_expansion = float(getattr(disp, "range_expansion", 0.0))
    if body_ratio >= DISPLACEMENT_STRONG_BODY_RATIO and range_expansion >= DISPLACEMENT_STRONG_RANGE_EXPANSION:
        return "strong"
    if body_ratio >= DISPLACEMENT_VALID_BODY_RATIO and range_expansion >= DISPLACEMENT_VALID_RANGE_EXPANSION:
        return "valid"
    return "weak"


def _breach_index(candles: list[dict[str, float | int]], gap: object, source_idx: int) -> int | None:
    for idx in range(source_idx + 1, len(candles)):
        candle = candles[idx]
        if gap.direction == "bearish" and float(candle["close"]) > float(gap.gap_high):
            return idx
        if gap.direction == "bullish" and float(candle["close"]) < float(gap.gap_low):
            return idx
    return None


def _retest_index(
    candles: list[dict[str, float | int]],
    breach_idx: int,
    low: float,
    high: float,
    min_bars: int,
    max_bars: int,
    side: str,
    min_depth: float,
) -> int | None:
    for idx in range(breach_idx + 1, min(len(candles), breach_idx + 1 + max_bars)):
        candle = candles[idx]
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            if _retest_depth(candle, low, high, side) < min_depth:
                continue
            return idx if idx - breach_idx >= min_bars else None
    return None


def _created_fvg_after_break(candles: list[dict[str, float | int]], index: int, direction: str) -> bool:
    if index < 2:
        return False
    c0 = candles[index - 2]
    c2 = candles[index]
    if direction == "bullish":
        return float(c0["high"]) < float(c2["low"])
    if direction == "bearish":
        return float(c0["low"]) > float(c2["high"])
    return False


def _context_target_reached_before_retest(
    candles: list[dict[str, float | int]],
    breach_idx: int,
    retest_idx: int,
    side: str,
    metadata: dict[str, object],
) -> bool:
    target = metadata.get("htf_objective_level")
    draw = metadata.get("htf_draw_direction")
    if not isinstance(target, (int, float)):
        return False
    if side == "long" and draw != "up":
        return False
    if side == "short" and draw != "down":
        return False
    for candle in candles[breach_idx + 1 : retest_idx]:
        if side == "long" and float(candle["high"]) >= float(target):
            return True
        if side == "short" and float(candle["low"]) <= float(target):
            return True
    return False


def _retest_depth(candle: dict[str, float | int], low: float, high: float, side: str) -> float:
    width = max(high - low, 1e-9)
    depth = (high - float(candle["low"])) / width if side == "long" else (float(candle["high"]) - low) / width
    return min(1.0, max(0.0, depth))


def _source_touches_before_breach(
    candles: list[dict[str, float | int]],
    gap: object,
    source_idx: int,
    breach_idx: int,
) -> int:
    touches = 0
    for candle in candles[source_idx + 1 : breach_idx]:
        if float(candle["low"]) <= float(gap.gap_high) and float(candle["high"]) >= float(gap.gap_low):
            touches += 1
    return touches


def _ce_breached_by_close(candle: dict[str, float | int], ce: float, side: str) -> bool:
    return float(candle["close"]) < ce if side == "long" else float(candle["close"]) > ce


__all__ = ["detect_setups"]
