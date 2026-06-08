# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_hyperliquid_recent_2026-02-10_2026-05-25
- models: silver_bullet
- symbols: SP500
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- commission_bps: 9.0
- slippage_bps: 2.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_hyperliquid_recent_2026-02-10_2026-05-25
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | edge | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | swing_or_fvg | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | conservative | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | unknown | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | high | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 84 | 84 | 81 |  | 2.461341 | 1.36197 | 0.142857 | 2.0 | 78.0 | -0.306574 | -0.070278 | -1.586453 | -1.586453 | 1.458047 | 0.003978 | 1.462026 | 0.142857 | 0.428571 | 0.142857 | 0.702381 | 1.333333 | 8.779661 | 7.944444 | 15.0 | 3 |  |
