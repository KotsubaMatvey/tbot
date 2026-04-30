from __future__ import annotations

from datetime import datetime, time
from typing import Any
from zoneinfo import ZoneInfo

from market_primitives.fvg import detect_fvg

from .common import buffered_stop, closed_candles, fixed_r_target, nearest_liquidity_target, setup
from .sessions import SILVER_BULLET_AM, SILVER_BULLET_PM

SILVER_BULLET_TZ = "America/New_York"
SILVER_BULLET_START = "10:00"
SILVER_BULLET_END = "11:00"
SILVER_BULLET_ENTRY_MODE = "edge"
SILVER_BULLET_TARGET_MODE = "fixed_r"
SILVER_BULLET_MAX_RETEST_BARS = 6
SILVER_BULLET_RETEST_MUST_OCCUR_WITHIN_WINDOW = True


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
    windows = _windows(cfg.get("silver_bullet_windows"), cfg)
    entry_mode = str(cfg.get("entry_mode") or cfg.get("silver_bullet_entry_mode") or SILVER_BULLET_ENTRY_MODE)
    if entry_mode not in {"edge", "ce"}:
        entry_mode = SILVER_BULLET_ENTRY_MODE
    target_mode = str(cfg.get("target_mode") or SILVER_BULLET_TARGET_MODE)
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    max_retest_bars = int(cfg.get("silver_bullet_max_retest_bars") or SILVER_BULLET_MAX_RETEST_BARS)
    retest_must_be_in_window = bool(cfg.get("silver_bullet_retest_must_occur_within_window", SILVER_BULLET_RETEST_MUST_OCCUR_WITHIN_WINDOW))
    use_ce_invalidation = bool(cfg.get("silver_bullet_use_ce_invalidation", False))
    zone = ZoneInfo(tz_name)

    gaps = detect_fvg(candles, symbol, timeframe, scan_back=30)
    results = []
    for gap in reversed(gaps):
        fvg_dt = datetime.fromtimestamp(gap.created_at / 1000, tz=ZoneInfo("UTC")).astimezone(zone)
        window = _matching_window(fvg_dt.timetz().replace(tzinfo=None), windows)
        retest = _first_retest(closed, gap.created_at, gap.gap_low, gap.gap_high, max_retest_bars)
        if retest is None:
            continue
        retest_dt = datetime.fromtimestamp(int(retest["time"]) / 1000, tz=ZoneInfo("UTC")).astimezone(zone)
        retest_window = _matching_window(retest_dt.timetz().replace(tzinfo=None), windows)
        signal_time = gap.created_at
        signal_dt = fvg_dt
        fvg_source = "created_in_window"
        if window is None:
            if retest_window is None:
                continue
            window = retest_window
            signal_time = int(retest["time"])
            signal_dt = retest_dt
            fvg_source = "first_retest_in_window"
        if retest_must_be_in_window and _matching_window(retest_dt.timetz().replace(tzinfo=None), [window]) is None:
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
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=signal_time,
            score=3,
            reason=f"Silver Bullet {gap.direction} FVG with constrained NY retest",
            metadata={
                "entry_mode": entry_mode,
                "stop_mode": "swing_or_fvg",
                "target_mode": target_mode,
                "session_window": _format_window(window),
                "ny_time": signal_dt.strftime("%Y-%m-%d %H:%M"),
                "signal_time": signal_time,
                "signal_ny_time": signal_dt.strftime("%Y-%m-%d %H:%M"),
                "silver_bullet_fvg_source": fvg_source,
                "fvg_time": gap.created_at,
                "fvg_ny_time": fvg_dt.strftime("%Y-%m-%d %H:%M"),
                "fvg_low": gap.gap_low,
                "fvg_high": gap.gap_high,
                "fvg_ce": (gap.gap_low + gap.gap_high) / 2,
                "silver_bullet_use_ce_invalidation": use_ce_invalidation,
                "entry_time": int(retest["time"]),
                "retest_time": int(retest["time"]),
                "retest_ny_time": retest_dt.strftime("%Y-%m-%d %H:%M"),
                "time_to_retest_bars": _bars_between(closed, gap.created_at, int(retest["time"])),
                "silver_bullet_max_retest_bars": max_retest_bars,
                "silver_bullet_retest_must_occur_within_window": retest_must_be_in_window,
            },
        )
        if item:
            results.append(item)
            break
    return results


def _parse_time(value: str) -> time:
    hour, minute = value.split(":", 1)
    return time(int(hour), int(minute))


def _windows(raw: object, cfg: dict[str, Any]) -> list[tuple[time, time]]:
    if raw is None:
        if cfg.get("silver_bullet_start") or cfg.get("silver_bullet_end"):
            start = _parse_time(str(cfg.get("silver_bullet_start") or SILVER_BULLET_START))
            end = _parse_time(str(cfg.get("silver_bullet_end") or SILVER_BULLET_END))
            return [(start, end)]
        raw = f"{SILVER_BULLET_AM},{SILVER_BULLET_PM}"
    if isinstance(raw, str):
        chunks = [item.strip() for item in raw.split(",") if item.strip()]
    else:
        chunks = [str(item).strip() for item in raw if str(item).strip()]
    windows: list[tuple[time, time]] = []
    for chunk in chunks:
        start_text, end_text = chunk.split("-", 1)
        windows.append((_parse_time(start_text), _parse_time(end_text)))
    return windows or [(_parse_time(SILVER_BULLET_START), _parse_time(SILVER_BULLET_END))]


def _in_window(value: time, start: time, end: time) -> bool:
    return start <= value <= end


def _matching_window(value: time, windows: list[tuple[time, time]]) -> tuple[time, time] | None:
    return next((window for window in windows if _in_window(value, window[0], window[1])), None)


def _format_window(window: tuple[time, time]) -> str:
    return f"{window[0].strftime('%H:%M')}-{window[1].strftime('%H:%M')}"


def _first_retest(candles: list[dict[str, float | int]], after: int, low: float, high: float, max_bars: int) -> dict[str, float | int] | None:
    checked = 0
    for candle in candles:
        if int(candle["time"]) <= after:
            continue
        checked += 1
        if checked > max_bars:
            return None
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            return candle
    return None


def _bars_between(candles: list[dict[str, float | int]], start: int, end: int) -> int | None:
    start_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == start), None)
    end_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == end), None)
    if start_idx is None or end_idx is None:
        return None
    return max(0, end_idx - start_idx)


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
