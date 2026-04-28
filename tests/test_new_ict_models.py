from __future__ import annotations

import unittest
from datetime import datetime, timezone

from backtesting.run_ict_models import _decision_score, _evaluate
from backtesting.run_ict_batch import build_run_args
from backtesting.score_threshold_report import summarize_thresholds
from backtesting.grid_filter_analysis import summarize_grid
from keyboards import MENU_ACTIONS, main_menu
from formatters import build_setup_summary
from handlers.common import user_ready
from handlers.trading import trading_keyboard
from market_primitives.smt import detect_smt
from presentation.alert_builders import from_entry_setup
from scanner.engine import STRATEGY_PATTERNS
from strategies.htf_context import HTFBias, HTFContext, HTFDealingRange, HTFObjective, HTFZone
from strategies.ict_models import registry
from strategies.ict_models.lifecycle import classify_setup_lifecycle
from strategies.ict_models.ifvg_retest import detect_setups as detect_ifvg_retest
from strategies.ict_models.model_filters import passes_model_filter, setup_filter_event
from strategies.ict_models.silver_bullet import detect_setups as detect_silver_bullet
from strategies.ict_models.turtle_soup import detect_setups as detect_turtle_soup
from strategies.pre_model_filter import evaluate_pre_model_filter
from strategies.types import EntrySetup, PrimitiveSnapshot, StrategyContext, default_components
from visuals import _CANDLE_COUNT, _datetime_format, _entry_index


def candle(ts: int, open_: float, high: float, low: float, close: float) -> dict[str, float | int]:
    return {"time": ts, "open": open_, "high": high, "low": low, "close": close, "volume": 100.0}


def ts(year: int, month: int, day: int, hour: int, minute: int) -> int:
    return int(datetime(year, month, day, hour, minute, tzinfo=timezone.utc).timestamp() * 1000)


