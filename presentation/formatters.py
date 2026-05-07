from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable

from market_primitives.common import fmt_price

from .types import AlertPayload


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%H:%M UTC")


def build_alert_message(symbol: str, timeframe: str, alerts: Iterable[AlertPayload]) -> str:
    payloads = list(alerts)
    if payloads and all(item.alert_kind == "strategy" for item in payloads):
        return "\n\n".join(build_strategy_alert_text(item) for item in payloads)

    lines = [f"{symbol}  {timeframe}"]
    lines.extend(f"- {alert.detail}" for alert in payloads)
    return "\n".join(lines)


def build_strategy_alert_text(alert: AlertPayload) -> str:
    lines = []
    if alert.context_timeframe:
        lines.append(f"{alert.symbol}  HTF {alert.context_timeframe} / LTF {alert.timeframe}")
    else:
        lines.append(f"{alert.symbol}  {alert.timeframe}")
    setup_parts = [f"{alert.pattern}  {(alert.trade_direction or '').upper()}"]
    if alert.status:
        setup_parts.append(f"Status: {alert.status.replace('_', ' ').upper()}")
    if alert.score is not None:
        setup_parts.append(f"Score: {alert.score}/5")
    lines.append(" | ".join(setup_parts))
    plan = _ict_plan_line(alert)
    if plan:
        lines.append(plan)
    else:
        htf_summary = _htf_summary_line(alert)
        if htf_summary:
            lines.append(htf_summary)
    risk_parts = []
    stop_model = alert.metadata.get("stop_model")
    if stop_model:
        risk_parts.append(str(stop_model))
    if alert.entry_low is not None and alert.entry_high is not None:
        risk_parts.append(f"Entry zone: {fmt_price(alert.entry_low)} - {fmt_price(alert.entry_high)}")
    if alert.invalidation is not None:
        risk_parts.append(f"Invalidation: {fmt_price(alert.invalidation)}")
    rr = alert.metadata.get("rr_to_target")
    if isinstance(rr, (int, float)):
        risk_parts.append(f"RR {float(rr):.2f}R")
    if risk_parts:
        lines.append("Risk: " + " | ".join(risk_parts))
    tp1 = alert.metadata.get("tp1_price")
    tp2 = alert.metadata.get("tp2_price")
    if isinstance(tp1, (int, float)) or isinstance(tp2, (int, float)):
        parts = []
        if isinstance(tp1, (int, float)):
            parts.append(f"TP1 {fmt_price(tp1)}")
        if isinstance(tp2, (int, float)):
            parts.append(f"TP2 {fmt_price(tp2)}")
        lines.append("Targets: " + " | ".join(parts))
    logical_price = alert.metadata.get("logical_invalidation_price")
    logical_model = alert.metadata.get("logical_invalidation_model")
    if isinstance(logical_price, (int, float)):
        lines.append(f"Logical invalidation: {logical_model or 'body_close'} {fmt_price(logical_price)}")
    if alert.reason:
        lines.append(f"Reason: {alert.reason}")
    return "\n".join(lines)


def _htf_summary_line(alert: AlertPayload) -> str | None:
    htf_bias = alert.metadata.get("htf_bias")
    if not htf_bias or htf_bias == "none":
        return None
    parts = [f"HTF: {alert.context_timeframe or '-'}", str(htf_bias)]
    htf_location = alert.metadata.get("htf_location")
    if htf_location and htf_location != "unknown":
        parts.append(str(htf_location))
    htf_zone = alert.metadata.get("htf_zone_type")
    if htf_zone and htf_zone != "None":
        parts.append(f"POI {htf_zone}")
    htf_objective = alert.metadata.get("htf_objective_type")
    if htf_objective and htf_objective != "none":
        parts.append(f"DOL {htf_objective}")
    return " ".join(parts)


