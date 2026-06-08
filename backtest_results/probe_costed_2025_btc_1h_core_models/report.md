# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: breaker_block, reclaimed_ob, ifvg_retest
- symbols: BTCUSDT
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
| breaker_block | 13 | 13 | 3 | 8 | 17.327972 | 8.287384 |  | 12.607311 | 98.384615 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.257346 |  | 0.230769 | 0.153846 | 0.230769 | 5.25 | 2.0 | 1.0 | 1.0 | 3 | 12 |
| reclaimed_ob | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 13 | 13 | 3 | 8 | 17.327972 | 8.287384 |  | 12.607311 | 98.384615 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.257346 |  | 0.230769 | 0.153846 | 0.230769 | 5.25 | 2.0 | 1.0 | 1.0 | 3 | 12 |
| reclaimed_ob | body_edge | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 13 | 13 | 3 | 8 | 17.327972 | 8.287384 |  | 12.607311 | 98.384615 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.257346 |  | 0.230769 | 0.153846 | 0.230769 | 5.25 | 2.0 | 1.0 | 1.0 | 3 | 12 |
| reclaimed_ob | block_extreme | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 13 | 13 | 3 | 8 | 17.327972 | 8.287384 |  | 12.607311 | 98.384615 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.257346 |  | 0.230769 | 0.153846 | 0.230769 | 5.25 | 2.0 | 1.0 | 1.0 | 3 | 12 |
| reclaimed_ob | conservative | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 16 | 16 | 5 | 8 | 10.600583 | 6.920093 |  | 17.445317 | 98.375 | -1.0 | -0.22 | -0.92386 | -0.92386 | 0.219956 |  | 0.1875 | 0.125 | 0.3125 | 4.466667 | 2.2 | 1.0 | 1.0 | 3 | 13 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 4 | 4 | 1 | 3 | 6.920093 | 6.920093 |  | 12.000121 | 98.5 | -1.0 | 0.3 | 0.139069 | 0.139069 | 0.040233 |  | 0.25 |  | 0.25 | 7.666667 | 2.0 | 1.0 |  | 1 | 3 |
| breaker_block | premium | 9 | 9 | 2 | 5 | 22.531911 | 22.531911 |  | 12.877173 | 98.333333 | -1.0 | 0.3 | -1.292285 | -1.292285 | 0.353841 |  | 0.222222 | 0.222222 | 0.222222 | 4.444444 | 2.0 | 1.0 | 1.0 | 2 | 9 |
| reclaimed_ob | premium | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | strong | 1 | 1 |  |  |  |  |  | 0.668579 | 100.0 |  |  |  |  |  |  |  |  |  | 3.0 |  |  |  |  | 1 |
| breaker_block | valid | 1 | 1 |  | 1 |  |  |  | 19.35797 | 100.0 |  |  |  |  |  |  |  |  |  | 16.0 |  |  |  |  |  |
| breaker_block | weak | 11 | 11 | 3 | 7 | 17.327972 | 8.287384 |  | 13.078954 | 98.090909 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.304137 |  | 0.272727 | 0.181818 | 0.272727 | 4.4 | 2.0 | 1.0 | 1.0 | 3 | 11 |
| reclaimed_ob | none | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 13 | 13 | 3 | 8 | 17.327972 | 8.287384 |  | 12.607311 | 98.384615 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.257346 |  | 0.230769 | 0.153846 | 0.230769 | 5.25 | 2.0 | 1.0 | 1.0 | 3 | 12 |
| reclaimed_ob | high | 3 | 3 | 2 |  | 0.509499 | 0.509499 |  | 38.410012 | 98.333333 | -1.0 | -1.0 | -1.086898 | -1.086898 | 0.057932 |  |  |  | 0.666667 | 1.333333 | 2.5 |  |  |  | 1 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | insufficient_displacement | 8 | 8 | 3 | 4 | 17.327972 | 8.287384 |  | 17.706294 | 99.25 | -1.0 | 0.3 | -0.815167 | -0.815167 | 0.418188 |  | 0.375 | 0.25 | 0.375 | 4.285714 | 2.0 | 1.0 | 1.0 | 3 | 8 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 3 | 3 |  | 3 |  |  |  | 0.739381 | 95.0 |  |  |  |  |  |  |  |  |  | 4.666667 |  |  |  |  | 3 |
| breaker_block | none | 1 | 1 |  | 1 |  |  |  | 19.35797 | 100.0 |  |  |  |  |  |  |  |  |  | 16.0 |  |  |  |  |  |
| breaker_block | target_rr_below_2 | 1 | 1 |  |  |  |  |  | 0.668579 | 100.0 |  |  |  |  |  |  |  |  |  | 3.0 |  |  |  |  | 1 |
| reclaimed_ob | none | 2 | 2 | 1 |  | 0.499778 | 0.499778 |  | 56.196615 | 100.0 | -1.0 | -1.0 | -1.079909 | -1.079909 | 0.039954 |  |  |  | 0.5 | 1.5 | 3.0 |  |  |  |  |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 0.51922 | 0.51922 |  | 2.836806 | 95.0 | -1.0 | -1.0 | -1.093887 | -1.093887 | 0.093887 |  |  |  | 1.0 | 1.0 | 2.0 |  |  |  | 1 |
