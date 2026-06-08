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
| turtle_soup | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.247065 | 0.247065 | 0.193313 | 0.000945 | 0.194258 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |
| turtle_soup | SOLUSDT | 55 | 55 | 55 |  | 3.931285 | 2.572817 | 0.436364 | 2.74161 | 76.909091 | 0.142835 | 0.266647 | 0.140251 | 0.140251 | 0.126602 | -0.000205 | 0.126396 | 0.436364 | 0.527273 | 0.236364 | 0.545455 | 1.0 | 3.966667 | 2.068966 | 1.923077 | 7 | 39 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 59 | 59 | 59 |  | 3.631604 | 2.098341 | 0.627119 | 1.561274 | 73.389831 | 0.300284 | 0.42066 | 0.254725 | 0.254725 | 0.164837 | 0.001099 | 0.165935 | 0.627119 | 0.525424 | 0.118644 | 0.322034 | 1.0 | 4.894737 | 4.645161 | 1.714286 | 4 | 52 |
| turtle_soup | valid | 80 | 80 | 80 |  | 3.765933 | 2.429642 | 0.4875 | 2.374236 | 76.0 | 0.223593 | 0.336472 | 0.167981 | 0.167981 | 0.16845 | 4.1e-05 | 0.168491 | 0.4875 | 0.5625 | 0.2625 | 0.4875 | 1.0 | 4.153846 | 2.377778 | 1.857143 | 9 | 60 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 139 | 139 | 139 |  | 3.708916 | 2.314313 | 0.546763 | 2.029166 | 74.892086 | 0.256146 | 0.372207 | 0.204801 | 0.204801 | 0.166916 | 0.00049 | 0.167406 | 0.546763 | 0.546763 | 0.201439 | 0.417266 | 1.0 | 4.396552 | 3.302632 | 1.821429 | 13 | 112 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 27 | 27 | 27 |  | 5.706719 | 4.67574 | 0.222222 | 5.836838 | 90.0 | 0.391181 | 0.555556 | 0.352173 | 0.352173 | 0.203313 | 7e-05 | 0.203383 | 0.222222 | 0.777778 | 0.555556 | 0.740741 | 1.0 | 4.3 | 1.142857 | 1.866667 | 9 |  |
| turtle_soup | target_rr_below_2 | 98 | 98 | 98 |  | 3.35752 | 1.987824 | 0.683673 | 0.912804 | 70.0 | 0.267026 | 0.354457 | 0.19895 | 0.19895 | 0.155395 | 0.000112 | 0.155507 | 0.683673 | 0.479592 | 0.102041 | 0.285714 | 1.0 | 4.5 | 4.106383 | 1.9 | 3 | 98 |
| turtle_soup | target_rr_below_3 | 14 | 14 | 14 |  | 2.315778 | 1.643365 | 0.214286 | 2.500331 | 80.0 | -0.080443 | 0.142857 | -0.038461 | -0.038461 | 0.177372 | 0.003946 | 0.181318 | 0.214286 | 0.571429 | 0.214286 | 0.714286 | 1.0 | 4.3 | 4.25 | 1.333333 | 1 | 14 |
