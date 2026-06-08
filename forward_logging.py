from __future__ import annotations

import csv
import hashlib
import json
import logging
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import LIVE_MODEL_FILTER_CONFIG
from presentation.types import AlertPayload

logger = logging.getLogger(__name__)

FORWARD_LOG_FIELDS = [
    "signal_id",
    "profile_name",
    "model",
    "symbol",
    "timeframe",
    "direction",
    "signal_time",
    "signal_timestamp",
    "entry_low",
    "entry_high",
    "entry_price",
    "target_price",
    "invalidation",
    "status",
    "fill_status",
    "fill_time",
    "fill_timestamp",
    "filled_price",
    "fill_price",
    "slippage_bps",
    "exit_time",
    "exit_timestamp",
    "exit_price",
    "exit_reason",
    "outcome_r",
    "net_outcome_r",
    "bars_to_fill",
    "bars_to_exit",
    "horizon_bars",
    "decision_score",
    "session_label",
    "session_window",
    "range_source",
    "turtle_quality",
    "has_smt_confirmation",
    "metadata_json",
]

_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class ForwardLogConfig:
    enabled: bool
    path: Path
    profile_name: str
    horizon_bars: int
    models: set[str]


def record_forward_shadow_alerts(alerts: list[AlertPayload], all_candles: dict[tuple[str, str], list[dict]]) -> None:
    config = load_forward_log_config()
    if not config.enabled:
        return
    rows = _read_rows(config.path)
    updated = update_forward_log_rows(
        rows,
        alerts,
        all_candles,
        profile_name=config.profile_name,
        horizon_bars=config.horizon_bars,
        models=config.models,
    )
    _write_rows(config.path, updated)


def load_forward_log_config() -> ForwardLogConfig:
    payload = _load_active_filter_payload()
    forward = payload.get("forward_log", {}) if isinstance(payload.get("forward_log"), dict) else {}
    enabled = _bool(os.getenv("FORWARD_LOG_ENABLED", forward.get("enabled", False)))
    path = _resolve_path(str(os.getenv("FORWARD_LOG_PATH") or forward.get("path") or "logs/forward_shadow.csv"))
    horizon_bars = _int_or_default(os.getenv("FORWARD_LOG_HORIZON_BARS") or forward.get("horizon_bars"), 24)
    models = {str(item) for item in forward.get("models", []) if str(item).strip()}
    return ForwardLogConfig(
        enabled=enabled,
        path=path,
        profile_name=str(payload.get("profile_name") or "unknown_profile"),
        horizon_bars=max(1, horizon_bars),
        models=models,
    )


def update_forward_log_rows(
    existing_rows: list[dict[str, Any]],
    alerts: list[AlertPayload],
    all_candles: dict[tuple[str, str], list[dict]],
    *,
    profile_name: str,
    horizon_bars: int,
    models: set[str] | None = None,
) -> list[dict[str, Any]]:
    model_filter = {str(item) for item in models or set()}
    rows_by_id = {str(row.get("signal_id")): dict(row) for row in existing_rows if row.get("signal_id")}
    for alert in alerts:
        if not _loggable_alert(alert, model_filter):
            continue
        signal_id = _signal_id(alert)
        rows_by_id.setdefault(signal_id, _new_signal_row(alert, signal_id, profile_name, horizon_bars))

    for row in rows_by_id.values():
        if str(row.get("status") or "") in {"closed", "missed"}:
            continue
        candles = all_candles.get((str(row.get("symbol")), str(row.get("timeframe"))), [])
        _update_signal_row(row, candles, horizon_bars)

    return sorted(rows_by_id.values(), key=lambda row: (str(row.get("signal_timestamp") or ""), str(row.get("signal_id") or "")))


def _load_active_filter_payload() -> dict[str, Any]:
    path = _resolve_path(os.getenv("LIVE_MODEL_FILTER_CONFIG", LIVE_MODEL_FILTER_CONFIG))
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Could not load forward log profile from %s: %s", path, exc)
        return {}
    return payload if isinstance(payload, dict) else {}


def _resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else _ROOT / path


