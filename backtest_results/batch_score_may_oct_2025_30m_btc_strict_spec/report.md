# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 17 | 17 | 17 |  | 15.22715 | 9.193407 | 0.294118 | 3.197427 | 100.0 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 | 2.705882 | 1.5 | 1.285714 | 1.0 |  | 11 |
| reclaimed_ob | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 17 | 17 | 17 |  | 15.22715 | 9.193407 | 0.294118 | 3.197427 | 100.0 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 | 2.705882 | 1.5 | 1.285714 | 1.0 |  | 11 |
| reclaimed_ob | body_edge | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | body_level | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 17 | 17 | 17 |  | 15.22715 | 9.193407 | 0.294118 | 3.197427 | 100.0 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 | 2.705882 | 1.5 | 1.285714 | 1.0 |  | 11 |
| reclaimed_ob | mean_threshold | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | wick_extreme | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 17 | 17 | 17 |  | 15.22715 | 9.193407 | 0.294118 | 3.197427 | 100.0 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 | 2.705882 | 1.5 | 1.285714 | 1.0 |  | 11 |
| reclaimed_ob | conservative | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | conservative | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 55 | 55 | 53 | 2 | 8.790077 | 5.182974 | 0.381818 | 3.402272 | 94.327273 | 0.133262 | 0.381818 | 0.436364 | 0.327273 | 0.563636 | 1.763636 | 1.548387 | 2.166667 | 1.055556 |  | 38 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 14 | 14 | 14 |  | 14.616715 | 9.88337 | 0.214286 | 3.231077 | 100.0 | -0.436245 | 0.214286 | 0.357143 | 0.285714 | 0.785714 | 3.071429 | 1.545455 | 1.4 | 1.0 |  | 9 |
| ifvg_retest | premium | 3 | 3 | 3 |  | 18.075844 | 6.781316 | 0.666667 | 3.040395 | 100.0 | 2.229766 | 0.666667 | 0.666667 | 0.666667 | 0.333333 | 1.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | discount | 7 | 7 | 6 | 1 | 7.432191 | 6.412403 | 0.285714 | 3.36776 | 92.142857 | -0.058554 | 0.285714 | 0.428571 | 0.285714 | 0.571429 | 2.142857 | 1.75 | 1.0 | 1.0 |  | 5 |
| reclaimed_ob | premium | 3 | 3 | 2 | 1 | 13.187832 | 13.187832 | 0.333333 | 16.059418 | 98.333333 | 0.5 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 2.666667 | 4.0 | 1.0 | 1.0 |  | 1 |
| rejection_block | discount | 27 | 27 | 27 |  | 4.916663 | 3.18275 | 0.444444 | 2.191567 | 91.222222 | 0.147722 | 0.444444 | 0.407407 | 0.259259 | 0.518519 | 1.0 | 1.357143 | 3.363636 | 1.142857 |  | 20 |
| rejection_block | premium | 1 | 1 | 1 |  | 3.293847 | 3.293847 | 1.0 | 1.843853 | 85.0 | 1.843853 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 5 | 5 | 5 |  | 14.434222 | 12.057696 |  | 2.765948 | 100.0 | -1.0 |  | 0.2 | 0.2 | 1.0 | 4.6 | 1.2 | 1.0 | 1.0 |  | 3 |
| ifvg_retest | valid | 12 | 12 | 12 |  | 15.557536 | 9.134894 | 0.416667 | 3.37721 | 100.0 | 0.465156 | 0.416667 | 0.5 | 0.416667 | 0.583333 | 1.916667 | 1.714286 | 1.333333 | 1.0 |  | 8 |
| reclaimed_ob | none | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | none | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 17 | 17 | 17 |  | 15.22715 | 9.193407 | 0.294118 | 3.197427 | 100.0 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 | 2.705882 | 1.5 | 1.285714 | 1.0 |  | 11 |
| reclaimed_ob | high | 10 | 10 | 8 | 2 | 8.871101 | 7.701916 | 0.3 | 7.175258 | 94.0 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 | 2.3 | 2.2 | 1.0 | 1.0 |  | 6 |
| rejection_block | high | 28 | 28 | 28 |  | 4.858705 | 3.238299 | 0.464286 | 2.179148 | 91.0 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 | 1.0 | 1.357143 | 3.166667 | 1.125 |  | 21 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 6 | 6 | 6 |  | 11.484027 | 8.843601 | 0.166667 | 6.315378 | 100.0 | 0.046112 | 0.166667 | 0.333333 | 0.333333 | 0.833333 | 2.833333 | 1.6 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 8 | 8 | 8 |  | 21.283119 | 18.077794 | 0.25 | 1.116571 | 100.0 | -0.462639 | 0.25 | 0.25 | 0.125 | 0.75 | 2.0 | 1.333333 | 2.0 | 1.0 |  | 8 |
| ifvg_retest | target_rr_below_3 | 3 | 3 | 3 |  | 6.564142 | 6.512768 | 0.666667 | 2.510475 | 100.0 | 1.335436 | 0.666667 | 1.0 | 1.0 | 0.333333 | 4.333333 | 2.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 4 | 4 | 3 | 1 | 14.048108 | 11.612722 | 0.25 | 15.915242 | 100.0 | 0.476849 | 0.25 | 0.75 | 0.75 | 0.5 | 2.75 | 4.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 3 | 3 | 2 | 1 | 8.835323 | 8.835323 | 0.333333 | 0.697203 | 85.0 | -0.390935 | 0.333333 | 0.333333 |  | 0.333333 | 2.0 | 1.0 | 1.0 |  |  | 3 |
| reclaimed_ob | target_rr_below_3 | 3 | 3 | 3 |  | 3.717947 | 3.044922 | 0.333333 | 2.0 | 95.0 |  | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 2.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | none | 7 | 7 | 7 |  | 4.907722 | 2.652439 | 0.142857 | 5.292769 | 100.0 | -0.427696 | 0.142857 | 0.285714 | 0.285714 | 0.857143 | 1.0 | 1.333333 | 1.0 | 1.0 |  |  |
| rejection_block | target_rr_below_2 | 19 | 19 | 19 |  | 4.921654 | 3.430551 | 0.578947 | 1.010424 | 87.263158 | 0.250542 | 0.578947 | 0.421053 | 0.263158 | 0.421053 | 1.0 | 1.375 | 2.75 | 1.2 |  | 19 |
| rejection_block | target_rr_below_3 | 2 | 2 | 2 |  | 4.089132 | 4.089132 | 0.5 | 2.384358 | 95.0 | 2.032961 | 0.5 | 1.0 | 0.5 |  | 1.0 |  | 7.0 | 1.0 |  | 2 |
