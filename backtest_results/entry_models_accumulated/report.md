# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m, 1h
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- generated_at: 2026-04-23T22:46:18.894210+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 1439
- warnings: 0
- skipped_outcome_events: 179

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 517 | 451 | 66 | 234 | 283 | 2.516768 | 1.330786 | 2.575044 | 1.037103 | 0.807095 | 0.609756 | 0.365854 | 0.564797 | 0.523282 | 0.297118 | 3.694391 | ETHUSDT | 1h |
| Entry Model 2 | 787 | 681 | 105 | 394 | 393 | 3.049493 | 1.875 | 2.904889 | 1.673726 | 0.810573 | 0.69163 | 0.469897 | 0.66582 | 0.54185 | 0.337739 | 4.395172 | BTCUSDT | 1h |
| Entry Model 3 | 135 | 127 | 8 | 63 | 72 | 10.058389 | 2.740019 | 33.639103 | 3.100023 | 0.84252 | 0.76378 | 0.614173 | 0.748148 | 0.551181 | 0.370079 | 3.955556 | BTCUSDT | 15m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 234 | 207 | 27 | 234 | 0 | 2.903634 | 1.451193 | 1.794314 | 0.831557 | 0.830918 | 0.63285 | 0.405797 | 0.508547 | 0.531401 | 0.318841 | 3.705128 | ETHUSDT | 1h |
| Entry Model 1 | short | 283 | 244 | 39 | 0 | 283 | 2.188565 | 1.173974 | 3.237384 | 1.218028 | 0.786885 | 0.590164 | 0.331967 | 0.611307 | 0.516393 | 0.278689 | 3.685512 | ETHUSDT | 15m |
| Entry Model 2 | long | 394 | 348 | 45 | 394 | 0 | 3.481476 | 2.143842 | 2.57381 | 1.378054 | 0.816092 | 0.706897 | 0.520115 | 0.619289 | 0.545977 | 0.373563 | 4.398477 | BTCUSDT | 1h |
| Entry Model 2 | short | 393 | 333 | 60 | 0 | 393 | 2.598052 | 1.692377 | 3.250881 | 1.868878 | 0.804805 | 0.675676 | 0.417417 | 0.712468 | 0.537538 | 0.3003 | 4.391858 | BTCUSDT | 15m |
| Entry Model 3 | long | 63 | 58 | 5 | 63 | 0 | 7.29115 | 3.336077 | 4.001666 | 2.600792 | 0.862069 | 0.793103 | 0.672414 | 0.714286 | 0.568966 | 0.362069 | 3.952381 | BTCUSDT | 1h |
| Entry Model 3 | short | 72 | 69 | 3 | 0 | 72 | 12.384473 | 2.254565 | 58.551731 | 3.629159 | 0.826087 | 0.73913 | 0.565217 | 0.777778 | 0.536232 | 0.376812 | 3.958333 | BTCUSDT | 15m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 267 | 236 | 31 | 116 | 151 | 2.319653 | 1.368944 | 2.131749 | 0.852806 | 0.877119 | 0.661017 | 0.381356 | 0.524345 | 0.580508 | 0.322034 | 3.842697 | BTCUSDT | 15m |
| Entry Model 1 | 1h | 250 | 215 | 35 | 118 | 132 | 2.733135 | 1.294451 | 3.061637 | 1.273937 | 0.730233 | 0.553488 | 0.348837 | 0.608 | 0.460465 | 0.269767 | 3.536 | ETHUSDT | 1h |
| Entry Model 2 | 15m | 410 | 351 | 59 | 208 | 202 | 2.911243 | 1.727088 | 2.977358 | 1.685248 | 0.826211 | 0.695157 | 0.42735 | 0.668293 | 0.552707 | 0.304843 | 4.519512 | BTCUSDT | 15m |
| Entry Model 2 | 1h | 377 | 330 | 46 | 186 | 191 | 3.196541 | 2.106726 | 2.827808 | 1.634708 | 0.793939 | 0.687879 | 0.515152 | 0.66313 | 0.530303 | 0.372727 | 4.259947 | BTCUSDT | 1h |
| Entry Model 3 | 15m | 82 | 77 | 5 | 38 | 44 | 11.54769 | 2.176796 | 50.811368 | 2.955303 | 0.844156 | 0.714286 | 0.506494 | 0.743902 | 0.506494 | 0.324675 | 3.963415 | BTCUSDT | 15m |
| Entry Model 3 | 1h | 53 | 50 | 3 | 25 | 28 | 7.764864 | 4.190992 | 7.193815 | 3.389278 | 0.84 | 0.84 | 0.78 | 0.754717 | 0.62 | 0.44 | 3.943396 | BTCUSDT | 1h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 368 | 327 | 41 | 167 | 201 | 2.769525 | 1.368432 | 3.051775 | 1.333089 | 0.816514 | 0.614679 | 0.379205 | 0.61413 | 0.513761 | 0.302752 | 4.0 | ETHUSDT | 1h |
| Entry Model 1 | low | 9 | 9 | 0 | 2 | 7 | 1.659948 | 1.126729 | 0.910525 | 0.300891 | 1.0 | 0.777778 | 0.111111 | 0.222222 | 0.777778 | 0.111111 | 2.0 | BTCUSDT | 1h |
| Entry Model 1 | medium | 140 | 115 | 25 | 65 | 75 | 1.865111 | 1.301391 | 1.349737 | 0.755745 | 0.765217 | 0.582609 | 0.347826 | 0.457143 | 0.530435 | 0.295652 | 3.0 | ETHUSDT | 15m |
| Entry Model 2 | high | 781 | 676 | 104 | 391 | 390 | 3.049683 | 1.855691 | 2.892363 | 1.673157 | 0.809172 | 0.689349 | 0.468935 | 0.663252 | 0.54142 | 0.338757 | 4.40589 | BTCUSDT | 1h |
| Entry Model 2 | medium | 6 | 5 | 1 | 3 | 3 | 3.023838 | 2.572073 | 4.59835 | 1.946312 | 1.0 | 1.0 | 0.6 | 1.0 | 0.6 | 0.2 | 3.0 | BTCUSDT | 1h |
| Entry Model 3 | high | 129 | 122 | 7 | 60 | 69 | 10.402583 | 2.909679 | 34.913942 | 3.271288 | 0.852459 | 0.770492 | 0.631148 | 0.75969 | 0.557377 | 0.377049 | 4.0 | BTCUSDT | 15m |
| Entry Model 3 | medium | 6 | 5 | 1 | 3 | 3 | 1.660039 | 1.118476 | 2.533034 | 2.147429 | 0.6 | 0.6 | 0.2 | 0.5 | 0.4 | 0.2 | 3.0 | ETHUSDT | 1h |

