# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.454545 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.454545 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | body_edge | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | body_level | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.454545 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | mean_threshold | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | wick_extreme | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.454545 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | conservative | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | conservative | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 119 | 119 | 106 | 1 | 7.097198 | 2.891235 | 0.277311 | 6.516928 | 96.327731 | 0.116458 | 0.156159 | 0.156159 | 0.277311 | 0.428571 | 0.310924 | 0.596639 | 1.271186 | 1.943662 | 1.686275 | 2.297297 |  | 67 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 8 | 8 | 5 |  | 29.162314 | 13.739913 | 0.25 | 14.788138 | 100.0 | 0.395611 | 0.216928 | 0.216928 | 0.25 | 0.25 | 0.25 | 0.375 | 1.875 | 1.333333 | 1.0 | 1.0 |  | 3 |
| ifvg_retest | premium | 14 | 14 | 9 |  | 6.400887 | 5.909981 | 0.071429 | 8.370642 | 100.0 | -0.879631 | -0.590742 | -0.590742 | 0.071429 | 0.142857 | 0.142857 | 0.571429 | 2.307692 | 1.5 | 1.0 | 1.0 |  | 6 |
| reclaimed_ob | discount | 6 | 6 | 2 | 1 | 2.662539 | 2.662539 |  | 41.154289 | 92.666667 | -1.0 | -0.35 | -0.35 |  | 0.166667 | 0.166667 | 0.333333 | 2.166667 | 2.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 4 | 4 | 3 |  | 41.420396 | 6.556014 | 0.5 | 3.502207 | 96.25 | 0.122936 | 0.536342 | 0.536342 | 0.5 | 0.5 | 0.5 | 0.25 | 1.25 | 2.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | discount | 24 | 24 | 24 |  | 3.714944 | 2.41612 | 0.291667 | 3.249717 | 95.083333 | 0.221702 | 0.183893 | 0.183893 | 0.291667 | 0.625 | 0.416667 | 0.625 | 1.0 | 2.066667 | 1.666667 | 2.3 |  | 13 |
| rejection_block | premium | 63 | 63 | 63 |  | 5.240294 | 2.813013 | 0.333333 | 3.191946 | 95.873016 | 0.231644 | 0.245436 | 0.245436 | 0.333333 | 0.460317 | 0.31746 | 0.666667 | 1.0 | 2.02381 | 1.862069 | 2.75 |  | 41 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 8 | 8 | 6 |  | 9.542657 | 9.824947 | 0.25 | 3.219659 | 100.0 | -0.275549 | -0.338719 | -0.338719 | 0.25 | 0.125 | 0.125 | 0.5 | 2.25 | 1.0 | 1.0 | 1.0 |  | 6 |
| ifvg_retest | valid | 14 | 14 | 8 |  | 18.270451 | 7.089148 | 0.071429 | 14.981202 | 100.0 | -0.535666 | -0.274966 | -0.274966 | 0.071429 | 0.214286 | 0.214286 | 0.5 | 2.076923 | 1.714286 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | none | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.454545 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | high | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.2 | 26.093456 | 94.1 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | high | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.321839 | 3.207883 | 95.655172 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 | 1.0 | 2.035088 | 1.795455 | 2.6 |  | 54 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 13 | 13 | 6 |  | 20.563278 | 4.723579 |  | 17.027452 | 100.0 | -1.0 | -0.783333 | -0.783333 |  | 0.076923 | 0.076923 | 0.461538 | 2.416667 | 1.666667 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 6 | 6 | 5 |  | 9.229179 | 7.118517 | 0.166667 | 1.031668 | 100.0 | -0.783336 | -0.783336 | -0.783336 | 0.166667 |  |  | 0.666667 | 2.166667 | 1.0 |  |  |  | 6 |
| ifvg_retest | target_rr_below_3 | 3 | 3 | 3 |  | 11.297997 | 13.0943 | 0.666667 | 2.649069 | 100.0 | 1.326019 | 1.461546 | 1.461546 | 0.666667 | 1.0 | 1.0 | 0.333333 | 1.0 | 2.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 6 | 6 | 3 |  | 40.68214 | 3.70286 |  | 42.856281 | 99.0 | -1.0 | -0.133333 | -0.133333 |  | 0.333333 | 0.333333 | 0.5 | 1.666667 | 2.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 4 | 4 | 2 | 1 | 3.769923 | 3.769923 | 0.5 | 0.949219 | 86.75 | 0.684404 | 0.654513 | 0.654513 | 0.5 | 0.25 | 0.25 |  | 2.0 |  | 1.0 | 1.0 |  | 4 |
| rejection_block | none | 33 | 33 | 33 |  | 7.539028 | 2.813013 | 0.212121 | 5.65828 | 99.727273 | 0.628229 | 0.496998 | 0.496998 | 0.212121 | 0.545455 | 0.484848 | 0.727273 | 1.0 | 2.291667 | 1.666667 | 2.3125 |  |  |
| rejection_block | target_rr_below_2 | 28 | 28 | 28 |  | 3.272271 | 2.29942 | 0.464286 | 1.147391 | 89.785714 | -0.0666 | -0.027087 | -0.027087 | 0.464286 | 0.464286 | 0.214286 | 0.535714 | 1.0 | 1.266667 | 2.153846 | 2.333333 |  | 28 |
| rejection_block | target_rr_below_3 | 26 | 26 | 26 |  | 3.034063 | 2.891235 | 0.307692 | 2.316754 | 96.807692 | 0.040295 | 0.162822 | 0.162822 | 0.307692 | 0.5 | 0.307692 | 0.692308 | 1.0 | 2.333333 | 1.615385 | 3.375 |  | 26 |
