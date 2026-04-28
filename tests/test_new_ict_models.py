from __future__ import annotations

import unittest
from datetime import datetime, timezone

from backtesting.run_ict_models import _decision_score, _evaluate
from backtesting.run_ict_batch import build_run_args
from backtesting.score_threshold_report import summarize_thresholds
from market_primitives.smt import detect_smt
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

        self.assertTrue(detect_ifvg_retest("BTCUSDT", "5m", body, config={"ifvg_require_displacement": False}))
        self.assertEqual(detect_ifvg_retest("BTCUSDT", "5m", wick_only), [])
        setup = detect_ifvg_retest("BTCUSDT", "5m", body, config={"ifvg_require_displacement": False})[0]
        self.assertEqual(setup.metadata["entry_mode"], "edge")
        self.assertEqual(setup.timestamp, 4)
        self.assertEqual(setup.metadata["entry_time"], 5)

    def test_ifvg_retest_default_requires_displacement(self) -> None:
        candles = [
            candle(1, 105, 106, 104, 105),
            candle(2, 104, 105, 101, 103),
            candle(3, 98, 99, 94, 95),
            candle(4, 100, 116, 100, 115),
            candle(5, 106, 107, 103, 105),
            candle(6, 105, 106, 104, 105),
        ]

        setups = detect_ifvg_retest("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertIn(setups[0].metadata["breach_displacement_grade"], {"valid", "strong"})

    def test_same_bar_policies(self) -> None:
        future = [candle(1, 100, 103, 97, 101)]

        conservative = _evaluate("long", 100, 98, 102, future, "conservative")
        optimistic = _evaluate("long", 100, 98, 102, future, "optimistic")
        neutral = _evaluate("long", 100, 98, 102, future, "neutral")

        self.assertFalse(conservative["target_before_invalidation"])
        self.assertTrue(optimistic["target_before_invalidation"])
        self.assertTrue(neutral["same_bar_ambiguous"])
        self.assertFalse(conservative["hit_1r_before_invalidation"])

    def test_crypto_smt_detects_primary_lower_low_vs_secondary_higher_low(self) -> None:
        btc = [
            candle(1, 102, 103, 101, 102),
            candle(2, 102, 103, 100, 101),
            candle(3, 101, 102, 99, 101),
            candle(4, 101, 104, 100, 103),
            candle(5, 103, 104, 101, 102),
            candle(6, 102, 103, 99, 100),
            candle(7, 100, 101, 97, 99),
            candle(8, 99, 103, 98, 102),
            candle(9, 102, 104, 101, 103),
            candle(10, 103, 104, 102, 103),
        ]
        eth = [
            candle(1, 52, 53, 51, 52),
            candle(2, 52, 53, 50, 51),
            candle(3, 51, 52, 49, 51),
            candle(4, 51, 54, 50, 53),
            candle(5, 53, 54, 52, 53),
            candle(6, 53, 54, 51, 52),
            candle(7, 52, 53, 50, 52),
            candle(8, 52, 54, 51, 53),
            candle(9, 53, 55, 52, 54),
            candle(10, 54, 55, 53, 54),
        ]

        divergences = detect_smt(btc, eth, "BTCUSDT", "ETHUSDT", "5m", min_correlation=-1)

        self.assertTrue(any(item.direction == "bullish" for item in divergences))

    def test_decision_score_records_penalties_without_blocking(self) -> None:
        score = _decision_score(
            "long",
            "ict2022_mss_fvg",
            {
                "htf_mode": "strict",
                "htf_bias": "bearish",
                "htf_location": "equilibrium",
                "displacement_grade": "weak",
                "has_smt_confirmation": False,
                "session_filter": "off",
            },
            1.5,
        )

        self.assertEqual(score["score_bucket"], "low")
        self.assertIn("against_htf_flow", score["no_trade_reasons"])
        self.assertIn("equilibrium", score["no_trade_reasons"])
        self.assertIn("target_rr_below_2", score["no_trade_reasons"])

    def test_score_threshold_report_filters_by_decision_score(self) -> None:
        report = summarize_thresholds(
            [
                {
                    "model": "ifvg_retest",
                    "decision_score": "75",
                    "activated_trade": "True",
                    "target_before_invalidation": "True",
                    "target_distance_r": "2.5",
                    "invalidated": "False",
                    "mfe_r": "3",
                    "no_trade_reasons": "",
                },
                {
                    "model": "ifvg_retest",
                    "decision_score": "45",
                    "activated_trade": "True",
                    "target_before_invalidation": "False",
                    "target_distance_r": "1.5",
                    "invalidated": "True",
                    "mfe_r": "0.5",
                    "no_trade_reasons": "target_rr_below_2",
                },
            ],
            [0, 70],
        )

        all_rows = [row for row in report if row["scope"] == "all"]
        self.assertEqual(all_rows[0]["count"], 2)
        self.assertEqual(all_rows[1]["count"], 1)
        self.assertEqual(all_rows[1]["expectancy"], 2.5)

    def test_ict_batch_builds_repeatable_run_args(self) -> None:
        args = build_run_args(
            {
                "data_dir": "data/history_2025-05-01_2025-06-30",
                "symbols": ["BTCUSDT", "ETHUSDT"],
                "models": ["turtle_soup", "ifvg_retest"],
                "context_mode": "aligned_only",
                "smt_pairs": ["BTCUSDT:ETHUSDT"],
                "forward_bars": 20,
            },
            {
                "symbols": ["BTCUSDT"],
                "timeframes": ["30m"],
                "out_dir": "backtest_results/example",
            },
        )

        self.assertIn("--data-dir", args)
        self.assertIn("data/history_2025-05-01_2025-06-30", args)
        self.assertIn("--symbols", args)
        self.assertIn("BTCUSDT", args)
        self.assertNotIn("ETHUSDT", args[args.index("--symbols") + 1 : args.index("--timeframes")])
        self.assertIn("--smt-pairs", args)
        self.assertIn("BTCUSDT:ETHUSDT", args)

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
