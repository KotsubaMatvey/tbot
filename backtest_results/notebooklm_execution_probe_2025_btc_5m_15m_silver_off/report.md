# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: silver_bullet
- symbols: BTCUSDT
- timeframes: 5m, 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | edge | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | swing_or_fvg | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | conservative | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | high | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 520 | 520 | 483 |  | 1.869028 | 1.158791 | 0.188462 | 2.0 | 78.0 | -0.078029 | 0.034367 | 0.034367 | 0.188462 | 0.398077 | 0.188462 | 0.588462 | 1.273077 | 6.372549 | 5.429952 | 7.163265 | 14 |  |
