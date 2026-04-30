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
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 11 | 11 | 11 |  | 21.476651 | 2.58886 | 0.545455 | 3.739624 | 100.0 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 | 3.181818 | 1.4 | 1.0 | 1.333333 |  | 6 |
| reclaimed_ob | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 11 | 11 | 11 |  | 21.476651 | 2.58886 | 0.545455 | 3.739624 | 100.0 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 | 3.181818 | 1.4 | 1.0 | 1.333333 |  | 6 |
| reclaimed_ob | body_edge | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | body_level | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 11 | 11 | 11 |  | 21.476651 | 2.58886 | 0.545455 | 3.739624 | 100.0 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 | 3.181818 | 1.4 | 1.0 | 1.333333 |  | 6 |
| reclaimed_ob | mean_threshold | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | wick_extreme | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 11 | 11 | 11 |  | 21.476651 | 2.58886 | 0.545455 | 3.739624 | 100.0 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 | 3.181818 | 1.4 | 1.0 | 1.333333 |  | 6 |
| reclaimed_ob | conservative | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | conservative | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 40 | 40 | 40 |  | 9.852785 | 3.727477 | 0.6 | 2.810224 | 92.3 | 0.827924 | 0.6 | 0.475 | 0.275 | 0.4 | 1.675 | 1.1875 | 1.105263 | 1.181818 |  | 28 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 6 | 6 | 6 |  | 29.284804 | 3.207952 | 0.5 | 4.051584 | 100.0 | 2.428289 | 0.5 | 0.666667 | 0.333333 | 0.5 | 1.833333 | 1.666667 | 1.0 | 1.5 |  | 3 |
| ifvg_retest | premium | 5 | 5 | 5 |  | 12.106867 | 2.58886 | 0.6 | 3.365273 | 100.0 | -0.14115 | 0.6 | 0.4 | 0.2 | 0.4 | 4.8 | 1.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | discount | 2 | 2 | 2 |  | 20.27678 | 20.27678 | 1.0 | 5.399852 | 93.5 | 5.399852 | 1.0 | 1.0 | 1.0 |  | 1.5 |  | 1.0 | 1.0 |  | 1 |
| reclaimed_ob | premium | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 0.857505 | 81.0 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | discount | 14 | 14 | 14 |  | 4.674486 | 3.526845 | 0.571429 | 1.972474 | 82.928571 | 0.328744 | 0.571429 | 0.571429 | 0.214286 | 0.428571 | 1.0 | 1.166667 | 1.25 | 1.333333 |  | 12 |
| rejection_block | premium | 11 | 11 | 11 |  | 3.74406 | 1.340261 | 0.636364 | 2.831249 | 98.363636 | 0.40116 | 0.636364 | 0.181818 | 0.181818 | 0.363636 | 1.0 | 1.0 | 1.0 | 1.0 |  | 7 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 6 | 6 | 6 |  | 16.7749 | 2.385866 | 0.5 | 2.799026 | 100.0 | -0.336207 | 0.5 | 0.666667 | 0.166667 | 0.5 | 4.166667 | 1.333333 | 1.0 | 1.0 |  | 4 |
| ifvg_retest | valid | 5 | 5 | 5 |  | 27.118752 | 4.54596 | 0.6 | 4.868342 | 100.0 | 3.176245 | 0.6 | 0.4 | 0.4 | 0.4 | 2.0 | 1.5 | 1.0 | 1.5 |  | 2 |
| reclaimed_ob | none | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | none | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 11 | 11 | 11 |  | 21.476651 | 2.58886 | 0.545455 | 3.739624 | 100.0 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 | 3.181818 | 1.4 | 1.0 | 1.333333 |  | 6 |
| reclaimed_ob | high | 4 | 4 | 4 |  | 12.810196 | 9.397534 | 0.75 | 3.128678 | 87.25 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 | 1.75 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | high | 25 | 25 | 25 |  | 4.265098 | 3.506069 | 0.6 | 2.350335 | 89.72 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 | 1.0 | 1.1 | 1.2 | 1.2 |  | 19 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 5 | 5 | 5 |  | 45.433077 | 33.024085 | 0.4 | 7.594709 | 100.0 | 2.902601 | 0.4 | 0.4 | 0.4 | 0.6 | 1.4 | 1.0 | 1.0 | 1.5 |  |  |
| ifvg_retest | target_rr_below_2 | 6 | 6 | 6 |  | 1.512963 | 1.444697 | 0.666667 | 0.527054 | 100.0 | -0.108171 | 0.666667 | 0.666667 | 0.166667 | 0.333333 | 4.666667 | 2.0 | 1.0 | 1.0 |  | 6 |
| reclaimed_ob | none | 1 | 1 | 1 |  | 12.01518 | 12.01518 | 1.0 | 8.42623 | 100.0 | 8.42623 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 0.857505 | 81.0 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 28.538381 | 28.538381 | 1.0 | 2.373474 | 87.0 | 2.373474 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | none | 6 | 6 | 6 |  | 8.740702 | 9.519803 | 0.333333 | 6.836221 | 99.0 | 0.802359 | 0.333333 | 0.5 | 0.5 | 0.666667 | 1.0 | 1.25 | 1.0 | 1.0 |  |  |
| rejection_block | target_rr_below_2 | 17 | 17 | 17 |  | 2.519013 | 2.485762 | 0.764706 | 0.753988 | 86.764706 | 0.364767 | 0.764706 | 0.411765 | 0.117647 | 0.235294 | 1.0 | 1.0 | 1.285714 | 1.5 |  | 17 |
| rejection_block | target_rr_below_3 | 2 | 2 | 2 |  | 5.680011 | 5.680011 |  | 2.461631 | 87.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 2 |
