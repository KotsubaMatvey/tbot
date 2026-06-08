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
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 7 | 7 | 7 |  | 3.689183 | 4.514163 | 0.857143 | 1.060677 | 71.428571 | 0.585851 | 0.766893 | 0.6221 | 0.6221 | 0.144704 | 8.8e-05 | 0.144792 | 0.857143 | 0.714286 | 0.285714 | 0.142857 | 1.0 | 12.0 | 1.6 | 1.0 |  | 7 |
| turtle_soup | valid | 13 | 13 | 13 |  | 3.842261 | 3.666389 | 0.692308 | 1.790802 | 73.846154 | 0.887611 | 0.751093 | 0.513573 | 0.513573 | 0.240552 | -0.003033 | 0.237519 | 0.692308 | 0.846154 | 0.538462 | 0.230769 | 1.0 | 10.333333 | 2.818182 | 1.571429 |  | 11 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 6.07309 | 6.07309 | 0.5 | 4.581823 | 90.0 | 1.038037 | 1.0 | 0.672486 | 0.672486 | 0.327514 |  | 0.327514 | 0.5 | 1.0 | 1.0 | 0.5 | 1.0 | 22.0 | 1.5 | 2.0 |  |  |
| turtle_soup | target_rr_below_2 | 16 | 16 | 16 |  | 3.607675 | 3.220168 | 0.8125 | 1.027566 | 70.0 | 0.736696 | 0.695778 | 0.501408 | 0.501408 | 0.196796 | -0.002426 | 0.194371 | 0.8125 | 0.75 | 0.375 | 0.125 | 1.0 | 4.5 | 2.666667 | 1.333333 |  | 16 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.952352 | 2.952352 | 0.5 | 2.550238 | 80.0 | 0.888347 | 1.0 | 0.831829 | 0.831829 | 0.168171 |  | 0.168171 | 0.5 | 1.0 | 0.5 | 0.5 | 1.0 | 12.0 | 2.0 | 1.0 |  | 2 |
