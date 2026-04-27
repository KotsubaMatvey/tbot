# Risk / Quality Refactor Comparison

Generated: 2026-04-27

This is event-study backtesting only. It does not model fees, slippage, live execution, partial exits, or breakeven.

## 1. Test Status

- `python -m unittest tests/test_ict_refactor.py`: passed, 10 tests.
- `pytest`: passed, 16 tests, 13 third-party deprecation warnings from matplotlib/pyparsing.
- `python -m compileall config.py market_primitives strategies backtesting scanner tests`: passed.

## 2. Code Changes

- Added `strategies/risk_policy.py` for stop-loss vs structural invalidation separation.
- Added `strategies/setup_quality.py` for gates / quality / risk score components.
- Extended displacement, IFVG, HTF context, swing/liquidity, scoring, replay serialization, summaries, and CLI flags.
- Added research specs `11_risk_invalidation.md`, `14_displacement_rules.md`, `15_ifvg_rules.md`, `16_bias_draw_liquidity.md`, `17_score_priority.md`, `18_swing_liquidity_significance.md`.

## 3. Risk / Stop Mode Summary

Run: `backtest_results/strict_model1_model2_structural`

- Events: 264.
- Valid outcomes: 264.
- Skipped outcomes: 0.
- Invalid risk count: 0.
- Model 1 structural: 49 events.
- Model 2 structural: 215 events.

Run: `backtest_results/model2_ifvg_quality`

- `stop_mode=standard` produced 0 events.
- Cause to investigate: current event entry price is midpoint-based while Model 2 standard stop uses IFVG CE; that can make risk too small under `MIN_RISK_BPS`.

## 4. Model 1 Summary

Strict structural run:

- Events: 49.
- Median MFE R: 1.364265.
- Avg MFE R: 1.870148.
- Median MAE R: 0.462621.
- Hit 1R before invalidation: 0.591837.
- Hit 2R before invalidation: 0.306122.
- Invalidation rate: 0.265306.
- Avg score: 4.591837.

## 5. Model 2 IFVG Quality Summary

Strict structural run:

- Events: 215.
- Median MFE R: 7.72194.
- Avg MFE R: 14.454856.
- Median MAE R: 5.921204.
- Hit 1R before invalidation: 0.706977.
- Hit 2R before invalidation: 0.562791.
- Invalidation rate: 0.809302.
- Avg score: 4.981395.

IFVG grades:

- Strong IFVG: 32 events, median MFE R 8.736993, hit 2R before invalidation 0.53125.
- Valid IFVG: 183 events, median MFE R 7.72194, hit 2R before invalidation 0.568306.

Model 2 stayed stable as the strongest event generator, but strong IFVG did not clearly outperform valid IFVG on hit-before-invalidation in this sample.

## 6. Model 3 Refined Summary

Available `data/history` range is 2026-04-20 to 2026-04-25, so the optional `2025-01-01` to `2025-12-31` date run was not applicable.

Refined source-zone stop:

- Events: 3.
- Valid outcomes: 3.
- Median MFE R: 3.12895.
- Hit 1R before invalidation: 0.0.
- Hit 2R before invalidation: 0.0.
- Invalidation rate: 1.0.

Refined LTF MSS stop:

- Events: 1.
- Hit 1R before invalidation: 0.0.
- Invalidation rate: 1.0.

Refined HTF OB stop:

- Events: 4.
- Median MFE R: 0.06539.
- Hit 1R before invalidation: 0.0.
- Invalidation rate: 0.0.

Prior `model3_fill_50` reference had 21 events, 18 valid outcomes, 3 skipped outcomes, and invalidation rate 0.809524. The refined source-zone/LTF-MSS variants reduced events and skipped outcomes but did not improve invalidation. HTF OB avoided invalidation on 4 events, but with very weak MFE.

## 7. Score Calibration Summary

Score calibration is still not good enough:

- Strict Model 1/2 summary has only high score bucket rows.
- No medium/low bucket comparison exists in the main run.
- High cannot be proven statistically better than medium from this output.

Score components are now serialized in `components_json`, and summaries by objective, POI, risk, displacement, IFVG, RR, and score component are generated.

## 8. Displacement Grade Summary

Model 1:

- Strong: 26 events, median MFE R 1.373053, hit 2R before invalidation 0.269231.
- Valid: 23 events, median MFE R 1.348599, hit 2R before invalidation 0.347826.

Model 2 displacement grade serialized as IFVG breach grade; `summary_by_ifvg_grade` is the more useful quality view for Model 2.

## 9. HTF Alignment / Objective Summary

Strict Model 1/2:

- All events had `objective_unreached=True`.
- Model 1 aligned: 42 events.
- Model 1 mixed: 7 events.
- Model 2 aligned: 192 events.
- Model 2 mixed: 23 events.

Objective direction no longer creates bias by itself; tests cover objective-above and objective-below neutral cases.

## 10. Swing / Liquidity Quality Summary

Sweep significance in strict Model 1/2:

- Model 1: 19 intermediate, 16 long, 14 short.
- Model 2: 62 intermediate, 97 long, 56 short.

Long-significance sweeps were the largest Model 2 subset and had median MFE R 8.949302.

## 11. Problems Found

- Model 2 `standard` stop generated 0 events with current midpoint entry semantics.
- Score buckets remain over-compressed into high.
- Model 3 source-zone and LTF-MSS variants still show 100% invalidation in the small refined sample.
- Model 3 HTF OB stop has low MFE despite low invalidation.
- Strong IFVG and strong displacement do not yet consistently outperform valid in this short data window.

## 12. Recommended Next Actions

1. Fix score calibration so medium/low buckets actually exist after gates pass.
2. Revisit Model 2 standard stop semantics: CE stop plus midpoint entry is too tight for current risk floor.
3. Keep Model 2 structural as the main candidate until standard stop is corrected and retested.
4. Keep Model 3 research-only; compare HTF OB stop on more data before accepting it.
5. Add a longer dataset window before making any conclusion about IFVG strong vs valid or displacement strong vs valid.
