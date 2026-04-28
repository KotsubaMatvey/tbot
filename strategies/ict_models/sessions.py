from __future__ import annotations

from datetime import datetime, time
from zoneinfo import ZoneInfo

NY_TZ = "America/New_York"
LONDON_OPEN = "02:00-05:00"
NY_OPEN = "07:00-10:00"
SILVER_BULLET_AM = "10:00-11:00"
SILVER_BULLET_PM = "14:00-15:00"
LONDON_TO_NY = "02:00-11:00"


def in_ny_windows(timestamp: int, windows: str | list[str] | tuple[str, ...]) -> bool:
    value = datetime.fromtimestamp(timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(ZoneInfo(NY_TZ)).time()
    chunks = [windows] if isinstance(windows, str) else list(windows)
    return any(_in_window(value, chunk) for chunk in chunks)


def ny_time_text(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp / 1000, tz=ZoneInfo("UTC")).astimezone(ZoneInfo(NY_TZ)).strftime("%Y-%m-%d %H:%M")


def _in_window(value: time, window: str) -> bool:
    start_text, end_text = window.split("-", 1)
    start = _parse_time(start_text)
    end = _parse_time(end_text)
    return start <= value <= end


def _parse_time(value: str) -> time:
    hour, minute = value.split(":", 1)
    return time(int(hour), int(minute))


__all__ = [
    "LONDON_OPEN",
    "LONDON_TO_NY",
    "NY_OPEN",
    "SILVER_BULLET_AM",
    "SILVER_BULLET_PM",
    "in_ny_windows",
    "ny_time_text",
]
