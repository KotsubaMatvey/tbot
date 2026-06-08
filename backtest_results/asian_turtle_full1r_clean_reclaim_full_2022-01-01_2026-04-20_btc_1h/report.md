# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 1h
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
| turtle_soup | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 21 | 21 | 21 |  | 4.134544 | 2.314313 | 0.714286 | 1.245267 | 72.380952 | 0.425712 | 0.613344 | 0.477739 | 0.477739 | 0.135605 |  | 0.135605 | 0.714286 | 0.619048 | 0.047619 | 0.190476 | 1.0 | 7.25 | 5.230769 | 1.0 | 1 | 20 |
| turtle_soup | valid | 21 | 21 | 21 |  | 3.437777 | 2.469999 | 0.47619 | 2.126569 | 76.190476 | 0.142603 | 0.376573 | 0.180067 | 0.180067 | 0.196506 |  | 0.196506 | 0.47619 | 0.619048 | 0.333333 | 0.52381 | 1.0 | 4.272727 | 1.769231 | 1.571429 | 2 | 15 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 42 | 42 | 42 |  | 3.786161 | 2.392156 | 0.595238 | 1.685918 | 74.285714 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 1.0 | 5.066667 | 3.5 | 1.5 | 3 | 35 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 7 | 7 | 7 |  | 4.470657 | 4.011702 | 0.142857 | 4.50181 | 90.0 | -0.417704 | 0.714286 | 0.452751 | 0.452751 | 0.261535 |  | 0.261535 | 0.142857 | 0.857143 | 0.428571 | 0.857143 | 1.0 | 5.5 | 1.166667 | 1.666667 | 2 |  |
| turtle_soup | target_rr_below_2 | 31 | 31 | 31 |  | 3.747127 | 2.098568 | 0.741935 | 0.902856 | 70.0 | 0.406788 | 0.444783 | 0.296061 | 0.296061 | 0.148722 |  | 0.148722 | 0.741935 | 0.548387 | 0.129032 | 0.225806 | 1.0 | 4.714286 | 3.588235 | 1.5 | 1 | 31 |
| turtle_soup | target_rr_below_3 | 4 | 4 | 4 |  | 2.890799 | 2.917808 | 0.25 | 2.826833 | 80.0 | 0.562026 | 0.5 | 0.3667 | 0.3667 | 0.1333 |  | 0.1333 | 0.25 | 0.75 | 0.25 | 0.5 | 1.0 | 5.0 | 7.666667 | 1.0 |  | 4 |
