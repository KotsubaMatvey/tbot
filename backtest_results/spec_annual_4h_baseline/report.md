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
| ifvg_retest | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | body_edge | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | body_level | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | mean_threshold | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | wick_extreme | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | conservative | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | conservative | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 74 | 74 | 21 |  | 4.108468 | 0.923018 | 0.040541 | 15.108066 | 96.810811 | -0.196404 | -0.156077 | -0.156077 | 0.040541 | 0.081081 | 0.040541 | 0.22973 | 4.0 | 3.941176 | 1.5 | 1.666667 |  | 18 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | premium | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | discount | 3 | 3 | 1 |  | 36.524943 | 36.524943 | 0.333333 | 10.043191 | 91.333333 | 1.725836 | 1.362918 | 1.362918 | 0.333333 | 0.333333 | 0.333333 |  | 1.666667 |  | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 6 | 6 | 2 |  | 11.648321 | 11.648321 | 0.166667 | 7.963103 | 100.0 | 4.790205 | 2.395103 | 2.395103 | 0.166667 | 0.166667 | 0.166667 | 0.166667 | 1.833333 | 1.0 | 1.0 | 1.0 |  | 1 |
| rejection_block | discount | 22 | 22 | 9 |  | 1.297132 | 0.636546 | 0.045455 | 6.084204 | 92.5 | -0.714526 | -0.381193 | -0.381193 | 0.045455 | 0.090909 | 0.045455 | 0.318182 | 4.764706 | 4.428571 | 2.5 | 3.0 |  | 11 |
| rejection_block | premium | 42 | 42 | 9 |  | 1.642451 | 0.923018 |  | 21.472399 | 98.928571 | -1.0 | -0.666667 | -0.666667 |  | 0.047619 |  | 0.214286 | 4.111111 | 3.888889 | 1.0 |  |  | 4 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | valid | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | none | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | none | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | high | 9 | 9 | 3 |  | 19.940528 | 15.879401 | 0.222222 | 8.656466 | 97.111111 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 | 1.777778 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | high | 64 | 64 | 18 |  | 1.469791 | 0.79004 | 0.015625 | 16.182707 | 96.71875 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 | 4.363636 | 4.125 | 1.75 | 3.0 |  | 15 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  | 8.0 |  |  |  |  |  |
| reclaimed_ob | none | 6 | 6 | 2 |  | 11.648321 | 11.648321 | 0.166667 | 12.453966 | 100.0 | 4.790205 | 2.395103 | 2.395103 | 0.166667 | 0.166667 | 0.166667 | 0.166667 | 1.833333 | 1.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 3 | 3 | 1 |  | 36.524943 | 36.524943 | 0.333333 | 1.061464 | 91.333333 | 1.725836 | 1.362918 | 1.362918 | 0.333333 | 0.333333 | 0.333333 |  | 1.666667 |  | 1.0 | 1.0 |  | 3 |
| rejection_block | none | 49 | 49 | 12 |  | 1.48222 | 0.889094 |  | 20.740699 | 99.510204 | -1.0 | -0.625 | -0.625 |  | 0.061224 | 0.020408 | 0.244898 | 3.83871 | 4.25 | 1.0 | 3.0 |  |  |
| rejection_block | target_rr_below_2 | 13 | 13 | 5 |  | 1.063032 | 0.5094 | 0.076923 | 1.101425 | 86.076923 | -0.486147 | -0.486147 | -0.486147 | 0.076923 |  |  | 0.230769 | 6.181818 | 2.333333 |  |  |  | 13 |
| rejection_block | target_rr_below_3 | 2 | 2 | 1 |  | 3.35444 | 3.35444 |  | 2.540238 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.5 |  | 0.5 | 2.5 | 8.0 | 4.0 |  |  | 2 |
