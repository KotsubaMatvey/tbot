# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT
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
| turtle_soup | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 36 | 36 | 36 |  | 3.58461 | 2.103067 | 0.583333 | 1.7014 | 73.055556 | 0.218602 | 0.360684 | 0.234643 | 0.234643 | 0.126041 |  | 0.126041 | 0.583333 | 0.555556 | 0.111111 | 0.361111 | 1.0 | 4.769231 | 4.55 | 4.0 | 2 | 33 |
| turtle_soup | valid | 37 | 37 | 37 |  | 3.666262 | 2.469999 | 0.432432 | 2.525323 | 77.027027 | -0.041405 | 0.387067 | 0.206421 | 0.206421 | 0.180646 |  | 0.180646 | 0.432432 | 0.621622 | 0.27027 | 0.567568 | 1.0 | 3.666667 | 2.086957 | 1.6 | 4 | 26 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 73 | 73 | 73 |  | 3.625995 | 2.185569 | 0.506849 | 2.119005 | 75.068493 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 1.0 | 4.088235 | 3.232558 | 2.285714 | 6 | 59 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 14 | 14 | 14 |  | 3.788567 | 2.624423 | 0.071429 | 5.936624 | 90.0 | -0.708852 | 0.285714 | 0.087029 | 0.087029 | 0.198685 |  | 0.198685 | 0.071429 | 0.642857 | 0.285714 | 0.928571 | 1.0 | 4.0 | 1.111111 | 1.5 | 4 |  |
| turtle_soup | target_rr_below_2 | 50 | 50 | 50 |  | 3.58701 | 2.103067 | 0.64 | 0.966046 | 70.0 | 0.173178 | 0.326122 | 0.181987 | 0.181987 | 0.144135 |  | 0.144135 | 0.64 | 0.52 | 0.12 | 0.34 | 1.0 | 4.235294 | 3.653846 | 2.0 | 2 | 50 |
| turtle_soup | target_rr_below_3 | 9 | 9 | 9 |  | 3.589689 | 2.672301 | 0.444444 | 2.585811 | 80.0 | 0.844747 | 0.777778 | 0.640775 | 0.640775 | 0.137003 |  | 0.137003 | 0.444444 | 0.888889 | 0.444444 | 0.444444 | 1.0 | 3.75 | 4.25 | 3.5 |  | 9 |
