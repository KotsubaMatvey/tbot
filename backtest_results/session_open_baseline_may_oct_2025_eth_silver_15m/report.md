# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: silver_bullet
- symbols: ETHUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | edge | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | swing_or_fvg | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | conservative | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 359 | 359 | 343 |  | 3.626558 | 2.031776 | 0.256267 | 2.0 | 77.888579 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 1.142061 | 6.219298 | 5.485714 | 7.858696 | 22 | 2 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | high | 357 | 357 | 341 |  | 3.646439 | 2.03712 | 0.257703 | 2.0 | 78.0 | -0.050031 | 0.103991 | 0.103991 | 0.257703 | 0.490196 | 0.257703 | 0.633053 | 1.142857 | 6.225664 | 5.485714 | 7.858696 | 22 |  |
| silver_bullet | medium | 2 | 2 | 2 |  | 0.236844 | 0.236844 |  | 2.0 | 58.0 | -1.0 | -1.0 | -1.0 |  |  |  | 1.0 | 1.0 | 5.5 |  |  |  | 2 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | none | 357 | 357 | 341 |  | 3.646439 | 2.03712 | 0.257703 | 2.0 | 78.0 | -0.050031 | 0.103991 | 0.103991 | 0.257703 | 0.490196 | 0.257703 | 0.633053 | 1.142857 | 6.225664 | 5.485714 | 7.858696 | 22 |  |
| silver_bullet | target_rr_below_2 | 2 | 2 | 2 |  | 0.236844 | 0.236844 |  | 2.0 | 58.0 | -1.0 | -1.0 | -1.0 |  |  |  | 1.0 | 1.0 | 5.5 |  |  |  | 2 |
