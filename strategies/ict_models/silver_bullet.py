from __future__ import annotations

from datetime import datetime, time
from typing import Any
from zoneinfo import ZoneInfo

from market_primitives.fvg import detect_fvg

from .common import buffered_stop, closed_candles, fixed_r_target, nearest_liquidity_target, setup

SILVER_BULLET_TZ = "America/New_York"
SILVER_BULLET_START = "10:00"
SILVER_BULLET_END = "11:00"
SILVER_BULLET_ENTRY_MODE = "edge"
SILVER_BULLET_TARGET_MODE = "fixed_r"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if len(closed) < 4:
        return []
    tz_name = str(cfg.get("silver_bullet_tz") or SILVER_BULLET_TZ)
    start = _parse_time(str(cfg.get("silver_bullet_start") or SILVER_BULLET_START))
    end = _parse_time(str(cfg.get("silver_bullet_end") or SILVER_BULLET_END))
    entry_mode = str(cfg.get("entry_mode") or cfg.get("silver_bullet_entry_mode") or SILVER_BULLET_ENTRY_MODE)
    if entry_mode not in {"edge", "ce"}:
        entry_mode = SILVER_BULLET_ENTRY_MODE
    target_mode = str(cfg.get("target_mode") or SILVER_BULLET_TARGET_MODE)
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    zone = ZoneInfo(tz_name)

    gaps = detect_fvg(candles, symbol, timeframe, scan_back=30)
    results = []
    for gap in reversed(gaps):
        fvg_dt = datetime.fromtimestamp(gap.created_at / 1000, tz=ZoneInfo("UTC")).astimezone(zone)
        if not _in_window(fvg_dt.timetz().replace(tzinfo=None), start, end):
            continue
        retest = _first_retest(closed, gap.created_at, gap.gap_low, gap.gap_high)
        if retest is None:
            continue
        entry = _entry(gap.gap_low, gap.gap_high, gap.direction, entry_mode)
        if gap.direction == "bullish":
            side = "long"
            swing_stop = _nearest_swing_low(closed, int(retest["time"])) or gap.gap_low
            stop = buffered_stop(side, swing_stop, entry, stop_bps)
        else:
            side = "short"
            swing_stop = _nearest_swing_high(closed, int(retest["time"])) or gap.gap_high
            stop = buffered_stop(side, swing_stop, entry, stop_bps)
        target = fixed_r_target(side, entry, stop) if target_mode == "fixed_r" else nearest_liquidity_target(closed, side, entry, stop)
        item = setup(
            model_name="silver_bullet",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=int(retest["time"]),
            score=3,
            reason=f"Silver Bullet {gap.direction} FVG retest inside NY 10:00-11:00",
            metadata={
                "entry_mode": entry_mode,
                "stop_mode": "swing_or_fvg",
                "target_mode": target_mode,
                "session_window": f"{SILVER_BULLET_START}-{SILVER_BULLET_END}",
                "ny_time": fvg_dt.strftime("%Y-%m-%d %H:%M"),
                "fvg_time": gap.created_at,
                "fvg_low": gap.gap_low,
                "fvg_high": gap.gap_high,
                "fvg_ce": (gap.gap_low + gap.gap_high) / 2,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _parse_time(value: str) -> time:
    hour, minute = value.split(":", 1)
    return time(int(hour), int(minute))


def _in_window(value: time, start: time, end: time) -> bool:
    return start <= value < end


def _first_retest(candles: list[dict[str, float | int]], after: int, low: float, high: float) -> dict[str, float | int] | None:
    for candle in candles:
        if int(candle["time"]) <= after:
            continue
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            return candle
    return None


def _entry(low: float, high: float, direction: str, mode: str) -> float:
    if mode == "ce":
        return (low + high) / 2
    return high if direction == "bullish" else low


def _nearest_swing_low(candles: list[dict[str, float | int]], before: int) -> float | None:
    lows = [float(c["low"]) for c in candles if int(c["time"]) <= before]
    return min(lows[-5:]) if lows else None


def _nearest_swing_high(candles: list[dict[str, float | int]], before: int) -> float | None:
    highs = [float(c["high"]) for c in candles if int(c["time"]) <= before]
    return max(highs[-5:]) if highs else None


__all__ = ["detect_setups"]
