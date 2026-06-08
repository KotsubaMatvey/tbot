from __future__ import annotations

import asyncio
import json
import logging
import os
from collections import defaultdict
from pathlib import Path

import aiohttp

from config import CANDLE_LIMIT, ENTRY_MODEL_HTF_MODE, LIVE_MODEL_FILTER_CONFIG, STRATEGY_TIMEFRAMES, SYMBOLS, TIMEFRAMES
from market_primitives import detect_smt
from presentation.alert_builders import build_primitive_alerts, from_entry_setup, from_smt_divergence
from presentation.types import AlertPayload
from scanner.cache import (
    get_active_zones,
    get_cached_candles,
    get_cached_patterns,
    replace_active_zones,
    replace_pattern_cache,
    set_cached_candles,
)
from scanner.confluence import build_confluence_messages
from scanner.dedup import should_skip_duplicate
from scanner.scoring import score_primitive_bundle
from scanner.snapshots import build_primitive_snapshot
from strategies import StrategyContext
from strategies.htf_context import build_htf_context
from strategies.ict_models.lifecycle import classify_setup_lifecycle
from strategies.ict_models.model_filters import passes_model_filter, setup_filter_event
from strategies.ict_models.registry import SELECTABLE_MODELS, get_live_models
from strategies.pre_model_filter import evaluate_pre_model_filter, merge_pre_model_metadata, setup_passes_pre_model_filter
from strategies.setup_utils import current_price
from timeframes import EXECUTION_HTF_MAP, MODEL_3_HTF_MAP, MODEL_3_LTF_MAP, execution_htf_for
from strategies.types import PrimitiveSnapshot

logger = logging.getLogger(__name__)

BINANCE_BASE = "https://fapi.binance.com"
PRIMITIVE_PATTERNS = [
    "FVG",
    "IFVG",
    "OB",
    "BOS",
    "CHoCH",
    "Swings",
    "Sweeps",
    "Liquidity",
    "Volume",
    "VP",
    "KL",
    "PD",
    "Breaker",
    "EQH",
    "EQL",
    "SMT",
]
STRATEGY_PATTERNS = list(SELECTABLE_MODELS)
ALL_PATTERNS = PRIMITIVE_PATTERNS + STRATEGY_PATTERNS

SMT_TIMEFRAMES = {"1m", "5m", "15m", "30m", "1h", "4h"}
SMT_PAIRS = [("BTCUSDT", "ETHUSDT"), ("ETHUSDT", "SOLUSDT")]

_sem = asyncio.Semaphore(5)
_model_filter_payload_cache: dict[str, object] | None = None
MODEL_DEDUP_PRIORITY = {
    "ict2022_mss_fvg": 10,
    "breaker_block": 20,
    "reclaimed_ob": 25,
    "ifvg_retest": 30,
    "rejection_block": 40,
    "turtle_soup": 50,
    "silver_bullet": 60,
    "mitigation_block": 70,
}


async def fetch_candles(
    session: aiohttp.ClientSession,
    symbol: str,
    interval: str,
    limit: int = CANDLE_LIMIT,
) -> list[dict]:
    url = f"{BINANCE_BASE}/fapi/v1/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    try:
        async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as response:
            data = await response.json()
        if not isinstance(data, list):
            logger.warning("Unexpected candle payload for %s %s: %s", symbol, interval, data)
            return []
        return [
            {
                "time": int(candle[0]),
                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5]),
            }
            for candle in data
        ]
    except Exception as exc:
        logger.error("fetch_candles %s %s: %s: %s", symbol, interval, type(exc).__name__, exc)
        return []


async def _fetch_with_sem(session: aiohttp.ClientSession, symbol: str, timeframe: str) -> list[dict]:
    async with _sem:
        return await fetch_candles(session, symbol, timeframe)


def _build_strategy_alerts(
    primary: PrimitiveSnapshot,
    higher: PrimitiveSnapshot | None,
    lower: PrimitiveSnapshot | None,
    htf_timeframe: str | None,
    smt_divergences: list | None = None,
) -> list[AlertPayload]:
    closed_higher = _closed_htf_snapshot(higher) if higher is not None else None
    context = StrategyContext(
        primary=primary,
        higher_timeframe=closed_higher,
        lower_timeframe=lower,
        htf_context=build_htf_context(closed_higher, current_price(primary)) if closed_higher is not None else None,
        htf_timeframe=htf_timeframe,
        execution_timeframe=primary.timeframe,
        htf_mode=ENTRY_MODEL_HTF_MODE,
    )
    setups = []
    model_filters = _load_model_filters()
    config = _strategy_base_config(_load_scanner_config(), smt_divergences)
    pre_model = evaluate_pre_model_filter(context, config)
    if not pre_model.passed:
        return []
    for model in get_live_models():
        model_rules = model_filters.get(model.name, {})
        if not _model_enabled(model.name, model_filters):
            continue
        setups.extend(model.detector(primary.symbol, primary.timeframe, primary.candles, context, _detector_config(config, model_rules)))

    best_by_key: dict[tuple[object, ...], AlertPayload] = {}
    for setup in setups:
        if not setup_passes_pre_model_filter(setup, pre_model):
            continue
        merge_pre_model_metadata(setup, pre_model)
        if not passes_model_filter(setup_filter_event(setup), model_filters.get(setup.model_name, {})):
            continue
        payload = from_entry_setup(setup)
        lifecycle = classify_setup_lifecycle(setup, primary.candles)
        payload.status = str(lifecycle.get("status") or payload.status or "setup_formed")
        payload.metadata.update(lifecycle)
        payload.metadata["live_filters_applied"] = bool(model_filters)
        key = (
            payload.trade_direction or "",
            _rounded_zone(payload.entry_low),
            _rounded_zone(payload.entry_high),
            _rounded_zone(payload.invalidation),
        )
        existing = best_by_key.get(key)
        if existing is None or _payload_rank(payload) < _payload_rank(existing):
            best_by_key[key] = payload
    return list(best_by_key.values())


