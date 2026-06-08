# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
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
| turtle_soup | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 27 | 27 | 27 |  | 3.922385 | 2.098568 | 0.555556 | 1.833193 | 73.333333 | 0.299031 | 0.463406 | 0.330119 | 0.330119 | 0.133288 |  | 0.133288 | 0.555556 | 0.62963 | 0.111111 | 0.37037 | 1.0 | 5.3 | 4.823529 | 5.0 | 2 | 25 |
| turtle_soup | valid | 26 | 26 | 26 |  | 3.202553 | 1.442453 | 0.307692 | 2.486356 | 76.923077 | -0.42502 | 0.156051 | -0.008965 | -0.008965 | 0.165016 |  | 0.165016 | 0.307692 | 0.5 | 0.115385 | 0.692308 | 1.0 | 2.722222 | 1.923077 | 1.666667 | 3 | 18 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 53 | 53 | 53 |  | 3.56926 | 1.892161 | 0.433962 | 2.153613 | 75.09434 | -0.056164 | 0.312628 | 0.163776 | 0.163776 | 0.148852 |  | 0.148852 | 0.433962 | 0.566038 | 0.113208 | 0.528302 | 1.0 | 3.642857 | 3.566667 | 3.333333 | 5 | 43 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 10 | 10 | 10 |  | 2.814683 | 1.442453 |  | 6.001797 | 90.0 | -1.0 | 0.2 | 0.015163 | 0.015163 | 0.184837 |  | 0.184837 |  | 0.6 | 0.1 | 1.0 | 1.0 | 2.4 | 1.0 | 1.0 | 3 |  |
| turtle_soup | target_rr_below_2 | 36 | 36 | 36 |  | 3.736831 | 1.687088 | 0.555556 | 0.999505 | 70.0 | 0.033258 | 0.265814 | 0.12312 | 0.12312 | 0.142694 |  | 0.142694 | 0.555556 | 0.5 | 0.055556 | 0.416667 | 1.0 | 4.4 | 3.888889 | 3.0 | 2 | 36 |
| turtle_soup | target_rr_below_3 | 7 | 7 | 7 |  | 3.78543 | 2.672301 | 0.428571 | 2.591618 | 80.0 | 0.83229 | 0.714286 | 0.585171 | 0.585171 | 0.129115 |  | 0.129115 | 0.428571 | 0.857143 | 0.428571 | 0.428571 | 1.0 | 4.0 | 5.166667 | 4.333333 |  | 7 |