def _ict_plan_line(alert: AlertPayload) -> str | None:
    metadata = alert.metadata
    bias = metadata.get("htf_bias")
    if not bias or bias == "none":
        return None
    location = metadata.get("htf_location")
    htf = f"HTF {bias}"
    if location and location != "unknown":
        htf = f"{htf} {location}"

    draw = metadata.get("htf_draw_direction") or metadata.get("htf_objective")
    objective_type = metadata.get("htf_objective_type") or "objective"
    objective_level = metadata.get("htf_objective_level")
    dol = f"DOL {draw or '-'} {objective_type}"
    if isinstance(objective_level, (int, float)):
        dol = f"{dol} {fmt_price(objective_level)}"

    poi_type = metadata.get("htf_zone_type")
    poi = str(poi_type or "POI")
    zone_low = metadata.get("htf_zone_low")
    zone_high = metadata.get("htf_zone_high")
    if isinstance(zone_low, (int, float)) and isinstance(zone_high, (int, float)):
        poi = f"{poi} {fmt_price(zone_low)}-{fmt_price(zone_high)}"

    direction = (alert.trade_direction or "").upper()
    return f"ICT plan: {htf} -> {dol} -> POI {poi} -> {direction} entry"


def build_chart_caption(symbol: str, timeframe: str, alerts: Iterable[AlertPayload]) -> str:
    payloads = list(alerts)
    if not payloads:
        return f"{symbol}  {timeframe}"
    strategy = next((alert for alert in payloads if alert.alert_kind == "strategy"), None)
    if strategy is not None:
        parts = [f"{symbol}  {timeframe}", f"{strategy.pattern} {str(strategy.trade_direction or '').upper()}"]
        if strategy.score is not None:
            parts.append(f"{strategy.score}/5")
        return " | ".join(part for part in parts if part)
    patterns = ", ".join(alert.pattern for alert in payloads[:3])
    return f"{symbol}  {timeframe} | {patterns}"


def build_payment_message(price: str | float, expired: bool = False) -> str:
    expired_line = "\nYour subscription has expired.\n" if expired else ""
    return (
        "Subscribe to ICT Crypto Alerts\n"
        f"{expired_line}\n"
        f"Price: `${price}` / month\n"
        "Pay in any crypto - USDT | TON | BTC | ETH\n\n"
        "Includes:\n"
        "- Real-time ICT pattern detection\n"
        "- Turtle Soup / Silver Bullet / IFVG / Breaker / Rejection / Mitigation alerts\n"
        "- Primitive FVG | IFVG | OB | BOS | CHoCH alerts\n"
        "- Multi-timeframe zone tracking\n"
        "After payment tap Check Payment below."
    )


def build_dashboard_message(user: dict, zone_count: int, alerts_today: int, sub_status: str) -> str:
    status = "Active" if user["active"] else "Paused"
    symbols = " | ".join(sorted(user["symbols"]))
    timeframes = " | ".join(sorted(user["timeframes"]))
    models = " | ".join(sorted(user.get("entry_models", [])))
    directions = set(user.get("trade_directions", []))
    direction_text = "Both" if directions == {"long", "short"} else " | ".join(sorted(item.upper() for item in directions))
    return (
        "ICT Crypto Alerts\n\n"
        f"Status: {status}\n"
        f"Pairs: {symbols}\n"
        f"Timeframes: {timeframes}\n"
        f"ICT Models: {models}\n"
        f"Directions: {direction_text}\n"
        f"Subscription: {sub_status}\n\n"
        f"Last scan: {utc_now()}\n"
        f"Active zones: {zone_count}\n"
        f"Alerts today: {alerts_today}"
    )


def build_setup_summary(symbols, patterns, timeframes, entry_models=None, trade_directions=None) -> str:
    symbols_text = ", ".join(sorted(symbols))
    patterns_text = ", ".join(sorted(patterns)) if patterns else "No zone alerts"
    timeframes_text = ", ".join(sorted(timeframes))
    lines = [f"Preferences set: {symbols_text} - {patterns_text} - {timeframes_text}"]
    if entry_models is not None:
        lines.append(f"ICT models: {', '.join(sorted(entry_models))}")
    if trade_directions is not None:
        directions = set(trade_directions)
        direction_text = "Both" if directions == {"long", "short"} else ", ".join(sorted(item.upper() for item in directions))
        lines.append(f"Directions: {direction_text}")
    lines += ["", "Alerts will arrive automatically."]
    return "\n".join(lines)


__all__ = [
    "build_alert_message",
    "build_chart_caption",
    "build_dashboard_message",
    "build_payment_message",
    "build_setup_summary",
    "build_strategy_alert_text",
    "utc_now",
]
