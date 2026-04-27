from __future__ import annotations

from .entry_model_1_legacy import detect_entry_model_1 as detect_legacy_model_1
from .entry_model_2_legacy import detect_entry_model_2 as detect_legacy_model_2
from .entry_model_3_legacy import detect_entry_model_3 as detect_legacy_model_3

__all__ = [
    "detect_legacy_model_1",
    "detect_legacy_model_2",
    "detect_legacy_model_3",
]
