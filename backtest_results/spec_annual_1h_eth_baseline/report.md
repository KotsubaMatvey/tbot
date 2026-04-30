# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: ETHUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | body_edge | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | body_level | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | mean_threshold | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | wick_extreme | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | conservative | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | conservative | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 62 | 62 | 23 |  | 7.573516 | 2.071261 | 0.032258 | 67.086846 | 98.177419 | -0.117967 | -0.101177 | -0.101177 | 0.032258 | 0.193548 | 0.080645 | 0.290323 | 4.473684 | 4.5 | 2.666667 | 2.4 |  | 5 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | discount | 3 | 3 | 1 |  | 1.622219 | 1.622219 |  | 77.197471 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.333333 | 2.333333 | 1.0 |  |  |  |  |
| reclaimed_ob | premium | 1 | 1 | 1 |  | 116.721341 | 116.721341 |  | 10.568833 | 100.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 | 1.0 | 1.0 |  |  |
| rejection_block | discount | 18 | 18 | 7 |  | 2.210779 | 1.470714 |  | 16.143488 | 95.055556 | -0.814746 | -0.386175 | -0.386175 |  | 0.111111 |  | 0.333333 | 5.125 | 6.0 | 5.0 |  |  | 3 |
| rejection_block | premium | 40 | 40 | 14 |  | 2.883704 | 2.294107 | 0.05 | 90.666011 | 99.625 | 0.356427 | 0.062583 | 0.062583 | 0.05 | 0.225 | 0.1 | 0.25 | 4.459459 | 4.2 | 2.333333 | 2.75 |  | 2 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | none | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | high | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | high | 58 | 58 | 21 |  | 2.659396 | 2.071261 | 0.034483 | 67.538331 | 98.206897 | -0.033964 | -0.087003 | -0.087003 | 0.034483 | 0.189655 | 0.068966 | 0.275862 | 4.660377 | 4.875 | 2.818182 | 2.75 |  | 5 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 4 | 4 | 2 |  | 59.17178 | 59.17178 |  | 60.540311 | 97.75 | -1.0 | -0.25 | -0.25 |  | 0.25 | 0.25 | 0.5 | 2.0 | 1.5 | 1.0 | 1.0 |  |  |
| rejection_block | none | 53 | 53 | 18 |  | 2.703217 | 1.977471 |  | 73.777146 | 99.433962 | -0.136976 | -0.177957 | -0.177957 |  | 0.169811 | 0.075472 | 0.283019 | 4.653061 | 5.066667 | 2.444444 | 2.75 |  |  |
| rejection_block | target_rr_below_2 | 4 | 4 | 3 |  | 2.396474 | 2.891235 | 0.5 | 1.061695 | 84.75 | 0.584104 | 0.458719 | 0.458719 | 0.5 | 0.5 |  | 0.25 | 4.666667 | 2.0 | 4.5 |  |  | 4 |
| rejection_block | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.787677 | 87.0 |  |  |  |  |  |  |  | 5.0 |  |  |  |  | 1 |
