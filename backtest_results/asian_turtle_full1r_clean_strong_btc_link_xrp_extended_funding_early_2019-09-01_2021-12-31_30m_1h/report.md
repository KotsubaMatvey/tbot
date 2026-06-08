# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2019-09-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, LINKUSDT, XRPUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2019-09-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 16 | 16 | 16 |  | 2.720206 | 2.198934 | 0.375 | 2.479901 | 76.25 | -0.381593 | 0.226967 | 0.090052 | 0.090052 | 0.136612 | 0.000302 | 0.136915 | 0.375 | 0.4375 | 0.125 | 0.625 | 1.0 | 4.0 | 2.285714 | 2.5 | 4 | 11 |
| turtle_soup | LINKUSDT | 9 | 9 | 9 |  | 5.845319 | 4.102192 | 0.111111 | 2.325084 | 74.444444 | -0.751972 | 0.333333 | 0.23173 | 0.23173 | 0.096316 | 0.005287 | 0.101603 | 0.111111 | 0.666667 | 0.222222 | 0.888889 | 1.0 | 3.75 | 2.666667 | 4.5 | 2 | 8 |
| turtle_soup | XRPUSDT | 8 | 8 | 8 |  | 2.570218 | 2.246465 | 0.25 | 2.55438 | 78.75 | -0.114234 | -0.06526 | -0.146291 | -0.146291 | 0.074552 | 0.006479 | 0.081031 | 0.25 | 0.375 | 0.375 | 0.625 | 1.0 | 4.0 | 8.333333 | 10.0 | 1 | 5 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 21 | 21 | 21 |  | 2.386816 | 2.223116 | 0.285714 | 2.056208 | 75.714286 | -0.35848 | -0.065168 | -0.169731 | -0.169731 | 0.101884 | 0.002679 | 0.104563 | 0.285714 | 0.333333 | 0.238095 | 0.666667 | 1.0 | 4.142857 | 5.571429 | 8.2 | 3 | 16 |
| turtle_soup | valid | 12 | 12 | 12 |  | 5.547482 | 2.805532 | 0.25 | 3.154903 | 77.5 | -0.521587 | 0.62316 | 0.493369 | 0.493369 | 0.12579 | 0.004 | 0.129791 | 0.25 | 0.75 | 0.166667 | 0.75 | 1.0 | 3.555556 | 2.0 | 1.5 | 4 | 8 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 33 | 33 | 33 |  | 3.536149 | 2.442512 | 0.272727 | 2.455734 | 76.363636 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 1.0 | 3.913043 | 3.5625 | 6.285714 | 7 | 24 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 9 | 9 | 9 |  | 5.729978 | 3.097411 |  | 5.703464 | 90.0 | -0.559225 | 0.777778 | 0.616094 | 0.616094 | 0.159972 | 0.001712 | 0.161684 |  | 0.888889 | 0.555556 | 0.888889 | 1.0 | 5.375 | 1.875 | 3.2 | 6 |  |
| turtle_soup | target_rr_below_2 | 21 | 21 | 21 |  | 2.853192 | 2.223116 | 0.428571 | 1.083691 | 70.0 | -0.274004 | 0.005209 | -0.093041 | -0.093041 | 0.094995 | 0.003255 | 0.098249 | 0.428571 | 0.333333 | 0.095238 | 0.571429 | 1.0 | 3.25 | 5.714286 | 14.0 |  | 21 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 1.735361 | 1.762585 |  | 2.316845 | 80.0 | -1.0 | -0.333333 | -0.411637 | -0.411637 | 0.07147 | 0.006834 | 0.078304 |  | 0.333333 |  | 1.0 | 1.0 | 2.666667 | 2.0 |  | 1 | 3 |
