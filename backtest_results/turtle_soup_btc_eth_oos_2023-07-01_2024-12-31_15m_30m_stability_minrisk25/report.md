# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m, 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 604 | 604 | 604 |  | 10.00841 | 6.151474 | 0.322848 | 6.014039 | 67.334437 | 0.703504 | 0.380543 | -0.460467 | -0.460467 | 0.840705 | 0.000305 | 0.84101 | 0.322848 | 0.68543 | 0.529801 | 0.662252 | 1.0 | 3.2525 | 1.181159 | 1.43125 | 284 | 176 |
| turtle_soup | ETHUSDT | 600 | 600 | 600 |  | 10.489895 | 6.099064 | 0.276667 | 7.236803 | 68.166667 | 0.740517 | 0.422565 | -0.336585 | -0.336585 | 0.759724 | -0.000574 | 0.75915 | 0.276667 | 0.71 | 0.541667 | 0.701667 | 1.0 | 3.190024 | 1.223005 | 1.476923 | 311 | 138 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 530 | 530 | 530 |  | 6.33064 | 4.118589 | 0.320755 | 4.38292 | 65.339623 | 0.377549 | 0.517411 | -0.003347 | -0.003347 | 0.5208 | -4.2e-05 | 0.520758 | 0.320755 | 0.754717 | 0.45283 | 0.658491 | 1.0 | 3.389685 | 1.3325 | 1.841667 | 193 | 215 |
| turtle_soup | valid | 674 | 674 | 674 |  | 13.329047 | 9.259736 | 0.283383 | 8.385184 | 69.643917 | 0.992768 | 0.310325 | -0.709642 | -0.709642 | 1.020172 | -0.000205 | 1.019967 | 0.283383 | 0.652819 | 0.60089 | 0.700297 | 1.0 | 3.095339 | 1.084091 | 1.224691 | 402 | 99 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1204 | 1204 | 1204 |  | 10.248353 | 6.11121 | 0.299834 | 6.62339 | 67.749169 | 0.721949 | 0.401484 | -0.398731 | -0.398731 | 0.800349 | -0.000133 | 0.800216 | 0.299834 | 0.697674 | 0.535714 | 0.681894 | 1.0 | 3.220463 | 1.202381 | 1.454264 | 595 | 314 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 914 | 914 | 914 |  | 11.604182 | 7.478619 | 0.237418 | 8.160229 | 72.045952 | 0.855897 | 0.386309 | -0.530494 | -0.530494 | 0.917212 | -0.000409 | 0.916803 | 0.237418 | 0.691466 | 0.583151 | 0.7407 | 1.0 | 3.184638 | 1.077532 | 1.358349 | 539 | 24 |
| turtle_soup | medium | 290 | 290 | 290 |  | 5.975155 | 3.404363 | 0.496552 | 1.779697 | 54.206897 | 0.299782 | 0.449314 | 0.016547 | 0.016547 | 0.43203 | 0.000737 | 0.432767 | 0.496552 | 0.717241 | 0.386207 | 0.496552 | 1.0 | 3.388889 | 1.581731 | 1.910714 | 56 | 290 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 890 | 890 | 890 |  | 11.696467 | 7.482378 | 0.225843 | 8.336612 | 71.977528 | 0.865752 | 0.375281 | -0.549406 | -0.549406 | 0.925146 | -0.00046 | 0.924687 | 0.225843 | 0.68764 | 0.58764 | 0.751685 | 1.0 | 3.19432 | 1.045752 | 1.365201 | 535 |  |
| turtle_soup | target_rr_below_2 | 181 | 181 | 181 |  | 5.12663 | 3.295502 | 0.618785 | 1.227122 | 51.436464 | 0.329104 | 0.38888 | 0.006827 | 0.006827 | 0.381245 | 0.000809 | 0.382054 | 0.618785 | 0.674033 | 0.320442 | 0.381215 | 1.0 | 3.217391 | 1.631148 | 1.551724 | 24 | 181 |
| turtle_soup | target_rr_below_3 | 133 | 133 | 133 |  | 7.528131 | 3.928448 | 0.360902 | 2.502767 | 61.654135 | 0.294282 | 0.593985 | 0.057617 | 0.057617 | 0.535598 | 0.000769 | 0.536368 | 0.360902 | 0.796992 | 0.481203 | 0.62406 | 1.0 | 3.433735 | 1.613208 | 2.09375 | 36 | 133 |
