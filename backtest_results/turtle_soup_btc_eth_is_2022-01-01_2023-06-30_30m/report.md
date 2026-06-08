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
| turtle_soup | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 17 | 17 | 17 |  | 3.528176 | 1.629994 | 0.529412 | 2.031685 | 75.294118 | 0.383324 | 0.151613 | -0.077282 | -0.077282 | 0.227109 | 0.001786 | 0.228895 | 0.529412 | 0.411765 | 0.235294 | 0.411765 | 1.0 | 3.285714 | 5.428571 | 2.75 | 2 | 14 |
| turtle_soup | ETHUSDT | 10 | 10 | 10 |  | 3.029212 | 2.530633 | 0.7 | 1.79986 | 74.0 | 0.783255 | 0.482109 | 0.332267 | 0.332267 | 0.149777 | 6.5e-05 | 0.149842 | 0.7 | 0.6 | 0.2 | 0.3 | 1.0 | 4.333333 | 1.833333 | 2.0 | 1 | 8 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 12 | 12 | 12 |  | 2.82255 | 1.729338 | 0.666667 | 1.393509 | 73.333333 | 0.58187 | 0.382672 | 0.166613 | 0.166613 | 0.213297 | 0.002763 | 0.216059 | 0.666667 | 0.583333 | 0.166667 | 0.25 | 1.0 | 2.333333 | 5.714286 | 3.5 | 1 | 11 |
| turtle_soup | valid | 15 | 15 | 15 |  | 3.760034 | 2.491164 | 0.533333 | 2.387676 | 76.0 | 0.491108 | 0.187097 | 0.000635 | 0.000635 | 0.186605 | -0.000143 | 0.186462 | 0.533333 | 0.4 | 0.266667 | 0.466667 | 1.0 | 4.142857 | 1.5 | 2.0 | 2 | 11 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 27 | 27 | 27 |  | 3.343374 | 1.935747 | 0.592593 | 1.945824 | 74.814815 | 0.531447 | 0.274019 | 0.074403 | 0.074403 | 0.198468 | 0.001148 | 0.199616 | 0.592593 | 0.481481 | 0.222222 | 0.37037 | 1.0 | 3.6 | 3.769231 | 2.5 | 3 | 22 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 5 | 5 | 5 |  | 8.529939 | 6.492125 | 0.6 | 5.545097 | 90.0 | 2.428436 | 1.0 | 0.806525 | 0.806525 | 0.193475 |  | 0.193475 | 0.6 | 1.0 | 1.0 | 0.4 | 1.0 | 6.5 | 1.4 | 1.8 | 2 |  |
| turtle_soup | target_rr_below_2 | 19 | 19 | 19 |  | 2.303339 | 1.522929 | 0.684211 | 0.936752 | 70.0 | 0.274047 | 0.284132 | 0.107323 | 0.107323 | 0.177599 | -0.00079 | 0.176809 | 0.684211 | 0.421053 | 0.052632 | 0.263158 | 1.0 | 3.4 | 5.25 | 6.0 |  | 19 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 1.28599 | 0.765989 |  | 2.337826 | 80.0 | -1.0 | -1.0 | -1.354297 | -1.354297 | 0.338961 | 0.015336 | 0.354297 |  |  |  | 1.0 | 1.0 | 2.0 |  |  | 1 | 3 |
