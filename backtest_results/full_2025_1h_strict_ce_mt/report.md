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
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.636364 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.636364 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | body_edge | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | body_level | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.636364 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | mean_threshold | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | wick_extreme | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.636364 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | conservative | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | conservative | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 119 | 119 | 106 | 1 | 7.097198 | 2.891235 | 0.294118 | 6.516928 | 96.327731 | 0.267003 | 0.294118 | 0.428571 | 0.319328 | 0.571429 | 1.271186 | 2.279412 | 1.686275 | 2.552632 |  | 67 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 8 | 8 | 5 |  | 29.162314 | 13.739913 | 0.25 | 14.788138 | 100.0 | 0.395611 | 0.25 | 0.25 | 0.25 | 0.375 | 1.875 | 1.333333 | 1.0 | 1.0 |  | 3 |
| ifvg_retest | premium | 14 | 14 | 9 |  | 6.400887 | 5.909981 | 0.071429 | 8.370642 | 100.0 | -0.879631 | 0.071429 | 0.142857 | 0.142857 | 0.571429 | 2.307692 | 1.75 | 1.0 | 1.0 |  | 6 |
| reclaimed_ob | discount | 6 | 6 | 2 | 1 | 2.662539 | 2.662539 |  | 41.154289 | 92.666667 | -1.0 |  | 0.166667 | 0.166667 | 0.333333 | 2.166667 | 2.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 4 | 4 | 3 |  | 41.420396 | 6.556014 | 0.75 | 3.502207 | 96.25 | 3.60625 | 0.75 | 0.5 | 0.5 |  | 1.25 |  | 1.0 | 1.0 |  | 2 |
| rejection_block | discount | 24 | 24 | 24 |  | 3.714944 | 2.41612 | 0.291667 | 3.249717 | 95.083333 | 0.349671 | 0.291667 | 0.625 | 0.458333 | 0.583333 | 1.0 | 3.357143 | 1.666667 | 3.181818 |  | 13 |
| rejection_block | premium | 63 | 63 | 63 |  | 5.240294 | 2.813013 | 0.349206 | 3.191946 | 95.873016 | 0.270319 | 0.349206 | 0.460317 | 0.31746 | 0.650794 | 1.0 | 2.097561 | 1.862069 | 2.75 |  | 41 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 8 | 8 | 6 |  | 9.542657 | 9.824947 | 0.25 | 3.219659 | 100.0 | -0.275549 | 0.25 | 0.125 | 0.125 | 0.5 | 2.25 | 1.0 | 1.0 | 1.0 |  | 6 |
| ifvg_retest | valid | 14 | 14 | 8 |  | 18.270451 | 7.089148 | 0.071429 | 14.981202 | 100.0 | -0.535666 | 0.071429 | 0.214286 | 0.214286 | 0.5 | 2.076923 | 2.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | none | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 22 | 22 | 14 |  | 14.529968 | 7.089148 | 0.136364 | 10.704277 | 100.0 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 | 2.142857 | 1.636364 | 1.0 | 1.0 |  | 9 |
| reclaimed_ob | high | 10 | 10 | 5 | 1 | 25.917253 | 3.70286 | 0.3 | 26.093456 | 94.1 | 1.76375 | 0.3 | 0.3 | 0.3 | 0.2 | 1.8 | 2.0 | 1.0 | 1.0 |  | 4 |
| rejection_block | high | 87 | 87 | 87 |  | 4.819507 | 2.534978 | 0.333333 | 3.207883 | 95.655172 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 | 1.0 | 2.418182 | 1.795455 | 2.903226 |  | 54 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 13 | 13 | 6 |  | 20.563278 | 4.723579 |  | 17.027452 | 100.0 | -1.0 |  | 0.076923 | 0.076923 | 0.461538 | 2.416667 | 1.833333 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 6 | 6 | 5 |  | 9.229179 | 7.118517 | 0.166667 | 1.031668 | 100.0 | -0.783336 | 0.166667 |  |  | 0.666667 | 2.166667 | 1.0 |  |  |  | 6 |
| ifvg_retest | target_rr_below_3 | 3 | 3 | 3 |  | 11.297997 | 13.0943 | 0.666667 | 2.649069 | 100.0 | 1.326019 | 0.666667 | 1.0 | 1.0 | 0.333333 | 1.0 | 3.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | none | 6 | 6 | 3 |  | 40.68214 | 3.70286 | 0.166667 | 42.856281 | 99.0 | 2.483314 | 0.166667 | 0.333333 | 0.333333 | 0.333333 | 1.666667 | 2.0 | 1.0 | 1.0 |  |  |
| reclaimed_ob | target_rr_below_2 | 4 | 4 | 2 | 1 | 3.769923 | 3.769923 | 0.5 | 0.949219 | 86.75 | 0.684404 | 0.5 | 0.25 | 0.25 |  | 2.0 |  | 1.0 | 1.0 |  | 4 |
| rejection_block | none | 33 | 33 | 33 |  | 7.539028 | 2.813013 | 0.212121 | 5.65828 | 99.727273 | 0.721298 | 0.212121 | 0.545455 | 0.515152 | 0.69697 | 1.0 | 2.913043 | 1.666667 | 2.882353 |  |  |
| rejection_block | target_rr_below_2 | 28 | 28 | 28 |  | 3.272271 | 2.29942 | 0.5 | 1.147391 | 89.785714 | 0.020418 | 0.5 | 0.464286 | 0.214286 | 0.5 | 1.0 | 1.071429 | 2.153846 | 2.333333 |  | 28 |
| rejection_block | target_rr_below_3 | 26 | 26 | 26 |  | 3.034063 | 2.891235 | 0.307692 | 2.316754 | 96.807692 | 0.040295 | 0.307692 | 0.5 | 0.307692 | 0.692308 | 1.0 | 2.833333 | 1.615385 | 3.375 |  | 26 |
