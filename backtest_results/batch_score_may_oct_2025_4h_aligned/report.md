# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 26 | 26 | 11 | 10 | 8.660527 | 5.273829 | 0.346154 | 2.679307 | 80.615385 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 | 6.444444 | 1.5 | 1.0 | 1.0 |  | 26 |
| ifvg_retest | 24 | 24 | 23 |  | 35.123343 | 9.722848 | 0.375 | 6.69314 | 98.875 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 | 3.652174 | 1.153846 | 1.1 | 1.0 |  | 18 |
| mitigation_block | 45 | 45 | 45 |  | 1.979989 | 0.774549 | 0.288889 | 0.883132 | 75.244444 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 | 1.0 | 3.5 | 1.555556 | 4.0 |  | 43 |
| reclaimed_ob | 5 | 5 | 5 |  | 12.860001 | 12.01518 | 0.8 | 4.364048 | 83.2 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 | 1.6 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | 44 | 44 | 44 |  | 4.985211 | 2.965326 | 0.704545 | 1.437243 | 80.704545 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 40 |
| turtle_soup | 127 | 127 | 127 |  | 3.84611 | 2.991057 | 0.102362 | 7.876176 | 73.503937 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 | 1.0 | 3.640777 | 2.931034 | 3.647059 |  | 43 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 26 | 26 | 11 | 10 | 8.660527 | 5.273829 | 0.346154 | 2.679307 | 80.615385 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 | 6.444444 | 1.5 | 1.0 | 1.0 |  | 26 |
| ifvg_retest | edge | 24 | 24 | 23 |  | 35.123343 | 9.722848 | 0.375 | 6.69314 | 98.875 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 | 3.652174 | 1.153846 | 1.1 | 1.0 |  | 18 |
| mitigation_block | body_zone_retest | 45 | 45 | 45 |  | 1.979989 | 0.774549 | 0.288889 | 0.883132 | 75.244444 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 | 1.0 | 3.5 | 1.555556 | 4.0 |  | 43 |
| reclaimed_ob | body_edge | 5 | 5 | 5 |  | 12.860001 | 12.01518 | 0.8 | 4.364048 | 83.2 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 | 1.6 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | body_level | 44 | 44 | 44 |  | 4.985211 | 2.965326 | 0.704545 | 1.437243 | 80.704545 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 40 |
| turtle_soup | close | 127 | 127 | 127 |  | 3.84611 | 2.991057 | 0.102362 | 7.876176 | 73.503937 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 | 1.0 | 3.640777 | 2.931034 | 3.647059 |  | 43 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 26 | 26 | 11 | 10 | 8.660527 | 5.273829 | 0.346154 | 2.679307 | 80.615385 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 | 6.444444 | 1.5 | 1.0 | 1.0 |  | 26 |
| ifvg_retest | ce | 24 | 24 | 23 |  | 35.123343 | 9.722848 | 0.375 | 6.69314 | 98.875 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 | 3.652174 | 1.153846 | 1.1 | 1.0 |  | 18 |
| mitigation_block | block_extreme | 45 | 45 | 45 |  | 1.979989 | 0.774549 | 0.288889 | 0.883132 | 75.244444 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 | 1.0 | 3.5 | 1.555556 | 4.0 |  | 43 |
| reclaimed_ob | mean_threshold | 5 | 5 | 5 |  | 12.860001 | 12.01518 | 0.8 | 4.364048 | 83.2 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 | 1.6 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | wick_extreme | 44 | 44 | 44 |  | 4.985211 | 2.965326 | 0.704545 | 1.437243 | 80.704545 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 40 |
| turtle_soup | sweep_extreme | 127 | 127 | 127 |  | 3.84611 | 2.991057 | 0.102362 | 7.876176 | 73.503937 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 | 1.0 | 3.640777 | 2.931034 | 3.647059 |  | 43 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 26 | 26 | 11 | 10 | 8.660527 | 5.273829 | 0.346154 | 2.679307 | 80.615385 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 | 6.444444 | 1.5 | 1.0 | 1.0 |  | 26 |
| ifvg_retest | conservative | 24 | 24 | 23 |  | 35.123343 | 9.722848 | 0.375 | 6.69314 | 98.875 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 | 3.652174 | 1.153846 | 1.1 | 1.0 |  | 18 |
| mitigation_block | conservative | 45 | 45 | 45 |  | 1.979989 | 0.774549 | 0.288889 | 0.883132 | 75.244444 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 | 1.0 | 3.5 | 1.555556 | 4.0 |  | 43 |
| reclaimed_ob | conservative | 5 | 5 | 5 |  | 12.860001 | 12.01518 | 0.8 | 4.364048 | 83.2 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 | 1.6 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | conservative | 44 | 44 | 44 |  | 4.985211 | 2.965326 | 0.704545 | 1.437243 | 80.704545 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 40 |
| turtle_soup | conservative | 127 | 127 | 127 |  | 3.84611 | 2.991057 | 0.102362 | 7.876176 | 73.503937 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 | 1.0 | 3.640777 | 2.931034 | 3.647059 |  | 43 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 271 | 271 | 255 | 10 | 6.918853 | 2.573175 | 0.291513 | 5.001371 | 78.070111 | 0.263838 | 0.291513 | 0.405904 | 0.225092 | 0.605166 | 1.618321 | 3.170732 | 2.072727 | 2.540984 |  | 174 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 14 | 14 | 5 | 5 | 5.602024 | 5.146011 | 0.285714 | 3.054562 | 85.214286 | 0.343966 | 0.285714 | 0.214286 | 0.214286 | 0.071429 | 6.5 | 1.0 | 1.0 | 1.0 |  | 14 |
| breaker_block | premium | 12 | 12 | 6 | 5 | 11.20928 | 7.867165 | 0.416667 | 2.24151 | 75.25 | 1.064913 | 0.416667 | 0.416667 | 0.333333 | 0.083333 | 6.4 | 2.0 | 1.0 | 1.0 |  | 12 |
| ifvg_retest | discount | 14 | 14 | 14 |  | 22.35925 | 8.812728 | 0.357143 | 6.439282 | 100.0 | 3.332968 | 0.357143 | 0.5 | 0.357143 | 0.571429 | 4.642857 | 1.25 | 1.0 | 1.0 |  | 10 |
| ifvg_retest | premium | 10 | 10 | 9 |  | 54.9786 | 10.115068 | 0.4 | 7.04854 | 97.3 | -0.240827 | 0.4 | 0.3 | 0.1 | 0.5 | 2.111111 | 1.0 | 1.333333 | 1.0 |  | 8 |
| mitigation_block | discount | 29 | 29 | 29 |  | 1.350576 | 0.435151 | 0.137931 | 0.996389 | 76.103448 | -0.719459 | 0.137931 | 0.034483 | 0.034483 | 0.862069 | 1.0 | 4.2 | 1.0 | 4.0 |  | 27 |
| mitigation_block | premium | 16 | 16 | 16 |  | 3.120801 | 0.974789 | 0.5625 | 0.677853 | 73.6875 | -0.162981 | 0.5625 | 0.5 |  | 0.4375 | 1.0 | 1.0 | 1.625 |  |  | 16 |
| reclaimed_ob | discount | 3 | 3 | 3 |  | 15.777816 | 12.01518 | 0.666667 | 6.782091 | 92.333333 | 3.266568 | 0.666667 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 2 | 2 | 2 |  | 8.483279 | 8.483279 | 1.0 | 0.736983 | 69.5 | 0.736983 | 1.0 | 1.0 | 0.5 |  | 1.5 |  | 1.0 | 1.0 |  | 2 |
| rejection_block | discount | 26 | 26 | 26 |  | 5.280865 | 2.965326 | 0.615385 | 1.672981 | 80.038462 | 0.176573 | 0.615385 | 0.5 | 0.269231 | 0.384615 | 1.0 | 1.1 | 1.0 | 1.142857 |  | 23 |
| rejection_block | premium | 18 | 18 | 18 |  | 4.558155 | 3.067313 | 0.833333 | 1.096733 | 81.666667 | 0.443667 | 0.833333 | 0.444444 | 0.166667 | 0.166667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 17 |
| turtle_soup | discount | 73 | 73 | 73 |  | 3.851529 | 3.320795 | 0.082192 | 7.377334 | 73.493151 | -0.08213 | 0.082192 | 0.479452 | 0.273973 | 0.808219 | 1.0 | 3.847458 | 3.428571 | 4.35 |  | 27 |
| turtle_soup | premium | 54 | 54 | 54 |  | 3.838785 | 2.110961 | 0.12963 | 8.550537 | 73.518519 | 0.375783 | 0.12963 | 0.425926 | 0.259259 | 0.814815 | 1.0 | 3.363636 | 2.173913 | 2.642857 |  | 16 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 26 | 26 | 11 | 10 | 8.660527 | 5.273829 | 0.346154 | 2.679307 | 80.615385 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 | 6.444444 | 1.5 | 1.0 | 1.0 |  | 26 |
| ifvg_retest | strong | 16 | 16 | 15 |  | 40.751232 | 8.083462 | 0.4375 | 7.872087 | 98.6875 | 2.388797 | 0.4375 | 0.5 | 0.3125 | 0.4375 | 4.0 | 1.142857 | 1.0 | 1.0 |  | 13 |
| ifvg_retest | valid | 8 | 8 | 8 |  | 24.571052 | 9.918958 | 0.25 | 4.335245 | 99.25 | 1.08277 | 0.25 | 0.25 | 0.125 | 0.75 | 3.0 | 1.166667 | 1.5 | 1.0 |  | 5 |
| mitigation_block | none | 45 | 45 | 45 |  | 1.979989 | 0.774549 | 0.288889 | 0.883132 | 75.244444 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 | 1.0 | 3.5 | 1.555556 | 4.0 |  | 43 |
| reclaimed_ob | none | 5 | 5 | 5 |  | 12.860001 | 12.01518 | 0.8 | 4.364048 | 83.2 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 | 1.6 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | none | 44 | 44 | 44 |  | 4.985211 | 2.965326 | 0.704545 | 1.437243 | 80.704545 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 40 |
| turtle_soup | none | 127 | 127 | 127 |  | 3.84611 | 2.991057 | 0.102362 | 7.876176 | 73.503937 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 | 1.0 | 3.640777 | 2.931034 | 3.647059 |  | 43 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 19 | 19 | 8 | 6 | 7.479246 | 6.032545 | 0.315789 | 3.372441 | 87.473684 | 0.730312 | 0.315789 | 0.315789 | 0.263158 | 0.105263 | 6.083333 | 1.5 | 1.0 | 1.0 |  | 19 |
| breaker_block | medium | 7 | 7 | 3 | 4 | 11.81061 | 5.273829 | 0.428571 | 0.797945 | 62.0 | 0.755604 | 0.428571 | 0.285714 | 0.285714 |  | 7.166667 |  | 1.0 | 1.0 |  | 7 |
| ifvg_retest | high | 24 | 24 | 23 |  | 35.123343 | 9.722848 | 0.375 | 6.69314 | 98.875 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 | 3.652174 | 1.153846 | 1.1 | 1.0 |  | 18 |
| mitigation_block | high | 39 | 39 | 39 |  | 2.081548 | 0.553648 | 0.230769 | 0.944453 | 77.282051 | -0.580266 | 0.230769 | 0.153846 | 0.025641 | 0.769231 | 1.0 | 3.666667 | 1.833333 | 4.0 |  | 37 |
| mitigation_block | medium | 6 | 6 | 6 |  | 1.319856 | 1.265115 | 0.666667 | 0.484545 | 62.0 | -0.140273 | 0.666667 | 0.5 |  | 0.333333 | 1.0 | 1.0 | 1.0 |  |  | 6 |
| reclaimed_ob | high | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 5.196088 | 88.5 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | medium | 1 | 1 | 1 |  | 13.059224 | 13.059224 | 1.0 | 1.035887 | 62.0 | 1.035887 | 1.0 | 1.0 |  |  | 1.0 |  | 1.0 |  |  | 1 |
| rejection_block | high | 38 | 38 | 38 |  | 5.371843 | 2.965326 | 0.657895 | 1.622806 | 83.657895 | 0.2896 | 0.657895 | 0.447368 | 0.263158 | 0.342105 | 1.0 | 1.076923 | 1.0 | 1.1 |  | 34 |
| rejection_block | medium | 6 | 6 | 6 |  | 2.536539 | 2.691597 | 1.0 | 0.262015 | 62.0 | 0.262015 | 1.0 | 0.666667 |  |  | 1.0 |  | 1.0 |  |  | 6 |
| turtle_soup | high | 85 | 85 | 85 |  | 3.983199 | 3.003668 | 0.070588 | 9.165708 | 79.882353 | 0.051958 | 0.070588 | 0.447059 | 0.282353 | 0.847059 | 1.0 | 3.708333 | 2.710526 | 3.916667 |  | 1 |
| turtle_soup | low | 4 | 4 | 4 |  | 1.0348 | 0.795213 |  | 1.287145 | 45.0 | -0.475495 |  | 0.25 |  | 0.75 | 1.0 | 3.0 | 16.0 |  |  | 4 |
| turtle_soup | medium | 38 | 38 | 38 |  | 3.83539 | 3.486445 | 0.184211 | 5.685278 | 62.236842 | 0.310063 | 0.184211 | 0.5 | 0.263158 | 0.736842 | 1.0 | 3.535714 | 2.684211 | 3.0 |  | 38 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | insufficient_displacement | 3 | 3 | 1 | 1 | 19.857954 | 19.857954 | 0.333333 | 9.36493 | 99.0 | 4.806316 | 0.333333 | 0.333333 | 0.333333 |  | 5.5 |  | 1.0 | 1.0 |  | 3 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 5 | 5 | 3 | 1 | 4.893397 | 3.912926 | 0.4 | 0.88969 | 82.6 | 0.16548 | 0.4 | 0.2 | 0.2 | 0.2 | 4.5 | 1.0 | 1.0 | 1.0 |  | 5 |
| breaker_block | poor_pd_location;insufficient_displacement | 4 | 4 | 1 | 2 | 1.505394 | 1.505394 |  | 5.774348 | 95.0 | -1.0 |  | 0.25 |  | 0.25 | 7.5 | 2.0 | 1.0 |  |  | 4 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_2 | 13 | 13 | 6 | 5 | 9.870377 | 6.728873 | 0.461538 | 0.853177 | 71.230769 | 0.634426 | 0.461538 | 0.384615 | 0.384615 |  | 6.111111 |  | 1.0 | 1.0 |  | 13 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_3 | 1 | 1 |  | 1 |  |  |  | 2.930064 | 80.0 |  |  |  |  |  | 17.0 |  |  |  |  | 1 |
| ifvg_retest | none | 6 | 6 | 6 |  | 44.096741 | 35.555607 | 0.166667 | 7.589857 | 100.0 | 1.494599 | 0.166667 | 0.166667 | 0.166667 | 0.833333 | 1.666667 | 1.0 | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 5 | 5 | 4 |  | 114.345833 | 24.39224 | 0.2 | 21.081922 | 99.4 | 8.906443 | 0.2 | 0.4 | 0.4 | 0.4 | 5.75 | 1.0 | 1.0 | 1.0 |  | 5 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 4 | 4 | 4 |  | 5.542064 | 5.336161 | 0.75 | 0.466588 | 94.75 | 0.093782 | 0.75 | 0.5 | 0.25 | 0.25 | 6.25 | 1.0 | 1.5 | 1.0 |  | 4 |
| ifvg_retest | poor_pd_location;target_rr_below_3 | 1 | 1 | 1 |  | 7.902607 | 7.902607 | 1.0 | 2.694071 | 100.0 | 2.694071 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | target_rr_below_2 | 8 | 8 | 8 |  | 6.975281 | 3.749653 | 0.375 | 0.640772 | 99.625 | -0.396057 | 0.375 | 0.5 | 0.125 | 0.625 | 3.125 | 1.4 | 1.0 | 1.0 |  | 8 |
| mitigation_block | none | 2 | 2 | 2 |  | 3.46526 | 3.46526 | 0.5 | 3.458389 | 98.5 | 1.175986 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.0 | 1.0 | 4.0 |  |  |
| mitigation_block | poor_pd_location;target_rr_below_2 | 28 | 28 | 28 |  | 0.850724 | 0.494399 | 0.214286 | 0.646046 | 70.285714 | -0.711962 | 0.214286 | 0.142857 |  | 0.785714 | 1.0 | 4.636364 | 1.0 |  |  | 28 |
| mitigation_block | poor_pd_location;target_rr_below_3 | 4 | 4 | 4 |  | 0.832271 | 0.832271 |  | 2.250943 | 76.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 4 |
| mitigation_block | target_rr_below_2 | 11 | 11 | 11 |  | 5.001785 | 1.644061 | 0.545455 | 0.52101 | 83.363636 | -0.171731 | 0.545455 | 0.363636 |  | 0.454545 | 1.0 | 1.0 | 2.25 |  |  | 11 |
| reclaimed_ob | none | 1 | 1 | 1 |  | 12.01518 | 12.01518 | 1.0 | 8.42623 | 100.0 | 8.42623 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  |  |
| reclaimed_ob | poor_pd_location | 1 | 1 | 1 |  | 6.779888 | 6.779888 |  | 9.546568 | 90.0 | -1.0 |  |  |  | 1.0 | 2.0 | 1.0 |  |  |  | 1 |
| reclaimed_ob | poor_pd_location;target_rr_below_2 | 1 | 1 | 1 |  | 13.059224 | 13.059224 | 1.0 | 1.035887 | 62.0 | 1.035887 | 1.0 | 1.0 |  |  | 1.0 |  | 1.0 |  |  | 1 |
| reclaimed_ob | target_rr_below_2 | 1 | 1 | 1 |  | 3.907334 | 3.907334 | 1.0 | 0.43808 | 77.0 | 0.43808 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  | 1 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 28.538381 | 28.538381 | 1.0 | 2.373474 | 87.0 | 2.373474 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | none | 4 | 4 | 4 |  | 6.40472 | 5.42097 |  | 7.257456 | 98.0 | -1.0 |  | 0.25 | 0.25 | 1.0 | 1.0 | 1.25 | 1.0 | 1.0 |  |  |
