# Entry Models Backtest Report

Config:
- symbols: BTCUSDT
- timeframes: 5m
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: 2025-05-01
- end: 2025-05-03
- generated_at: 2026-04-24T11:18:08.153526+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 253
- warnings: 1
- skipped_outcome_events: 38

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 95 | 83 | 12 | 51 | 44 | 3.025005 | 1.653872 | 2.742336 | 1.152305 | 0.819277 | 0.674699 | 0.445783 | 0.663158 | 0.554217 | 0.349398 | 3.989474 | BTCUSDT | 5m |
| Entry Model 2 | 158 | 132 | 26 | 81 | 77 | 2.454065 | 1.580838 | 2.368169 | 1.663326 | 0.795455 | 0.666667 | 0.386364 | 0.683544 | 0.515152 | 0.295455 | 4.740506 | BTCUSDT | 5m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 51 | 44 | 7 | 51 | 0 | 2.818469 | 1.98302 | 2.739764 | 1.116338 | 0.863636 | 0.659091 | 0.5 | 0.686275 | 0.5 | 0.363636 | 3.980392 | BTCUSDT | 5m |
| Entry Model 1 | short | 44 | 39 | 5 | 0 | 44 | 3.25802 | 1.419421 | 2.745237 | 1.270823 | 0.769231 | 0.692308 | 0.384615 | 0.636364 | 0.615385 | 0.333333 | 4.0 | BTCUSDT | 5m |
| Entry Model 2 | long | 81 | 69 | 12 | 81 | 0 | 2.489694 | 1.618117 | 2.447454 | 1.655071 | 0.797101 | 0.666667 | 0.391304 | 0.691358 | 0.507246 | 0.304348 | 4.679012 | BTCUSDT | 5m |
| Entry Model 2 | short | 77 | 63 | 14 | 0 | 77 | 2.415044 | 1.526071 | 2.281333 | 1.728603 | 0.793651 | 0.666667 | 0.380952 | 0.675325 | 0.52381 | 0.285714 | 4.805195 | BTCUSDT | 5m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 5m | 95 | 83 | 12 | 51 | 44 | 3.025005 | 1.653872 | 2.742336 | 1.152305 | 0.819277 | 0.674699 | 0.445783 | 0.663158 | 0.554217 | 0.349398 | 3.989474 | BTCUSDT | 5m |
| Entry Model 2 | 5m | 158 | 132 | 26 | 81 | 77 | 2.454065 | 1.580838 | 2.368169 | 1.663326 | 0.795455 | 0.666667 | 0.386364 | 0.683544 | 0.515152 | 0.295455 | 4.740506 | BTCUSDT | 5m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 94 | 82 | 12 | 50 | 44 | 3.040308 | 1.651884 | 2.762733 | 1.164029 | 0.817073 | 0.670732 | 0.45122 | 0.659574 | 0.560976 | 0.353659 | 4.0 | BTCUSDT | 5m |
| Entry Model 1 | medium | 1 | 1 | 0 | 1 | 0 | 1.770138 | 1.770138 | 1.069745 | 1.069745 | 1.0 | 1.0 | 0.0 | 1.0 | 0.0 | 0.0 | 3.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 158 | 132 | 26 | 81 | 77 | 2.454065 | 1.580838 | 2.368169 | 1.663326 | 0.795455 | 0.666667 | 0.386364 | 0.683544 | 0.515152 | 0.295455 | 4.740506 | BTCUSDT | 5m |

## 6. Warnings / skipped events
- Entry Model 3 BTCUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- f370aebd28c4c1ba: invalid risk (risk is not positive; R metrics are skipped)
- e67e7a208e39216e: invalid risk (risk is not positive; R metrics are skipped)
- 842d63f150d184e5: invalid risk (risk is not positive; R metrics are skipped)
- 9a506a84afb2a0bb: invalid risk (risk is not positive; R metrics are skipped)
- 1205ad67bde6a006: invalid risk (risk is not positive; R metrics are skipped)
- 995ffdeb54764add: invalid risk (risk is not positive; R metrics are skipped)
- 56bb134ae826f6bf: invalid risk (risk is not positive; R metrics are skipped)
- 17aff481dc8f9f1b: invalid risk (risk is not positive; R metrics are skipped)
- a4d30c227526031b: invalid risk (risk is not positive; R metrics are skipped)
- fa8c3136e6238502: invalid risk (risk is not positive; R metrics are skipped)
- d6a77d24a307ad86: invalid risk (risk is not positive; R metrics are skipped)
- 8c1773cbbae740ca: invalid risk (risk is not positive; R metrics are skipped)
- 6920d4a86b603935: invalid risk (risk is not positive; R metrics are skipped)
- 293d297d4dfe89e1: invalid risk (risk is not positive; R metrics are skipped)
- f44f3dcd17c615f2: invalid risk (risk is not positive; R metrics are skipped)
- 0140f0b97f4cc1a1: invalid risk (risk is not positive; R metrics are skipped)
- 8ca3731b6052c380: invalid risk (risk is not positive; R metrics are skipped)
- 6de737e733325756: invalid risk (risk is not positive; R metrics are skipped)
- 7fa27a7260915810: invalid risk (risk is not positive; R metrics are skipped)
- 7c8f3a1c45cb3c1e: invalid risk (risk is not positive; R metrics are skipped)
- 47e74880dbcdc680: invalid risk (risk is not positive; R metrics are skipped)
- 5dd64cb6f536f135: invalid risk (risk is not positive; R metrics are skipped)
- 1cfbe91cd0e678d0: invalid risk (risk is not positive; R metrics are skipped)
- 6fc484e1e3d38946: invalid risk (risk is not positive; R metrics are skipped)
- cd6d73abff56e407: invalid risk (risk is not positive; R metrics are skipped)
- bbe8732d2263f2d8: invalid risk (risk is not positive; R metrics are skipped)
- 4fe9baf6d34f5e56: invalid risk (risk is not positive; R metrics are skipped)
- 81c38ccae508e96f: invalid risk (risk is not positive; R metrics are skipped)
- afa4ce0799399112: invalid risk (risk is not positive; R metrics are skipped)
- d92a2b1c8f2057cd: invalid risk (risk is not positive; R metrics are skipped)
- 7dca276677070597: invalid risk (risk is not positive; R metrics are skipped)
- 6cb8d26565bcfba1: invalid risk (risk is not positive; R metrics are skipped)
- 7e0c2afc3b3fa7ef: invalid risk (risk is not positive; R metrics are skipped)
- 4a2f79897c1fe1e0: invalid risk (risk is not positive; R metrics are skipped)
- a55f8a9d91bb17be: invalid risk (risk is not positive; R metrics are skipped)
- f067955731e4f888: invalid risk (risk is not positive; R metrics are skipped)
- 5cb0d684a5a26cd3: invalid risk (risk is not positive; R metrics are skipped)
- 77c6a7629a0b960d: invalid risk (risk is not positive; R metrics are skipped)

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
