# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 11 | 11 | 4 | 5 | 15.78748 | 15.159227 | 0.363636 | 1.928618 | 78.545455 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  | 8.428571 |  | 1.0 | 1.0 |  | 11 |
| ifvg_retest | 8 | 8 | 7 |  | 77.619041 | 9.722848 | 0.5 | 7.916192 | 99.25 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 | 3.142857 | 1.0 | 1.25 | 1.0 |  | 7 |
| mitigation_block | 12 | 12 | 12 |  | 3.184502 | 1.598802 | 0.333333 | 0.533201 | 79.416667 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 | 1.0 | 1.0 | 2.333333 |  |  | 12 |
| reclaimed_ob | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | 14 | 14 | 14 |  | 5.547183 | 2.408596 | 0.571429 | 2.145225 | 84.928571 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 11 |
| turtle_soup | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 11 | 11 | 4 | 5 | 15.78748 | 15.159227 | 0.363636 | 1.928618 | 78.545455 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  | 8.428571 |  | 1.0 | 1.0 |  | 11 |
| ifvg_retest | edge | 8 | 8 | 7 |  | 77.619041 | 9.722848 | 0.5 | 7.916192 | 99.25 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 | 3.142857 | 1.0 | 1.25 | 1.0 |  | 7 |
| mitigation_block | body_zone_retest | 12 | 12 | 12 |  | 3.184502 | 1.598802 | 0.333333 | 0.533201 | 79.416667 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 | 1.0 | 1.0 | 2.333333 |  |  | 12 |
| reclaimed_ob | body_edge | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | body_level | 14 | 14 | 14 |  | 5.547183 | 2.408596 | 0.571429 | 2.145225 | 84.928571 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 11 |
| turtle_soup | close | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 11 | 11 | 4 | 5 | 15.78748 | 15.159227 | 0.363636 | 1.928618 | 78.545455 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  | 8.428571 |  | 1.0 | 1.0 |  | 11 |
| ifvg_retest | ce | 8 | 8 | 7 |  | 77.619041 | 9.722848 | 0.5 | 7.916192 | 99.25 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 | 3.142857 | 1.0 | 1.25 | 1.0 |  | 7 |
| mitigation_block | block_extreme | 12 | 12 | 12 |  | 3.184502 | 1.598802 | 0.333333 | 0.533201 | 79.416667 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 | 1.0 | 1.0 | 2.333333 |  |  | 12 |
| reclaimed_ob | mean_threshold | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | wick_extreme | 14 | 14 | 14 |  | 5.547183 | 2.408596 | 0.571429 | 2.145225 | 84.928571 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 11 |
| turtle_soup | sweep_extreme | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 11 | 11 | 4 | 5 | 15.78748 | 15.159227 | 0.363636 | 1.928618 | 78.545455 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  | 8.428571 |  | 1.0 | 1.0 |  | 11 |
| ifvg_retest | conservative | 8 | 8 | 7 |  | 77.619041 | 9.722848 | 0.5 | 7.916192 | 99.25 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 | 3.142857 | 1.0 | 1.25 | 1.0 |  | 7 |
| mitigation_block | conservative | 12 | 12 | 12 |  | 3.184502 | 1.598802 | 0.333333 | 0.533201 | 79.416667 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 | 1.0 | 1.0 | 2.333333 |  |  | 12 |
| reclaimed_ob | conservative | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | conservative | 14 | 14 | 14 |  | 5.547183 | 2.408596 | 0.571429 | 2.145225 | 84.928571 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 11 |
| turtle_soup | conservative | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 102 | 102 | 94 | 5 | 10.255853 | 2.965326 | 0.264706 | 6.139794 | 64.872549 | 0.230883 | 0.264706 | 0.411765 | 0.264706 | 0.607843 | 1.71134 | 2.596774 | 2.333333 | 2.185185 |  | 49 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 4 | 4 | 1 | 2 | 3.912926 | 3.912926 | 0.25 | 1.691242 | 84.25 | 1.094762 | 0.25 | 0.25 | 0.25 |  | 12.5 |  | 1.0 | 1.0 |  | 4 |
| breaker_block | equilibrium | 3 | 3 |  | 3 |  |  |  | 1.445801 | 62.0 |  |  |  |  |  | 11.5 |  |  |  |  | 3 |
| breaker_block | premium | 4 | 4 | 3 |  | 19.745664 | 19.857954 | 0.75 | 2.528106 | 85.25 | 2.203984 | 0.75 | 0.75 | 0.75 |  | 3.666667 |  | 1.0 | 1.0 |  | 4 |
| ifvg_retest | discount | 4 | 4 | 4 |  | 32.623093 | 8.812728 | 0.5 | 4.393027 | 100.0 | 3.665416 | 0.5 | 0.5 | 0.5 | 0.5 | 4.5 | 1.0 | 1.0 | 1.0 |  | 3 |
| ifvg_retest | equilibrium | 1 | 1 |  |  |  |  |  | 24.174174 | 100.0 |  |  |  |  |  |  |  |  |  |  | 1 |
| ifvg_retest | premium | 3 | 3 | 3 |  | 137.613638 | 12.584042 | 0.666667 | 7.19442 | 98.0 | 0.286913 | 0.666667 | 0.666667 | 0.333333 | 0.333333 | 1.333333 | 1.0 | 1.5 | 1.0 |  | 3 |
| mitigation_block | discount | 6 | 6 | 6 |  | 3.467252 | 0.820766 | 0.166667 | 0.578791 | 81.0 | -0.832316 | 0.166667 |  |  | 0.833333 | 1.0 | 1.0 |  |  |  | 6 |
| mitigation_block | equilibrium | 2 | 2 | 2 |  | 6.754334 | 6.754334 | 0.5 | 0.607648 | 72.0 | -0.035747 | 0.5 | 0.5 |  | 0.5 | 1.0 | 1.0 | 1.0 |  |  | 2 |
| mitigation_block | premium | 4 | 4 | 4 |  | 0.975459 | 0.924126 | 0.5 | 0.427592 | 80.75 | -0.146103 | 0.5 | 0.5 |  | 0.5 | 1.0 | 1.0 | 3.0 |  |  | 4 |
| reclaimed_ob | discount | 1 | 1 | 1 |  | 6.779888 | 6.779888 |  | 9.546568 | 90.0 | -1.0 |  |  |  | 1.0 | 2.0 | 1.0 |  |  |  | 1 |
| reclaimed_ob | premium | 1 | 1 | 1 |  | 3.907334 | 3.907334 | 1.0 | 0.43808 | 77.0 | 0.43808 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | discount | 7 | 7 | 7 |  | 6.083228 | 2.965326 | 0.428571 | 2.757786 | 85.571429 | -0.098532 | 0.428571 | 0.428571 | 0.428571 | 0.571429 | 1.0 | 1.25 | 1.0 | 1.333333 |  | 5 |
| rejection_block | equilibrium | 1 | 1 | 1 |  | 1.600923 | 1.600923 | 1.0 | 0.196669 | 82.0 | 0.196669 | 1.0 | 1.0 |  |  | 1.0 |  | 1.0 |  |  | 1 |
| rejection_block | premium | 6 | 6 | 6 |  | 5.579508 | 1.935478 | 0.666667 | 1.755331 | 84.666667 | 0.102756 | 0.666667 | 0.333333 | 0.166667 | 0.333333 | 1.0 | 1.0 | 1.0 | 1.0 |  | 5 |
| turtle_soup | none | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 11 | 11 | 4 | 5 | 15.78748 | 15.159227 | 0.363636 | 1.928618 | 78.545455 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  | 8.428571 |  | 1.0 | 1.0 |  | 11 |
| ifvg_retest | strong | 5 | 5 | 4 |  | 106.071717 | 10.243325 | 0.4 | 9.635231 | 99.4 | 0.465061 | 0.4 | 0.4 | 0.4 | 0.4 | 1.25 | 1.0 | 1.0 | 1.0 |  | 5 |
| ifvg_retest | valid | 3 | 3 | 3 |  | 39.682139 | 9.722848 | 0.666667 | 5.051129 | 99.0 | 4.554054 | 0.666667 | 0.666667 | 0.333333 | 0.333333 | 5.666667 | 1.0 | 1.5 | 1.0 |  | 2 |
| mitigation_block | none | 12 | 12 | 12 |  | 3.184502 | 1.598802 | 0.333333 | 0.533201 | 79.416667 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 | 1.0 | 1.0 | 2.333333 |  |  | 12 |
| reclaimed_ob | none | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | none | 14 | 14 | 14 |  | 5.547183 | 2.408596 | 0.571429 | 2.145225 | 84.928571 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 11 |
| turtle_soup | none | 55 | 55 | 55 |  | 4.200093 | 2.608813 | 0.109091 | 9.005426 | 48.181818 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 | 1.0 | 3.227273 | 3.125 | 3.066667 |  | 6 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 7 | 7 | 3 | 2 | 11.41046 | 10.460501 | 0.428571 | 2.198301 | 88.0 | 2.072475 | 0.428571 | 0.428571 | 0.428571 |  | 7.75 |  | 1.0 | 1.0 |  | 7 |
| breaker_block | medium | 4 | 4 | 1 | 3 | 28.918538 | 28.918538 | 0.25 | 1.456672 | 62.0 | 1.489288 | 0.25 | 0.25 | 0.25 |  | 9.333333 |  | 1.0 | 1.0 |  | 4 |
| ifvg_retest | high | 8 | 8 | 7 |  | 77.619041 | 9.722848 | 0.5 | 7.916192 | 99.25 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 | 3.142857 | 1.0 | 1.25 | 1.0 |  | 7 |
| mitigation_block | high | 11 | 11 | 11 |  | 2.391287 | 1.598802 | 0.363636 | 0.555602 | 81.0 | -0.422709 | 0.363636 | 0.272727 |  | 0.636364 | 1.0 | 1.0 | 2.333333 |  |  | 11 |
| mitigation_block | medium | 1 | 1 | 1 |  | 11.909865 | 11.909865 |  | 0.28679 | 62.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| reclaimed_ob | high | 2 | 2 | 2 |  | 5.343611 | 5.343611 | 0.5 | 4.992324 | 83.5 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | high | 13 | 13 | 13 |  | 5.812714 | 2.721903 | 0.538462 | 2.294154 | 86.692308 | -0.00659 | 0.538462 | 0.461538 | 0.307692 | 0.461538 | 1.0 | 1.166667 | 1.0 | 1.25 |  | 10 |
| rejection_block | medium | 1 | 1 | 1 |  | 2.095289 | 2.095289 | 1.0 | 0.209153 | 62.0 | 0.209153 | 1.0 |  |  |  | 1.0 |  |  |  |  | 1 |
| turtle_soup | low | 6 | 6 | 6 |  | 1.517192 | 0.862982 | 0.166667 | 1.734155 | 33.333333 | -0.233797 | 0.166667 | 0.5 |  | 0.666667 | 1.0 | 4.25 | 8.333333 |  |  | 6 |
| turtle_soup | medium | 49 | 49 | 49 |  | 4.528612 | 3.880096 | 0.102041 | 9.895786 | 50.0 | 0.121733 | 0.102041 | 0.428571 | 0.306122 | 0.816327 | 1.0 | 3.125 | 2.380952 | 3.066667 |  |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | equilibrium;insufficient_displacement;target_rr_below_2 | 3 | 3 |  | 3 |  |  |  | 1.445801 | 62.0 |  |  |  |  |  | 11.5 |  |  |  |  | 3 |
| breaker_block | insufficient_displacement | 2 | 2 | 1 |  | 19.857954 | 19.857954 | 0.5 | 4.153395 | 98.5 | 4.806316 | 0.5 | 0.5 | 0.5 |  | 1.0 |  | 1.0 | 1.0 |  | 2 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 1 | 1 | 1 |  | 3.912926 | 3.912926 | 1.0 | 1.094762 | 97.0 | 1.094762 | 1.0 | 1.0 | 1.0 |  | 8.0 |  | 1.0 | 1.0 |  | 1 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_2 | 4 | 4 | 2 | 1 | 19.689519 | 19.689519 | 0.5 | 1.136444 | 76.0 | 0.902818 | 0.5 | 0.5 | 0.5 |  | 5.0 |  | 1.0 | 1.0 |  | 4 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_3 | 1 | 1 |  | 1 |  |  |  | 2.930064 | 80.0 |  |  |  |  |  | 17.0 |  |  |  |  | 1 |
| ifvg_retest | equilibrium | 1 | 1 |  |  |  |  |  | 24.174174 | 100.0 |  |  |  |  |  |  |  |  |  |  | 1 |
| ifvg_retest | none | 1 | 1 | 1 |  | 107.550483 | 107.550483 | 1.0 | 13.967595 | 100.0 | 13.967595 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 1 | 1 | 1 |  | 398.483784 | 398.483784 |  | 19.722519 | 100.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 2 | 2 | 2 |  | 5.747968 | 5.747968 | 0.5 | 0.592896 | 98.5 | -0.152716 | 0.5 | 0.5 |  | 0.5 | 8.0 | 1.0 | 2.0 |  |  | 2 |
| ifvg_retest | poor_pd_location;target_rr_below_3 | 1 | 1 | 1 |  | 7.902607 | 7.902607 | 1.0 | 2.694071 | 100.0 | 2.694071 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | target_rr_below_2 | 2 | 2 | 2 |  | 8.950237 | 8.950237 | 0.5 | 0.792695 | 98.5 | 0.083086 | 0.5 | 0.5 | 0.5 | 0.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 2 |
| mitigation_block | equilibrium;target_rr_below_2 | 2 | 2 | 2 |  | 6.754334 | 6.754334 | 0.5 | 0.607648 | 72.0 | -0.035747 | 0.5 | 0.5 |  | 0.5 | 1.0 | 1.0 | 1.0 |  |  | 2 |
| mitigation_block | poor_pd_location;target_rr_below_2 | 5 | 5 | 5 |  | 1.861141 |  | 0.2 | 0.416817 | 77.2 | -0.736419 | 0.2 | 0.2 |  | 0.8 | 1.0 | 1.0 | 1.0 |  |  | 5 |
| mitigation_block | target_rr_below_2 | 5 | 5 | 5 |  | 3.07993 | 1.598802 | 0.4 | 0.619806 | 84.6 | -0.379243 | 0.4 | 0.2 |  | 0.6 | 1.0 | 1.0 | 5.0 |  |  | 5 |
| reclaimed_ob | poor_pd_location | 1 | 1 | 1 |  | 6.779888 | 6.779888 |  | 9.546568 | 90.0 | -1.0 |  |  |  | 1.0 | 2.0 | 1.0 |  |  |  | 1 |
| reclaimed_ob | target_rr_below_2 | 1 | 1 | 1 |  | 3.907334 | 3.907334 | 1.0 | 0.43808 | 77.0 | 0.43808 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | equilibrium;target_rr_below_2 | 1 | 1 | 1 |  | 1.600923 | 1.600923 | 1.0 | 0.196669 | 82.0 | 0.196669 | 1.0 | 1.0 |  |  | 1.0 |  | 1.0 |  |  | 1 |
| rejection_block | none | 3 | 3 | 3 |  | 7.538151 | 7.837513 |  | 7.808377 | 97.333333 | -1.0 |  | 0.333333 | 0.333333 | 1.0 | 1.0 | 1.333333 | 1.0 | 1.0 |  |  |
| rejection_block | poor_pd_location;target_rr_below_2 | 6 | 6 | 6 |  | 8.000578 | 2.965326 | 0.833333 | 0.597377 | 76.0 | 0.413369 | 0.833333 | 0.5 | 0.333333 | 0.166667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | target_rr_below_2 | 4 | 4 | 4 |  | 1.36043 | 1.058491 | 0.5 | 0.706773 | 89.75 | 0.111649 | 0.5 | 0.25 | 0.25 | 0.5 | 1.0 | 1.0 | 1.0 | 2.0 |  | 4 |
