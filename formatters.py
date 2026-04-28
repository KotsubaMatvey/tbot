"""Backward-compatible formatting exports."""
from presentation.formatters import (
    build_alert_message,
    build_chart_caption,
    build_dashboard_message,
    build_payment_message,
    build_setup_summary,
    build_strategy_alert_text,
    utc_now,
)

__all__ = [
    "build_alert_message",
    "build_chart_caption",
    "build_dashboard_message",
    "build_payment_message",
    "build_setup_summary",
    "build_strategy_alert_text",
    "utc_now",
]
