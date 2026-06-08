# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
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
| turtle_soup | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 18 | 18 | 18 |  | 3.088897 | 2.684161 | 0.833333 | 1.306275 | 72.777778 | 0.75125 | 0.66224 | 0.501896 | 0.501896 | 0.160344 |  | 0.160344 | 0.833333 | 0.722222 | 0.333333 | 0.166667 | 1.0 | 4.333333 | 1.384615 | 1.833333 | 1 | 16 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 3.324387 | 3.324387 | 0.5 | 4.01074 | 90.0 | 1.038037 |  | -0.324147 | -0.324147 | 0.324147 |  | 0.324147 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 2.0 | 2.0 | 3.0 |  |  |
| turtle_soup | target_rr_below_2 | 15 | 15 | 15 |  | 2.972478 | 2.469999 | 0.866667 | 0.847652 | 70.0 | 0.577983 | 0.728021 | 0.593345 | 0.593345 | 0.134675 |  | 0.134675 | 0.866667 | 0.733333 | 0.266667 | 0.133333 | 1.0 | 5.5 | 1.363636 | 1.75 | 1 | 15 |
| turtle_soup | target_rr_below_3 | 1 | 1 | 1 |  | 4.364205 | 4.364205 | 1.0 | 2.776694 | 80.0 | 2.776694 | 1.0 | 0.782236 | 0.782236 | 0.217764 |  | 0.217764 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
