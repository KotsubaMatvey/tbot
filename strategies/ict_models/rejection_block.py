from __future__ import annotations

from typing import Any

from market_primitives.common import collect_swings

from .common import buffered_stop, closed_candles, context_metadata, nearest_liquidity_target, setup
from .sessions import LONDON_OPEN, NY_OPEN, in_ny_windows

ENABLED_BY_DEFAULT = False
RESEARCH_ONLY = True
REJECTION_ENTRY_MODE = "body_level"
REJECTION_STOP_MODE = "wick_extreme"


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    cfg = config or {}
    closed = closed_candles(candles)
    if len(closed) < 10:
        return []
    htf_mode = str(cfg.get("context_mode") or cfg.get("htf_mode") or "off")
    require_killzone = bool(cfg.get("rejection_block_require_killzone", False))
    stop_bps = float(cfg.get("stop_buffer_bps") or 2)
    scan = closed[-80:]
    current = scan[-1]
    if require_killzone and not in_ny_windows(int(current["time"]), [LONDON_OPEN, NY_OPEN]):
        return []
    highs, lows = collect_swings(scan[:-1], symbol, timeframe)
    results = []

    high = next((item for item in reversed(highs) if item.body_level is not None), None)
    if high is not None:
        body_level = float(high.body_level)
        wick_extreme = float(high.level)
        swept_body = float(current["high"]) >= body_level
        respected_wick = float(current["high"]) < wick_extreme
        closed_back = float(current["close"]) < body_level
        if swept_body and respected_wick and closed_back:
            entry = body_level
            stop_ref = max(wick_extreme, float(current["high"]))
            stop = buffered_stop("short", stop_ref, entry, stop_bps)
            metadata = context_metadata(context, "short", htf_mode, cfg)
            item = setup(
                model_name="rejection_block",
                direction="short",
                symbol=symbol,
                timeframe=timeframe,
                entry_low=entry,
                entry_high=entry,
                entry_price=entry,
                stop_loss=stop,
                target_hint=nearest_liquidity_target(closed, "short", entry, stop),
                timestamp=int(current["time"]),
                score=2,
                reason="Bearish rejection block body sweep below prior wick extreme",
                metadata={
                    **metadata,
                    "entry_mode": REJECTION_ENTRY_MODE,
                    "stop_mode": REJECTION_STOP_MODE,
                    "target_mode": "nearest_liquidity",
                    "session_filter": "london_or_ny_open" if require_killzone else "off",
                    "rejection_body_level": body_level,
                    "rejection_wick_extreme": wick_extreme,
                    "current_wick_extreme": float(current["high"]),
                    "source_swing_time": high.timestamp,
                    "source_swing_significance": high.significance,
                },
            )
            if item:
                results.append(item)

    low = next((item for item in reversed(lows) if item.body_level is not None), None)
    if low is not None:
        body_level = float(low.body_level)
        wick_extreme = float(low.level)
        swept_body = float(current["low"]) <= body_level
        respected_wick = float(current["low"]) > wick_extreme
        closed_back = float(current["close"]) > body_level
        if swept_body and respected_wick and closed_back:
            entry = body_level
            stop_ref = min(wick_extreme, float(current["low"]))
            stop = buffered_stop("long", stop_ref, entry, stop_bps)
            metadata = context_metadata(context, "long", htf_mode, cfg)
            item = setup(
                model_name="rejection_block",
                direction="long",
                symbol=symbol,
                timeframe=timeframe,
                entry_low=entry,
                entry_high=entry,
                entry_price=entry,
                stop_loss=stop,
                target_hint=nearest_liquidity_target(closed, "long", entry, stop),
                timestamp=int(current["time"]),
                score=2,
                reason="Bullish rejection block body sweep above prior wick extreme",
                metadata={
                    **metadata,
                    "entry_mode": REJECTION_ENTRY_MODE,
                    "stop_mode": REJECTION_STOP_MODE,
                    "target_mode": "nearest_liquidity",
                    "session_filter": "london_or_ny_open" if require_killzone else "off",
                    "rejection_body_level": body_level,
                    "rejection_wick_extreme": wick_extreme,
                    "current_wick_extreme": float(current["low"]),
                    "source_swing_time": low.timestamp,
                    "source_swing_significance": low.significance,
                },
            )
            if item:
                results.append(item)

    return results[:1]


__all__ = ["ENABLED_BY_DEFAULT", "RESEARCH_ONLY", "detect_setups"]
