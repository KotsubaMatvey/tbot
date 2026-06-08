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
| turtle_soup | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 17 | 17 | 17 |  | 7.743378 | 5.364886 | 0.411765 | 4.793366 | 84.705882 | 1.016373 | 0.882353 | 0.393699 | 0.393699 | 0.485433 | 0.003222 | 0.488654 | 0.411765 | 0.941176 | 0.588235 | 0.588235 | 1.0 | 4.8 | 1.8125 | 1.2 | 6 | 6 |
| turtle_soup | ETHUSDT | 10 | 10 | 10 |  | 7.950293 | 6.142534 | 0.5 | 5.457629 | 83.0 | 0.728719 | 1.0 | 0.654791 | 0.654791 | 0.345209 |  | 0.345209 | 0.5 | 1.0 | 0.8 | 0.5 | 1.0 | 4.0 | 1.0 | 1.125 | 4 | 5 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 12 | 12 | 12 |  | 5.758157 | 4.634734 | 0.583333 | 3.091721 | 83.333333 | 1.291806 | 0.833333 | 0.451438 | 0.451438 | 0.377043 | 0.004852 | 0.381895 | 0.583333 | 0.916667 | 0.5 | 0.416667 | 1.0 | 5.4 | 1.909091 | 1.166667 | 3 | 5 |
| turtle_soup | valid | 15 | 15 | 15 |  | 9.469498 | 6.900063 | 0.333333 | 6.597524 | 84.666667 | 0.604257 | 1.0 | 0.521569 | 0.521569 | 0.478662 | -0.00023 | 0.478431 | 0.333333 | 1.0 | 0.8 | 0.666667 | 1.0 | 4.1 | 1.2 | 1.166667 | 7 | 6 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 27 | 27 | 27 |  | 7.820013 | 5.644968 | 0.444444 | 5.039389 | 84.074074 | 0.909834 | 0.925926 | 0.490399 | 0.490399 | 0.433498 | 0.002028 | 0.435526 | 0.444444 | 0.962963 | 0.666667 | 0.555556 | 1.0 | 4.533333 | 1.5 | 1.166667 | 10 | 11 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 16 | 16 | 16 |  | 9.661461 | 6.641644 | 0.4375 | 7.231284 | 90.0 | 1.450781 | 0.875 | 0.369935 | 0.369935 | 0.501269 | 0.003795 | 0.505065 | 0.4375 | 0.9375 | 0.875 | 0.5625 | 1.0 | 3.777778 | 1.0 | 1.142857 | 9 |  |
| turtle_soup | target_rr_below_2 | 5 | 5 | 5 |  | 4.17703 | 2.330396 | 0.6 | 1.186724 | 70.0 | 0.201717 | 1.0 | 0.651493 | 0.651493 | 0.349199 | -0.000691 | 0.348507 | 0.6 | 1.0 | 0.2 | 0.4 | 1.0 | 6.5 | 1.6 | 1.0 |  | 5 |
| turtle_soup | target_rr_below_3 | 6 | 6 | 6 |  | 5.945305 | 4.660375 | 0.333333 | 2.404889 | 80.0 | 0.057409 | 1.0 | 0.677392 | 0.677392 | 0.323024 | -0.000416 | 0.322607 | 0.333333 | 1.0 | 0.5 | 0.666667 | 1.0 | 5.25 | 2.666667 | 1.333333 | 1 | 6 |
