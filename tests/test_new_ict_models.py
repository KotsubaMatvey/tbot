from __future__ import annotations

import unittest
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from backtesting.run_ict_models import EVENT_FIELDS, _candles_until, _context_aligned, _date_scan_bounds, _decision_score, _evaluate, _execution_costs, _models_need_accumulated_primary, _scan_session_window_matches, _timestamp_in_date_range, _with_execution_costs
from backtesting.run_ict_batch import build_run_args
from backtesting.score_threshold_report import summarize_thresholds
from backtesting.grid_filter_analysis import summarize_grid
from backtesting.walk_forward_report import summarize_walk_forward
from backtesting.data_coverage_report import summarize_coverage
from backtesting.forward_log_report import summarize_forward_logs
from database import DEFAULT_ENTRY_MODELS, _normalize_entry_models
from keyboards import MENU_ACTIONS, main_menu
from formatters import build_setup_summary, build_strategy_alert_text
from alerts import _digest_alert_detail, _timeframe_enabled_for_user
from handlers.common import user_ready
from handlers.trading import trading_keyboard
from market_primitives.common import BreakerBlock, FairValueGap, LiquiditySweep, OrderBlock, StructureBreak
from market_primitives.smt import detect_smt
from presentation.alert_builders import from_entry_setup
from scanner.engine import STRATEGY_PATTERNS, _detector_config, _model_enabled
from strategies.htf_context import HTFBias, HTFContext, HTFDealingRange, HTFObjective, HTFZone
from strategies.ict_models import registry
from strategies.ict_models.breaker_block import detect_setups as detect_breaker_block
from strategies.ict_models.lifecycle import classify_setup_lifecycle
from strategies.ict_models.ict2022_mss_fvg import detect_setups as detect_ict2022_mss_fvg
from strategies.ict_models.ifvg_retest import detect_setups as detect_ifvg_retest
from strategies.ict_models.model_filters import passes_model_filter, setup_filter_event
from strategies.ict_models.reclaimed_ob import detect_setups as detect_reclaimed_ob
from strategies.ict_models.rejection_block import detect_setups as detect_rejection_block
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
        self.assertEqual(registry.DEFAULT_MODELS, ["silver_bullet", "ifvg_retest", "ict2022_mss_fvg", "turtle_soup"])
        self.assertEqual(registry.SELECTABLE_MODELS, [*registry.DEFAULT_MODELS, "breaker_block", "reclaimed_ob"])
        self.assertEqual([item.name for item in registry.resolve_models(None)], registry.DEFAULT_MODELS)
        self.assertNotIn("rejection_block", [item.name for item in registry.get_live_models()])
        self.assertEqual(STRATEGY_PATTERNS, registry.SELECTABLE_MODELS)
        self.assertNotIn("mitigation_block", STRATEGY_PATTERNS)
        with self.assertRaises(ValueError):
            registry.resolve_models(["model1"])
        self.assertEqual(registry.resolve_models(["model1"], include_legacy=True)[0].name, "legacy_model1")

    def test_database_entry_model_defaults_match_live_models(self) -> None:
        self.assertEqual(DEFAULT_ENTRY_MODELS, registry.DEFAULT_MODELS)
        self.assertEqual(_normalize_entry_models({"turtle_soup", "ifvg_retest", "mitigation_block"}), {"turtle_soup", "ifvg_retest"})
        self.assertEqual(_normalize_entry_models({"model1"}), set(DEFAULT_ENTRY_MODELS))

    def test_live_scanner_skips_disabled_model_detectors(self) -> None:
        self.assertFalse(_model_enabled("turtle_soup", {"turtle_soup": {"enabled": False}}))
        self.assertTrue(_model_enabled("ifvg_retest", {"ifvg_retest": {"min_target_distance_r": 3}}))

    def test_live_scanner_passes_model_rules_to_detector_config(self) -> None:
        config = _detector_config(
            {"context_mode": "strict", "htf_mode": "strict"},
            {"silver_bullet_windows": ["02:30-02:30", "10:45-11:00"]},
        )

        self.assertEqual(config["context_mode"], "strict")
        self.assertEqual(config["silver_bullet_windows"], ["02:30-02:30", "10:45-11:00"])

    def test_live_silver_bullet_uses_notebooklm_am_pm_windows(self) -> None:
        config = json.loads(Path("configs/live_model_filters_2025.json").read_text(encoding="utf-8"))
        rules = config["model_filters"]["silver_bullet"]

        self.assertEqual(rules["silver_bullet_windows"], ["10:00-11:00", "14:00-15:00"])
        self.assertEqual(rules["allowed_symbols"], ["BTCUSDT"])
        self.assertEqual(rules["silver_bullet_max_retest_bars"], 1)
        self.assertEqual(rules["silver_bullet_min_retest_depth"], 0.15)
        self.assertTrue(rules["require_htf_draw"])
        self.assertTrue(rules["require_bias_alignment"])
        self.assertTrue(rules["require_premium_discount_alignment"])

    def test_live_enabled_models_require_htf_quality_gates(self) -> None:
        config = json.loads(Path("configs/live_model_filters_2025.json").read_text(encoding="utf-8"))
        filters = config["model_filters"]

        for model_name in ("silver_bullet", "ifvg_retest", "breaker_block", "reclaimed_ob"):
            rules = filters[model_name]
            self.assertTrue(rules["enabled"])
            self.assertEqual(rules["allowed_symbols"], ["BTCUSDT"])
            self.assertTrue(rules["require_htf_draw"])
            self.assertTrue(rules["require_bias_alignment"])
            self.assertTrue(rules["require_premium_discount_alignment"])
            self.assertEqual(rules["allowed_htf_context_alignments"], ["aligned"])

    def test_backtest_exports_live_filter_htf_fields(self) -> None:
        for field in ("htf_draw_direction", "htf_objective_level", "htf_objective_unreached"):
            self.assertIn(field, EVENT_FIELDS)

    def test_live_turtle_soup_is_prepared_session_fallback_but_disabled(self) -> None:
        config = json.loads(Path("configs/live_model_filters_2025.json").read_text(encoding="utf-8"))
        rules = config["model_filters"]["turtle_soup"]

        self.assertFalse(rules["enabled"])
        self.assertEqual(rules["allowed_timeframes"], ["5m", "15m"])
        self.assertEqual(rules["target_mode"], "dol_hierarchy")
        self.assertTrue(rules["turtle_soup_require_killzone"])
        self.assertEqual(rules["turtle_soup_session_windows"], ["02:00-05:00", "07:00-10:00", "13:30-16:00"])
        self.assertFalse(rules.get("require_smt", False))

    def test_live_ict2022_is_prepared_session_fallback_but_disabled(self) -> None:
        config = json.loads(Path("configs/live_model_filters_2025.json").read_text(encoding="utf-8"))
        rules = config["model_filters"]["ict2022_mss_fvg"]

        self.assertFalse(rules["enabled"])
        self.assertEqual(rules["allowed_timeframes"], ["5m", "15m"])
        self.assertTrue(rules["ict2022_require_killzone"])
        self.assertEqual(rules["ict2022_session_windows"], ["02:00-05:00", "07:00-10:00", "13:30-16:00"])
        self.assertFalse(rules["ict2022_retest_must_occur_within_session"])
        self.assertEqual(rules["ict2022_max_fvg_retest_bars"], 3)
        self.assertFalse(rules["ict2022_require_strong_displacement"])

    def test_backtest_scan_session_window_can_include_next_bar(self) -> None:
        candles = [
            candle(ts(2025, 5, 1, 6, 15), 100, 101, 99, 100),
            candle(ts(2025, 5, 1, 6, 30), 100, 101, 99, 100),
            candle(ts(2025, 5, 1, 6, 45), 100, 101, 99, 100),
        ]

        self.assertTrue(_scan_session_window_matches(candles, 1, ["02:30-02:30"], 0))
        self.assertFalse(_scan_session_window_matches(candles, 2, ["02:30-02:30"], 0))
        self.assertTrue(_scan_session_window_matches(candles, 2, ["02:30-02:30"], 1))

    def test_backtest_date_window_filters_scan_timestamps(self) -> None:
        self.assertFalse(_timestamp_in_date_range(ts(2025, 4, 30, 23, 59), "2025-05-01", "2025-05-31"))
        self.assertTrue(_timestamp_in_date_range(ts(2025, 5, 31, 23, 59), "2025-05-01", "2025-05-31"))
        self.assertFalse(_timestamp_in_date_range(ts(2025, 6, 1, 0, 0), "2025-05-01", "2025-05-31"))

    def test_backtest_date_window_limits_scan_bounds(self) -> None:
        candles = [
            candle(ts(2025, 4, 30, 23, 45), 100, 101, 99, 100),
            candle(ts(2025, 5, 1, 0, 0), 100, 101, 99, 100),
            candle(ts(2025, 5, 31, 23, 45), 100, 101, 99, 100),
            candle(ts(2025, 6, 1, 0, 0), 100, 101, 99, 100),
        ]

        self.assertEqual(_date_scan_bounds(candles, 0, "2025-05-01", "2025-05-31"), (1, 3))
        self.assertEqual(_date_scan_bounds(candles, 2, "2025-05-01", "2025-05-31"), (2, 3))

    def test_silver_bullet_backtest_can_skip_accumulated_primary(self) -> None:
        self.assertFalse(_models_need_accumulated_primary([SimpleNamespace(name="silver_bullet")]))
        self.assertTrue(_models_need_accumulated_primary([SimpleNamespace(name="silver_bullet"), SimpleNamespace(name="ifvg_retest")]))

    def test_strategy_alerts_ignore_user_zone_timeframes(self) -> None:
        strategy = EntrySetup(
            model_name="ifvg_retest",
            direction="long",
            symbol="BTCUSDT",
            timeframe="1m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=99,
            invalidation=99,
            target_hint=103,
            sweep_level=None,
            structure_level=None,
            context_timeframe="15m",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={},
        )
        primitive = from_entry_setup(strategy)
        primitive.alert_kind = "primitive"
        primitive.pattern = "FVG"
        user = {"timeframes": {"5m"}}

        self.assertTrue(_timeframe_enabled_for_user(from_entry_setup(strategy), "1m", user))
        self.assertFalse(_timeframe_enabled_for_user(primitive, "1m", user))

    def test_strategy_alert_text_includes_risk_plan(self) -> None:
        setup = EntrySetup(
            model_name="ifvg_retest",
            direction="long",
            symbol="BTCUSDT",
            timeframe="1m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=99,
            invalidation=99,
            target_hint=104,
            sweep_level=None,
            structure_level=None,
            context_timeframe="15m",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={
                "htf_bias": "bullish",
                "htf_location": "discount",
                "htf_draw_direction": "up",
                "htf_objective_type": "swing_high",
                "htf_objective_level": 104,
                "htf_zone_type": "FVG",
                "htf_zone_low": 99,
                "htf_zone_high": 101,
                "tp1_price": 102,
                "tp2_price": 104,
                "rr_to_target": 2.33,
                "stop_model": "ce_fvg",
                "logical_invalidation_model": "ce_fvg",
                "logical_invalidation_price": 100,
            },
        )

        text = build_strategy_alert_text(from_entry_setup(setup))

        self.assertIn("ICT plan: HTF bullish discount -> DOL up swing_high 104.00 -> POI FVG 99.00-101.00 -> LONG entry", text)
        self.assertIn("Status: TRIGGERED | Score: 4/5", text)
        self.assertIn("Risk: ce_fvg | Entry zone: 100.00 - 101.00 | Invalidation: 99.00 | RR 2.33R", text)
        self.assertIn("Targets: TP1", text)
        self.assertIn("Logical invalidation: ce_fvg", text)
        self.assertIn("Reason: test", text)
        self.assertNotIn("\nHTF:", text)

    def test_digest_uses_strategy_summary_when_detail_is_empty(self) -> None:
        setup = EntrySetup(
            model_name="ifvg_retest",
            direction="long",
            symbol="BTCUSDT",
            timeframe="1m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=99,
            invalidation=99,
            target_hint=104,
            sweep_level=None,
            structure_level=None,
            context_timeframe="15m",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={},
        )

        self.assertEqual(_digest_alert_detail(from_entry_setup(setup)), "ifvg_retest LONG | TRIGGERED | 4/5")

    def test_main_menu_exposes_trading_button(self) -> None:
        labels = [[button.text for button in row] for row in main_menu().keyboard]

        self.assertTrue(any(MENU_ACTIONS["trading"] in row for row in labels))

    def test_trading_keyboard_uses_strategy_patterns(self) -> None:
        markup = trading_keyboard({"silver_bullet"})
        buttons = [button for row in markup.inline_keyboard for button in row]

        self.assertEqual(buttons[0].callback_data, "trade_model_silver_bullet")
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
            "entry_models": {"ifvg_retest"},
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

    def test_pre_model_filter_can_allow_aligned_discount_without_poi(self) -> None:
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
                allows_long=False,
                allows_short=False,
                score_modifier=0,
                reason="test",
            ),
        )

        decision = evaluate_pre_model_filter(context, {"context_mode": "strict", "pre_model_require_htf_poi": False})

        self.assertTrue(decision.passed)
        self.assertEqual(decision.allowed_directions, {"long"})

    def test_backtest_context_alignment_can_skip_htf_poi_requirement(self) -> None:
        setup = EntrySetup(
            model_name="silver_bullet",
            direction="long",
            symbol="BTCUSDT",
            timeframe="15m",
            status="triggered",
            entry_low=100,
            entry_high=100,
            entry_price=100,
            stop_loss=99,
            invalidation=99,
            target_hint=102,
            sweep_level=None,
            structure_level=None,
            context_timeframe="1h",
            score=3,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={},
        )
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "15m", [candle(1, 100, 101, 99, 100)]),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bullish", 0.8, "test"),
                zone=HTFZone("OB", "bullish", 80, 85, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(70, 110, 90, "discount"),
                objective=HTFObjective("up", 120, "swing_high", "test", objective_unreached=True),
                inside_zone=False,
                approaching_zone=False,
                allows_long=False,
                allows_short=False,
                score_modifier=0,
                reason="test",
            ),
        )

        self.assertFalse(_context_aligned(setup, context))
        self.assertTrue(_context_aligned(setup, context, require_htf_poi=False))

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
        self.assertEqual(setup.metadata["logical_invalidation_model"], "sweep_extreme")
        self.assertEqual(setup.metadata["logical_invalidation_price"], setup.metadata["sweep_extreme"])

    def test_turtle_soup_can_target_htf_draw_on_liquidity(self) -> None:
        candles = [
            candle(1, 101, 102, 100, 101),
            candle(2, 101, 102, 98, 99),
            candle(3, 99, 103, 99, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 104, 102, 103),
            candle(6, 103, 104, 97, 99),
            candle(7, 99, 100, 98, 99),
        ]
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", candles),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bullish", 0.8, "test"),
                zone=HTFZone("OB", "bullish", 96, 99, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(90, 110, 100, "discount"),
                objective=HTFObjective("up", 110, "swing_high", "test", objective_unreached=True),
                inside_zone=True,
                approaching_zone=False,
                allows_long=True,
                allows_short=False,
                score_modifier=0,
                reason="test",
                draw_direction="up",
            ),
        )

        setups = detect_turtle_soup(
            "BTCUSDT",
            "5m",
            candles,
            context=context,
            config={"turtle_min_swing_age": 1, "target_mode": "dol_hierarchy", "context_mode": "strict"},
        )

        setup = next(item for item in setups if item.direction == "long")
        self.assertEqual(setup.target_hint, 110)
        self.assertEqual(setup.metadata["target_mode"], "dol_hierarchy")
        self.assertEqual(setup.metadata["dol_source"], "swing_high")

    def test_turtle_soup_records_intraday_session_metadata(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 13, 35), 101, 102, 100, 101),
            candle(ts(2026, 4, 20, 13, 40), 101, 102, 98, 99),
            candle(ts(2026, 4, 20, 13, 45), 99, 103, 99, 102),
            candle(ts(2026, 4, 20, 13, 50), 102, 104, 101, 103),
            candle(ts(2026, 4, 20, 13, 55), 103, 104, 102, 103),
            candle(ts(2026, 4, 20, 14, 0), 103, 104, 97, 99),
            candle(ts(2026, 4, 20, 14, 5), 99, 100, 98, 99),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "5m",
            candles,
            config={
                "turtle_min_swing_age": 1,
                "turtle_soup_require_killzone": True,
                "turtle_soup_session_windows": ["10:00-11:00"],
            },
        )

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["session_window"], "10:00-11:00")
        self.assertEqual(setups[0].metadata["session_date"], "2026-04-20")
        self.assertEqual(setups[0].metadata["session_label"], "ny_am")

    def test_turtle_soup_asian_range_reclaim(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 0, 0), 105, 108, 102, 106),
            candle(ts(2026, 4, 20, 2, 0), 106, 110, 101, 107),
            candle(ts(2026, 4, 20, 4, 0), 107, 109, 100, 104),
            candle(ts(2026, 4, 20, 8, 0), 104, 107, 103, 105),
            candle(ts(2026, 4, 20, 14, 0), 105, 106, 98, 101),
            candle(ts(2026, 4, 20, 14, 30), 101, 103, 100, 102),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "30m",
            candles,
            config={
                "turtle_soup_range_source": "asian_range",
                "turtle_soup_require_killzone": True,
                "turtle_soup_session_windows": ["08:30-12:00"],
                "target_mode": "fixed_r",
                "turtle_soup_asian_min_range_bps": 0,
            },
        )

        self.assertEqual(len(setups), 1)
        setup = setups[0]
        self.assertEqual(setup.direction, "long")
        self.assertEqual(setup.entry_price, 101)
        self.assertLess(setup.stop_loss or 0, 98)
        self.assertEqual(setup.metadata["range_source"], "asian_range")
        self.assertEqual(setup.metadata["asian_range_high"], 110)
        self.assertEqual(setup.metadata["asian_range_low"], 100)
        self.assertEqual(setup.metadata["session_label"], "ny_open")

    def test_turtle_soup_can_apply_min_stop_bps(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 0, 0), 105, 108, 102, 106),
            candle(ts(2026, 4, 20, 2, 0), 106, 110, 101, 107),
            candle(ts(2026, 4, 20, 4, 0), 107, 109, 100, 104),
            candle(ts(2026, 4, 20, 8, 0), 104, 107, 103, 105),
            candle(ts(2026, 4, 20, 14, 0), 100.5, 101, 99.7, 100.2),
            candle(ts(2026, 4, 20, 14, 30), 100.2, 101, 100, 100.5),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "30m",
            candles,
            config={
                "turtle_soup_range_source": "asian_range",
                "turtle_soup_require_killzone": True,
                "turtle_soup_session_windows": ["08:30-12:00"],
                "target_mode": "fixed_r",
                "turtle_soup_min_stop_bps": 100,
            },
        )

        self.assertTrue(setups)
        setup = setups[0]
        self.assertTrue(setup.metadata["turtle_soup_min_stop_applied"])
        self.assertAlmostEqual((setup.entry_price or 0) - (setup.stop_loss or 0), (setup.entry_price or 0) * 0.01)

    def test_turtle_soup_asian_range_first_signal_only(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 0, 0), 105, 108, 102, 106),
            candle(ts(2026, 4, 20, 2, 0), 106, 110, 101, 107),
            candle(ts(2026, 4, 20, 4, 0), 107, 109, 100, 104),
            candle(ts(2026, 4, 20, 8, 0), 104, 107, 103, 105),
            candle(ts(2026, 4, 20, 13, 30), 105, 106, 99, 101),
            candle(ts(2026, 4, 20, 14, 0), 101, 106, 98, 101),
            candle(ts(2026, 4, 20, 14, 30), 101, 103, 100, 102),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "30m",
            candles,
            config={
                "turtle_soup_range_source": "asian_range",
                "turtle_soup_require_killzone": True,
                "turtle_soup_session_windows": ["08:30-12:00"],
                "target_mode": "fixed_r",
            },
        )

        self.assertEqual(setups, [])

    def test_turtle_soup_require_killzone_rejects_outside_session(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 15, 35), 101, 102, 100, 101),
            candle(ts(2026, 4, 20, 15, 40), 101, 102, 98, 99),
            candle(ts(2026, 4, 20, 15, 45), 99, 103, 99, 102),
            candle(ts(2026, 4, 20, 15, 50), 102, 104, 101, 103),
            candle(ts(2026, 4, 20, 15, 55), 103, 104, 102, 103),
            candle(ts(2026, 4, 20, 16, 0), 103, 104, 97, 99),
            candle(ts(2026, 4, 20, 16, 5), 99, 100, 98, 99),
        ]

        setups = detect_turtle_soup(
            "BTCUSDT",
            "5m",
            candles,
            config={
                "turtle_min_swing_age": 1,
                "turtle_soup_require_killzone": True,
                "turtle_soup_session_windows": ["10:00-11:00"],
            },
        )

        self.assertEqual(setups, [])

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
        self.assertEqual(setups[0].metadata["session_date"], "2026-04-20")
        self.assertEqual(setups[0].metadata["session_label"], "ny_am")
        self.assertEqual(setups[0].timestamp, ts(2026, 4, 20, 14, 5))
        self.assertEqual(setups[0].metadata["entry_time"], ts(2026, 4, 20, 14, 10))
        self.assertIsNone(setups[0].metadata["logical_invalidation_model"])
        self.assertIsNone(setups[0].metadata["logical_invalidation_price"])
        self.assertAlmostEqual(setups[0].metadata["fvg_fill_depth"], 0.2)
        self.assertEqual(setups[0].metadata["silver_bullet_min_retest_depth"], 0.15)

    def test_silver_bullet_accepts_pm_window(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 18, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 18, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 18, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 18, 10), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 18, 15), 105, 106, 104, 105),
        ]

        setups = detect_silver_bullet("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["session_window"], "14:00-15:00")
        self.assertEqual(setups[0].metadata["session_label"], "ny_pm")

    def test_silver_bullet_preserves_htf_draw_metadata(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 14, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 14, 10), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 14, 15), 105, 106, 104, 105),
        ]
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", candles),
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
                draw_direction="up",
                objective_unreached=True,
                location="discount",
                context_alignment="aligned",
            ),
        )

        setups = detect_silver_bullet("BTCUSDT", "5m", candles, context, config={"context_mode": "strict"})

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["htf_draw_direction"], "up")
        self.assertEqual(setups[0].metadata["htf_objective_type"], "swing_high")
        self.assertTrue(setups[0].metadata["htf_objective_unreached"])
        self.assertEqual(setups[0].metadata["bias_alignment"], "aligned")
        self.assertEqual(setups[0].metadata["is_in_p_d"], "discount")

    def test_silver_bullet_caps_fvg_fill_depth_at_full_fill(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 14, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 14, 10), 107, 107, 95, 106),
            candle(ts(2026, 4, 20, 14, 15), 106, 107, 105, 106),
        ]

        setups = detect_silver_bullet("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["fvg_fill_depth"], 1.0)

    def test_silver_bullet_can_require_deeper_fvg_retest(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 14, 3), 99, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 14, 10), 107, 107, 104, 105),
            candle(ts(2026, 4, 20, 14, 15), 105, 106, 104, 105),
        ]

        setups = detect_silver_bullet(
            "BTCUSDT",
            "5m",
            candles,
            config={"silver_bullet_min_retest_depth": 0.25},
        )

        self.assertEqual(setups, [])

    def test_silver_bullet_accepts_first_retest_of_prior_fvg_inside_window(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 13, 40), 99, 100, 98, 99),
            candle(ts(2026, 4, 20, 13, 45), 109, 110, 99, 109),
            candle(ts(2026, 4, 20, 13, 50), 106, 108, 105, 107),
            candle(ts(2026, 4, 20, 13, 55), 107, 109, 106, 108),
            candle(ts(2026, 4, 20, 14, 0), 108, 109, 106, 107),
            candle(ts(2026, 4, 20, 14, 5), 107, 108, 104, 105),
            candle(ts(2026, 4, 20, 14, 10), 105, 106, 104, 105),
        ]

        setups = detect_silver_bullet("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertEqual(setups[0].timestamp, ts(2026, 4, 20, 14, 5))
        self.assertEqual(setups[0].metadata["fvg_time"], ts(2026, 4, 20, 13, 50))
        self.assertEqual(setups[0].metadata["silver_bullet_fvg_source"], "first_retest_in_window")

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
            candle(5, 107, 108, 106, 107),
            candle(6, 107, 108, 106, 107),
            candle(7, 107, 108, 106, 107),
            candle(8, 107, 108, 106, 107),
            candle(9, 106, 106, 104, 105),
            candle(10, 105, 106, 104, 105),
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
        self.assertEqual(setup.metadata["entry_time"], 9)
        self.assertEqual(setup.metadata["stop_model"], "ce_fvg")
        self.assertEqual(setup.metadata["logical_invalidation_model"], "ce_fvg")
        self.assertEqual(setup.metadata["logical_invalidation_price"], setup.metadata["ifvg_ce"])
        self.assertIsNotNone(setup.metadata["tp1_price"])
        self.assertIsNotNone(setup.metadata["rr_to_target"])
        self.assertAlmostEqual(setup.metadata["ifvg_fill_depth"], 1 / 6)
        self.assertEqual(setup.metadata["ifvg_min_retest_depth"], 0.15)

    def test_ifvg_retest_can_require_deeper_fill(self) -> None:
        candles = [
            candle(1, 105, 106, 105, 105.5),
            candle(2, 104, 105, 101, 103),
            candle(3, 98, 99, 94, 95),
            candle(4, 104, 108, 103, 106),
            candle(5, 107, 108, 106, 107),
            candle(6, 107, 108, 106, 107),
            candle(7, 107, 108, 106, 107),
            candle(8, 107, 108, 106, 107),
            candle(9, 106, 106, 104, 105),
            candle(10, 105, 106, 104, 105),
        ]

        setups = detect_ifvg_retest(
            "BTCUSDT",
            "5m",
            candles,
            config={"ifvg_require_displacement": False, "ifvg_min_retest_depth": 0.25},
        )

        self.assertEqual(setups, [])

    def test_ifvg_retest_default_requires_displacement(self) -> None:
        candles = [
            candle(1, 105, 106, 104, 105),
            candle(2, 104, 105, 101, 103),
            candle(3, 98, 99, 94, 95),
            candle(4, 106, 122, 106, 121),
            candle(5, 116, 117, 116, 116),
            candle(6, 116, 117, 116, 116),
            candle(7, 116, 117, 116, 116),
            candle(8, 116, 117, 116, 116),
            candle(9, 106, 107, 103, 105),
            candle(10, 105, 106, 104, 105),
        ]

        setups = detect_ifvg_retest("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertIn(setups[0].metadata["breach_displacement_grade"], {"valid", "strong"})

    def test_ict2022_uses_fvg_retest_as_entry_time(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 101, 98, 100),
            candle(3, 100, 103, 99, 102),
            candle(4, 104, 107, 104, 106),
            candle(5, 106, 108, 105, 107),
            candle(6, 107, 108, 103, 104),
        ]
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="5m",
            candles=candles,
            sweeps=[
                LiquiditySweep(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    timestamp=2,
                    liquidity_level=99,
                    wick_extreme=98,
                    close_back_inside=100,
                    source_swing_index=0,
                    clean=True,
                )
            ],
            structure_breaks=[
                StructureBreak(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    break_type="MSS",
                    direction="bullish",
                    timestamp=4,
                    broken_level=103,
                    close_price=106,
                    source_swing_index=0,
                    strength=1.0,
                    displacement_factor=2.5,
                    has_displacement=True,
                    body_ratio=0.8,
                    range_expansion=2.0,
                    created_fvg_after_break=True,
                    displacement_grade="strong",
                    close_beyond_structure=True,
                )
            ],
            fvgs=[
                FairValueGap(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    created_at=4,
                    gap_low=101,
                    gap_high=104,
                    mitigated=True,
                    invalidated=False,
                    mitigated_at=6,
                    invalidated_at=None,
                    fill_ratio=0.5,
                )
            ],
        )

        setups = detect_ict2022_mss_fvg(
            "BTCUSDT",
            "5m",
            candles,
            StrategyContext(primary=snapshot),
            config={"ict2022_require_killzone": False, "ict2022_max_fvg_retest_bars": 3},
        )

        self.assertTrue(setups)
        self.assertEqual(setups[0].timestamp, 4)
        self.assertEqual(setups[0].metadata["entry_time"], 6)
        self.assertEqual(setups[0].metadata["time_to_retest_bars"], 2)

    def test_ict2022_records_intraday_session_retest_metadata(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 13, 55), 100, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 0), 100, 101, 98, 100),
            candle(ts(2026, 4, 20, 14, 5), 100, 103, 99, 102),
            candle(ts(2026, 4, 20, 14, 10), 104, 107, 104, 106),
            candle(ts(2026, 4, 20, 14, 15), 106, 108, 103, 107),
        ]
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="5m",
            candles=candles,
            sweeps=[
                LiquiditySweep(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 0),
                    liquidity_level=99,
                    wick_extreme=98,
                    close_back_inside=100,
                    source_swing_index=0,
                    clean=True,
                )
            ],
            structure_breaks=[
                StructureBreak(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    break_type="MSS",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 10),
                    broken_level=103,
                    close_price=106,
                    source_swing_index=0,
                    strength=1.0,
                    displacement_factor=2.5,
                    has_displacement=True,
                    body_ratio=0.8,
                    range_expansion=2.0,
                    created_fvg_after_break=True,
                    displacement_grade="strong",
                    close_beyond_structure=True,
                )
            ],
            fvgs=[
                FairValueGap(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    created_at=ts(2026, 4, 20, 14, 10),
                    gap_low=101,
                    gap_high=104,
                    mitigated=True,
                    invalidated=False,
                    mitigated_at=ts(2026, 4, 20, 14, 15),
                    invalidated_at=None,
                    fill_ratio=0.5,
                )
            ],
        )

        setups = detect_ict2022_mss_fvg(
            "BTCUSDT",
            "5m",
            candles,
            StrategyContext(primary=snapshot),
            config={
                "ict2022_session_windows": ["10:00-11:00"],
                "ict2022_retest_must_occur_within_session": True,
                "ict2022_max_fvg_retest_bars": 3,
            },
        )

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["entry_time"], ts(2026, 4, 20, 14, 15))
        self.assertEqual(setups[0].metadata["session_window"], "10:00-11:00")
        self.assertEqual(setups[0].metadata["session_date"], "2026-04-20")
        self.assertEqual(setups[0].metadata["session_label"], "ny_am")
        self.assertTrue(setups[0].metadata["ict2022_retest_must_occur_within_session"])

    def test_ict2022_can_require_retest_inside_same_session(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 40), 100, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 45), 100, 101, 98, 100),
            candle(ts(2026, 4, 20, 14, 50), 100, 103, 99, 102),
            candle(ts(2026, 4, 20, 14, 55), 104, 107, 104, 106),
            candle(ts(2026, 4, 20, 15, 5), 106, 108, 103, 107),
        ]
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="5m",
            candles=candles,
            sweeps=[
                LiquiditySweep(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 45),
                    liquidity_level=99,
                    wick_extreme=98,
                    close_back_inside=100,
                    source_swing_index=0,
                    clean=True,
                )
            ],
            structure_breaks=[
                StructureBreak(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    break_type="MSS",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 55),
                    broken_level=103,
                    close_price=106,
                    source_swing_index=0,
                    strength=1.0,
                    displacement_factor=2.5,
                    has_displacement=True,
                    body_ratio=0.8,
                    range_expansion=2.0,
                    created_fvg_after_break=True,
                    displacement_grade="strong",
                    close_beyond_structure=True,
                )
            ],
            fvgs=[
                FairValueGap(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    created_at=ts(2026, 4, 20, 14, 55),
                    gap_low=101,
                    gap_high=104,
                    mitigated=True,
                    invalidated=False,
                    mitigated_at=ts(2026, 4, 20, 15, 5),
                    invalidated_at=None,
                    fill_ratio=0.5,
                )
            ],
        )

        strict = detect_ict2022_mss_fvg(
            "BTCUSDT",
            "5m",
            candles,
            StrategyContext(primary=snapshot),
            config={
                "ict2022_session_windows": ["10:00-11:00"],
                "ict2022_retest_must_occur_within_session": True,
                "ict2022_max_fvg_retest_bars": 3,
            },
        )
        relaxed = detect_ict2022_mss_fvg(
            "BTCUSDT",
            "5m",
            candles,
            StrategyContext(primary=snapshot),
            config={
                "ict2022_session_windows": ["10:00-11:00"],
                "ict2022_retest_must_occur_within_session": False,
                "ict2022_max_fvg_retest_bars": 3,
            },
        )

        self.assertEqual(strict, [])
        self.assertTrue(relaxed)

    def test_ict2022_skips_when_target_reached_before_retest(self) -> None:
        candles = [
            candle(ts(2026, 4, 20, 14, 0), 100, 101, 99, 100),
            candle(ts(2026, 4, 20, 14, 5), 100, 101, 98, 100),
            candle(ts(2026, 4, 20, 14, 10), 100, 103, 99, 102),
            candle(ts(2026, 4, 20, 14, 15), 104, 107, 104, 106),
            candle(ts(2026, 4, 20, 14, 20), 106, 110, 105, 109),
            candle(ts(2026, 4, 20, 14, 25), 109, 111, 105, 106),
            candle(ts(2026, 4, 20, 14, 30), 106, 108, 103, 107),
        ]
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="5m",
            candles=candles,
            sweeps=[
                LiquiditySweep(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 5),
                    liquidity_level=99,
                    wick_extreme=98,
                    close_back_inside=100,
                    source_swing_index=0,
                    clean=True,
                )
            ],
            structure_breaks=[
                StructureBreak(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    break_type="MSS",
                    direction="bullish",
                    timestamp=ts(2026, 4, 20, 14, 15),
                    broken_level=103,
                    close_price=106,
                    source_swing_index=0,
                    strength=1.0,
                    displacement_factor=2.5,
                    has_displacement=True,
                    body_ratio=0.8,
                    range_expansion=2.0,
                    created_fvg_after_break=True,
                    displacement_grade="strong",
                    close_beyond_structure=True,
                )
            ],
            fvgs=[
                FairValueGap(
                    symbol="BTCUSDT",
                    timeframe="5m",
                    direction="bullish",
                    created_at=ts(2026, 4, 20, 14, 15),
                    gap_low=101,
                    gap_high=104,
                    mitigated=True,
                    invalidated=False,
                    mitigated_at=ts(2026, 4, 20, 14, 30),
                    invalidated_at=None,
                    fill_ratio=0.5,
                )
            ],
        )
        context = StrategyContext(
            primary=snapshot,
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bullish", 0.8, "test"),
                zone=HTFZone("OB", "bullish", 96, 99, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(90, 110, 100, "discount"),
                objective=HTFObjective("up", 110, "swing_high", "test", objective_unreached=True),
                inside_zone=True,
                approaching_zone=False,
                allows_long=True,
                allows_short=False,
                score_modifier=0,
                reason="test",
                draw_direction="up",
                objective_unreached=True,
                location="discount",
                poi_direction="bullish",
                context_alignment="aligned",
            ),
        )

        setups = detect_ict2022_mss_fvg(
            "BTCUSDT",
            "5m",
            candles,
            context,
            config={
                "context_mode": "strict",
                "ict2022_session_windows": ["10:00-11:00"],
                "ict2022_retest_must_occur_within_session": False,
                "ict2022_max_fvg_retest_bars": 5,
            },
        )

        self.assertEqual(setups, [])

    def test_breaker_block_default_requires_displacement(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 104, 101, 103),
        ]
        weak_block = BreakerBlock(
            symbol="BTCUSDT",
            timeframe="5m",
            direction="bullish",
            timestamp=4,
            origin_time=2,
            trigger_time=3,
            zone_low=100,
            zone_high=101,
            retested=True,
            source_order_block_time=2,
            source_order_block_direction="bearish",
            sweep_time=1,
            failed_ob_confirmed=True,
            metadata={"displacement_grade": "weak"},
        )
        snapshot = PrimitiveSnapshot(symbol="BTCUSDT", timeframe="5m", candles=candles, breaker_blocks=[weak_block])
        context = StrategyContext(primary=snapshot)

        self.assertEqual(detect_breaker_block("BTCUSDT", "5m", candles, context), [])
        self.assertTrue(detect_breaker_block("BTCUSDT", "5m", candles, context, config={"breaker_require_displacement": False}))

    def test_reclaimed_ob_default_stop_uses_block_extreme(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 103, 100.25, 101.2),
            candle(5, 101.2, 105, 101.1, 104.5),
            candle(6, 104.5, 105.5, 100.5, 101),
        ]
        block = OrderBlock(
            symbol="BTCUSDT",
            timeframe="5m",
            direction="bullish",
            timestamp=6,
            origin_time=2,
            zone_low=100,
            zone_high=101,
            midpoint=100.5,
            mitigated=True,
            invalidated=False,
            open=101,
            close=100,
            high=102,
            low=99,
            mean_threshold=100.5,
            validated=True,
            validation_time=3,
        )
        snapshot = PrimitiveSnapshot(symbol="BTCUSDT", timeframe="5m", candles=candles, order_blocks=[block])
        setups = detect_reclaimed_ob("BTCUSDT", "5m", candles, StrategyContext(primary=snapshot))

        self.assertTrue(setups)
        self.assertEqual(setups[0].metadata["stop_mode"], "block_extreme")
        self.assertLess(setups[0].stop_loss or 0, block.zone_low)
        self.assertEqual(setups[0].metadata["logical_invalidation_model"], "mean_threshold")

    def test_reclaimed_ob_rejects_without_prior_reaction(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 101.2, 100, 101.1),
            candle(4, 101.1, 101.2, 100.5, 101),
        ]
        block = OrderBlock(
            symbol="BTCUSDT",
            timeframe="5m",
            direction="bullish",
            timestamp=4,
            origin_time=2,
            zone_low=100,
            zone_high=101,
            midpoint=100.5,
            mitigated=True,
            invalidated=False,
            open=101,
            close=100,
            high=102,
            low=99,
            mean_threshold=100.5,
            validated=True,
            validation_time=3,
        )
        snapshot = PrimitiveSnapshot(symbol="BTCUSDT", timeframe="5m", candles=candles, order_blocks=[block])

        self.assertEqual(detect_reclaimed_ob("BTCUSDT", "5m", candles, StrategyContext(primary=snapshot)), [])

    def test_reclaimed_ob_rejects_body_close_through_mean_threshold(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 105, 101.2, 104.5),
            candle(5, 104.5, 105, 99.8, 100.4),
        ]
        block = OrderBlock(
            symbol="BTCUSDT",
            timeframe="5m",
            direction="bullish",
            timestamp=5,
            origin_time=2,
            zone_low=100,
            zone_high=101,
            midpoint=100.5,
            mitigated=True,
            invalidated=False,
            open=101,
            close=100,
            high=102,
            low=99,
            mean_threshold=100.5,
            validated=True,
            validation_time=3,
        )
        snapshot = PrimitiveSnapshot(symbol="BTCUSDT", timeframe="5m", candles=candles, order_blocks=[block])

        self.assertEqual(detect_reclaimed_ob("BTCUSDT", "5m", candles, StrategyContext(primary=snapshot)), [])

    def test_rejection_block_uses_swing_body_limit_entry(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 105, 102, 104),
            candle(6, 105, 110, 104, 106),
            candle(7, 104, 108, 103, 104),
            candle(8, 103, 105, 101, 102),
            candle(9, 102, 105, 100, 101),
            candle(10, 102, 107, 100, 101),
            candle(11, 101, 102, 100, 101),
        ]
        context = StrategyContext(
            primary=PrimitiveSnapshot("BTCUSDT", "5m", candles),
            htf_context=HTFContext(
                timeframe="1h",
                bias=HTFBias("bearish", 0.8, "test"),
                zone=HTFZone("OB", "bearish", 106, 110, 1, 0.8, "test"),
                dealing_range=HTFDealingRange(90, 110, 100, "premium"),
                objective=HTFObjective("down", 90, "swing_low", "test", objective_unreached=True),
                inside_zone=True,
                approaching_zone=False,
                allows_long=False,
                allows_short=True,
                score_modifier=0,
                reason="test",
                draw_direction="down",
            ),
        )

        setups = detect_rejection_block("BTCUSDT", "5m", candles, context=context, config={"context_mode": "strict"})

        self.assertTrue(setups)
        setup = setups[0]
        self.assertEqual(setup.direction, "short")
        self.assertEqual(setup.timestamp, 6)
        self.assertEqual(setup.metadata["entry_time"], 10)
        self.assertEqual(setup.entry_price, 106)
        self.assertGreater(setup.stop_loss or 0, 110)
        self.assertEqual(setup.target_hint, 90)
        self.assertEqual(setup.metadata["dol_priority"], 1)
        self.assertEqual(setup.metadata["target_mode"], "dol_hierarchy")
        self.assertEqual(setup.metadata["logical_invalidation_model"], "wick_extreme")
        self.assertEqual(setup.metadata["logical_invalidation_price"], 110)
        self.assertEqual(setup.metadata["rejection_zone_low"], 106)
        self.assertEqual(setup.metadata["rejection_zone_high"], 110)
        self.assertTrue(setup.metadata["body_liquidity_sweep"])
        self.assertEqual(setup.metadata["rejection_min_wick_fraction"], 0.2)
        self.assertGreater(setup.metadata["rejection_body_sweep_bps"], 0)

    def test_rejection_block_requires_meaningful_source_wick(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 105, 102, 104),
            candle(6, 105, 106.2, 104, 106),
            candle(7, 104, 105, 103, 104),
            candle(8, 103, 104, 101, 102),
            candle(9, 102, 103, 100, 101),
            candle(10, 102, 106, 100, 101),
            candle(11, 101, 102, 100, 101),
        ]

        self.assertEqual(detect_rejection_block("BTCUSDT", "5m", candles), [])

        relaxed = detect_rejection_block(
            "BTCUSDT",
            "5m",
            candles,
            config={"rejection_block_min_wick_fraction": 0.05},
        )

        self.assertTrue(relaxed)
        self.assertEqual(relaxed[0].entry_price, 106)

    def test_rejection_block_rebuilds_after_fresh_extreme_before_entry(self) -> None:
        candles = [
            candle(1, 100, 101, 99, 100),
            candle(2, 100, 102, 99, 101),
            candle(3, 101, 103, 100, 102),
            candle(4, 102, 104, 101, 103),
            candle(5, 103, 105, 102, 104),
            candle(6, 105, 110, 104, 106),
            candle(7, 104, 108, 103, 104),
            candle(8, 103, 111, 101, 102),
            candle(9, 102, 105, 100, 101),
            candle(10, 102, 107, 100, 101),
            candle(11, 101, 102, 100, 101),
        ]

        setups = detect_rejection_block("BTCUSDT", "5m", candles)

        self.assertTrue(setups)
        self.assertEqual(setups[0].timestamp, 8)
        self.assertEqual(setups[0].entry_price, 103)
        self.assertEqual(setups[0].metadata["rejection_wick_extreme"], 111)

    def test_same_bar_policies(self) -> None:
        future = [candle(1, 100, 103, 97, 101)]

        conservative = _evaluate("long", 100, 98, 102, future, "conservative")
        optimistic = _evaluate("long", 100, 98, 102, future, "optimistic")
        neutral = _evaluate("long", 100, 98, 102, future, "neutral")

        self.assertFalse(conservative["target_before_invalidation"])
        self.assertTrue(optimistic["target_before_invalidation"])
        self.assertTrue(conservative["same_bar_ambiguous"])
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

    def test_candles_until_can_limit_recent_history(self) -> None:
        candles = [candle(idx, 100, 101, 99, 100) for idx in range(1, 6)]

        visible = _candles_until(candles, 4, limit=2)

        self.assertEqual([item["time"] for item in visible], [3, 4])

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

    def test_decision_score_accepts_silver_bullet_two_r_target(self) -> None:
        score = _decision_score(
            "long",
            "silver_bullet",
            {
                "htf_mode": "off",
                "session_window": "10:00-11:00",
                "displacement_grade": "valid",
            },
            2.0,
        )

        self.assertEqual(score["target_rr_score"], 20)
        self.assertNotIn("target_rr_below_3", score["no_trade_reasons"])

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

    def test_execution_costs_create_net_managed_outcome(self) -> None:
        outcome = {"activated_trade": True, "managed_outcome_r": 1.5}
        costs = _execution_costs(100, 2, outcome, SimpleNamespace(commission_bps=4.0, slippage_bps=1.0))

        net = _with_execution_costs(outcome, costs)

        self.assertEqual(costs["round_trip_cost_bps"], 10.0)
        self.assertEqual(costs["execution_cost_r"], 0.05)
        self.assertEqual(net["gross_managed_outcome_r"], 1.5)
        self.assertEqual(net["net_managed_outcome_r"], 1.45)

    def test_score_threshold_report_prefers_net_managed_outcome(self) -> None:
        report = summarize_thresholds(
            [
                {
                    "model": "silver_bullet",
                    "decision_score": "100",
                    "managed_outcome_r": "1.5",
                    "gross_managed_outcome_r": "1.5",
                    "net_managed_outcome_r": "1.45",
                    "execution_cost_r": "0.05",
                    "activated_trade": "True",
                    "target_before_invalidation": "True",
                    "target_distance_r": "2",
                    "invalidated": "False",
                    "mfe_r": "2",
                }
            ],
            [70],
        )

        row = next(item for item in report if item["scope"] == "model")
        self.assertEqual(row["gross_managed_expectancy"], 1.5)
        self.assertEqual(row["managed_expectancy"], 1.45)
        self.assertEqual(row["avg_execution_cost_r"], 0.05)

    def test_walk_forward_quality_gates_fail_on_small_sample(self) -> None:
        events = [
            {
                "model": "silver_bullet",
                "symbol": "BTCUSDT",
                "timestamp": ts(2025, 5, day, 14, 0),
                "session_date": f"2025-05-{day:02d}",
                "session_window": "10:00-11:00",
                "activated_trade": "True",
                "net_managed_outcome_r": "1.0",
            }
            for day in range(1, 4)
        ]

        report = summarize_walk_forward(events, min_total_trades=30, min_phase_trades=10)

        self.assertFalse(report[0]["passed"])
        self.assertIn("min_total_trades", report[0]["failed_gates"])

    def test_walk_forward_quality_gates_pass_balanced_sample(self) -> None:
        events = [
            {
                "model": "silver_bullet",
                "symbol": "BTCUSDT",
                "timestamp": ts(2025, 5, day, 14, 0),
                "session_date": f"2025-05-{day:02d}",
                "session_window": "10:00-11:00",
                "activated_trade": "True",
                "net_managed_outcome_r": "1.0" if day % 3 else "-0.5",
            }
            for day in range(1, 31)
        ]

        report = summarize_walk_forward(events, min_total_trades=30, min_phase_trades=10, min_managed_expectancy_r=0.3)

        self.assertTrue(report[0]["passed"])
        self.assertEqual(report[0]["session_overtrade_count"], 0)

    def test_data_coverage_report_flags_missing_or_sparse_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "BTCUSDT_5m.csv"
            path.write_text(
                "time,open,high,low,close,volume\n"
                "2025-05-01T00:00:00+00:00,1,1,1,1,1\n"
                "2025-05-01T00:05:00+00:00,1,1,1,1,1\n"
                "2025-05-01T00:20:00+00:00,1,1,1,1,1\n",
                encoding="utf-8",
            )

            rows = summarize_coverage(
                Path(tmp),
                ["BTCUSDT", "ETHUSDT"],
                ["5m"],
                required_start="2025-05-01",
                required_end="2025-05-01",
                min_coverage_pct=90,
                max_gap_bars=2,
            )

        btc = next(row for row in rows if row["symbol"] == "BTCUSDT")
        eth = next(row for row in rows if row["symbol"] == "ETHUSDT")
        self.assertFalse(btc["passes"])
        self.assertIn("gap_above_max", btc["missing_reason"])
        self.assertFalse(eth["passes"])
        self.assertEqual(eth["missing_reason"], "file_missing")

    def test_forward_log_report_summarizes_fill_and_slippage_quality(self) -> None:
        report = summarize_forward_logs(
            [
                {"model": "silver_bullet", "symbol": "BTCUSDT", "status": "filled", "slippage_bps": "1.0", "net_outcome_r": "1.2"},
                {"model": "silver_bullet", "symbol": "BTCUSDT", "status": "filled", "slippage_bps": "1.5", "net_outcome_r": "-0.4"},
                {"model": "silver_bullet", "symbol": "BTCUSDT", "status": "missed", "slippage_bps": "", "net_outcome_r": ""},
            ],
            min_signals=3,
            min_fill_rate=0.5,
            max_avg_slippage_bps=2.0,
            min_avg_net_outcome_r=0.0,
        )

        overall = report[0]
        self.assertTrue(overall["passed"])
        self.assertEqual(overall["signals"], 3)
        self.assertEqual(overall["filled"], 2)
        self.assertEqual(overall["missing_fill_count"], 1)
        self.assertEqual(overall["avg_slippage_bps"], 1.25)

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
        self.assertTrue(passes_model_filter(event, {"allowed_timeframes": ["1h"], "allowed_symbols": ["BTCUSDT"]}))
        self.assertFalse(passes_model_filter(event, {"allowed_timeframes": ["4h"]}))
        self.assertTrue(passes_model_filter({**event, "session_label": "ny_open", "range_source": "asian_range"}, {"allowed_directions": ["long"], "allowed_session_labels": ["ny_open"], "allowed_range_sources": ["asian_range"]}))
        self.assertFalse(passes_model_filter({**event, "session_label": "ny_pm"}, {"allowed_session_labels": ["ny_open"]}))
        event["htf_inside_poi"] = True
        event["htf_zone_type"] = "FVG"
        event["htf_bias"] = "bullish"
        event["htf_location"] = "discount"
        event["htf_context_alignment"] = "aligned"
        event["htf_draw_direction"] = "up"
        event["htf_objective_type"] = "swing_high"
        event["htf_objective_unreached"] = True
        self.assertTrue(passes_model_filter(event, {"require_htf_inside_poi": True, "allowed_htf_zone_types": ["FVG"]}))
        self.assertFalse(passes_model_filter({**event, "htf_inside_poi": False}, {"require_htf_inside_poi": True}))
        self.assertFalse(passes_model_filter(event, {"allowed_htf_zone_types": ["PD"]}))
        self.assertTrue(passes_model_filter(event, {"require_htf_draw": True}))
        self.assertFalse(passes_model_filter({**event, "htf_draw_direction": "down"}, {"require_htf_draw": True}))
        self.assertTrue(passes_model_filter(event, {"require_bias_alignment": True, "require_premium_discount_alignment": True}))
        self.assertFalse(passes_model_filter({**event, "htf_bias": "bearish"}, {"require_bias_alignment": True}))
        self.assertFalse(passes_model_filter({**event, "htf_location": "premium"}, {"require_premium_discount_alignment": True}))
        self.assertFalse(passes_model_filter({**event, "htf_objective_unreached": False}, {"require_htf_draw": True}))
        self.assertTrue(passes_model_filter(event, {"allowed_htf_context_alignments": ["aligned"]}))
        self.assertFalse(passes_model_filter({**event, "htf_context_alignment": "mixed"}, {"allowed_htf_context_alignments": ["aligned"]}))
        event["risk_bps"] = 100
        event["execution_cost_r"] = 0.2
        self.assertTrue(passes_model_filter(event, {"min_risk_bps": 80, "max_execution_cost_r": 0.3}))
        self.assertFalse(passes_model_filter(event, {"min_risk_bps": 120}))
        self.assertFalse(passes_model_filter(event, {"max_risk_bps": 80}))
        self.assertFalse(passes_model_filter(event, {"max_execution_cost_r": 0.1}))

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

    def test_lifecycle_uses_tp1_and_logical_invalidation(self) -> None:
        setup = EntrySetup(
            model_name="ifvg_retest",
            direction="long",
            symbol="BTCUSDT",
            timeframe="5m",
            status="triggered",
            entry_low=100,
            entry_high=101,
            entry_price=100.5,
            stop_loss=98,
            invalidation=98,
            target_hint=106,
            sweep_level=None,
            structure_level=None,
            context_timeframe="1h",
            score=4,
            reason="test",
            components=default_components(),
            timestamp=1,
            metadata={"entry_time": 2, "tp1_price": 103, "logical_invalidation_price": 99, "logical_invalidation_model": "ce_fvg"},
        )

        cancelled = classify_setup_lifecycle(setup, [candle(1, 102, 103.5, 101.5, 103), candle(2, 102, 102, 100, 101)])
        tp1 = classify_setup_lifecycle(setup, [candle(1, 102, 102, 101.5, 102), candle(2, 102, 102, 100, 101), candle(3, 101, 103.5, 100, 102)])
        invalidated = classify_setup_lifecycle(setup, [candle(1, 102, 102, 101.5, 102), candle(2, 102, 102, 100, 101), candle(3, 101, 102, 98.5, 98.8)])

        self.assertEqual(cancelled["status"], "cancelled")
        self.assertEqual(cancelled["lifecycle_reason"], "target_reached_before_entry")
        self.assertEqual(tp1["status"], "tp1_hit")
        self.assertTrue(tp1["moved_to_be"])
        self.assertEqual(invalidated["status"], "invalidated")
        self.assertEqual(invalidated["exit_reason"], "ce_violation")

    def test_ict_batch_builds_repeatable_run_args(self) -> None:
        args = build_run_args(
            {
                "data_dir": "data/history_2025-05-01_2025-10-31",
                "symbols": ["BTCUSDT", "ETHUSDT"],
                "models": ["turtle_soup", "ifvg_retest"],
                "context_mode": "aligned_only",
                "smt_pairs": ["BTCUSDT:ETHUSDT"],
                "forward_bars": 20,
                "commission_bps": 4.0,
                "slippage_bps": 1.0,
                "start_date": "2025-05-01",
                "end_date": "2025-05-31",
                "turtle_soup_session_windows": "02:00-05:00,07:00-10:00,13:30-16:00",
                "turtle_soup_min_stop_bps": 80,
                "pre_model_require_smt": True,
                "pre_model_filter": False,
                "pre_model_require_htf_poi": False,
                "silver_bullet_windows": "10:00-11:00,14:00-15:00",
                "silver_bullet_max_retest_bars": 6,
                "silver_bullet_min_retest_depth": 0.5,
                "silver_bullet_retest_must_occur_within_window": True,
                "silver_bullet_use_ce_invalidation": False,
                "ict2022_max_fvg_retest_bars": 12,
                "ict2022_session_windows": "02:00-05:00,07:00-10:00,13:30-16:00",
                "ict2022_retest_must_occur_within_session": True,
                "ict2022_require_strong_displacement": False,
                "ifvg_min_retest_depth": 0.25,
                "rejection_block_min_wick_fraction": 0.25,
                "scan_session_windows": "02:30-02:30,10:45-11:00",
                "scan_session_lag_bars": 1,
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
        self.assertIn("--commission-bps", args)
        self.assertIn("4.0", args)
        self.assertIn("--slippage-bps", args)
        self.assertIn("1.0", args)
        self.assertIn("--start-date", args)
        self.assertIn("2025-05-01", args)
        self.assertIn("--end-date", args)
        self.assertIn("2025-05-31", args)
        self.assertIn("--pre-model-require-smt", args)
        self.assertIn("--no-pre-model-filter", args)
        self.assertIn("--no-pre-model-require-htf-poi", args)
        self.assertIn("--turtle-soup-session-windows", args)
        self.assertIn("02:00-05:00,07:00-10:00,13:30-16:00", args)
        self.assertIn("--turtle-soup-min-stop-bps", args)
        self.assertIn("80", args)
        self.assertIn("--silver-bullet-windows", args)
        self.assertIn("10:00-11:00,14:00-15:00", args)
        self.assertIn("--silver-bullet-max-retest-bars", args)
        self.assertIn("6", args)
        self.assertIn("--silver-bullet-min-retest-depth", args)
        self.assertIn("0.5", args)
        self.assertIn("--silver-bullet-retest-must-occur-within-window", args)
        self.assertIn("--no-silver-bullet-use-ce-invalidation", args)
        self.assertIn("--ifvg-min-retest-depth", args)
        self.assertIn("0.25", args)
        self.assertIn("--ict2022-max-fvg-retest-bars", args)
        self.assertIn("12", args)
        self.assertIn("--ict2022-session-windows", args)
        self.assertIn("02:00-05:00,07:00-10:00,13:30-16:00", args)
        self.assertIn("--ict2022-retest-must-occur-within-session", args)
        self.assertIn("--no-ict2022-require-strong-displacement", args)
        self.assertIn("--rejection-block-min-wick-fraction", args)
        self.assertIn("0.25", args)
        self.assertIn("--scan-session-windows", args)
        self.assertIn("02:30-02:30,10:45-11:00", args)
        self.assertIn("--scan-session-lag-bars", args)

    def test_ict_batch_can_disable_smt_pairs(self) -> None:
        args = build_run_args(
            {
                "data_dir": "tests/fixtures",
                "symbols": ["BTCUSDT"],
                "models": ["silver_bullet"],
                "smt_pairs": [],
            },
            {
                "timeframes": ["5m"],
                "out_dir": "backtest_results/example",
            },
        )

        self.assertIn("--smt-pairs", args)
        self.assertEqual(args.index("--smt-pairs"), len(args) - 1)

    def test_r_hits_are_measured_from_entry_time(self) -> None:
        future = [
            candle(2, 100, 104, 99, 103),
            candle(3, 100, 102.5, 99, 102),
        ]

        outcome = _evaluate("long", 100, 98, 104, future, "conservative", entry_time=3)

        self.assertTrue(outcome["hit_1r_before_invalidation"])
        self.assertFalse(outcome["hit_2r_before_invalidation"])
        self.assertEqual(outcome["time_to_entry_bars"], 2)

    def test_backtest_can_cancel_if_tp1_hits_before_limit_entry(self) -> None:
        future = [
            candle(2, 100, 103, 99, 102),
            candle(3, 100, 101, 99, 100),
        ]

        outcome = _evaluate("long", 100, 98, 106, future, "conservative", entry_time=3, tp1=102, cancel_on_pre_entry_tp1=True)

        self.assertFalse(outcome["activated_trade"])
        self.assertTrue(outcome["target_reached_before_entry"])
        self.assertEqual(outcome["exit_reason"], "target_reached_before_entry")

    def test_backtest_managed_partial_tp_then_be(self) -> None:
        future = [
            candle(1, 100, 102.2, 99.5, 101),
            candle(2, 101, 101.5, 99.8, 100.2),
        ]

        outcome = _evaluate(
            "long",
            100,
            98,
            106,
            future,
            "conservative",
            entry_time=1,
            tp1_r=1.0,
            partial_close_fraction=0.5,
            move_to_be_after_tp1=True,
        )

        self.assertTrue(outcome["tp1_hit"])
        self.assertTrue(outcome["moved_to_be"])
        self.assertEqual(outcome["managed_exit_reason"], "be_after_tp1")
        self.assertEqual(outcome["managed_outcome_r"], 0.5)

    def test_backtest_closes_unresolved_trade_at_horizon_close(self) -> None:
        future = [
            candle(1, 100, 101, 99.5, 100.5),
            candle(2, 100.5, 101.5, 100.2, 101),
        ]

        outcome = _evaluate("long", 100, 98, 104, future, "conservative", entry_time=1)

        self.assertEqual(outcome["managed_exit_reason"], "horizon_close")
        self.assertEqual(outcome["exit_reason"], "horizon_close")
        self.assertEqual(outcome["managed_outcome_r"], 0.5)


if __name__ == "__main__":
    unittest.main()