def _loggable_alert(alert: AlertPayload, models: set[str]) -> bool:
    if alert.alert_kind != "strategy":
        return False
    if models and alert.pattern not in models:
        return False
    return True


def _new_signal_row(alert: AlertPayload, signal_id: str, profile_name: str, horizon_bars: int) -> dict[str, Any]:
    metadata = dict(alert.metadata)
    entry = _entry_price(alert)
    target = _first_float(alert.target_hint, metadata.get("final_target"), metadata.get("tp2_price"))
    invalidation = _first_float(alert.invalidation, metadata.get("stop_loss"))
    return {
        "signal_id": signal_id,
        "profile_name": profile_name,
        "model": alert.pattern,
        "symbol": alert.symbol,
        "timeframe": alert.timeframe,
        "direction": alert.trade_direction or "",
        "signal_time": _iso_ms(alert.timestamp),
        "signal_timestamp": alert.timestamp,
        "entry_low": _cell(alert.entry_low),
        "entry_high": _cell(alert.entry_high),
        "entry_price": _cell(entry),
        "target_price": _cell(target),
        "invalidation": _cell(invalidation),
        "status": "open",
        "fill_status": "pending",
        "fill_time": "",
        "fill_timestamp": "",
        "filled_price": "",
        "fill_price": "",
        "slippage_bps": "",
        "exit_time": "",
        "exit_timestamp": "",
        "exit_price": "",
        "exit_reason": "",
        "outcome_r": "",
        "net_outcome_r": "",
        "bars_to_fill": "",
        "bars_to_exit": "",
        "horizon_bars": horizon_bars,
        "decision_score": _cell(alert.score),
        "session_label": _cell(metadata.get("session_label")),
        "session_window": _cell(metadata.get("session_window")),
        "range_source": _cell(metadata.get("range_source")),
        "turtle_quality": _cell(metadata.get("turtle_quality")),
        "has_smt_confirmation": _cell(metadata.get("has_smt_confirmation")),
        "metadata_json": json.dumps(metadata, sort_keys=True, default=str),
    }


def _update_signal_row(row: dict[str, Any], candles: list[dict], horizon_bars: int) -> None:
    signal_timestamp = _int_or_none(row.get("signal_timestamp"))
    if signal_timestamp is None:
        return
    future = [candle for candle in candles if _int_or_none(candle.get("time")) is not None and int(candle["time"]) > signal_timestamp][:horizon_bars]
    if not future:
        return

    if str(row.get("fill_status") or "") != "filled":
        fill = _first_fill(row, future)
        if fill is None:
            if len(future) >= horizon_bars:
                row["status"] = "missed"
                row["fill_status"] = "missed"
            return
        index, candle = fill
        entry = _float_or_none(row.get("entry_price"))
        row["status"] = "filled"
        row["fill_status"] = "filled"
        row["fill_timestamp"] = int(candle["time"])
        row["fill_time"] = _iso_ms(int(candle["time"]))
        row["filled_price"] = _cell(entry)
        row["fill_price"] = _cell(entry)
        row["slippage_bps"] = 0.0
        row["bars_to_fill"] = index + 1

    _update_exit(row, future, horizon_bars)


def _first_fill(row: dict[str, Any], future: list[dict]) -> tuple[int, dict] | None:
    entry_low = _float_or_none(row.get("entry_low"))
    entry_high = _float_or_none(row.get("entry_high"))
    if entry_low is None or entry_high is None:
        return None
    low_bound = min(entry_low, entry_high)
    high_bound = max(entry_low, entry_high)
    for index, candle in enumerate(future):
        if float(candle["low"]) <= high_bound and float(candle["high"]) >= low_bound:
            return index, candle
    return None


