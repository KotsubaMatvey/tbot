# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: reclaimed_ob
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | body_edge | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | block_extreme | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | conservative | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | discount | 5 | 5 | 4 |  | 2.166609 | 1.76075 |  | 28.356535 | 96.6 | -1.0 | 0.125 | 0.125 |  | 0.6 | 0.2 | 0.8 | 1.2 | 4.25 | 1.0 | 2.0 | 2 | 1 |
| reclaimed_ob | premium | 4 | 4 | 3 | 1 | 25.937373 | 5.902339 |  | 105.001763 | 99.25 | -1.0 | 0.5 | 0.5 |  | 0.75 | 0.75 | 0.75 | 1.25 | 3.666667 | 1.0 | 1.0 | 3 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | high | 9 | 9 | 7 | 1 | 12.354079 | 3.725986 |  | 62.421081 | 97.777778 | -1.0 | 0.285714 | 0.285714 |  | 0.666667 | 0.444444 | 0.777778 | 1.222222 | 4.0 | 1.0 | 1.25 | 5 | 1 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 8 | 8 | 6 | 1 | 14.094478 | 4.011513 |  | 69.929127 | 98.125 | -1.0 | 0.25 | 0.25 |  | 0.625 | 0.5 | 0.75 | 1.25 | 4.166667 | 1.0 | 1.25 | 4 |  |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 1.911688 | 1.911688 |  | 2.356716 | 95.0 | -1.0 | 0.5 | 0.5 |  | 1.0 |  | 1.0 | 1.0 | 3.0 | 1.0 |  | 1 | 1 |
