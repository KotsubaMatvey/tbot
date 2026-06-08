# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: None
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 34 | 34 | 34 |  | 3.869968 | 1.994614 | 0.676471 | 1.379165 | 73.235294 | 0.461863 | 0.543532 | 0.350895 | 0.350895 | 0.192637 |  | 0.192637 | 0.676471 | 0.588235 | 0.088235 | 0.235294 | 1.0 | 4.75 | 6.25 | 2.666667 | 3 | 31 |
| turtle_soup | valid | 30 | 30 | 30 |  | 3.065534 | 1.419339 | 0.466667 | 1.788957 | 74.333333 | -0.119832 | 0.115287 | -0.069663 | -0.069663 | 0.184949 |  | 0.184949 | 0.466667 | 0.366667 | 0.1 | 0.533333 | 1.0 | 3.4375 | 2.454545 | 1.666667 | 3 | 24 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 9 | 9 | 9 |  | 6.401523 | 4.011702 | 0.222222 | 4.690103 | 90.0 | 0.100179 | 0.777778 | 0.527268 | 0.527268 | 0.25051 |  | 0.25051 | 0.222222 | 0.888889 | 0.555556 | 0.777778 | 1.0 | 3.142857 | 1.0 | 1.4 | 4 |  |
| turtle_soup | target_rr_below_2 | 49 | 49 | 49 |  | 3.160699 | 1.482015 | 0.714286 | 0.873577 | 70.0 | 0.300722 | 0.345688 | 0.171989 | 0.171989 | 0.173699 |  | 0.173699 | 0.714286 | 0.428571 | 0.020408 | 0.244898 | 1.0 | 4.583333 | 5.809524 | 6.0 | 1 | 49 |
| turtle_soup | target_rr_below_3 | 6 | 6 | 6 |  | 1.842827 | 1.1187 |  | 2.590686 | 80.0 | -0.588098 | -0.333333 | -0.555387 | -0.555387 | 0.222054 |  | 0.222054 |  | 0.333333 |  | 0.833333 | 1.0 | 3.2 | 11.0 |  | 1 | 6 |
