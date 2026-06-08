# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, SOLUSDT
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
| turtle_soup | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |
| turtle_soup | SOLUSDT | 22 | 22 | 22 |  | 5.062469 | 2.63735 | 0.636364 | 2.433207 | 77.272727 | 0.900395 | 0.388445 | 0.246545 | 0.246545 | 0.142093 | -0.000193 | 0.1419 | 0.636364 | 0.636364 | 0.318182 | 0.363636 | 1.0 | 3.375 | 2.642857 | 1.857143 | 1 | 16 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 10 | 10 | 10 |  | 3.733671 | 3.414238 | 0.7 | 2.176023 | 75.0 | 0.638163 | 0.436825 | 0.263623 | 0.263623 | 0.173236 | -3.4e-05 | 0.173202 | 0.7 | 0.6 | 0.3 | 0.3 | 1.0 | 6.333333 | 1.5 | 1.0 |  | 8 |
| turtle_soup | valid | 32 | 32 | 32 |  | 4.681602 | 3.026164 | 0.6875 | 1.952359 | 75.3125 | 0.908342 | 0.603437 | 0.431841 | 0.431841 | 0.172931 | -0.001335 | 0.171596 | 0.6875 | 0.75 | 0.40625 | 0.28125 | 1.0 | 5.666667 | 2.791667 | 1.769231 | 1 | 26 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 42 | 42 | 42 |  | 4.455905 | 3.026164 | 0.690476 | 2.005612 | 75.238095 | 0.844014 | 0.563768 | 0.391789 | 0.391789 | 0.173004 | -0.001025 | 0.171979 | 0.690476 | 0.714286 | 0.380952 | 0.285714 | 1.0 | 5.833333 | 2.533333 | 1.625 | 1 | 34 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 8 | 8 | 8 |  | 6.59695 | 6.985109 | 0.5 | 5.26342 | 90.0 | 1.69249 | 0.25 | 0.00191 | 0.00191 | 0.248594 | -0.000504 | 0.24809 | 0.5 | 0.625 | 0.625 | 0.5 | 1.0 | 8.25 | 1.6 | 2.0 |  |  |
| turtle_soup | target_rr_below_2 | 28 | 28 | 28 |  | 4.206121 | 2.599384 | 0.785714 | 0.996687 | 70.0 | 0.625224 | 0.631366 | 0.476985 | 0.476985 | 0.155775 | -0.001394 | 0.154381 | 0.785714 | 0.714286 | 0.285714 | 0.178571 | 1.0 | 3.4 | 2.95 | 1.5 | 1 | 28 |
| turtle_soup | target_rr_below_3 | 6 | 6 | 6 |  | 2.766834 | 2.40944 | 0.5 | 2.370187 | 80.0 | 0.73373 | 0.666667 | 0.514047 | 0.514047 | 0.152619 |  | 0.152619 | 0.5 | 0.833333 | 0.5 | 0.5 | 1.0 | 6.666667 | 1.8 | 1.333333 |  | 6 |
