# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 14 | 14 | 14 |  | 2.292957 | 2.20373 | 0.357143 | 2.0 | 80.0 | 0.183327 | -0.088271 | -0.361037 | -0.361037 | 0.272765 | 0.357143 | 0.428571 | 0.357143 | 0.571429 | 1.0 | 2.375 | 4.0 | 6.6 |  | 14 |
| turtle_soup | medium | 87 | 87 | 87 |  | 3.645856 | 2.126295 | 0.241379 | 2.0 | 60.0 | -0.134911 | 0.034865 | -0.252528 | -0.252528 | 0.287393 | 0.241379 | 0.505747 | 0.241379 | 0.689655 | 1.0 | 3.233333 | 3.636364 | 6.666667 | 11 | 87 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 101 | 101 | 101 |  | 3.458326 | 2.126295 | 0.257426 | 2.0 | 62.772277 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 1.0 | 3.132353 | 3.68 | 6.653846 | 11 | 101 |
