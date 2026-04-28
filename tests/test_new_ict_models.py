from __future__ import annotations

import unittest
from datetime import datetime, timezone

from backtesting.run_ict_models import _evaluate
from strategies.ict_models import registry
from strategies.ict_models.ifvg_retest import detect_setups as detect_ifvg_retest
from strategies.ict_models.silver_bullet import detect_setups as detect_silver_bullet
from strategies.ict_models.turtle_soup import detect_setups as detect_turtle_soup


def candle(ts: int, open_: float, high: float, low: float, close: float) -> dict[str, float | int]:
    return {"time": ts, "open": open_, "high": high, "low": low, "close": close, "volume": 100.0}


def ts(year: int, month: int, day: int, hour: int, minute: int) -> int:
    return int(datetime(year, month, day, hour, minute, tzinfo=timezone.utc).timestamp() * 1000)


class NewICTModelTests(unittest.TestCase):
    def test_registry_defaults_are_new_models(self) -> None:
        self.assertEqual(registry.DEFAULT_MODELS, ["turtle_soup", "silver_bullet", "ifvg_retest"])
        self.assertEqual([item.name for item in registry.resolve_models(None)], registry.DEFAULT_MODELS)
        with self.assertRaises(ValueError):
            registry.resolve_models(["model1"])
        self.assertEqual(registry.resolve_models(["model1"], include_legacy=True)[0].name, "legacy_model1")

    def test_turtle_soup_long_sweep_close_back(self) -> None:
        candles = [
            candle(1, 101, 102, 100, 101),
            candle(2, 101, 102, 98, 99),
            candle(3, 99, 103, 99, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 104, 102, 103),
            candle(6, 103, 104, 97, 99),
            candle(7, 99, 100, 98, 99),
        ]

        setups = detect_turtle_soup("BTCUSDT", "5m", candles, config={"turtle_min_swing_age": 1})

        self.assertTrue(any(item.direction == "long" for item in setups))
        setup = next(item for item in setups if item.direction == "long")
        self.assertLess(setup.stop_loss or 0, setup.metadata["sweep_extreme"])

    def test_turtle_soup_body_close_beyond_level_is_not_sweep(self) -> None:
        candles = [
            candle(1, 101, 102, 100, 101),
            candle(2, 101, 102, 98, 99),
            candle(3, 99, 103, 99, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 104, 102, 103),
            candle(6, 103, 104, 97, 97.5),
            candle(7, 99, 100, 98, 99),
        ]

        self.assertEqual(detect_turtle_soup("BTCUSDT", "5m", candles, config={"turtle_min_swing_age": 1}), [])

    def test_turtle_soup_quality_filter_rejects_small_wick(self) -> None:
        candles = [
            candle(1, 101, 102, 100, 101),
            candle(2, 101, 102, 98, 99),
            candle(3, 99, 103, 99, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 104, 102, 103),
            candle(6, 103, 104, 97, 99),
            candle(7, 99, 100, 98, 99),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "5m",
            candles,
            config={"turtle_min_swing_age": 1, "turtle_soup_min_wick_fraction": 0.8},
        )

        self.assertEqual(setups, [])

    def test_silver_bullet_accepts_fvg_inside_ny_window(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 14, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 14, 10), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 14, 15), 105, 106, 104, 105),
        ]

        setups = detect_silver_bullet("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["session_window"], "10:00-11:00")
        self.assertEqual(setups[0].timestamp, ts(2026, 4, 20, 14, 5))
        self.assertEqual(setups[0].metadata["entry_time"], ts(2026, 4, 20, 14, 10))

    def test_silver_bullet_ignores_fvg_outside_window(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 12, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 12, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 12, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 12, 10), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 12, 15), 105, 106, 104, 105),
        ]

        self.assertEqual(detect_silver_bullet("BTCUSDT", "5m", candles), [])

    def test_silver_bullet_rejects_late_retest(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 14, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 15, 15), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 15, 20), 105, 106, 104, 105),
        ]

        self.assertEqual(detect_silver_bullet("BTCUSDT", "5m", candles), [])

    def test_ifvg_retest_body_breach_accepts_wick_only_rejects(self) -> None:
        body = [
            candle(1, 105, 106, 105, 105.5),
            candle(2, 104, 105, 101, 103),
            candle(3, 98, 99, 94, 95),
            candle(4, 104, 108, 103, 106),
            candle(5, 106, 106, 104, 105),
            candle(6, 105, 106, 104, 105),
        ]
        wick_only = [
            candle(1, 105, 106, 105, 105.5),
            candle(2, 104, 105, 101, 103),
            candle(3, 98, 99, 94, 95),
            candle(4, 104, 108, 103, 104),
            candle(5, 106, 106, 104, 105),
            candle(6, 105, 106, 104, 105),
        ]

        self.assertTrue(detect_ifvg_retest("BTCUSDT", "5m", body))
        self.assertEqual(detect_ifvg_retest("BTCUSDT", "5m", wick_only), [])
        self.assertEqual(detect_ifvg_retest("BTCUSDT", "5m", body)[0].metadata["entry_mode"], "edge")
        self.assertEqual(detect_ifvg_retest("BTCUSDT", "5m", body)[0].timestamp, 4)
        self.assertEqual(detect_ifvg_retest("BTCUSDT", "5m", body)[0].metadata["entry_time"], 5)

    def test_same_bar_policies(self) -> None:
        future = [candle(1, 100, 103, 97, 101)]

        conservative = _evaluate("long", 100, 98, 102, future, "conservative")
        optimistic = _evaluate("long", 100, 98, 102, future, "optimistic")
        neutral = _evaluate("long", 100, 98, 102, future, "neutral")

        self.assertFalse(conservative["target_before_invalidation"])
        self.assertTrue(optimistic["target_before_invalidation"])
        self.assertTrue(neutral["same_bar_ambiguous"])
        self.assertFalse(conservative["hit_1r_before_invalidation"])

    def test_r_hits_are_measured_from_entry_time(self) -> None:
        future = [
            candle(2, 100, 104, 99, 103),
            candle(3, 100, 102.5, 99, 102),
        ]

        outcome = _evaluate("long", 100, 98, 104, future, "conservative", entry_time=3)

        self.assertTrue(outcome["hit_1r_before_invalidation"])
        self.assertFalse(outcome["hit_2r_before_invalidation"])
        self.assertEqual(outcome["time_to_entry_bars"], 2)


if __name__ == "__main__":
    unittest.main()
