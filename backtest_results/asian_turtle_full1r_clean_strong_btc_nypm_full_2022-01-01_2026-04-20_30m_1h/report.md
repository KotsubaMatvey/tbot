# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m, 1h
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
| turtle_soup | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 11 | 11 | 11 |  | 2.503776 | 1.020809 | 0.545455 | 1.423508 | 71.818182 | 0.150308 | 0.13153 | -0.070953 | -0.070953 | 0.202483 |  | 0.202483 | 0.545455 | 0.454545 | 0.090909 | 0.363636 | 1.0 | 4.0 | 8.6 | 5.0 |  | 10 |
| turtle_soup | valid | 10 | 10 | 10 |  | 2.765956 | 2.616794 | 0.5 | 2.167163 | 78.0 | 0.167358 | 0.553068 | 0.336851 | 0.336851 | 0.216217 |  | 0.216217 | 0.5 | 0.5 | 0.1 | 0.4 | 1.0 | 3.25 | 1.0 | 6.0 | 3 | 7 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 21 | 21 | 21 |  | 2.628623 | 2.244792 | 0.52381 | 1.77763 | 74.761905 | 0.158428 | 0.332263 | 0.123239 | 0.123239 | 0.209023 |  | 0.209023 | 0.52381 | 0.47619 | 0.095238 | 0.380952 | 1.0 | 3.625 | 4.8 | 5.5 | 3 | 17 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 4 | 4 | 4 |  | 2.684836 | 3.058891 |  | 4.75104 | 90.0 | -1.0 |  | -0.30814 | -0.30814 | 0.30814 |  | 0.30814 |  | 0.5 |  | 1.0 | 1.0 | 2.75 | 1.0 |  | 2 |  |
| turtle_soup | target_rr_below_2 | 15 | 15 | 15 |  | 2.661288 | 1.120002 | 0.733333 | 0.856083 | 70.0 | 0.401956 | 0.331834 | 0.142325 | 0.142325 | 0.189509 |  | 0.189509 | 0.733333 | 0.4 | 0.066667 | 0.2 | 1.0 | 3.666667 | 7.333333 | 5.0 |  | 15 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.271216 | 2.271216 |  | 2.742406 | 80.0 | 0.64882 | 1.0 | 0.842857 | 0.842857 | 0.157143 |  | 0.157143 |  | 1.0 | 0.5 | 0.5 | 1.0 | 7.0 | 1.0 | 6.0 | 1 | 2 |
