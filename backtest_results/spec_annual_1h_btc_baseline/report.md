# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | body_edge | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | body_level | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | mean_threshold | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | wick_extreme | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | conservative | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | conservative | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 65 | 65 | 19 |  | 2.857996 | 2.460562 | 0.030769 | 47.552909 | 98.692308 | -0.621317 | -0.091803 | -0.091803 | 0.030769 | 0.153846 | 0.061538 | 0.246154 | 3.839286 | 4.125 | 2.2 | 5.25 |  | 4 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | premium | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | discount | 1 | 1 |  |  |  |  |  | 18.443997 | 100.0 |  |  |  |  |  |  |  | 2.0 |  |  |  |  |  |
| reclaimed_ob | premium | 2 | 2 | 1 |  | 0.983833 | 0.983833 | 0.5 | 4.306619 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.5 |  |  |  | 1.5 |  |  |  |  | 1 |
| rejection_block | discount | 16 | 16 | 7 |  | 1.756086 | 1.855134 | 0.0625 | 25.949956 | 94.6875 | -0.149919 | 0.001616 | 0.001616 | 0.0625 | 0.25 | 0.1875 | 0.3125 | 3.142857 | 6.2 | 2.25 | 5.333333 |  | 3 |
| rejection_block | premium | 45 | 45 | 11 |  | 3.72959 | 2.99517 |  | 52.30121 | 100.0 | -1.0 | -0.181818 | -0.181818 |  | 0.133333 | 0.022222 | 0.244444 | 3.973684 | 3.181818 | 2.166667 | 5.0 |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | none | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | none | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | high | 3 | 3 | 1 |  | 0.983833 | 0.983833 | 0.333333 | 9.019078 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 0.333333 |  |  |  | 1.666667 |  |  |  |  | 1 |
| rejection_block | high | 61 | 61 | 18 |  | 2.962116 | 2.674853 | 0.016393 | 45.389405 | 98.606557 | -0.669413 | -0.110483 | -0.110483 | 0.016393 | 0.163934 | 0.065574 | 0.262295 | 3.75 | 4.125 | 2.2 | 5.25 |  | 3 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 1 | 1 |  |  |  |  |  | 295.128135 | 100.0 |  |  |  |  |  |  |  | 15.0 |  |  |  |  |  |
| reclaimed_ob | none | 2 | 2 |  |  |  |  |  | 13.406408 | 100.0 |  |  |  |  |  |  |  | 2.0 |  |  |  |  |  |
| reclaimed_ob | target_rr_below_2 | 1 | 1 | 1 |  | 0.983833 | 0.983833 | 1.0 | 0.24442 | 100.0 | 0.24442 | 0.24442 | 0.24442 | 1.0 |  |  |  | 1.0 |  |  |  |  | 1 |
| rejection_block | none | 58 | 58 | 17 |  | 3.128475 | 2.889144 |  | 47.729489 | 99.586207 | -0.709456 | -0.117647 | -0.117647 |  | 0.172414 | 0.068966 | 0.275862 | 3.82 | 4.125 | 2.2 | 5.25 |  |  |
| rejection_block | target_rr_below_2 | 3 | 3 | 1 |  | 0.134025 | 0.134025 | 0.333333 | 0.147785 | 79.666667 | 0.011314 | 0.011314 | 0.011314 | 0.333333 |  |  |  | 2.0 |  |  |  |  | 3 |
