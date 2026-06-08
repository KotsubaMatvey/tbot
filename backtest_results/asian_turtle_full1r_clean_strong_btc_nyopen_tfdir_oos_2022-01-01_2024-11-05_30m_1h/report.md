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
| turtle_soup | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 32 | 32 | 32 |  | 3.862956 | 2.000575 | 0.6875 | 1.385574 | 73.125 | 0.331249 | 0.422764 | 0.22409 | 0.22409 | 0.198673 |  | 0.198673 | 0.6875 | 0.53125 | 0.0625 | 0.28125 | 1.0 | 3.777778 | 2.882353 | 4.5 | 2 | 29 |
| turtle_soup | valid | 32 | 32 | 32 |  | 3.842808 | 2.788826 | 0.34375 | 2.430485 | 76.875 | -0.265451 | 0.308388 | 0.059911 | 0.059911 | 0.248477 |  | 0.248477 | 0.34375 | 0.59375 | 0.28125 | 0.625 | 1.0 | 3.35 | 2.631579 | 3.444444 | 7 | 22 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 64 | 64 | 64 |  | 3.852882 | 2.405383 | 0.515625 | 1.908029 | 75.0 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 1.0 | 3.482759 | 2.75 | 3.636364 | 9 | 51 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 13 | 13 | 13 |  | 5.672839 | 3.979606 |  | 5.348909 | 90.0 | -0.267042 | 0.692308 | 0.345152 | 0.345152 | 0.347156 |  | 0.347156 |  | 0.846154 | 0.538462 | 0.846154 | 1.0 | 3.636364 | 2.818182 | 4.571429 | 8 |  |
| turtle_soup | target_rr_below_2 | 45 | 45 | 45 |  | 3.583828 | 1.892161 | 0.733333 | 0.831455 | 70.0 | 0.257268 | 0.364374 | 0.171862 | 0.171862 | 0.192513 |  | 0.192513 | 0.733333 | 0.511111 | 0.066667 | 0.266667 | 1.0 | 3.0 | 2.782609 | 1.666667 |  | 45 |
| turtle_soup | target_rr_below_3 | 6 | 6 | 6 |  | 1.927544 | 1.550151 |  | 2.527095 | 80.0 | -1.0 | -0.333333 | -0.522119 | -0.522119 | 0.188785 |  | 0.188785 |  | 0.333333 | 0.166667 | 1.0 | 1.0 | 4.166667 | 2.0 | 3.0 | 1 | 6 |
