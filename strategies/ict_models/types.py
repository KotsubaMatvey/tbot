from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from strategies.types import EntrySetup

CandleDict = dict[str, float | int]
ICTDetector = Callable[[str, str, list[CandleDict], object | None, dict[str, Any] | None], list[EntrySetup]]


@dataclass(frozen=True, slots=True)
class ICTModelSpec:
    name: str
    display_name: str
    detector: ICTDetector
    model_family: str = "ict"
    research_only: bool = False
    legacy: bool = False


__all__ = ["CandleDict", "ICTDetector", "ICTModelSpec"]