def _payload_rank(payload: AlertPayload) -> tuple[int, int]:
    return (MODEL_DEDUP_PRIORITY.get(payload.pattern, 100), -(payload.score or 0))


def _rounded_zone(value: float | None) -> float | None:
    return round(float(value), 5) if value is not None else None


def _closed_htf_snapshot(snapshot: PrimitiveSnapshot) -> PrimitiveSnapshot | None:
    closed = snapshot.candles[:-1]
    if not closed:
        return None
    return build_primitive_snapshot(snapshot.symbol, snapshot.timeframe, closed)


def _load_model_filter_payload() -> dict[str, object]:
    global _model_filter_payload_cache
    if _model_filter_payload_cache is not None:
        return _model_filter_payload_cache
    path = Path(os.getenv("LIVE_MODEL_FILTER_CONFIG", LIVE_MODEL_FILTER_CONFIG))
    if not path.is_absolute():
        path = Path(__file__).resolve().parent.parent / path
    if not path.exists():
        _model_filter_payload_cache = {}
        return _model_filter_payload_cache
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Could not load live model filters from %s: %s", path, exc)
        _model_filter_payload_cache = {}
        return _model_filter_payload_cache
    _model_filter_payload_cache = payload if isinstance(payload, dict) else {}
    return _model_filter_payload_cache


def _load_model_filters() -> dict[str, dict]:
    payload = _load_model_filter_payload()
    filters = payload.get("model_filters", payload)
    return filters if isinstance(filters, dict) else {}


def _load_scanner_config() -> dict[str, object]:
    payload = _load_model_filter_payload()
    config = payload.get("scanner_config", {})
    return config if isinstance(config, dict) else {}


def _model_enabled(model_name: str, model_filters: dict[str, dict]) -> bool:
    return model_filters.get(model_name, {}).get("enabled", True) is not False


def _detector_config(base_config: dict, model_rules: dict) -> dict:
    return {**base_config, **model_rules}


def _strategy_base_config(scanner_config: dict[str, object], smt_divergences: list | None) -> dict:
    context_mode = str(scanner_config.get("context_mode") or ENTRY_MODEL_HTF_MODE)
    htf_mode = str(scanner_config.get("htf_mode") or context_mode)
    config = {
        "context_mode": context_mode,
        "htf_mode": htf_mode,
        "smt_divergences": list(smt_divergences or []),
        "has_smt_confirmation": bool(smt_divergences),
    }
    for name in (
        "pre_model_filter",
        "pre_model_filter_enabled",
        "pre_model_require_htf_poi",
        "pre_model_allow_neutral_htf",
        "pre_model_allow_equilibrium",
        "pre_model_require_smt",
        "pre_model_require_killzone",
        "pre_model_killzone_windows",
    ):
        if name in scanner_config:
            config[name] = scanner_config[name]
    return config


def _build_smt_map(all_candles: dict[tuple[str, str], list[dict]]) -> dict[tuple[str, str], list]:
    smt_by_key: dict[tuple[str, str], list] = {}
    for symbol_a, symbol_b in SMT_PAIRS:
        for timeframe in sorted(SMT_TIMEFRAMES):
            candles_a = all_candles.get((symbol_a, timeframe))
            candles_b = all_candles.get((symbol_b, timeframe))
            if not candles_a or not candles_b:
                continue
            divergences = detect_smt(candles_a, candles_b, symbol_a, symbol_b, timeframe)
            if divergences:
                smt_by_key.setdefault((symbol_a, timeframe), []).extend(divergences)
    return smt_by_key


def _score_primitive_alerts(
    symbol: str,
    timeframe: str,
    snapshot: PrimitiveSnapshot,
    alerts: list[AlertPayload],
) -> None:
    bundle = {alert.pattern: alert.detail for alert in alerts if alert.alert_kind == "primitive"}
    if not bundle:
        return
    score = score_primitive_bundle(bundle, timeframe, snapshot)
    for alert in alerts:
        if alert.alert_kind == "primitive":
            alert.score = score


