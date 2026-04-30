# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 15 | 15 | 5 |  | 8.982657 | 2.038557 | 0.2 | 2.942714 | 99.466667 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 | 5.714286 | 2.0 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 15 | 15 | 5 |  | 8.982657 | 2.038557 | 0.2 | 2.942714 | 99.466667 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 | 5.714286 | 2.0 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | body_edge | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | body_level | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 15 | 15 | 5 |  | 8.982657 | 2.038557 | 0.2 | 2.942714 | 99.466667 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 | 5.714286 | 2.0 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | mean_threshold | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | wick_extreme | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 15 | 15 | 5 |  | 8.982657 | 2.038557 | 0.2 | 2.942714 | 99.466667 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 | 5.714286 | 2.0 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | conservative | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | conservative | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 49 | 49 | 33 |  | 5.35022 | 2.038557 | 0.285714 | 2.410096 | 94.428571 | 0.309496 | 0.307646 | 0.307646 | 0.285714 | 0.265306 | 0.163265 | 0.387755 | 2.520833 | 2.157895 | 1.076923 | 1.125 |  | 35 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 7 | 7 | 4 |  | 3.690693 | 1.529003 | 0.285714 | 2.917882 | 98.857143 | 0.701518 | 0.816063 | 0.816063 | 0.285714 | 0.428571 | 0.142857 | 0.285714 | 4.5 | 2.0 | 1.0 | 1.0 |  | 4 |
| ifvg_retest | premium | 8 | 8 | 1 |  | 30.150513 | 30.150513 | 0.125 | 2.964442 | 100.0 | 11.146421 | 8.102495 | 8.102495 | 0.125 | 0.125 | 0.125 |  | 6.625 |  | 1.0 | 1.0 |  | 5 |
| reclaimed_ob | discount | 3 | 3 | 1 |  | 36.524943 | 36.524943 | 0.333333 | 3.415342 | 91.333333 | 1.033878 | 1.023715 | 1.023715 | 0.333333 | 0.333333 | 0.333333 |  | 1.666667 |  | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 6 | 6 | 2 |  | 11.648321 | 11.648321 | 0.166667 | 1.920704 | 92.5 | -0.14446 | -0.101122 | -0.101122 | 0.166667 | 0.166667 | 0.166667 | 0.166667 | 1.833333 | 1.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | discount | 6 | 6 | 6 |  | 3.278649 | 3.541359 | 0.166667 | 1.764987 | 86.0 | -0.602101 | -0.188137 | -0.188137 | 0.166667 | 0.5 | 0.166667 | 0.833333 | 1.0 | 3.2 | 1.333333 | 1.0 |  | 6 |
| rejection_block | premium | 19 | 19 | 19 |  | 2.744763 | 1.340261 | 0.421053 | 2.189148 | 94.210526 | -0.045867 | -0.04774 | -0.04774 | 0.421053 | 0.210526 | 0.157895 | 0.578947 | 1.0 | 1.818182 | 1.0 | 1.333333 |  | 14 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 10 | 10 | 4 |  | 11.038622 | 6.492262 | 0.3 | 3.224273 | 100.0 | 3.738123 | 3.091686 | 3.091686 | 0.3 | 0.4 | 0.2 | 0.1 | 5.555556 | 2.0 | 1.0 | 1.0 |  | 6 |
| ifvg_retest | valid | 5 | 5 | 1 |  | 0.758798 | 0.758798 |  | 2.379597 | 98.4 | -1.0 | -1.0 | -1.0 |  |  |  | 0.2 | 6.0 | 2.0 |  |  |  | 3 |
| reclaimed_ob | none | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | none | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 15 | 15 | 5 |  | 8.982657 | 2.038557 | 0.2 | 2.942714 | 99.466667 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 | 5.714286 | 2.0 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | high | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 2.418917 | 92.111111 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | high | 25 | 25 | 25 |  | 2.872896 | 1.357874 | 0.36 | 2.087349 | 92.24 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 | 1.0 | 2.25 | 1.142857 | 1.25 |  | 20 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 6 | 6 | 2 |  | 20.54824 | 20.54824 | 0.333333 | 6.126871 | 100.0 | 7.758486 | 5.73094 | 5.73094 | 0.333333 | 0.333333 | 0.333333 |  | 8.4 |  | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 9 | 9 | 3 |  | 1.272268 | 1.019449 | 0.111111 | 0.819943 | 99.111111 | -0.521493 | -0.031712 | -0.031712 | 0.111111 | 0.222222 |  | 0.222222 | 4.222222 | 2.0 | 1.0 |  |  | 9 |
| reclaimed_ob | none | 3 | 3 |  |  |  |  |  | 5.607857 | 100.0 |  |  |  |  |  |  |  | 2.333333 |  |  |  |  |  |
| reclaimed_ob | target_rr_below_2 | 6 | 6 | 3 |  | 19.940528 | 15.879401 | 0.333333 | 0.824446 | 88.166667 | 0.248319 | 0.273823 | 0.273823 | 0.333333 | 0.333333 | 0.333333 | 0.166667 | 1.5 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | none | 5 | 5 | 5 |  | 5.958891 | 7.250988 | 0.2 | 5.774961 | 100.0 | 0.299235 | 0.289465 | 0.289465 | 0.2 | 0.4 | 0.4 | 0.8 | 1.0 | 2.0 | 1.0 | 1.5 |  |  |
| rejection_block | target_rr_below_2 | 18 | 18 | 18 |  | 2.191583 | 1.321839 | 0.444444 | 1.006637 | 90.222222 | -0.221125 | -0.082401 | -0.082401 | 0.444444 | 0.277778 | 0.111111 | 0.555556 | 1.0 | 2.4 | 1.2 | 1.0 |  | 18 |
| rejection_block | target_rr_below_3 | 2 | 2 | 2 |  | 1.289724 | 1.289724 |  | 2.594738 | 91.0 | -1.0 | -1.0 | -1.0 |  |  |  | 1.0 | 1.0 | 2.0 |  |  |  | 2 |
