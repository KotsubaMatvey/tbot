from __future__ import annotations

from datetime import datetime, time
from typing import Any
from zoneinfo import ZoneInfo

from .common import buffered_stop, closed_candles, context_metadata, nearest_liquidity_target, setup
from .sessions import LONDON_OPEN, NY_OPEN, NY_PM_SESSION, NY_TZ, in_ny_windows

ICT2022_REQUIRE_HTF = False
ICT2022_REQUIRE_DISPLACEMENT = True
ICT2022_REQUIRE_KILLZONE = True
ICT2022_ENTRY_MODE = "edge"
ICT2022_STOP_MODE = "sweep_extreme"
ICT2022_TARGET_MODE = "nearest_liquidity"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    entry_mode = str(cfg.get("entry_mode") or ICT2022_ENTRY_MODE)
    if entry_mode not in {"edge", "ce"}:
        entry_mode = ICT2022_ENTRY_MODE
    require_displacement = bool(cfg.get("ict2022_require_displacement", ICT2022_REQUIRE_DISPLACEMENT))
    require_strong_displacement = bool(cfg.get("ict2022_require_strong_displacement", True))
    require_body_close = bool(cfg.get("ict2022_require_body_close", True))
    require_killzone = bool(cfg.get("ict2022_require_killzone", ICT2022_REQUIRE_KILLZONE))
    session_windows = _window_list(cfg.get("ict2022_session_windows") or [LONDON_OPEN, NY_OPEN, NY_PM_SESSION])
    require_same_session = bool(cfg.get("ict2022_require_same_session", True))
    retest_must_be_in_session = bool(cfg.get("ict2022_retest_must_occur_within_session", False))
    max_sweep_age_bars = int(cfg.get("ict2022_max_sweep_age_bars", 20))
    max_fvg_retest_bars = int(cfg.get("ict2022_max_fvg_retest_bars", 20))
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    snapshot = getattr(context, "primary", None) if context is not None else None
    if snapshot is None:
        from scanner.snapshots import build_primitive_snapshot

        snapshot = build_primitive_snapshot(symbol, timeframe, candles)
    results = []
    for side, direction in (("long", "bullish"), ("short", "bearish")):
        sweep = next((s for s in sorted(snapshot.sweeps + snapshot.raids, key=lambda x: x.timestamp, reverse=True) if s.direction == direction), None)
        if sweep is None:
            continue
        structure = next(
            (
                item
                for item in sorted(snapshot.structure_breaks, key=lambda x: x.timestamp)
                if item.direction == direction
                and item.timestamp > sweep.timestamp
                and (item.displacement_grade in {"valid", "strong"} or not require_displacement)
                and (item.displacement_grade == "strong" or not require_strong_displacement)
                and (item.close_beyond_structure or not require_body_close)
            ),
            None,
        )
        if structure is None:
            continue
        sweep_age = _bars_between(snapshot.candles, sweep.timestamp, structure.timestamp)
        if sweep_age is not None and sweep_age > max_sweep_age_bars:
            continue
        sweep_window = _matching_window(sweep.timestamp, session_windows)
        structure_window = _matching_window(structure.timestamp, session_windows)
        if require_killzone:
            if sweep_window is None or structure_window is None:
                continue
            if require_same_session and sweep_window != structure_window:
                continue
        fvg = next((g for g in snapshot.fvgs if g.direction == direction and g.created_at >= structure.timestamp and not g.invalidated), None)
        if fvg is None:
            continue
        retest_idx = _first_retest_index(snapshot.candles, fvg.created_at, fvg.gap_low, fvg.gap_high, max_fvg_retest_bars)
        if retest_idx is None:
            continue
        retest = snapshot.candles[retest_idx]
        retest_window = _matching_window(int(retest["time"]), session_windows)
        if retest_must_be_in_session and retest_window != (structure_window or sweep_window):
            continue
        session_window = retest_window or structure_window or sweep_window
        ce = (fvg.gap_low + fvg.gap_high) / 2
        entry = fvg.gap_high if side == "long" and entry_mode == "edge" else fvg.gap_low if side == "short" and entry_mode == "edge" else ce
        stop = buffered_stop(side, sweep.wick_extreme, entry, stop_bps)
        metadata = context_metadata(context, side, htf_mode, cfg)
        context_target = _target_from_context(metadata, side)
        target = context_target or nearest_liquidity_target(closed_candles(candles), side, entry, stop)
        if _target_reached_before_retest(snapshot.candles, fvg.created_at, int(retest["time"]), side, target):
            continue
        item = setup(
            model_name="ict2022_mss_fvg",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            entry_price=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=max(sweep.timestamp, structure.timestamp, fvg.created_at),
            score=4 if structure.displacement_grade == "strong" else 3,
            reason="ICT 2022 sweep, MSS and displacement FVG",
            metadata={
                **metadata,
                **_session_metadata(int(retest["time"]), session_window),
                "entry_mode": entry_mode,
                "stop_mode": ICT2022_STOP_MODE,
                "target_mode": "htf_external_liquidity" if context_target is not None else ICT2022_TARGET_MODE,
                "target_reached_before_entry_policy": "skip_before_retest",
                "session_filter": "configured" if require_killzone else "off",
                "ict2022_session_windows": ",".join(session_windows),
                "ict2022_retest_must_occur_within_session": retest_must_be_in_session,
                "sweep_time": sweep.timestamp,
                "sweep_age_bars": sweep_age,
                "sweep_level": sweep.liquidity_level,
                "swept_level": sweep.liquidity_level,
                "sweep_extreme": sweep.wick_extreme,
                "mss_time": structure.timestamp,
                "structure_level": structure.broken_level,
                "displacement_grade": structure.displacement_grade,
                "displacement_factor": structure.displacement_factor,
                "body_ratio": structure.body_ratio,
                "fvg_low": fvg.gap_low,
                "fvg_high": fvg.gap_high,
                "fvg_ce": ce,
                "fvg_ce_invalidation": ce,
                "entry_time": int(retest["time"]),
                "retest_time": int(retest["time"]),
                "time_to_retest_bars": retest_idx - _index_at_time(snapshot.candles, fvg.created_at),
                "ict2022_max_fvg_retest_bars": max_fvg_retest_bars,
            },
        )
        if item:
            results.append(item)
    return results


