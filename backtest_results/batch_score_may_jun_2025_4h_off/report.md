# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 4h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | 36 | 36 | 34 |  | 33.322074 | 12.948559 | 0.277778 | 7.265434 | 70.777778 | 0.838629 | 0.277778 | 0.305556 | 0.25 | 0.666667 | 4.058824 | 1.125 | 1.090909 | 1.111111 |  | 19 |
| mitigation_block | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | edge | 36 | 36 | 34 |  | 33.322074 | 12.948559 | 0.277778 | 7.265434 | 70.777778 | 0.838629 | 0.277778 | 0.305556 | 0.25 | 0.666667 | 4.058824 | 1.125 | 1.090909 | 1.111111 |  | 19 |
| mitigation_block | body_zone_retest | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | body_edge | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | body_level | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | close | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | ce | 36 | 36 | 34 |  | 33.322074 | 12.948559 | 0.277778 | 7.265434 | 70.777778 | 0.838629 | 0.277778 | 0.305556 | 0.25 | 0.666667 | 4.058824 | 1.125 | 1.090909 | 1.111111 |  | 19 |
| mitigation_block | block_extreme | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | mean_threshold | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | wick_extreme | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | sweep_extreme | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | conservative | 36 | 36 | 34 |  | 33.322074 | 12.948559 | 0.277778 | 7.265434 | 70.777778 | 0.838629 | 0.277778 | 0.305556 | 0.25 | 0.666667 | 4.058824 | 1.125 | 1.090909 | 1.111111 |  | 19 |
| mitigation_block | conservative | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | conservative | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | conservative | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | conservative | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 839 | 839 | 829 | 7 | 5.66127 | 2.605268 | 0.328963 | 4.771476 | 46.607867 | 0.213388 | 0.328963 | 0.423123 | 0.261025 | 0.589988 | 1.260192 | 3.10101 | 2.08169 | 2.949772 |  | 482 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | unknown | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | unknown | 36 | 36 | 34 |  | 33.322074 | 12.948559 | 0.277778 | 7.265434 | 70.777778 | 0.838629 | 0.277778 | 0.305556 | 0.25 | 0.666667 | 4.058824 | 1.125 | 1.090909 | 1.111111 |  | 19 |
| mitigation_block | unknown | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | unknown | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | unknown | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | none | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 36 | 36 | 28 | 7 | 14.464833 | 11.290358 | 0.611111 | 1.918009 | 45.222222 | 1.118073 | 0.611111 | 0.583333 | 0.555556 | 0.166667 | 4.424242 | 1.0 | 1.0 | 1.0 |  | 36 |
| ifvg_retest | strong | 20 | 20 | 18 |  | 40.685016 | 12.948559 | 0.2 | 7.820338 | 74.0 | -0.350312 | 0.2 | 0.25 | 0.25 | 0.7 | 3.5 | 1.142857 | 1.0 | 1.2 |  | 11 |
| ifvg_retest | valid | 16 | 16 | 16 |  | 25.038764 | 12.025082 | 0.375 | 6.571803 | 66.75 | 2.176189 | 0.375 | 0.375 | 0.25 | 0.625 | 4.6875 | 1.1 | 1.166667 | 1.0 |  | 8 |
| mitigation_block | none | 227 | 227 | 227 |  | 2.275095 | 1.144226 | 0.427313 | 0.695993 | 43.022026 | -0.308373 | 0.427313 | 0.251101 | 0.092511 | 0.54185 | 1.0 | 1.97561 | 1.438596 | 1.571429 |  | 224 |
| reclaimed_ob | none | 3 | 3 | 3 |  | 34.007325 | 13.437902 | 0.333333 | 1.280299 | 48.0 | -0.45556 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| rejection_block | none | 141 | 141 | 141 |  | 6.600719 | 3.541359 | 0.652482 | 2.213019 | 46.794326 | 0.911736 | 0.652482 | 0.624113 | 0.35461 | 0.326241 | 1.0 | 2.826087 | 1.306818 | 2.12 |  | 114 |
| turtle_soup | none | 396 | 396 | 396 |  | 4.0557 | 2.640012 | 0.136364 | 8.07777 | 46.515152 | 0.151242 | 0.136364 | 0.44697 | 0.29798 | 0.742424 | 1.0 | 3.833333 | 2.870056 | 4.033898 |  | 86 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | low | 23 | 23 | 19 | 4 | 14.79061 | 12.120215 | 0.608696 | 1.125117 | 38.0 | 0.504136 | 0.608696 | 0.608696 | 0.565217 | 0.217391 | 3.863636 | 1.0 | 1.0 | 1.0 |  | 23 |
| breaker_block | medium | 13 | 13 | 9 | 3 | 13.777079 | 10.460501 | 0.615385 | 3.320818 | 58.0 | 2.414163 | 0.615385 | 0.538462 | 0.538462 | 0.076923 | 5.545455 | 1.0 | 1.0 | 1.0 |  | 13 |
| ifvg_retest | high | 21 | 21 | 19 |  | 51.169456 | 22.458386 | 0.190476 | 11.560623 | 79.904762 | 1.510638 | 0.190476 | 0.238095 | 0.190476 | 0.714286 | 4.052632 | 1.133333 | 1.2 | 1.0 |  | 4 |
| ifvg_retest | medium | 15 | 15 | 15 |  | 10.715391 | 7.316444 | 0.4 | 1.252168 | 58.0 | -0.012582 | 0.4 | 0.4 | 0.333333 | 0.6 | 4.066667 | 1.111111 | 1.0 | 1.2 |  | 15 |
| mitigation_block | low | 183 | 183 | 183 |  | 2.261951 | 1.186658 | 0.442623 | 0.689234 | 39.311475 | -0.285727 | 0.442623 | 0.251366 | 0.103825 | 0.535519 | 1.0 | 1.938776 | 1.521739 | 1.631579 |  | 183 |
| mitigation_block | medium | 44 | 44 | 44 |  | 2.329763 | 0.702849 | 0.363636 | 0.724105 | 58.454545 | -0.40256 | 0.363636 | 0.25 | 0.045455 | 0.568182 | 1.0 | 2.12 | 1.090909 | 1.0 |  | 41 |
| reclaimed_ob | low | 2 | 2 | 2 |  | 44.292036 | 44.292036 | 0.5 | 1.47638 | 43.0 | -0.18334 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | medium | 1 | 1 | 1 |  | 13.437902 | 13.437902 |  | 0.888137 | 58.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| rejection_block | high | 2 | 2 | 2 |  | 9.519195 | 9.519195 |  | 9.399269 | 78.0 | -1.0 |  | 1.0 | 0.5 | 1.0 | 1.0 | 3.5 | 1.0 | 1.0 |  |  |
| rejection_block | low | 88 | 88 | 88 |  | 5.601265 | 2.992732 | 0.693182 | 1.131795 | 39.477273 | 0.389671 | 0.693182 | 0.590909 | 0.295455 | 0.306818 | 1.0 | 2.62963 | 1.403846 | 2.807692 |  | 88 |
| rejection_block | medium | 51 | 51 | 51 |  | 8.210815 | 4.578839 | 0.607843 | 3.796846 | 58.196078 | 1.887523 | 0.607843 | 0.666667 | 0.45098 | 0.333333 | 1.0 | 3.058824 | 1.176471 | 1.391304 |  | 26 |
| turtle_soup | low | 86 | 86 | 86 |  | 1.996441 | 1.223856 | 0.337209 | 1.741952 | 33.953488 | 0.182738 | 0.337209 | 0.395349 | 0.174419 | 0.476744 | 1.0 | 4.97561 | 5.235294 | 8.133333 |  | 86 |
| turtle_soup | medium | 310 | 310 | 310 |  | 4.626978 | 2.983969 | 0.080645 | 9.835449 | 50.0 | 0.142505 | 0.080645 | 0.46129 | 0.332258 | 0.816129 | 1.0 | 3.648221 | 2.307692 | 3.436893 |  |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | insufficient_displacement | 7 | 7 | 3 | 3 | 23.691933 | 19.857954 | 0.428571 | 5.649489 | 58.0 | 6.498426 | 0.428571 | 0.428571 | 0.428571 |  | 7.8 |  | 1.0 | 1.0 |  | 7 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 29 | 29 | 25 | 4 | 13.35758 | 10.389677 | 0.655172 | 1.017307 | 42.137931 | 0.472431 | 0.655172 | 0.62069 | 0.586207 | 0.206897 | 3.821429 | 1.0 | 1.0 | 1.0 |  | 29 |
| ifvg_retest | none | 17 | 17 | 15 |  | 63.434044 | 37.139865 | 0.176471 | 14.067888 | 80.352941 | 2.06717 | 0.176471 | 0.235294 | 0.235294 | 0.705882 | 3.933333 | 1.166667 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 15 | 15 | 15 |  | 8.756739 | 6.549134 | 0.333333 | 0.892174 | 59.333333 | -0.354135 | 0.333333 | 0.333333 | 0.2 | 0.666667 | 5.0 | 1.1 | 1.2 | 1.0 |  | 15 |
| ifvg_retest | target_rr_below_3 | 4 | 4 | 4 |  | 12.522197 | 6.046157 | 0.5 | 2.254727 | 73.0 | 0.704468 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.0 | 1.0 | 1.5 |  | 4 |
| mitigation_block | none | 3 | 3 | 3 |  | 1.600473 | 1.359312 |  | 4.960744 | 58.0 | -1.0 |  | 0.666667 |  | 1.0 | 1.0 | 2.666667 | 1.5 |  |  |  |
| mitigation_block | target_rr_below_2 | 198 | 198 | 198 |  | 2.370059 | 1.02051 | 0.454545 | 0.43779 | 41.939394 | -0.330055 | 0.454545 | 0.217172 | 0.070707 | 0.515152 | 1.0 | 1.813725 | 1.27907 | 1.0 |  | 198 |
| mitigation_block | target_rr_below_3 | 26 | 26 | 26 |  | 1.629755 | 1.664705 | 0.269231 | 2.170226 | 49.538462 | -0.063453 | 0.269231 | 0.461538 | 0.269231 | 0.692308 | 1.0 | 2.777778 | 2.0 | 2.714286 |  | 26 |
| reclaimed_ob | target_rr_below_2 | 2 | 2 | 2 |  | 9.110061 | 9.110061 | 0.5 | 0.760728 | 48.0 | -0.18334 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 83.801852 | 83.801852 |  | 2.31944 | 48.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| rejection_block | none | 27 | 27 | 27 |  | 11.806316 | 8.347528 | 0.37037 | 7.18426 | 59.481481 | 3.239468 | 0.37037 | 0.814815 | 0.666667 | 0.518519 | 1.0 | 3.285714 | 1.0 | 1.333333 |  |  |
| rejection_block | target_rr_below_2 | 100 | 100 | 100 |  | 4.919671 | 2.843888 | 0.74 | 0.836456 | 43.0 | 0.276563 | 0.74 | 0.56 | 0.23 | 0.26 | 1.0 | 2.884615 | 1.482143 | 2.913043 |  | 100 |
| rejection_block | target_rr_below_3 | 14 | 14 | 14 |  | 8.568832 | 5.645714 | 0.571429 | 2.458214 | 49.428571 | 0.959481 | 0.571429 | 0.714286 | 0.642857 | 0.428571 | 1.0 | 1.5 | 1.0 | 1.666667 |  | 14 |
| turtle_soup | none | 310 | 310 | 310 |  | 4.626978 | 2.983969 | 0.080645 | 9.835449 | 50.0 | 0.142505 | 0.080645 | 0.46129 | 0.332258 | 0.816129 | 1.0 | 3.648221 | 2.307692 | 3.436893 |  |  |
| turtle_soup | target_rr_below_2 | 52 | 52 | 52 |  | 1.755091 | 1.223856 | 0.403846 | 1.248076 | 30.0 | 0.162216 | 0.403846 | 0.365385 | 0.096154 | 0.403846 | 1.0 | 3.047619 | 6.526316 | 8.8 |  | 52 |
| turtle_soup | target_rr_below_3 | 34 | 34 | 34 |  | 2.365565 | 1.36063 | 0.235294 | 2.497293 | 40.0 | 0.214125 | 0.235294 | 0.441176 | 0.294118 | 0.588235 | 1.0 | 7.0 | 3.6 | 7.8 |  | 34 |