async def run_scanner() -> tuple[list[AlertPayload], list[dict[str, str]], dict[tuple[str, str], list[dict]]]:
    all_alerts: list[AlertPayload] = []
    all_candles: dict[tuple[str, str], list[dict]] = {}
    snapshots: dict[tuple[str, str], PrimitiveSnapshot] = {}
    alerts_by_symbol: dict[str, dict[str, list[AlertPayload]]] = {symbol: {} for symbol in SYMBOLS}

    fetch_timeframes = sorted(
        set(TIMEFRAMES)
        | set(STRATEGY_TIMEFRAMES)
        | {tf for tf in EXECUTION_HTF_MAP.values() if tf}
        | {tf for tf in MODEL_3_HTF_MAP.values() if tf}
        | {tf for tf in MODEL_3_LTF_MAP.values() if tf}
    )

    connector = aiohttp.TCPConnector(limit=10, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        combos = [(symbol, timeframe) for symbol in SYMBOLS for timeframe in fetch_timeframes]
        tasks = [_fetch_with_sem(session, symbol, timeframe) for symbol, timeframe in combos]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    for (symbol, timeframe), candles in zip(combos, results):
        if isinstance(candles, Exception) or not candles:
            continue
        all_candles[(symbol, timeframe)] = candles
        set_cached_candles(symbol, timeframe, candles)

    for (symbol, timeframe), candles in all_candles.items():
        snapshots[(symbol, timeframe)] = build_primitive_snapshot(symbol, timeframe, candles)

    smt_by_key = _build_smt_map(all_candles)

    for symbol in SYMBOLS:
        for timeframe in sorted(set(TIMEFRAMES) | set(STRATEGY_TIMEFRAMES)):
            primary = snapshots.get((symbol, timeframe))
            if primary is None:
                continue
            higher_tf = execution_htf_for(timeframe)
            lower_tf = MODEL_3_LTF_MAP.get(timeframe)

            primitive_alerts = (
                build_primitive_alerts(
                    swings=primary.swings,
                    sweeps=primary.sweeps,
                    raids=primary.raids,
                    structure_breaks=primary.structure_breaks,
                    fvgs=primary.fvgs[-2:],
                    ifvgs=primary.ifvgs[-2:],
                    order_blocks=primary.order_blocks,
                    breaker_blocks=primary.breaker_blocks,
                    equal_highs=primary.equal_highs,
                    equal_lows=primary.equal_lows,
                    key_levels=primary.key_levels[:1],
                    volume_signals=primary.volume_signals,
                    pd_zones=primary.pd_zones,
                    smt_divergences=[],
                )
                if timeframe in TIMEFRAMES
                else []
            )
            strategy_alerts = (
                _build_strategy_alerts(
                    primary,
                    snapshots.get((symbol, higher_tf)) if higher_tf else None,
                    snapshots.get((symbol, lower_tf)) if lower_tf else None,
                    higher_tf,
                    smt_by_key.get((symbol, timeframe), []),
                )
                if timeframe in STRATEGY_TIMEFRAMES
                else []
            )
            combined = primitive_alerts + strategy_alerts
            if not combined:
                continue
            _score_primitive_alerts(symbol, timeframe, primary, combined)
            alerts_by_symbol[symbol][timeframe] = combined

    for (symbol, timeframe), divergences in smt_by_key.items():
        if timeframe in TIMEFRAMES:
            for divergence in divergences:
                alert = from_smt_divergence(divergence)
                alerts_by_symbol.setdefault(symbol, {}).setdefault(timeframe, []).append(alert)

    active_zones: dict[str, dict[str, list[AlertPayload]]] = {}
    grouped_for_confluence: dict[str, dict[str, list[AlertPayload]]] = defaultdict(dict)

    for symbol, by_timeframe in alerts_by_symbol.items():
        for timeframe, alerts in by_timeframe.items():
            unique_alerts: list[AlertPayload] = []
            for alert in alerts:
                if should_skip_duplicate(alert):
                    continue
                unique_alerts.append(alert)
                all_alerts.append(alert)
            if unique_alerts:
                active_zones.setdefault(symbol, {})[timeframe] = unique_alerts
                grouped_for_confluence[symbol][timeframe] = unique_alerts

    confluences: list[dict[str, str]] = []
    for symbol, by_timeframe in grouped_for_confluence.items():
        for message in build_confluence_messages(symbol, by_timeframe):
            confluences.append({"symbol": symbol, "message": message})

    replace_active_zones(active_zones)
    replace_pattern_cache(all_alerts)
    return all_alerts, confluences, all_candles


__all__ = [
    "ALL_PATTERNS",
    "EXECUTION_HTF_MAP",
    "MODEL_3_HTF_MAP",
    "MODEL_3_LTF_MAP",
    "PRIMITIVE_PATTERNS",
    "STRATEGY_TIMEFRAMES",
    "STRATEGY_PATTERNS",
    "fetch_candles",
    "get_active_zones",
    "get_cached_candles",
    "get_cached_patterns",
    "run_scanner",
]
