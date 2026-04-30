# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: breaker_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 3 | 3 | 2 | 1 | 10.423655 | 10.423655 | 0.333333 | 9.636327 | 96.333333 | -0.468903 | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 2.5 | 1.0 | 1.0 | 1.0 |  | 2 |
| breaker_block | premium | 1 | 1 | 1 |  | 8.145282 | 8.145282 |  | 12.089592 | 100.0 | 8.145282 |  | 1.0 | 1.0 |  | 5.0 |  | 1.0 | 1.0 |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | strong | 3 | 3 | 2 | 1 | 6.407295 | 6.407295 | 0.333333 | 13.2478 | 99.0 | 4.103737 | 0.333333 | 0.666667 | 0.666667 |  | 4.5 |  | 1.0 | 1.0 |  | 1 |
| breaker_block | valid | 1 | 1 | 1 |  | 16.178002 | 16.178002 |  | 1.255172 | 92.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 4 | 4 | 3 | 1 | 9.664197 | 8.145282 | 0.25 | 10.249643 | 97.25 | 2.402492 | 0.25 | 0.5 | 0.5 | 0.25 | 3.333333 | 1.0 | 1.0 | 1.0 |  | 2 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 2 | 2 | 1 | 1 | 8.145282 | 8.145282 |  | 19.840604 | 100.0 | 8.145282 |  | 0.5 | 0.5 |  | 5.0 |  | 1.0 | 1.0 |  |  |
| breaker_block | target_rr_below_2 | 2 | 2 | 2 |  | 10.423655 | 10.423655 | 0.5 | 0.658682 | 94.5 | -0.468903 | 0.5 | 0.5 | 0.5 | 0.5 | 2.5 | 1.0 | 1.0 | 1.0 |  | 2 |
