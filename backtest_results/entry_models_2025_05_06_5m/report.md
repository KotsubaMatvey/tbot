# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 5m
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: 2025-05-01
- end: 2025-06-30
- generated_at: 2026-04-24T12:05:47.118985+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 9557
- warnings: 2
- skipped_outcome_events: 1265

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 3589 | 3159 | 430 | 1801 | 1788 | 2.891685 | 1.485306 | 3.075823 | 1.173491 | 0.813549 | 0.644191 | 0.386515 | 0.606018 | 0.539411 | 0.305476 | 3.954305 | ETHUSDT | 5m |
| Entry Model 2 | 5968 | 5133 | 835 | 2927 | 3041 | 3.444528 | 1.807736 | 3.199558 | 1.643564 | 0.816482 | 0.679525 | 0.464251 | 0.691354 | 0.525619 | 0.329242 | 4.668733 | ETHUSDT | 5m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 1801 | 1581 | 220 | 1801 | 0 | 3.297066 | 1.546695 | 3.62391 | 1.163314 | 0.82859 | 0.656546 | 0.403542 | 0.603554 | 0.552182 | 0.316256 | 3.965019 | ETHUSDT | 5m |
| Entry Model 1 | short | 1788 | 1578 | 210 | 0 | 1788 | 2.485534 | 1.434243 | 2.526695 | 1.18231 | 0.798479 | 0.631812 | 0.369455 | 0.608501 | 0.526616 | 0.294677 | 3.943512 | ETHUSDT | 5m |
| Entry Model 2 | long | 2927 | 2532 | 395 | 2927 | 0 | 3.356768 | 1.844555 | 3.13212 | 1.612124 | 0.826619 | 0.690363 | 0.474329 | 0.682952 | 0.531201 | 0.336888 | 4.697984 | ETHUSDT | 5m |
| Entry Model 2 | short | 3041 | 2601 | 440 | 0 | 3041 | 3.52996 | 1.774926 | 3.265207 | 1.678825 | 0.806613 | 0.668973 | 0.454441 | 0.699441 | 0.520185 | 0.321799 | 4.640579 | ETHUSDT | 5m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 5m | 3589 | 3159 | 430 | 1801 | 1788 | 2.891685 | 1.485306 | 3.075823 | 1.173491 | 0.813549 | 0.644191 | 0.386515 | 0.606018 | 0.539411 | 0.305476 | 3.954305 | ETHUSDT | 5m |
| Entry Model 2 | 5m | 5968 | 5133 | 835 | 2927 | 3041 | 3.444528 | 1.807736 | 3.199558 | 1.643564 | 0.816482 | 0.679525 | 0.464251 | 0.691354 | 0.525619 | 0.329242 | 4.668733 | ETHUSDT | 5m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 3426 | 3028 | 398 | 1738 | 1688 | 2.90806 | 1.493241 | 3.148818 | 1.199262 | 0.811427 | 0.64432 | 0.388705 | 0.612668 | 0.537979 | 0.305812 | 4.0 | ETHUSDT | 5m |
| Entry Model 1 | low | 1 | 1 | 0 | 0 | 1 | 0.172296 | 0.172296 | 2.451613 | 2.451613 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 2.0 | ETHUSDT | 5m |
| Entry Model 1 | medium | 162 | 130 | 32 | 63 | 99 | 2.531206 | 1.422345 | 1.380404 | 0.693522 | 0.869231 | 0.646154 | 0.338462 | 0.462963 | 0.576923 | 0.3 | 3.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 5965 | 5130 | 835 | 2927 | 3038 | 3.44577 | 1.809006 | 3.201382 | 1.64523 | 0.816764 | 0.679727 | 0.464327 | 0.691702 | 0.525731 | 0.32924 | 4.669573 | ETHUSDT | 5m |
| Entry Model 2 | medium | 3 | 3 | 0 | 0 | 3 | 1.320269 | 0.457421 | 0.079556 | 0.096173 | 0.333333 | 0.333333 | 0.333333 | 0.0 | 0.333333 | 0.333333 | 3.0 | ETHUSDT | 5m |

## 6. Warnings / skipped events
- Entry Model 3 BTCUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- Entry Model 3 ETHUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
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
- 9616a5714c9e521b: invalid risk (risk is not positive; R metrics are skipped)
- eceeef9f8bb72888: invalid risk (risk is not positive; R metrics are skipped)
- d4572b11e5bd6186: invalid risk (risk is not positive; R metrics are skipped)
- e0699504529538fe: invalid risk (risk is not positive; R metrics are skipped)
- fcebf9d4a2581319: invalid risk (risk is not positive; R metrics are skipped)
- f14d9a28c428742a: invalid risk (risk is not positive; R metrics are skipped)
- ee76aec11431cb2b: invalid risk (risk is not positive; R metrics are skipped)
- 4a0d2a840c0ad22f: invalid risk (risk is not positive; R metrics are skipped)
- 80d3f5ddcfb595f4: invalid risk (risk is not positive; R metrics are skipped)
- b69304189ec34bfa: invalid risk (risk is not positive; R metrics are skipped)
- bb8b1977b04d8a89: invalid risk (risk is not positive; R metrics are skipped)
- bb45b0b5afef14c6: invalid risk (risk is not positive; R metrics are skipped)

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
