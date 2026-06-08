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
- timeframes: 1h
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
| turtle_soup | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 12 | 12 | 12 |  | 2.199988 | 1.74267 | 0.5 | 2.005918 | 73.333333 | -0.175458 | 0.135956 | 0.007869 | 0.007869 | 0.128731 | -0.000645 | 0.128086 | 0.5 | 0.333333 | 0.083333 | 0.5 | 1.0 | 3.0 | 2.75 | 2.0 | 2 | 10 |
| turtle_soup | LINKUSDT | 7 | 7 | 7 |  | 6.653587 | 4.102192 | 0.142857 | 2.344008 | 74.285714 | -0.681107 | 0.428571 | 0.339142 | 0.339142 | 0.087737 | 0.001692 | 0.089429 | 0.142857 | 0.714286 | 0.285714 | 0.857143 | 1.0 | 3.166667 | 2.6 | 4.5 | 2 | 6 |
| turtle_soup | XRPUSDT | 5 | 5 | 5 |  | 3.168903 | 2.442512 | 0.4 | 2.340512 | 78.0 | 0.417225 | 0.495583 | 0.414835 | 0.414835 | 0.074486 | 0.006263 | 0.080748 | 0.4 | 0.6 | 0.6 | 0.4 | 1.0 | 4.0 | 8.333333 | 10.0 | 1 | 3 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 13 | 13 | 13 |  | 2.513317 | 2.390096 | 0.461538 | 1.409191 | 73.076923 | 0.036302 | 0.048575 | -0.041112 | -0.041112 | 0.090655 | -0.000968 | 0.089686 | 0.461538 | 0.307692 | 0.307692 | 0.461538 | 1.0 | 3.0 | 8.0 | 9.5 | 1 | 11 |
| turtle_soup | valid | 11 | 11 | 11 |  | 5.104215 | 2.729548 | 0.272727 | 3.078377 | 76.363636 | -0.478095 | 0.588902 | 0.461551 | 0.461551 | 0.122987 | 0.004364 | 0.127351 | 0.272727 | 0.727273 | 0.181818 | 0.727273 | 1.0 | 3.375 | 2.125 | 1.5 | 4 | 8 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 24 | 24 | 24 |  | 3.700812 | 2.522187 | 0.375 | 2.174235 | 74.583333 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 0.375 | 0.5 | 0.25 | 0.583333 | 1.0 | 3.214286 | 4.083333 | 6.833333 | 5 | 19 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 5 | 5 | 5 |  | 6.706325 | 2.966974 |  | 6.368747 | 90.0 | -0.206605 | 1.0 | 0.834799 | 0.834799 | 0.162123 | 0.003078 | 0.165201 |  | 1.0 | 0.8 | 0.8 | 1.0 | 4.5 | 2.0 | 3.25 | 4 |  |
| turtle_soup | target_rr_below_2 | 18 | 18 | 18 |  | 2.911464 | 2.332814 | 0.5 | 1.012529 | 70.0 | -0.153005 | 0.061633 | -0.031332 | -0.031332 | 0.091852 | 0.001112 | 0.092964 | 0.5 | 0.333333 | 0.111111 | 0.5 | 1.0 | 2.666667 | 6.166667 | 14.0 |  | 18 |
| turtle_soup | target_rr_below_3 | 1 | 1 | 1 |  | 2.881517 | 2.881517 |  | 2.112369 | 80.0 | -1.0 | 1.0 | 0.932577 | 0.932577 | 0.067423 |  | 0.067423 |  | 1.0 |  | 1.0 | 1.0 | 3.0 | 2.0 |  | 1 | 1 |
