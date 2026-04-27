from __future__ import annotations

from typing import Any

from .common import buffered_stop, closed_candles, nearest_liquidity_target, setup

ICT2022_REQUIRE_HTF = False
ICT2022_REQUIRE_DISPLACEMENT = True
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
            ),
            None,
        )
        if structure is None:
            continue
        fvg = next((g for g in snapshot.fvgs if g.direction == direction and g.created_at >= structure.timestamp and not g.invalidated), None)
        if fvg is None:
            continue
        ce = (fvg.gap_low + fvg.gap_high) / 2
        entry = fvg.gap_high if side == "long" and entry_mode == "edge" else fvg.gap_low if side == "short" and entry_mode == "edge" else ce
        stop = buffered_stop(side, sweep.wick_extreme, entry, stop_bps)
        target = nearest_liquidity_target(closed_candles(candles), side, entry, stop)
        item = setup(
            model_name="ict2022_mss_fvg",
            direction=side,
            symbol=symbol,
            timeframe=timeframe,
            entry_low=entry,
            entry_high=entry,
            stop_loss=stop,
            target_hint=target,
            timestamp=max(sweep.timestamp, structure.timestamp, fvg.created_at),
            score=4 if structure.displacement_grade == "strong" else 3,
            reason="ICT 2022 sweep, MSS and displacement FVG",
            metadata={
                "entry_mode": entry_mode,
                "stop_mode": ICT2022_STOP_MODE,
                "target_mode": ICT2022_TARGET_MODE,
                "sweep_time": sweep.timestamp,
                "sweep_level": sweep.liquidity_level,
                "sweep_extreme": sweep.wick_extreme,
                "mss_time": structure.timestamp,
                "structure_level": structure.broken_level,
                "displacement_grade": structure.displacement_grade,
                "fvg_low": fvg.gap_low,
                "fvg_high": fvg.gap_high,
                "fvg_ce": ce,
            },
        )
        if item:
            results.append(item)
    return results


__all__ = ["detect_setups"]
