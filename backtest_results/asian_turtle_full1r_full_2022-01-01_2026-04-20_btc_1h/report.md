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
- timeframes: 1h
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
| turtle_soup | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 58 | 58 | 58 |  | 3.587288 | 2.180341 | 0.62069 | 1.53895 | 73.62069 | 0.277049 | 0.46881 | 0.317314 | 0.317314 | 0.151496 |  | 0.151496 | 0.62069 | 0.568966 | 0.155172 | 0.327586 | 1.0 | 5.421053 | 3.30303 | 1.555556 | 3 | 50 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 8 | 8 | 8 |  | 4.146308 | 3.889711 | 0.125 | 4.807616 | 90.0 | -0.490491 | 0.75 | 0.488535 | 0.488535 | 0.261465 |  | 0.261465 | 0.125 | 0.875 | 0.375 | 0.875 | 1.0 | 6.428571 | 1.571429 | 1.666667 | 2 |  |
| turtle_soup | target_rr_below_2 | 45 | 45 | 45 |  | 3.592859 | 2.098568 | 0.755556 | 0.826124 | 70.0 | 0.35765 | 0.404244 | 0.268196 | 0.268196 | 0.136048 |  | 0.136048 | 0.755556 | 0.488889 | 0.111111 | 0.222222 | 1.0 | 4.8 | 3.136364 | 1.6 | 1 | 45 |
| turtle_soup | target_rr_below_3 | 5 | 5 | 5 |  | 2.642722 | 1.650412 | 0.2 | 2.724518 | 80.0 | 0.779704 | 0.6 | 0.48542 | 0.48542 | 0.11458 |  | 0.11458 | 0.2 | 0.8 | 0.2 | 0.4 | 1.0 | 5.0 | 7.25 | 1.0 |  | 5 |
