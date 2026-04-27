from __future__ import annotations

from typing import Any

ENABLED_BY_DEFAULT = False
RESEARCH_ONLY = True


def detect_setups(
    symbol: str,
    timeframe: str,
    candles: list[dict[str, float | int]],
    context: object | None = None,
    config: dict[str, Any] | None = None,
) -> list:
    # Research-only skeleton. Kept disabled until a stricter definition is tested.
    return []


__all__ = ["ENABLED_BY_DEFAULT", "RESEARCH_ONLY", "detect_setups"]
