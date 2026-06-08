# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, SOLUSDT, BNBUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, LINKUSDT, AVAXUSDT
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
| turtle_soup | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | ADAUSDT | 25 | 25 | 25 |  | 2.713385 | 2.227306 | 0.44 | 2.394427 | 77.6 | 0.225925 | 0.415873 | 0.301614 | 0.301614 | 0.112167 | 0.002092 | 0.11426 | 0.44 | 0.64 | 0.32 | 0.52 | 1.0 | 3.923077 | 1.8125 | 2.875 | 3 | 17 |
| turtle_soup | AVAXUSDT | 22 | 22 | 22 |  | 2.758244 | 2.569183 | 0.5 | 2.027116 | 76.818182 | 0.228401 | 0.380556 | 0.292452 | 0.292452 | 0.090226 | -0.002122 | 0.088104 | 0.5 | 0.5 | 0.227273 | 0.454545 | 1.0 | 2.6 | 4.454545 | 10.8 | 2 | 17 |
| turtle_soup | BNBUSDT | 6 | 6 | 6 |  | 3.248693 | 0.668376 | 0.166667 | 3.315811 | 83.333333 | -0.159166 | -0.333333 | -0.606617 | -0.606617 | 0.273284 |  | 0.273284 | 0.166667 | 0.333333 | 0.166667 | 0.833333 | 1.0 | 2.0 | 1.0 | 1.0 | 1 | 2 |
| turtle_soup | BTCUSDT | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |
| turtle_soup | DOGEUSDT | 31 | 31 | 31 |  | 4.120365 | 2.729843 | 0.516129 | 1.793149 | 75.483871 | 0.453415 | 0.423916 | 0.306384 | 0.306384 | 0.116729 | 0.000802 | 0.117531 | 0.516129 | 0.612903 | 0.225806 | 0.419355 | 1.0 | 5.461538 | 3.421053 | 5.285714 | 3 | 26 |
| turtle_soup | LINKUSDT | 21 | 21 | 21 |  | 3.031591 | 2.795639 | 0.52381 | 1.859083 | 74.285714 | 0.374016 | 0.519548 | 0.38682 | 0.38682 | 0.132491 | 0.000236 | 0.132728 | 0.52381 | 0.666667 | 0.238095 | 0.428571 | 1.0 | 3.555556 | 1.714286 | 3.2 | 2 | 17 |
| turtle_soup | SOLUSDT | 22 | 22 | 22 |  | 5.062469 | 2.63735 | 0.636364 | 2.433207 | 77.272727 | 0.900395 | 0.388445 | 0.246545 | 0.246545 | 0.142093 | -0.000193 | 0.1419 | 0.636364 | 0.636364 | 0.318182 | 0.363636 | 1.0 | 3.375 | 2.642857 | 1.857143 | 1 | 16 |
| turtle_soup | XRPUSDT | 17 | 17 | 17 |  | 4.993655 | 2.699944 | 0.352941 | 3.647997 | 82.941176 | 0.920624 | 0.476039 | 0.335812 | 0.335812 | 0.144259 | -0.004032 | 0.140227 | 0.352941 | 0.647059 | 0.411765 | 0.411765 | 1.0 | 3.428571 | 1.909091 | 3.857143 | 2 | 8 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 65 | 65 | 65 |  | 3.144673 | 2.465497 | 0.415385 | 2.192204 | 77.076923 | 0.304211 | 0.444237 | 0.322034 | 0.322034 | 0.12269 | -0.000487 | 0.122204 | 0.415385 | 0.630769 | 0.246154 | 0.492308 | 1.0 | 3.875 | 2.512195 | 5.5 | 8 | 47 |
| turtle_soup | valid | 99 | 99 | 99 |  | 4.111508 | 2.729843 | 0.585859 | 2.249888 | 76.666667 | 0.635895 | 0.44158 | 0.294823 | 0.294823 | 0.147207 | -0.00045 | 0.146757 | 0.585859 | 0.626263 | 0.333333 | 0.373737 | 1.0 | 4.324324 | 2.629032 | 2.909091 | 6 | 74 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 164 | 164 | 164 |  | 3.728311 | 2.60583 | 0.518293 | 2.227025 | 76.829268 | 0.504435 | 0.442633 | 0.305608 | 0.305608 | 0.13749 | -0.000464 | 0.137026 | 0.518293 | 0.628049 | 0.29878 | 0.420732 | 1.0 | 4.115942 | 2.582524 | 3.755102 | 14 | 121 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 43 | 43 | 43 |  | 4.378528 | 3.420195 | 0.27907 | 4.935873 | 90.0 | 1.067182 | 0.44186 | 0.27919 | 0.27919 | 0.162262 | 0.000408 | 0.16267 | 0.27907 | 0.72093 | 0.511628 | 0.581395 | 1.0 | 4.16 | 1.903226 | 3.454545 | 7 |  |
| turtle_soup | target_rr_below_2 | 95 | 95 | 95 |  | 3.16021 | 2.314313 | 0.673684 | 0.962585 | 70.0 | 0.258957 | 0.448521 | 0.324591 | 0.324591 | 0.12505 | -0.001119 | 0.12393 | 0.673684 | 0.568421 | 0.168421 | 0.315789 | 1.0 | 3.666667 | 3.12963 | 3.0625 | 4 | 95 |
| turtle_soup | target_rr_below_3 | 26 | 26 | 26 |  | 4.728706 | 2.569183 | 0.346154 | 2.367077 | 80.0 | 0.470678 | 0.422399 | 0.279938 | 0.279938 | 0.141976 | 0.000486 | 0.142462 | 0.346154 | 0.692308 | 0.423077 | 0.538462 | 1.0 | 5.0 | 2.111111 | 5.363636 | 3 | 26 |
