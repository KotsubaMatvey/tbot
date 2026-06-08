# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
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
| turtle_soup | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 4 | 4 | 4 |  | 3.430537 | 3.414238 | 1.0 | 0.512863 | 70.0 | 0.512863 | 0.592062 | 0.480759 | 0.480759 | 0.111303 |  | 0.111303 | 1.0 | 0.5 | 0.25 |  | 1.0 |  | 1.5 | 1.0 |  | 4 |
| turtle_soup | valid | 7 | 7 | 7 |  | 4.91828 | 4.671872 | 0.857143 | 2.485194 | 77.142857 | 1.472684 | 1.0 | 0.730428 | 0.730428 | 0.269572 |  | 0.269572 | 0.857143 | 1.0 | 0.857143 | 0.142857 | 1.0 | 22.0 | 1.428571 | 1.666667 |  | 5 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.639639 | 0.639639 | 0.21202 |  | 0.21202 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 6.07309 | 6.07309 | 0.5 | 4.581823 | 90.0 | 1.038037 | 1.0 | 0.672486 | 0.672486 | 0.327514 |  | 0.327514 | 0.5 | 1.0 | 1.0 | 0.5 | 1.0 | 22.0 | 1.5 | 2.0 |  |  |
| turtle_soup | target_rr_below_2 | 8 | 8 | 8 |  | 3.954965 | 4.090276 | 1.0 | 0.938434 | 70.0 | 0.938434 | 0.796031 | 0.613603 | 0.613603 | 0.182428 |  | 0.182428 | 1.0 | 0.75 | 0.5 |  | 1.0 |  | 1.5 | 1.5 |  | 8 |
| turtle_soup | target_rr_below_3 | 1 | 1 | 1 |  | 4.364205 | 4.364205 | 1.0 | 2.776694 | 80.0 | 2.776694 | 1.0 | 0.782236 | 0.782236 | 0.217764 |  | 0.217764 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
