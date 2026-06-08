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
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 23 | 23 | 23 |  | 2.08216 | 1.316428 | 0.086957 | 2.0 | 80.0 | -0.272983 | 0.025472 | -0.185833 | -0.185833 | 0.211305 | 0.086957 | 0.521739 | 0.086957 | 0.695652 | 1.0 | 8.0625 | 6.166667 | 8.0 | 2 | 23 |
