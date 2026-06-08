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
| turtle_soup | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 50 | 50 | 50 |  | 3.804911 | 2.566325 | 0.68 | 1.703286 | 73.8 | 0.275379 | 0.561255 | 0.384328 | 0.384328 | 0.176928 |  | 0.176928 | 0.68 | 0.64 | 0.2 | 0.32 | 1.0 | 4.0 | 1.96875 | 1.7 | 5 | 42 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 8 | 8 | 8 |  | 4.302056 | 3.995654 | 0.125 | 5.635234 | 90.0 | -0.490491 | 0.75 | 0.377722 | 0.377722 | 0.372278 |  | 0.372278 | 0.125 | 0.875 | 0.5 | 0.875 | 1.0 | 4.142857 | 1.571429 | 1.75 | 4 |  |
| turtle_soup | target_rr_below_2 | 39 | 39 | 39 |  | 3.736854 | 2.314313 | 0.820513 | 0.81434 | 70.0 | 0.433748 | 0.540071 | 0.402154 | 0.402154 | 0.137917 |  | 0.137917 | 0.820513 | 0.589744 | 0.128205 | 0.179487 | 1.0 | 3.571429 | 2.173913 | 1.8 | 1 | 39 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 3.363928 | 4.364205 | 0.333333 | 2.774381 | 80.0 | 0.258898 | 0.333333 | 0.170205 | 0.170205 | 0.163128 |  | 0.163128 | 0.333333 | 0.666667 | 0.333333 | 0.666667 | 1.0 | 5.0 | 1.0 | 1.0 |  | 3 |
