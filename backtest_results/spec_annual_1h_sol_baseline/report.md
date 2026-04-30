# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | body_edge | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | body_level | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | mean_threshold | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | wick_extreme | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | conservative | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | conservative | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 26 | 26 | 5 | 1 | 2.295812 | 0.877707 | 0.038462 | 20.717259 | 98.076923 | -0.151088 | 0.029046 | 0.029046 | 0.038462 | 0.076923 | 0.076923 | 0.115385 | 3.958333 | 3.666667 | 1.0 | 1.0 |  | 3 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | discount | 2 | 2 | 1 | 1 | 3.70286 | 3.70286 |  | 10.003426 | 92.5 | -1.0 | 0.5 | 0.5 |  | 0.5 | 0.5 | 0.5 | 2.0 | 3.0 | 1.0 | 1.0 |  | 1 |
| reclaimed_ob | premium | 1 | 1 | 1 |  | 6.556014 | 6.556014 | 1.0 | 2.198663 | 95.0 | 2.198663 | 1.599332 | 1.599332 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | discount | 13 | 13 | 2 |  | 0.461802 | 0.461802 |  | 22.180997 | 97.923077 | -0.477051 | -0.477051 | -0.477051 |  |  |  | 0.076923 | 4.272727 | 5.0 |  |  |  | 1 |
| rejection_block | premium | 10 | 10 | 1 |  | 0.296583 | 0.296583 |  | 22.809025 | 99.7 | -1.0 | -1.0 | -1.0 |  |  |  | 0.1 | 4.3 | 3.0 |  |  |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | none | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | high | 3 | 3 | 2 | 1 | 5.129437 | 5.129437 | 0.333333 | 7.401838 | 93.333333 | 0.599332 | 1.049666 | 1.049666 | 0.333333 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 3.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | high | 23 | 23 | 3 |  | 0.406729 | 0.296583 |  | 22.454053 | 98.695652 | -0.651368 | -0.651368 | -0.651368 |  |  |  | 0.086957 | 4.285714 | 4.0 |  |  |  | 1 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reclaimed_ob | none | 1 | 1 | 1 |  | 3.70286 | 3.70286 |  | 18.506803 | 100.0 | -1.0 | 0.5 | 0.5 |  | 1.0 | 1.0 | 1.0 | 1.0 | 3.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 1 | 1 |  | 1 |  |  |  | 1.500049 | 85.0 |  |  |  |  |  |  |  | 3.0 |  |  |  |  | 1 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 6.556014 | 6.556014 | 1.0 | 2.198663 | 95.0 | 2.198663 | 1.599332 | 1.599332 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| rejection_block | none | 22 | 22 | 2 |  | 0.587145 | 0.587145 |  | 23.453917 | 99.318182 | -1.0 | -1.0 | -1.0 |  |  |  | 0.090909 | 4.4 | 4.0 |  |  |  |  |
| rejection_block | target_rr_below_2 | 1 | 1 | 1 |  | 0.045897 | 0.045897 |  | 0.457053 | 85.0 | 0.045897 | 0.045897 | 0.045897 |  |  |  |  | 2.0 |  |  |  |  | 1 |
