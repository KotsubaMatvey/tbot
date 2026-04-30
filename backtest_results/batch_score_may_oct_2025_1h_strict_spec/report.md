# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 21 | 21 | 20 |  | 15.215602 | 10.539107 | 0.285714 | 6.654852 | 98.952381 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 | 2.25 | 1.357143 | 1.0 | 1.0 |  | 10 |
| reclaimed_ob | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 21 | 21 | 20 |  | 15.215602 | 10.539107 | 0.285714 | 6.654852 | 98.952381 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 | 2.25 | 1.357143 | 1.0 | 1.0 |  | 10 |
| reclaimed_ob | body_edge | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | body_level | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 21 | 21 | 20 |  | 15.215602 | 10.539107 | 0.285714 | 6.654852 | 98.952381 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 | 2.25 | 1.357143 | 1.0 | 1.0 |  | 10 |
| reclaimed_ob | mean_threshold | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | wick_extreme | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 21 | 21 | 20 |  | 15.215602 | 10.539107 | 0.285714 | 6.654852 | 98.952381 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 | 2.25 | 1.357143 | 1.0 | 1.0 |  | 10 |
| reclaimed_ob | conservative | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | conservative | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 117 | 117 | 115 | 1 | 7.57703 | 4.012932 | 0.452991 | 5.090434 | 91.931624 | 0.309998 | 0.452991 | 0.598291 | 0.376068 | 0.521368 | 1.241379 | 2.508197 | 1.685714 | 2.340909 |  | 83 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 12 | 12 | 11 |  | 16.337525 | 10.645276 | 0.25 | 4.020734 | 98.166667 | 0.103332 | 0.25 | 0.166667 | 0.166667 | 0.666667 | 2.454545 | 1.0 | 1.0 | 1.0 |  | 6 |
| ifvg_retest | premium | 9 | 9 | 9 |  | 13.844363 | 7.118517 | 0.333333 | 10.167008 | 100.0 | 0.018323 | 0.333333 | 0.555556 | 0.555556 | 0.666667 | 2.0 | 1.833333 | 1.0 | 1.0 |  | 4 |
| reclaimed_ob | discount | 6 | 6 | 5 | 1 | 4.329635 | 3.70286 | 0.333333 | 36.885114 | 87.5 | -0.245077 | 0.333333 | 0.666667 | 0.666667 | 0.5 | 1.5 | 3.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | premium | 3 | 3 | 3 |  | 44.806686 | 11.142703 | 1.0 | 3.896247 | 87.333333 | 3.896247 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 2 |
| rejection_block | discount | 43 | 43 | 43 |  | 4.857511 | 3.788706 | 0.44186 | 2.452389 | 87.093023 | 0.05134 | 0.44186 | 0.627907 | 0.302326 | 0.534884 | 1.0 | 3.521739 | 1.296296 | 2.076923 |  | 36 |
| rejection_block | premium | 44 | 44 | 44 |  | 4.593299 | 2.891235 | 0.522727 | 2.667654 | 94.227273 | 0.492665 | 0.522727 | 0.659091 | 0.386364 | 0.477273 | 1.0 | 2.095238 | 2.37931 | 3.647059 |  | 32 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 8 | 8 | 8 |  | 20.81664 | 16.067113 | 0.125 | 4.157997 | 99.25 | -0.864585 | 0.125 |  |  | 0.875 | 2.125 | 1.0 |  |  |  | 4 |
| ifvg_retest | valid | 13 | 13 | 12 |  | 11.481577 | 7.081298 | 0.384615 | 8.191378 | 98.769231 | 0.684854 | 0.384615 | 0.538462 | 0.538462 | 0.538462 | 2.333333 | 1.714286 | 1.0 | 1.0 |  | 6 |
| reclaimed_ob | none | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | none | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 21 | 21 | 20 |  | 15.215602 | 10.539107 | 0.285714 | 6.654852 | 98.952381 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 | 2.25 | 1.357143 | 1.0 | 1.0 |  | 10 |
| reclaimed_ob | high | 9 | 9 | 8 | 1 | 19.508529 | 5.801969 | 0.555556 | 25.888825 | 87.444444 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 | 1.333333 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | high | 87 | 87 | 87 |  | 4.723887 | 2.891235 | 0.482759 | 2.561259 | 90.701149 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 | 1.0 | 2.840909 | 1.857143 | 2.966667 |  | 68 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 11 | 11 | 10 |  | 22.036961 | 11.737836 | 0.272727 | 11.547798 | 100.0 | 0.495703 | 0.272727 | 0.454545 | 0.454545 | 0.636364 | 3.0 | 1.428571 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 7 | 7 | 7 |  | 10.1024 | 7.118517 | 0.285714 | 0.638883 | 96.857143 | -0.644462 | 0.285714 |  |  | 0.714286 | 1.571429 | 1.0 |  |  |  | 7 |
| ifvg_retest | target_rr_below_3 | 3 | 3 | 3 |  | 4.408544 | 3.095485 | 0.333333 | 2.751309 | 100.0 | 0.285256 | 0.333333 | 0.666667 | 0.666667 | 0.666667 | 1.333333 | 2.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 4 | 4 | 4 |  | 31.282771 | 3.393763 | 0.25 | 56.945436 | 98.5 | 1.612486 | 0.25 | 0.75 | 0.75 | 0.75 | 1.0 | 3.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 5 | 5 | 4 | 1 | 7.734287 | 7.37326 | 0.8 | 1.043536 | 78.6 | 1.003354 | 0.8 | 0.8 | 0.8 |  | 1.6 |  | 1.0 | 1.0 |  | 5 |
| rejection_block | none | 19 | 19 | 19 |  | 7.804083 | 5.945999 | 0.157895 | 6.099517 | 99.052632 | -0.23172 | 0.157895 | 0.473684 | 0.421053 | 0.842105 | 1.0 | 2.5625 | 1.444444 | 1.875 |  |  |
| rejection_block | target_rr_below_2 | 38 | 38 | 38 |  | 4.192922 | 2.51579 | 0.684211 | 0.955792 | 84.736842 | 0.343534 | 0.684211 | 0.631579 | 0.210526 | 0.289474 | 1.0 | 2.181818 | 2.208333 | 3.25 |  | 38 |
| rejection_block | target_rr_below_3 | 30 | 30 | 30 |  | 3.44565 | 2.891235 | 0.433333 | 2.353954 | 92.966667 | 0.507775 | 0.433333 | 0.766667 | 0.466667 | 0.566667 | 1.0 | 3.529412 | 1.652174 | 3.428571 |  | 30 |
