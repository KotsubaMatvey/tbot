# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | body_zone_retest | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | body_edge | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | body_level | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | edge | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | block_extreme | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | block_extreme | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | wick_extreme | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | swing_or_fvg | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | conservative | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | conservative | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | conservative | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | conservative | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 32 | 32 | 23 |  | 1.735594 | 1.785091 | 0.34375 | 7.416985 | 86.46875 | -0.10499 | 0.143253 | 0.143253 | 0.34375 | 0.34375 | 0.09375 | 0.375 | 1.307692 | 4.0 | 3.181818 | 4.0 | 2 | 18 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | discount | 3 | 3 | 3 |  | 0.072158 |  |  | 3.417312 | 83.666667 | -1.0 | -1.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 2 |
| mitigation_block | premium | 14 | 14 | 14 |  | 1.465022 | 1.360966 | 0.642857 | 0.716186 | 77.714286 | 0.047857 | 0.202657 | 0.202657 | 0.642857 | 0.428571 |  | 0.357143 | 1.0 | 4.8 | 3.166667 |  |  | 14 |
| reclaimed_ob | discount | 2 | 2 | 2 |  | 2.953426 | 2.953426 |  | 13.365736 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.5 | 1.0 | 1.0 | 5.5 | 1.0 | 2.0 | 1 |  |
| reclaimed_ob | premium | 1 | 1 | 1 |  | 5.902339 | 5.902339 |  | 6.627858 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 1.0 | 1.0 | 1.0 | 6.0 | 1.0 | 1.0 | 1 |  |
| rejection_block | discount | 4 | 4 | 1 |  | 1.958823 | 1.958823 | 0.25 | 8.036682 | 89.5 | 1.915226 | 1.457613 | 1.457613 | 0.25 | 0.25 |  |  | 2.0 |  | 5.0 |  |  | 2 |
| rejection_block | premium | 7 | 7 | 1 |  | 1.834568 | 1.834568 |  | 21.36556 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.142857 | 3.0 | 4.0 |  |  |  |  |
| silver_bullet | premium | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | none | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | none | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | none | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | none | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | high | 17 | 17 | 17 |  | 1.219223 | 0.936841 | 0.529412 | 1.192855 | 78.764706 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 | 1.0 | 3.375 | 3.166667 |  |  | 16 |
| reclaimed_ob | high | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | high | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |
| silver_bullet | high | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mitigation_block | none | 1 | 1 | 1 |  |  |  |  | 8.65751 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  |  |
| mitigation_block | target_rr_below_2 | 15 | 15 | 15 |  | 1.26278 | 0.936841 | 0.6 | 0.63904 | 77.0 | -0.022 | 0.02248 | 0.02248 | 0.6 | 0.333333 |  | 0.4 | 1.0 | 2.0 | 2.2 |  |  | 15 |
| mitigation_block | target_rr_below_3 | 1 | 1 | 1 |  | 1.785091 | 1.785091 |  | 2.035433 | 87.0 | -1.0 | 0.5 | 0.5 |  | 1.0 |  | 1.0 | 1.0 | 14.0 | 8.0 |  |  | 1 |
| reclaimed_ob | none | 3 | 3 | 3 |  | 3.936397 | 4.297039 |  | 11.119776 | 97.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 1.0 | 5.666667 | 1.0 | 1.5 | 2 |  |
| rejection_block | none | 9 | 9 | 1 |  | 1.834568 | 1.834568 |  | 19.7345 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.111111 | 3.0 | 4.0 |  |  |  |  |
| rejection_block | target_rr_below_2 | 1 | 1 | 1 |  | 1.958823 | 1.958823 | 1.0 | 1.915226 | 77.0 | 1.915226 | 1.457613 | 1.457613 | 1.0 | 1.0 |  |  | 2.0 |  | 5.0 |  |  | 1 |
| rejection_block | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.179919 | 87.0 |  |  |  |  |  |  |  | 2.0 |  |  |  |  | 1 |
| silver_bullet | none | 1 | 1 | 1 |  | 3.589295 | 3.589295 | 1.0 | 2.0 | 100.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 8.0 | 9.0 |  |  |
