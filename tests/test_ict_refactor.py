from __future__ import annotations

import unittest

from backtesting.run_entry_models import _build_parser
from market_primitives.common import FairValueGap, LiquiditySweep, StructureBreak, SwingPoint
from market_primitives.displacement import evaluate_displacement
from market_primitives.fvg import detect_fvg
from market_primitives.ifvg import detect_ifvg
from strategies.entry_model_1 import detect_entry_model_1
from strategies.htf_context import HTFBias, HTFContext, HTFDealingRange, HTFObjective, HTFZone, build_htf_context
from strategies.risk_policy import model1_risk_plan, model2_risk_plan, model3_risk_plan
from strategies.types import PrimitiveSnapshot, StrategyContext


def candle(ts: int, open_: float, high: float, low: float, close: float) -> dict[str, float | int]:
    return {"time": ts, "open": open_, "high": high, "low": low, "close": close, "volume": 100.0}


def bullish_htf() -> HTFContext:
    return HTFContext(
        timeframe="1h",
        bias=HTFBias("bullish", 0.8, "test"),
        zone=HTFZone("OB", "bullish", 99, 101, 1, 0.8, "test"),
        dealing_range=HTFDealingRange(90, 110, 100, "discount"),
        objective=HTFObjective("up", 120, "swing_high", "test"),
        inside_zone=True,
        approaching_zone=True,
        allows_long=True,
        allows_short=False,
        score_modifier=0.0,
        reason="test",
    )


