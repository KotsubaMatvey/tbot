from __future__ import annotations

from backtesting import Candle
from backtesting.accumulator import ReplaySnapshotCache
from scanner.snapshots import build_primitive_snapshot
from strategies import PrimitiveSnapshot, StrategyContext
from strategies.htf_context import build_htf_context
from strategies.setup_utils import current_price, timeframe_to_ms
from timeframes import MODEL_3_LTF_MAP, execution_htf_for

CandleStore = dict[tuple[str, str], list[Candle]]


def slice_candles_until(candles: list[Candle], timestamp: int) -> list[Candle]:
    return [candle for candle in candles if int(candle["time"]) <= timestamp]


def slice_closed_candles_until(candles: list[Candle], timeframe: str, timestamp: int) -> list[Candle]:
    tf_ms = timeframe_to_ms(timeframe)
    if tf_ms is None:
        return slice_candles_until(candles, timestamp)
    return [candle for candle in candles if int(candle["time"]) + tf_ms <= timestamp]


def build_strategy_context_for_replay(
    *,
    symbol: str,
    timeframe: str,
    primary_visible: list[Candle],
    current_timestamp: int,
    candle_store: CandleStore,
    higher_timeframe: str | None = None,
    lower_timeframe: str | None = None,
    htf_mode: str = "strict",
    require_displacement: bool = True,
    model3_fill_threshold: float = 0.5,
    stop_mode: str = "structural",
    model3_stop_mode: str = "source_zone_extreme",
    stop_buffer_bps: float = 2.0,
    invalidation_confirmation: str = "close",
    model3_reaction_bars: int = 10,
    model3_min_rr_to_objective: float = 1.5,
    model3_source_zone: str = "any",
) -> StrategyContext:
    primary = build_primitive_snapshot(symbol, timeframe, primary_visible)

    htf = higher_timeframe if higher_timeframe is not None else execution_htf_for(timeframe)
    ltf = lower_timeframe if lower_timeframe is not None else MODEL_3_LTF_MAP.get(timeframe)

    higher = None
    htf_context = None
    if htf:
        # Lookahead guard: HTF context uses only candles closed before the current
        # primary bar. A daily/4h candle whose open is <= current_timestamp can
        # still be forming, so slicing by open time alone is not enough.
        visible = slice_closed_candles_until(candle_store.get((symbol, htf), []), htf, current_timestamp)
        if visible:
            higher = build_primitive_snapshot(symbol, htf, visible)
            htf_context = build_htf_context(higher, current_price(primary))

    lower = None
    if ltf:
        # Lookahead guard: LTF context is also timestamp-sliced before snapshot creation.
        visible = slice_candles_until(candle_store.get((symbol, ltf), []), current_timestamp)
        if visible:
            lower = build_primitive_snapshot(symbol, ltf, visible)

    return StrategyContext(
        primary=primary,
        higher_timeframe=higher,
        lower_timeframe=lower,
        htf_context=htf_context,
        htf_timeframe=htf,
        execution_timeframe=timeframe,
        htf_mode=htf_mode,
        require_displacement=require_displacement,
        model3_fill_threshold=model3_fill_threshold,
        stop_mode=stop_mode,
        model3_stop_mode=model3_stop_mode,
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
        model3_reaction_bars=model3_reaction_bars,
        model3_min_rr_to_objective=model3_min_rr_to_objective,
        model3_source_zone=model3_source_zone,
    )


def build_accumulated_strategy_context_for_replay(
    *,
    symbol: str,
    timeframe: str,
    current_timestamp: int,
    snapshot_cache: ReplaySnapshotCache,
    primary_visible: list[Candle] | None = None,
    accumulate_primary: bool = True,
    higher_timeframe: str | None = None,
    lower_timeframe: str | None = None,
    htf_mode: str = "strict",
    require_displacement: bool = True,
    model3_fill_threshold: float = 0.5,
    stop_mode: str = "structural",
    model3_stop_mode: str = "source_zone_extreme",
    stop_buffer_bps: float = 2.0,
    invalidation_confirmation: str = "close",
    model3_reaction_bars: int = 10,
    model3_min_rr_to_objective: float = 1.5,
    model3_source_zone: str = "any",
) -> StrategyContext | None:
    if accumulate_primary:
        primary = snapshot_cache.get_snapshot(symbol, timeframe, current_timestamp)
    elif primary_visible:
        primary = PrimitiveSnapshot(symbol=symbol, timeframe=timeframe, candles=primary_visible)
    else:
        primary = None
    if primary is None:
        return None

    htf = higher_timeframe if higher_timeframe is not None else execution_htf_for(timeframe)
    ltf = lower_timeframe if lower_timeframe is not None else MODEL_3_LTF_MAP.get(timeframe)

    htf_visible_timestamp = None
    if htf:
        tf_ms = timeframe_to_ms(htf)
        htf_visible_timestamp = current_timestamp - tf_ms if tf_ms is not None else current_timestamp
    higher = snapshot_cache.get_snapshot(symbol, htf, htf_visible_timestamp) if htf and htf_visible_timestamp is not None else None
    lower = snapshot_cache.get_snapshot(symbol, ltf, current_timestamp) if ltf else None
    return StrategyContext(
        primary=primary,
        higher_timeframe=higher,
        lower_timeframe=lower,
        htf_context=build_htf_context(higher, current_price(primary)) if higher is not None else None,
        htf_timeframe=htf,
        execution_timeframe=timeframe,
        htf_mode=htf_mode,
        require_displacement=require_displacement,
        model3_fill_threshold=model3_fill_threshold,
        stop_mode=stop_mode,
        model3_stop_mode=model3_stop_mode,
        stop_buffer_bps=stop_buffer_bps,
        invalidation_confirmation=invalidation_confirmation,
        model3_reaction_bars=model3_reaction_bars,
        model3_min_rr_to_objective=model3_min_rr_to_objective,
        model3_source_zone=model3_source_zone,
    )


__all__ = [
    "CandleStore",
    "build_accumulated_strategy_context_for_replay",
    "build_strategy_context_for_replay",
    "slice_closed_candles_until",
    "slice_candles_until",
]
