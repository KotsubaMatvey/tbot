# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ifvg_retest
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | BTCUSDT | 5 | 5 |  |  |  |  |  | 2.544696 | 65.0 |  |  |  |  |  |  |  |  |  |  |  | 14.0 |  |  |  |  | 4 |
| ifvg_retest | ETHUSDT | 10 | 10 | 5 |  | 14.955335 | 8.115986 | 0.1 | 7.16964 | 74.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.563295 |  | 0.563295 | 0.1 | 0.1 | 0.1 | 0.4 | 2.8 | 1.0 | 1.0 | 1.0 | 4 | 1 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 15 | 15 | 5 |  | 14.955335 | 8.115986 | 0.066667 | 5.627992 | 71.0 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.37553 |  | 0.37553 | 0.066667 | 0.066667 | 0.066667 | 0.266667 | 6.533333 | 1.0 | 1.0 | 1.0 | 4 | 5 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 8 | 8 | 3 |  | 19.548946 | 20.608633 | 0.125 | 4.863237 | 71.75 | 0.681964 | 0.174316 | -0.782454 | -0.782454 | 0.358789 |  | 0.358789 | 0.125 | 0.125 | 0.125 | 0.25 | 9.0 | 1.0 | 1.0 | 1.0 | 2 | 3 |
| ifvg_retest | valid | 7 | 7 | 2 |  | 8.06492 | 8.06492 |  | 6.501998 | 70.142857 | -1.0 | -1.0 | -2.381323 | -2.381323 | 0.394664 |  | 0.394664 |  |  |  | 0.285714 | 3.714286 | 1.0 |  |  | 2 | 2 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 10 | 10 | 5 |  | 14.955335 | 8.115986 | 0.1 | 7.459737 | 75.5 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.563295 |  | 0.563295 | 0.1 | 0.1 | 0.1 | 0.4 | 2.8 | 1.0 | 1.0 | 1.0 | 4 |  |
| ifvg_retest | medium | 5 | 5 |  |  |  |  |  | 1.964502 | 62.0 |  |  |  |  |  |  |  |  |  |  |  | 14.0 |  |  |  |  | 5 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 10 | 10 | 5 |  | 14.955335 | 8.115986 | 0.1 | 7.459737 | 75.5 | 0.009179 | -0.295411 | -1.422002 | -1.422002 | 0.563295 |  | 0.563295 | 0.1 | 0.1 | 0.1 | 0.4 | 2.8 | 1.0 | 1.0 | 1.0 | 4 |  |
| ifvg_retest | target_rr_below_2 | 2 | 2 |  |  |  |  |  | 1.04742 | 58.0 |  |  |  |  |  |  |  |  |  |  |  | 16.0 |  |  |  |  | 2 |
| ifvg_retest | target_rr_below_3 | 3 | 3 |  |  |  |  |  | 2.57589 | 64.666667 |  |  |  |  |  |  |  |  |  |  |  | 12.666667 |  |  |  |  | 3 |
