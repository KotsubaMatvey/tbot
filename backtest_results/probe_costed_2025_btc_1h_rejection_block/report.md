# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: rejection_block
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
| rejection_block | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | body_level | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | wick_extreme | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | conservative | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | discount | 14 | 14 | 7 |  | 1.756086 | 1.855134 | 0.071429 | 9.957259 | 93.928571 | -0.149919 | -0.112669 | -0.265205 | -0.265205 | 0.076268 | 0.071429 | 0.285714 | 0.214286 | 0.357143 | 3.25 | 6.2 | 2.25 | 5.333333 | 1 | 3 |
| rejection_block | premium | 38 | 38 | 11 |  | 3.72959 | 2.99517 |  | 37.509085 | 100.0 | -1.0 | -0.290909 | -0.591726 | -0.591726 | 0.087079 |  | 0.157895 | 0.026316 | 0.289474 | 4.129032 | 3.181818 | 2.166667 | 5.0 | 2 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | high | 52 | 52 | 18 |  | 2.962116 | 2.674853 | 0.019231 | 30.091286 | 98.365385 | -0.669413 | -0.221594 | -0.464745 | -0.464745 | 0.084168 | 0.019231 | 0.192308 | 0.076923 | 0.307692 | 3.883721 | 4.125 | 2.2 | 5.25 | 3 | 3 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 49 | 49 | 17 |  | 3.128475 | 2.889144 |  | 31.924561 | 99.510204 | -0.709456 | -0.235294 | -0.492182 | -0.492182 | 0.089124 |  | 0.204082 | 0.081633 | 0.326531 | 3.97561 | 4.125 | 2.2 | 5.25 | 3 |  |
| rejection_block | target_rr_below_2 | 3 | 3 | 1 |  | 0.134025 | 0.134025 | 0.333333 | 0.147785 | 79.666667 | 0.011314 | 0.011314 | 0.001683 | 0.001683 | 0.00321 | 0.333333 |  |  |  | 2.0 |  |  |  |  | 3 |