class NewICTModelTests(unittest.TestCase):
    def test_registry_defaults_are_new_models(self) -> None:
        self.assertEqual(registry.DEFAULT_MODELS, ["turtle_soup", "silver_bullet", "ifvg_retest"])
        self.assertEqual([item.name for item in registry.resolve_models(None)], registry.DEFAULT_MODELS)
        self.assertIn("rejection_block", [item.name for item in registry.get_live_models()])
        self.assertIn("mitigation_block", STRATEGY_PATTERNS)
        with self.assertRaises(ValueError):
            registry.resolve_models(["model1"])
        self.assertEqual(registry.resolve_models(["model1"], include_legacy=True)[0].name, "legacy_model1")

    def test_main_menu_exposes_trading_button(self) -> None:
        labels = [[button.text for button in row] for row in main_menu().keyboard]

        self.assertTrue(any(MENU_ACTIONS["trading"] in row for row in labels))

    def test_trading_keyboard_uses_strategy_patterns(self) -> None:
        markup = trading_keyboard({"turtle_soup"})
        buttons = [button for row in markup.inline_keyboard for button in row]

        self.assertEqual(buttons[0].callback_data, "trade_model_turtle_soup")
        self.assertIn("OK", buttons[0].text)
        self.assertEqual(buttons[-1].callback_data, "trade_model_CONFIRM")

    def test_settings_summary_excludes_trading_choices(self) -> None:
        summary = build_setup_summary({"BTCUSDT"}, {"FVG"}, {"5m"})

        self.assertIn("BTCUSDT", summary)
        self.assertNotIn("ICT models", summary)
        self.assertNotIn("Directions", summary)

    def test_user_can_run_strategy_only_without_zone_alerts(self) -> None:
        user = {
            "setup_done": True,
            "symbols": {"BTCUSDT"},
            "patterns": set(),
            "timeframes": {"5m"},
            "entry_models": {"turtle_soup"},
            "trade_directions": {"long"},
        }
        summary = build_setup_summary(user["symbols"], user["patterns"], user["timeframes"])

        self.assertTrue(user_ready(user))
        self.assertIn("No zone alerts", summary)

    def test_chart_window_uses_more_context_with_readable_dates(self) -> None:
        self.assertGreaterEqual(_CANDLE_COUNT["5m"], 120)
        self.assertEqual(_datetime_format("1h"), "%m-%d %H:%M")
        self.assertEqual(_datetime_format("1d"), "%Y-%m-%d")

    def test_chart_entry_marker_uses_entry_time(self) -> None:
        import pandas as pd

        frame = pd.DataFrame(
            [
                {"Open": 100, "High": 101, "Low": 99, "Close": 100, "Volume": 1},
                {"Open": 101, "High": 102, "Low": 100, "Close": 101, "Volume": 1},
            ],
            index=pd.to_datetime([1, 2], unit="ms", utc=True),
        )
        alert = EntrySetup(
            model_name="turtle_soup",
            direction="long",
            symbol="BTCUSDT",
            timeframe="5m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=99,
            invalidation=99,
            target_hint=103,
            sweep_level=None,
            structure_level=None,
            context_timeframe="1h",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={"entry_time": 2},
        )

        self.assertEqual(_entry_index(frame, from_entry_setup(alert)), 1)

    def test_pre_model_filter_allows_only_htf_aligned_direction(self) -> None:
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", [candle(1, 100, 101, 99, 100)]),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bullish", 0.8, "test"),
                zone=HTFZone("OB", "bullish", 99, 101, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(90, 110, 100, "discount"),
                objective=HTFObjective("up", 120, "swing_high", "test", objective_unreached=True),
                inside_zone=True,
                approaching_zone=False,
                allows_long=True,
                allows_short=False,
                score_modifier=0,
                reason="test",
            ),
        )

        decision = evaluate_pre_model_filter(context, {"context_mode": "strict"})

        self.assertTrue(decision.passed)
        self.assertEqual(decision.allowed_directions, {"long"})
        self.assertEqual(decision.metadata["pre_model_allowed_directions"], "long")

    def test_pre_model_filter_blocks_neutral_equilibrium(self) -> None:
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", [candle(1, 100, 101, 99, 100)]),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("neutral", 0.1, "test"),
                zone=HTFZone("None", "neutral", None, None, None, 0, "test"),
                dealing_range=HTFDealingRange(90, 110, 100, "equilibrium"),
                objective=HTFObjective("none", None, "none", "test"),
                inside_zone=False,
                approaching_zone=False,
                allows_long=False,
                allows_short=False,
                score_modifier=0,
                reason="test",
            ),
        )

        decision = evaluate_pre_model_filter(context, {"context_mode": "strict"})

        self.assertFalse(decision.passed)
        self.assertIn("neutral_htf_bias", decision.reasons)
        self.assertIn("equilibrium", decision.reasons)

    def test_pre_model_filter_requires_htf_poi_by_default(self) -> None:
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", [candle(1, 100, 101, 99, 100)]),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bullish", 0.8, "test"),
                zone=HTFZone("OB", "bullish", 80, 85, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(70, 110, 90, "discount"),
                objective=HTFObjective("up", 120, "swing_high", "test", objective_unreached=True),
                inside_zone=False,
                approaching_zone=False,
                allows_long=True,
                allows_short=False,
                score_modifier=0,
                reason="test",
            ),
        )

        blocked = evaluate_pre_model_filter(context, {"context_mode": "strict"})
        allowed = evaluate_pre_model_filter(context, {"context_mode": "strict", "pre_model_require_htf_poi": False})

        self.assertFalse(blocked.passed)
        self.assertIn("not_in_htf_poi", blocked.reasons)
        self.assertTrue(allowed.passed)

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

    def test_score_threshold_report_applies_model_filters(self) -> None:
        report = summarize_thresholds(
            [
                {
                    "model": "turtle_soup",
                    "decision_score": "60",
                    "target_distance_r": "3",
                    "activated_trade": "True",
                    "target_before_invalidation": "True",
                    "invalidated": "False",
                    "mfe_r": "3",
                    "no_trade_reasons": "",
                },
                {
                    "model": "turtle_soup",
                    "decision_score": "60",
                    "target_distance_r": "1",
                    "activated_trade": "True",
                    "target_before_invalidation": "False",
                    "invalidated": "True",
                    "mfe_r": "0.5",
                    "no_trade_reasons": "target_rr_below_2",
                },
            ],
            [50],
            model_filters={"turtle_soup": {"min_target_distance_r": 2.0}},
        )

        filtered = next(row for row in report if row["scope"] == "filtered_model")
        self.assertEqual(filtered["count"], 1)
        self.assertEqual(filtered["filtered_out"], 1)
        self.assertEqual(filtered["expectancy"], 3.0)

    def test_filter_grid_summarizes_candidate_rules(self) -> None:
        report = summarize_grid(
            [
                {
                    "model": "ifvg_retest",
                    "decision_score": "75",
                    "target_distance_r": "3",
                    "has_smt_confirmation": "True",
                    "session_window": "10:00-11:00",
                    "displacement_grade": "valid",
                    "htf_location": "discount",
                    "target_before_invalidation": "True",
                    "invalidated": "False",
                    "hit_2r_before_invalidation": "True",
                    "mfe_r": "3",
                },
                {
                    "model": "ifvg_retest",
                    "decision_score": "40",
                    "target_distance_r": "1",
                    "has_smt_confirmation": "False",
                    "session_window": "",
                    "displacement_grade": "weak",
                    "htf_location": "equilibrium",
                    "target_before_invalidation": "False",
                    "invalidated": "True",
                    "hit_2r_before_invalidation": "False",
                    "mfe_r": "0.2",
                    "no_trade_reasons": "equilibrium;target_rr_below_2",
                },
            ],
            min_count=1,
        )

        self.assertTrue(report)
        self.assertEqual(report[0]["rank"], 1)
        self.assertGreaterEqual(float(report[0]["expectancy"]), 1.0)

    def test_live_model_filter_event_uses_setup_rr(self) -> None:
        setup = EntrySetup(
            model_name="breaker_block",
            direction="long",
            symbol="BTCUSDT",
            timeframe="1h",
            status="triggered",
            entry_low=100,
            entry_high=100,
            entry_price=100,
            stop_loss=99,
            invalidation=99,
            target_hint=104,
            sweep_level=None,
            structure_level=None,
            context_timeframe="4h",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={"displacement_grade": "valid"},
        )

        event = setup_filter_event(setup)

        self.assertTrue(passes_model_filter(event, {"min_target_distance_r": 3, "allowed_displacement_grades": ["valid"]}))
        self.assertFalse(passes_model_filter(event, {"min_target_distance_r": 5}))

    def test_lifecycle_marks_pending_filled_and_target(self) -> None:
        setup = EntrySetup(
            model_name="ict2022_mss_fvg",
            direction="long",
            symbol="BTCUSDT",
            timeframe="5m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=98,
            invalidation=98,
            target_hint=105,
            sweep_level=None,
            structure_level=None,
            context_timeframe="1h",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={},
        )

        pending = classify_setup_lifecycle(setup, [candle(1, 102, 103, 101.5, 102)])
        filled = classify_setup_lifecycle(setup, [candle(1, 102, 103, 101.5, 102), candle(2, 102, 102, 100, 101)])
        target = classify_setup_lifecycle(
            setup,
            [candle(1, 102, 103, 101.5, 102), candle(2, 102, 102, 100, 101), candle(3, 101, 106, 100, 105)],
        )

        self.assertEqual(pending["status"], "limit_pending")
        self.assertEqual(filled["status"], "entry_filled")
        self.assertEqual(target["status"], "tp_hit")

    def test_ict_batch_builds_repeatable_run_args(self) -> None:
        args = build_run_args(
            {
                "data_dir": "data/history_2025-05-01_2025-10-31",
                "symbols": ["BTCUSDT", "ETHUSDT"],
                "models": ["turtle_soup", "ifvg_retest"],
                "context_mode": "aligned_only",
                "smt_pairs": ["BTCUSDT:ETHUSDT"],
                "forward_bars": 20,
                "pre_model_require_smt": True,
                "pre_model_filter": False,
                "pre_model_require_htf_poi": False,
            },
            {
                "symbols": ["BTCUSDT"],
                "timeframes": ["30m"],
                "out_dir": "backtest_results/example",
            },
        )

        self.assertIn("--data-dir", args)
        self.assertIn("data/history_2025-05-01_2025-10-31", args)
        self.assertIn("--symbols", args)
        self.assertIn("BTCUSDT", args)
        self.assertNotIn("ETHUSDT", args[args.index("--symbols") + 1 : args.index("--timeframes")])
        self.assertIn("--smt-pairs", args)
        self.assertIn("BTCUSDT:ETHUSDT", args)
        self.assertIn("--pre-model-require-smt", args)
        self.assertIn("--no-pre-model-filter", args)
        self.assertIn("--no-pre-model-require-htf-poi", args)

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
