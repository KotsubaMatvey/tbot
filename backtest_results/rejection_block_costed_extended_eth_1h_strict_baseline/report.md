# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
- models: rejection_block
- symbols: ETHUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | body_level | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | wick_extreme | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | conservative | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | discount | 33 | 33 | 13 |  | 1.442419 | 1.32029 | 0.030303 | 11.83327 | 94.0 | -0.781305 | -0.327476 | -0.430669 | -0.430669 | 0.040652 | 0.030303 | 0.181818 |  | 0.333333 | 5.366667 | 5.181818 | 4.333333 |  | 2 | 7 |
| rejection_block | premium | 71 | 71 | 26 |  | 2.880078 | 2.138284 | 0.028169 | 29.302824 | 99.014085 | 0.038728 | 0.232994 | 0.083771 | 0.083771 | 0.054645 | 0.028169 | 0.225352 | 0.112676 | 0.295775 | 4.118644 | 5.333333 | 2.875 | 3.625 | 5 | 8 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | high | 104 | 104 | 39 |  | 2.400858 | 1.79843 | 0.028846 | 23.7596 | 97.423077 | -0.234616 | 0.046171 | -0.087709 | -0.087709 | 0.050205 | 0.028846 | 0.211538 | 0.076923 | 0.307692 | 4.539326 | 5.28125 | 3.272727 | 3.625 | 7 | 15 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 89 | 89 | 31 |  | 2.475446 | 1.79843 |  | 27.458321 | 99.292135 | -0.240278 | -0.009947 | -0.154294 | -0.154294 | 0.050278 |  | 0.179775 | 0.089888 | 0.303371 | 4.532468 | 4.962963 | 2.3125 | 3.625 | 7 |  |
| rejection_block | target_rr_below_2 | 9 | 9 | 6 |  | 2.30074 | 2.882197 | 0.333333 | 1.198721 | 81.444444 | 0.049762 | 0.2515 | 0.150402 | 0.150402 | 0.067398 | 0.333333 | 0.444444 |  | 0.333333 | 5.428571 | 5.0 | 5.25 |  |  | 9 |
| rejection_block | target_rr_below_3 | 6 | 6 | 2 |  | 1.545106 | 1.545106 |  | 2.736565 | 93.666667 | -1.0 | 0.3 | 0.230019 | 0.230019 | 0.023327 |  | 0.333333 |  | 0.333333 | 3.4 | 10.0 | 7.0 |  |  | 6 |
