# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 30 | 30 | 30 |  | 3.347259 | 1.48157 | 0.533333 | 1.428872 | 73.333333 | 0.102199 | 0.208464 | 0.061161 | 0.061161 | 0.147303 | 0.533333 | 0.466667 | 0.033333 | 0.4 | 1.0 | 4.0 | 4.214286 | 1.0 | 1 | 26 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 4 | 4 | 4 |  | 2.666082 | 2.624423 |  | 4.324826 | 90.0 | -1.0 | 0.125 | -0.136293 | -0.136293 | 0.261293 |  | 0.75 | 0.25 | 1.0 | 1.0 | 2.0 | 1.0 | 1.0 | 1 |  |
| turtle_soup | target_rr_below_2 | 24 | 24 | 24 |  | 3.647962 | 1.380579 | 0.666667 | 0.850535 | 70.0 | 0.267315 | 0.236123 | 0.100949 | 0.100949 | 0.135174 | 0.666667 | 0.416667 |  | 0.291667 | 1.0 | 4.714286 | 5.0 |  |  | 24 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 1.101179 | 1.101179 |  | 2.576999 | 80.0 | 0.325206 | 0.043484 | -0.021388 | -0.021388 | 0.064871 |  | 0.5 |  | 0.5 | 1.0 | 7.0 | 6.0 |  |  | 2 |
