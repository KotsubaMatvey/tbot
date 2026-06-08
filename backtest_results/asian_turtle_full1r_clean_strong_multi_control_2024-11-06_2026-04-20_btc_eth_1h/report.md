# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
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
| turtle_soup | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 8 | 8 | 8 |  | 2.890398 | 3.278595 | 0.75 | 0.706794 | 70.0 | 0.099479 | 0.184083 | 0.076358 | 0.076358 | 0.107725 |  | 0.107725 | 0.75 | 0.375 | 0.125 | 0.25 | 1.0 | 3.0 | 3.0 | 1.0 |  | 8 |
| turtle_soup | valid | 11 | 11 | 11 |  | 4.762302 | 4.364205 | 0.727273 | 2.617427 | 77.272727 | 0.865324 | 0.933103 | 0.715514 | 0.715514 | 0.21759 |  | 0.21759 | 0.727273 | 0.909091 | 0.636364 | 0.272727 | 1.0 | 9.333333 | 2.3 | 1.571429 | 1 | 8 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 19 | 19 | 19 |  | 3.974132 | 4.242876 | 0.736842 | 1.81295 | 74.210526 | 0.542863 | 0.617726 | 0.446395 | 0.446395 | 0.171331 |  | 0.171331 | 0.736842 | 0.684211 | 0.421053 | 0.263158 | 1.0 | 6.8 | 2.461538 | 1.5 | 1 | 16 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 3 | 3 | 3 |  | 8.291571 | 6.642168 | 0.333333 | 5.664978 | 90.0 | 0.358691 | 1.0 | 0.714566 | 0.714566 | 0.285434 |  | 0.285434 | 0.333333 | 1.0 | 1.0 | 0.666667 | 1.0 | 12.5 | 1.333333 | 1.666667 | 1 |  |
| turtle_soup | target_rr_below_2 | 14 | 14 | 14 |  | 3.201757 | 3.132447 | 0.857143 | 0.880011 | 70.0 | 0.532973 | 0.4812 | 0.33336 | 0.33336 | 0.147841 |  | 0.147841 | 0.857143 | 0.571429 | 0.285714 | 0.142857 | 1.0 | 3.0 | 3.125 | 1.5 |  | 14 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.904596 | 2.904596 | 0.5 | 2.565486 | 80.0 | 0.888347 | 1.0 | 0.83539 | 0.83539 | 0.16461 |  | 0.16461 | 0.5 | 1.0 | 0.5 | 0.5 | 1.0 | 3.0 | 1.5 | 1.0 |  | 2 |
