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
- timeframes: 30m
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
| turtle_soup | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 23 | 23 | 23 |  | 9.787818 | 5.364886 | 0.478261 | 5.471472 | 83.478261 | 1.000838 | 0.913043 | 0.448799 | 0.448799 | 0.461863 | 0.002381 | 0.464244 | 0.478261 | 0.956522 | 0.565217 | 0.521739 | 1.0 | 4.666667 | 1.590909 | 1.153846 | 7 | 9 |
| turtle_soup | ETHUSDT | 14 | 14 | 14 |  | 7.363143 | 5.910686 | 0.571429 | 4.331874 | 80.0 | 0.784724 | 0.857143 | 0.537197 | 0.537197 | 0.319946 |  | 0.319946 | 0.571429 | 0.928571 | 0.714286 | 0.428571 | 1.0 | 3.833333 | 1.0 | 1.2 | 4 | 9 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 21 | 21 | 21 |  | 8.677601 | 5.018019 | 0.619048 | 4.070408 | 80.47619 | 1.090138 | 0.809524 | 0.451261 | 0.451261 | 0.355491 | 0.002773 | 0.358263 | 0.619048 | 0.904762 | 0.47619 | 0.380952 | 1.0 | 4.75 | 1.526316 | 1.1 | 4 | 11 |
| turtle_soup | valid | 16 | 16 | 16 |  | 9.123387 | 6.770082 | 0.375 | 6.31322 | 84.375 | 0.694532 | 1.0 | 0.522917 | 0.522917 | 0.477299 | -0.000216 | 0.477083 | 0.375 | 1.0 | 0.8125 | 0.625 | 1.0 | 4.1 | 1.1875 | 1.230769 | 7 | 7 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |
| turtle_soup | 1 | 6 | 6 | 6 |  | 15.341572 | 5.141122 | 0.666667 | 6.141585 | 75.0 | 0.714599 | 0.666667 | 0.262748 | 0.262748 | 0.403919 |  | 0.403919 | 0.666667 | 0.833333 | 0.666667 | 0.333333 | 1.0 | 4.5 | 1.0 | 1.25 | 1 | 5 |
| turtle_soup | 4 | 3 | 3 | 3 |  | 4.699133 | 5.003081 | 0.666667 | 4.088125 | 83.333333 | 1.279864 | 1.0 | 0.737124 | 0.737124 | 0.262876 |  | 0.262876 | 0.666667 | 1.0 | 0.333333 | 0.333333 | 1.0 | 2.0 | 1.0 | 1.0 |  | 1 |
| turtle_soup | 8 | 1 | 1 | 1 |  | 10.91663 | 10.91663 | 1.0 | 1.312699 | 70.0 | 1.312699 | 1.0 | 0.814492 | 0.814492 | 0.185508 |  | 0.185508 | 1.0 | 1.0 |  |  | 1.0 |  | 1.0 |  |  | 1 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 37 | 37 | 37 |  | 8.870373 | 5.644968 | 0.513514 | 5.040273 | 82.162162 | 0.919065 | 0.891892 | 0.482247 | 0.482247 | 0.408165 | 0.00148 | 0.409645 | 0.513514 | 0.945946 | 0.621622 | 0.486486 | 1.0 | 4.388889 | 1.371429 | 1.173913 | 11 | 18 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 19 | 19 | 19 |  | 8.887099 | 6.56741 | 0.421053 | 8.181736 | 90.0 | 1.281539 | 0.894737 | 0.421267 | 0.421267 | 0.470274 | 0.003196 | 0.47347 | 0.421053 | 0.947368 | 0.842105 | 0.578947 | 1.0 | 3.818182 | 1.0 | 1.125 | 10 |  |
| turtle_soup | target_rr_below_2 | 11 | 11 | 11 |  | 10.885943 | 4.251449 | 0.727273 | 1.323555 | 70.0 | 0.660279 | 0.818182 | 0.475597 | 0.475597 | 0.342899 | -0.000314 | 0.342585 | 0.727273 | 0.909091 | 0.272727 | 0.272727 | 1.0 | 5.333333 | 1.3 | 1.0 |  | 11 |
| turtle_soup | target_rr_below_3 | 7 | 7 | 7 |  | 5.657651 | 3.931726 | 0.428571 | 2.353999 | 80.0 | 0.341873 | 1.0 | 0.658213 | 0.658213 | 0.342144 | -0.000357 | 0.341787 | 0.428571 | 1.0 | 0.571429 | 0.571429 | 1.0 | 5.25 | 2.428571 | 1.5 | 1 | 7 |
