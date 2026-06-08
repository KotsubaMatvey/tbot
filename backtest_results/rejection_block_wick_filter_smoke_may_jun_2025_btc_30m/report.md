# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: rejection_block
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | body_level | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | wick_extreme | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | conservative | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | discount | 23 | 23 | 3 |  | 4.161055 | 3.9935 | 0.086957 | 4.411052 | 94.478261 | 0.196877 | 0.691825 | 0.691825 | 0.086957 | 0.086957 | 0.043478 | 0.043478 | 5.615385 | 7.0 | 2.0 | 4.0 | 1 | 12 |
| rejection_block | premium | 5 | 5 | 2 |  | 2.812491 | 2.812491 |  | 20.641847 | 100.0 | -1.0 | -0.25 | -0.25 |  | 0.2 | 0.2 | 0.4 | 2.25 | 6.5 | 5.0 | 10.0 | 1 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | high | 28 | 28 | 5 |  | 3.621629 | 3.293847 | 0.071429 | 7.309409 | 95.464286 | -0.281874 | 0.315095 | 0.315095 | 0.071429 | 0.107143 | 0.071429 | 0.107143 | 4.823529 | 6.666667 | 3.0 | 7.0 | 2 | 12 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 16 | 16 | 3 |  | 4.039832 | 3.293847 |  | 11.704096 | 100.0 | -1.0 |  |  |  | 0.125 | 0.125 | 0.1875 | 3.888889 | 6.666667 | 3.5 | 7.0 | 2 |  |
| rejection_block | target_rr_below_2 | 10 | 10 | 2 |  | 2.994325 | 2.994325 | 0.2 | 1.182388 | 88.5 | 0.795316 | 0.787737 | 0.787737 | 0.2 | 0.1 |  |  | 6.142857 |  | 2.0 |  |  | 10 |
| rejection_block | target_rr_below_3 | 2 | 2 |  |  |  |  |  | 2.787014 | 94.0 |  |  |  |  |  |  |  | 4.0 |  |  |  |  | 2 |