class ICTRefactorTests(unittest.TestCase):
    def test_displacement_strong_body_and_range_passes(self) -> None:
        candles = [
            candle(1, 100, 102, 99, 101),
            candle(2, 101, 103, 100, 102),
            candle(3, 102, 104, 101, 103),
            candle(4, 103, 120, 102, 118),
        ]

        quality = evaluate_displacement(candles, 3, direction="bullish", structure_level=110, created_fvg_after_break=True)

        self.assertTrue(quality.has_displacement)
        self.assertEqual(quality.displacement_grade, "strong")
        self.assertGreaterEqual(quality.body_ratio, 0.55)
        self.assertGreaterEqual(quality.range_expansion, 1.2)

    def test_displacement_weak_break_fails(self) -> None:
        candles = [
            candle(1, 100, 102, 99, 101),
            candle(2, 101, 103, 100, 102),
            candle(3, 102, 104, 101, 103),
            candle(4, 103, 105, 102, 104),
        ]

        quality = evaluate_displacement(candles, 3, direction="bullish", structure_level=103.5)

        self.assertFalse(quality.has_displacement)
        self.assertEqual(quality.displacement_grade, "weak")

    def test_displacement_valid_requires_close_beyond_and_fvg(self) -> None:
        candles = [
            candle(1, 100, 102, 99, 101),
            candle(2, 101, 103, 100, 102),
            candle(3, 102, 104, 101, 103),
            candle(4, 103, 112, 102, 109),
        ]

        no_fvg = evaluate_displacement(candles, 3, direction="bullish", structure_level=105, created_fvg_after_break=False)
        valid = evaluate_displacement(candles, 3, direction="bullish", structure_level=105, created_fvg_after_break=True)

        self.assertFalse(no_fvg.has_displacement)
        self.assertTrue(valid.has_displacement)
        self.assertEqual(valid.displacement_grade, "valid")

    def test_fvg_lifecycle_tracks_partial_fill(self) -> None:
        candles = [
            candle(1, 96, 100, 95, 99),
            candle(2, 99, 101, 98, 100),
            candle(3, 103, 105, 102, 104),
            candle(4, 104, 105, 101, 103),
            candle(5, 103, 104, 102, 103),
        ]

        gaps = detect_fvg(candles, "BTCUSDT", "5m", scan_back=10)
        bullish = next(gap for gap in gaps if gap.direction == "bullish")

        self.assertEqual(bullish.status, "partially_filled")
        self.assertGreater(bullish.fill_percent, 0)
        self.assertEqual(bullish.consequent_encroachment, 101)

    def test_ifvg_requires_body_close_not_wick_only(self) -> None:
        wick_only = [
            candle(1, 105, 106, 100, 104),
            candle(2, 104, 105, 101, 103),
            candle(3, 99, 99, 94, 95),
            candle(4, 96, 105, 95, 99.5),
            candle(5, 100, 101, 99, 100),
        ]

        self.assertEqual(detect_ifvg(wick_only, "BTCUSDT", "5m"), [])

    def test_ifvg_bearish_source_breached_up_becomes_bullish(self) -> None:
        candles = [
            candle(1, 105, 106, 100, 104),
            candle(2, 104, 105, 101, 103),
            candle(3, 99, 99, 94, 95),
            candle(4, 96, 119, 95, 113),
            candle(5, 100, 101, 99, 100),
        ]

        ifvgs = detect_ifvg(candles, "BTCUSDT", "5m")

        self.assertEqual(len(ifvgs), 1)
        self.assertEqual(ifvgs[0].source_direction, "bearish")
        self.assertEqual(ifvgs[0].direction, "bullish")
        self.assertIn(ifvgs[0].ifvg_grade, {"valid", "strong"})
        self.assertGreater(ifvgs[0].breach_displacement_factor, 0)

    def test_risk_policy_model_stops_are_positive(self) -> None:
        m1 = model1_risk_plan(
            side="long",
            entry_low=100,
            entry_high=102,
            sweep_extreme=98,
            stop_mode="structural",
            stop_buffer_bps=10,
            invalidation_confirmation="close",
        )
        m2 = model2_risk_plan(
            side="long",
            zone_low=100,
            zone_high=104,
            sweep_extreme=98,
            stop_mode="standard",
            stop_buffer_bps=10,
            invalidation_confirmation="close",
        )
        m3 = model3_risk_plan(
            side="long",
            entry_low=100,
            entry_high=102,
            ltf_protected_swing=99,
            source_zone_low=98,
            source_zone_high=103,
            htf_ob_low=None,
            htf_ob_high=None,
            model3_stop_mode="source_zone_extreme",
            stop_buffer_bps=2,
            invalidation_confirmation="close",
        )

        self.assertLess(m1.stop_loss, 98)
        self.assertLess(m2.stop_loss, 102)
        self.assertLess(m3.stop_loss, 98)
        self.assertTrue(m1.risk_valid)
        self.assertTrue(m2.risk_valid)
        self.assertTrue(m3.risk_valid)

    def test_htf_objective_alone_does_not_create_bias(self) -> None:
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="1h",
            candles=[candle(1, 100, 101, 99, 100), candle(2, 100, 101, 99, 100)],
            swings=[
                SwingPoint("BTCUSDT", "1h", "low", 1, 0, 90, 2, "intermediate", 0.7),
                SwingPoint("BTCUSDT", "1h", "high", 2, 1, 120, 2, "intermediate", 0.7),
            ],
        )

        context = build_htf_context(snapshot, current_price_value=100)

        self.assertEqual(context.objective.direction, "up")
        self.assertEqual(context.bias.direction, "neutral")

    def test_model1_rejects_sequence_without_displacement_when_required(self) -> None:
        snapshot = PrimitiveSnapshot(
            symbol="BTCUSDT",
            timeframe="5m",
            candles=[
                candle(1, 100, 101, 98, 100),
                candle(2, 100, 102, 99, 101),
                candle(3, 101, 103, 100, 102),
                candle(4, 102, 103, 100.5, 101),
            ],
            sweeps=[
                LiquiditySweep("BTCUSDT", "5m", "bullish", 1, 99, 98, 100, 0, True, 1.0, "short")
            ],
            structure_breaks=[
                StructureBreak("BTCUSDT", "5m", "MSS", "bullish", 2, 101, 102, 0, 0.4)
            ],
            fvgs=[
                FairValueGap("BTCUSDT", "5m", "bullish", 3, 100.5, 101.5, False, False, None, None, 0.0)
            ],
        )
        context = StrategyContext(primary=snapshot, htf_context=bullish_htf(), htf_mode="strict", require_displacement=True)

        self.assertEqual(detect_entry_model_1(context), [])

    def test_backtest_cli_risk_flags_parse(self) -> None:
        args = _build_parser().parse_args(
            [
                "--symbols",
                "BTCUSDT",
                "--timeframes",
                "5m",
                "--stop-mode",
                "standard",
                "--model3-stop-mode",
                "ltf_mss",
                "--stop-buffer-bps",
                "3.5",
                "--invalidation-confirmation",
                "wick",
                "--model3-reaction-bars",
                "12",
                "--model3-min-rr-to-objective",
                "2.0",
                "--model3-source-zone",
                "fvg_ce",
            ]
        )

        self.assertEqual(args.stop_mode, "standard")
        self.assertEqual(args.model3_stop_mode, "ltf_mss")
        self.assertEqual(args.stop_buffer_bps, 3.5)
        self.assertEqual(args.invalidation_confirmation, "wick")
        self.assertEqual(args.model3_reaction_bars, 12)
        self.assertEqual(args.model3_min_rr_to_objective, 2.0)
        self.assertEqual(args.model3_source_zone, "fvg_ce")


if __name__ == "__main__":
    unittest.main()