def _update_exit(row: dict[str, Any], future: list[dict], horizon_bars: int) -> None:
    fill_timestamp = _int_or_none(row.get("fill_timestamp"))
    if fill_timestamp is None:
        return
    entry = _float_or_none(row.get("entry_price"))
    invalidation = _float_or_none(row.get("invalidation"))
    target = _float_or_none(row.get("target_price"))
    if entry is None or invalidation is None:
        return
    risk = abs(entry - invalidation)
    if risk <= 0:
        return
    outcome_candles = [candle for candle in future if int(candle["time"]) >= fill_timestamp]
    for index, candle in enumerate(outcome_candles, start=1):
        if _stop_hit(str(row.get("direction") or ""), candle, invalidation):
            _close_row(row, candle, invalidation, "stop_loss", -1.0, index)
            return
        if target is not None and _target_hit(str(row.get("direction") or ""), candle, target):
            outcome_r = _price_outcome_r(str(row.get("direction") or ""), entry, invalidation, target)
            _close_row(row, candle, target, "target", outcome_r, index)
            return
    if len(future) >= horizon_bars and outcome_candles:
        candle = outcome_candles[-1]
        exit_price = float(candle["close"])
        outcome_r = _price_outcome_r(str(row.get("direction") or ""), entry, invalidation, exit_price)
        _close_row(row, candle, exit_price, "horizon_close", outcome_r, len(outcome_candles))


def _close_row(row: dict[str, Any], candle: dict, exit_price: float, reason: str, outcome_r: float, bars_to_exit: int) -> None:
    timestamp = int(candle["time"])
    row["status"] = "closed"
    row["exit_timestamp"] = timestamp
    row["exit_time"] = _iso_ms(timestamp)
    row["exit_price"] = round(float(exit_price), 8)
    row["exit_reason"] = reason
    row["outcome_r"] = round(outcome_r, 6)
    row["net_outcome_r"] = round(outcome_r, 6)
    row["bars_to_exit"] = bars_to_exit


def _signal_id(alert: AlertPayload) -> str:
    metadata = alert.metadata
    parts = [
        alert.pattern,
        alert.symbol,
        alert.timeframe,
        alert.trade_direction or "",
        str(alert.timestamp),
        _rounded(alert.entry_low),
        _rounded(alert.entry_high),
        _rounded(alert.invalidation),
        _rounded(alert.target_hint or metadata.get("final_target") or metadata.get("tp2_price")),
    ]
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:16]


def _entry_price(alert: AlertPayload) -> float | None:
    metadata_entry = _float_or_none(alert.metadata.get("entry_price"))
    if metadata_entry is not None:
        return metadata_entry
    if alert.entry_low is None or alert.entry_high is None:
        return None
    return (float(alert.entry_low) + float(alert.entry_high)) / 2


def _stop_hit(direction: str, candle: dict, invalidation: float) -> bool:
    if direction == "long":
        return float(candle["low"]) <= invalidation
    if direction == "short":
        return float(candle["high"]) >= invalidation
    return False


def _target_hit(direction: str, candle: dict, target: float) -> bool:
    if direction == "long":
        return float(candle["high"]) >= target
    if direction == "short":
        return float(candle["low"]) <= target
    return False


def _price_outcome_r(direction: str, entry: float, invalidation: float, price: float) -> float:
    risk = abs(entry - invalidation)
    if risk <= 0:
        return 0.0
    if direction == "long":
        return (price - entry) / risk
    if direction == "short":
        return (entry - price) / risk
    return 0.0


def _read_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FORWARD_LOG_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FORWARD_LOG_FIELDS})


def _iso_ms(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).isoformat()


def _first_float(*values: Any) -> float | None:
    for value in values:
        parsed = _float_or_none(value)
        if parsed is not None:
            return parsed
    return None


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _int_or_none(value: Any) -> int | None:
    if value in {None, ""}:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _int_or_default(value: Any, default: int) -> int:
    parsed = _int_or_none(value)
    return parsed if parsed is not None else default


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _rounded(value: Any) -> str:
    parsed = _float_or_none(value)
    return "" if parsed is None else f"{parsed:.8f}"


def _cell(value: Any) -> Any:
    return "" if value is None else value


__all__ = [
    "FORWARD_LOG_FIELDS",
    "ForwardLogConfig",
    "load_forward_log_config",
    "record_forward_shadow_alerts",
    "update_forward_log_rows",
]
