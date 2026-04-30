# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: breaker_block
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | unknown | 36 | 36 | 15 |  | 11.7464 | 9.835254 | 0.25 | 4.206959 | 65.777778 | 0.285815 | 0.420947 | 0.420947 | 0.25 | 0.277778 | 0.25 | 0.166667 | 3.083333 | 1.333333 | 1.0 | 1.0 |  | 23 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | strong | 16 | 16 | 7 |  | 12.397213 | 11.202193 | 0.25 | 1.920895 | 68.625 | 0.35916 | 0.251009 | 0.251009 | 0.25 | 0.25 | 0.1875 | 0.1875 | 2.6875 | 1.0 | 1.0 | 1.0 |  | 12 |
| breaker_block | valid | 20 | 20 | 8 |  | 11.176938 | 9.665989 | 0.25 | 6.03581 | 63.5 | 0.221638 | 0.569642 | 0.569642 | 0.25 | 0.3 | 0.3 | 0.15 | 3.4 | 1.666667 | 1.0 | 1.0 |  | 11 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 17 | 17 | 6 |  | 13.150758 | 10.121701 | 0.117647 | 7.622329 | 75.647059 | -0.28389 | 0.191388 | 0.191388 | 0.117647 | 0.235294 | 0.176471 | 0.235294 | 3.235294 | 1.5 | 1.0 | 1.0 |  | 4 |
| breaker_block | medium | 19 | 19 | 9 |  | 10.810161 | 9.835254 | 0.368421 | 1.151101 | 56.947368 | 0.665618 | 0.573985 | 0.573985 | 0.368421 | 0.315789 | 0.315789 | 0.105263 | 2.947368 | 1.0 | 1.0 | 1.0 |  | 19 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 13 | 13 | 4 |  | 15.709352 | 14.930896 |  | 9.504682 | 74.538462 | -1.0 | -0.25 | -0.25 |  | 0.153846 | 0.153846 | 0.307692 | 3.461538 | 1.5 | 1.0 | 1.0 |  |  |
| breaker_block | target_rr_below_2 | 19 | 19 | 10 |  | 9.819062 | 9.665989 | 0.421053 | 0.960519 | 58.526316 | 0.621867 | 0.577992 | 0.577992 | 0.421053 | 0.368421 | 0.315789 | 0.105263 | 2.631579 | 1.0 | 1.0 | 1.0 |  | 19 |
| breaker_block | target_rr_below_3 | 4 | 4 | 1 |  | 15.16797 | 15.16797 | 0.25 | 2.409945 | 71.75 | 2.068555 | 1.534278 | 1.534278 | 0.25 | 0.25 | 0.25 |  | 4.0 |  | 1.0 | 1.0 |  | 4 |