## 6. Warnings / skipped events
- c28400f07f11006b: invalid risk (risk is not positive; R metrics are skipped)
- ca2637ce7b0bbfa2: invalid risk (risk is not positive; R metrics are skipped)
- efcb119ff120cbbf: invalid risk (risk is not positive; R metrics are skipped)
- 3a7148e257dc31c7: invalid risk (risk is not positive; R metrics are skipped)
- 58011dc1f1cdb7f2: invalid risk (risk is not positive; R metrics are skipped)
- e3f96f36d0399252: invalid risk (risk is not positive; R metrics are skipped)
- d9c10579eef4c5c5: invalid risk (risk is not positive; R metrics are skipped)
- 440f39d63924fbeb: invalid risk (risk is not positive; R metrics are skipped)
- b006401f210e9d7f: invalid risk (risk is not positive; R metrics are skipped)
- ab94ff6e22b8acf3: invalid risk (risk is not positive; R metrics are skipped)
- d3a4b1764961edab: invalid risk (risk is not positive; R metrics are skipped)
- 5603fe30b31e56b8: invalid risk (risk is not positive; R metrics are skipped)
- e54dd349db32f42e: invalid risk (risk is not positive; R metrics are skipped)
- 8d41e87cedd0c961: invalid risk (risk is not positive; R metrics are skipped)
- 8e25b73612896949: invalid risk (risk is not positive; R metrics are skipped)
- 43a63946c330a8f9: invalid risk (risk is not positive; R metrics are skipped)
- 4eb62a6fb56303e9: invalid risk (risk is not positive; R metrics are skipped)
- 9aaa6edf4cfbf918: invalid risk (risk is not positive; R metrics are skipped)
- 3380cd65c43d7904: invalid risk (risk is not positive; R metrics are skipped)
- 56f79588d2c018b2: invalid risk (risk is not positive; R metrics are skipped)
- 4758b697e3227dff: invalid risk (risk is not positive; R metrics are skipped)
- 5e195aa27c306500: invalid risk (risk is not positive; R metrics are skipped)
- cf13b140b0a09684: invalid risk (risk is not positive; R metrics are skipped)
- 84e0d01511b1927c: invalid risk (risk is not positive; R metrics are skipped)
- 787ad7edd747a720: invalid risk (risk is not positive; R metrics are skipped)
- 8048e77c0c9b3358: invalid risk (risk is not positive; R metrics are skipped)
- b17e83a0d9bd44f0: invalid risk (risk is not positive; R metrics are skipped)
- 81ad8e5cef4b7d2a: invalid risk (risk is not positive; R metrics are skipped)
- 2247f6e30173e15e: invalid risk (risk is not positive; R metrics are skipped)
- f609620eac89a0c5: invalid risk (risk is not positive; R metrics are skipped)
- 51eb6eb50d03819c: invalid risk (risk is not positive; R metrics are skipped)
- a1d37118cdbd56ff: invalid risk (risk is not positive; R metrics are skipped)
- 3739af9402a1a5c5: invalid risk (risk is not positive; R metrics are skipped)
- c1c2b2de863db683: invalid risk (risk is not positive; R metrics are skipped)
- a9413a4160d4d1d6: invalid risk (risk is not positive; R metrics are skipped)
- e00e92fa62be1811: invalid risk (risk is not positive; R metrics are skipped)
- 30c9c5aed8495ea3: invalid risk (risk is not positive; R metrics are skipped)
- e839e188ac56f9b9: invalid risk (risk is not positive; R metrics are skipped)
- 77c5f2d0c694d2f5: invalid risk (risk is not positive; R metrics are skipped)
- 93c25c15ed1b135d: invalid risk (risk is not positive; R metrics are skipped)
- 440c68a4514919a6: invalid risk (risk is not positive; R metrics are skipped)
- 7bb461b00a70e162: invalid risk (risk is not positive; R metrics are skipped)
- d64de26f9700a25c: invalid risk (risk is not positive; R metrics are skipped)
- 340e1e9d1b0bb21c: invalid risk (risk is not positive; R metrics are skipped)
- 39623599dae8d918: invalid risk (risk is not positive; R metrics are skipped)
- ef52263428d2e05d: invalid risk (risk is not positive; R metrics are skipped)
- 4759871c5dac9c6d: invalid risk (risk is not positive; R metrics are skipped)
- a8aed6e14c14bd69: invalid risk (risk is not positive; R metrics are skipped)
- 32607efa78de6845: invalid risk (risk is not positive; R metrics are skipped)
- e633a13b24554be1: invalid risk (risk is not positive; R metrics are skipped)

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
