# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: reclaimed_ob
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | body_edge | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | block_extreme | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | conservative | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | discount | 7 | 7 | 1 | 1 | 1.324589 | 1.324589 |  | 6.82487 | 96.428571 | -1.0 | 0.5 | 0.5 |  | 0.142857 |  | 0.142857 | 2.142857 | 2.0 | 1.0 |  |  | 3 |
| reclaimed_ob | premium | 3 | 3 |  |  |  |  |  | 82.15589 | 100.0 |  |  |  |  |  |  |  | 2.666667 |  |  |  |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | high | 10 | 10 | 1 | 1 | 1.324589 | 1.324589 |  | 29.424176 | 97.5 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 | 2.3 | 2.0 | 1.0 |  |  | 3 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 7 | 7 |  | 1 |  |  |  | 41.434049 | 100.0 |  |  |  |  |  |  |  | 2.571429 |  |  |  |  |  |
| reclaimed_ob | target_rr_below_2 | 1 | 1 |  |  |  |  |  | 0.203417 | 85.0 |  |  |  |  |  |  |  | 2.0 |  |  |  |  | 1 |
| reclaimed_ob | target_rr_below_3 | 2 | 2 | 1 |  | 1.324589 | 1.324589 |  | 2.0 | 95.0 | -1.0 | 0.5 | 0.5 |  | 0.5 |  | 0.5 | 1.5 | 2.0 | 1.0 |  |  | 2 |
