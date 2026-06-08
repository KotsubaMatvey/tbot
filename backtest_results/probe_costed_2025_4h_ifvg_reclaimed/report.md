# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | body_edge | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | block_extreme | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | conservative | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 4 |  | 10.387332 | 9.004895 |  | 20.799845 | 99.272727 | -1.0 | -0.35 | -0.705348 | -0.705348 | 0.129217 |  | 0.181818 | 0.181818 | 0.363636 | 2.363636 | 1.5 | 1.0 | 1.0 | 3 | 2 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | premium | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | discount | 3 | 3 | 1 |  | 19.364053 | 19.364053 |  | 24.214504 | 99.0 | -1.0 | 0.3 | -0.001597 | -0.001597 | 0.100532 |  | 0.333333 | 0.333333 | 0.333333 | 1.666667 | 2.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | premium | 6 | 6 | 2 |  | 6.316655 | 6.316655 |  | 24.056759 | 99.166667 | -1.0 | -0.35 | -0.82786 | -0.82786 | 0.159287 |  | 0.166667 | 0.166667 | 0.333333 | 1.833333 | 1.5 | 1.0 | 1.0 | 2 | 2 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 1 | 1 | 1 |  | 9.551966 | 9.551966 |  | 7.418735 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.164073 |  |  |  | 1.0 | 1.0 | 1.0 |  |  | 1 |  |
| ifvg_retest | valid | 1 | 1 |  |  |  |  |  | 4.395491 | 100.0 |  |  |  |  |  |  |  |  |  | 9.0 |  |  |  |  |  |
| reclaimed_ob | none | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | high | 9 | 9 | 3 |  | 10.665788 | 8.457824 |  | 24.109341 | 99.111111 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.139702 |  | 0.222222 | 0.222222 | 0.333333 | 1.777778 | 1.666667 | 1.0 | 1.0 | 2 | 2 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 2 | 2 | 1 |  | 9.551966 | 9.551966 |  | 5.907113 | 100.0 | -1.0 | -1.0 | -1.164073 | -1.164073 | 0.082036 |  |  |  | 0.5 | 5.0 | 1.0 |  |  | 1 |  |
| reclaimed_ob | none | 7 | 7 | 3 |  | 10.665788 | 8.457824 |  | 30.50689 | 99.571429 | -1.0 | -0.133333 | -0.552439 | -0.552439 | 0.179617 |  | 0.285714 | 0.285714 | 0.428571 | 1.571429 | 1.666667 | 1.0 | 1.0 | 2 |  |
| reclaimed_ob | target_rr_below_2 | 1 | 1 |  |  |  |  |  | 0.501985 | 100.0 |  |  |  |  |  |  |  |  |  | 2.0 |  |  |  |  | 1 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.93385 | 95.0 |  |  |  |  |  |  |  |  |  | 3.0 |  |  |  |  | 1 |