def _target_from_context(metadata: dict[str, object], side: str) -> float | None:
    level = metadata.get("htf_objective_level")
    draw = metadata.get("htf_draw_direction")
    if not isinstance(level, (int, float)):
        return None
    if side == "long" and draw == "up":
        return float(level)
    if side == "short" and draw == "down":
        return float(level)
    return None


def _target_reached_before_retest(
    candles: list[dict[str, float | int]],
    after: int,
    before: int,
    side: str,
    target: float | None,
) -> bool:
    if target is None:
        return False
    for candle in candles:
        ts = int(candle["time"])
        if ts <= after:
            continue
        if ts >= before:
            return False
        if side == "long" and float(candle["high"]) >= target:
            return True
        if side == "short" and float(candle["low"]) <= target:
            return True
    return False


def _first_retest_index(candles: list[dict[str, float | int]], after: int, low: float, high: float, max_bars: int) -> int | None:
    checked = 0
    for idx, candle in enumerate(candles):
        if int(candle["time"]) <= after:
            continue
        checked += 1
        if checked > max_bars:
            return None
        if float(candle["low"]) <= high and float(candle["high"]) >= low:
            return idx
    return None


def _index_at_time(candles: list[dict[str, float | int]], timestamp: int) -> int:
    return next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == timestamp), 0)


def _bars_between(candles: list[dict[str, float | int]], start: int, end: int) -> int | None:
    start_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == start), None)
    end_idx = next((idx for idx, candle in enumerate(candles) if int(candle["time"]) == end), None)
    if start_idx is None or end_idx is None:
        return None
    return max(0, end_idx - start_idx)


def _window_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return [str(item).strip() for item in value if str(item).strip()]


def _matching_window(timestamp: int, windows: list[str]) -> str | None:
    return next((window for window in windows if in_ny_windows(timestamp, window)), None)


def _session_metadata(timestamp: int, window: str | None) -> dict[str, object]:
    if window is None:
        return {}
    dt = datetime.fromtimestamp(timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(ZoneInfo(NY_TZ))
    return {
        "session_window": window,
        "session_date": dt.strftime("%Y-%m-%d"),
        "session_label": _session_label(window),
        "ny_time": dt.strftime("%Y-%m-%d %H:%M"),
    }


def _session_label(window: str) -> str:
    start = _parse_time(window.split("-", 1)[0])
    if start < time(5, 0):
        return "london_open"
    if start < time(10, 0):
        return "ny_open"
    if start < time(12, 0):
        return "ny_am"
    if start >= time(14, 0) and start < time(16, 0):
        return "ny_pm"
    return "custom"


def _parse_time(value: str) -> time:
    hour, minute = value.split(":", 1)
    return time(int(hour), int(minute))


__all__ = ["detect_setups"]
