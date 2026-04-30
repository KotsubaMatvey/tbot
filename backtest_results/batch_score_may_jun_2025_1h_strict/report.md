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
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 31 | 31 | 13 | 14 | 11.647242 | 9.19118 | 0.225806 | 4.350119 | 77.548387 | 0.521575 | 0.225806 | 0.258065 | 0.193548 | 0.193548 | 8.217391 | 1.166667 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | 28 | 28 | 26 |  | 24.866026 | 16.874769 | 0.214286 | 5.217411 | 94.892857 | -0.139175 | 0.214286 | 0.285714 | 0.285714 | 0.714286 | 2.576923 | 1.2 | 1.0 | 1.0 |  | 18 |
| mitigation_block | 78 | 78 | 78 |  | 1.947558 | 1.503239 | 0.307692 | 1.13764 | 78.051282 | -0.566923 | 0.307692 | 0.166667 | 0.038462 | 0.692308 | 1.0 | 2.259259 | 3.153846 | 4.666667 |  | 78 |
| reclaimed_ob | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | 70 | 70 | 70 |  | 5.799647 | 4.572091 | 0.557143 | 2.40827 | 84.171429 | 0.746023 | 0.557143 | 0.585714 | 0.4 | 0.385714 | 1.0 | 3.518519 | 1.390244 | 2.571429 |  | 64 |
| silver_bullet | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 31 | 31 | 13 | 14 | 11.647242 | 9.19118 | 0.225806 | 4.350119 | 77.548387 | 0.521575 | 0.225806 | 0.258065 | 0.193548 | 0.193548 | 8.217391 | 1.166667 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | edge | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | edge | 28 | 28 | 26 |  | 24.866026 | 16.874769 | 0.214286 | 5.217411 | 94.892857 | -0.139175 | 0.214286 | 0.285714 | 0.285714 | 0.714286 | 2.576923 | 1.2 | 1.0 | 1.0 |  | 18 |
| mitigation_block | body_zone_retest | 78 | 78 | 78 |  | 1.947558 | 1.503239 | 0.307692 | 1.13764 | 78.051282 | -0.566923 | 0.307692 | 0.166667 | 0.038462 | 0.692308 | 1.0 | 2.259259 | 3.153846 | 4.666667 |  | 78 |
| reclaimed_ob | body_edge | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | body_level | 70 | 70 | 70 |  | 5.799647 | 4.572091 | 0.557143 | 2.40827 | 84.171429 | 0.746023 | 0.557143 | 0.585714 | 0.4 | 0.385714 | 1.0 | 3.518519 | 1.390244 | 2.571429 |  | 64 |
| silver_bullet | edge | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | close | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 31 | 31 | 13 | 14 | 11.647242 | 9.19118 | 0.225806 | 4.350119 | 77.548387 | 0.521575 | 0.225806 | 0.258065 | 0.193548 | 0.193548 | 8.217391 | 1.166667 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | sweep_extreme | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | ce | 28 | 28 | 26 |  | 24.866026 | 16.874769 | 0.214286 | 5.217411 | 94.892857 | -0.139175 | 0.214286 | 0.285714 | 0.285714 | 0.714286 | 2.576923 | 1.2 | 1.0 | 1.0 |  | 18 |
| mitigation_block | block_extreme | 78 | 78 | 78 |  | 1.947558 | 1.503239 | 0.307692 | 1.13764 | 78.051282 | -0.566923 | 0.307692 | 0.166667 | 0.038462 | 0.692308 | 1.0 | 2.259259 | 3.153846 | 4.666667 |  | 78 |
| reclaimed_ob | mean_threshold | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | wick_extreme | 70 | 70 | 70 |  | 5.799647 | 4.572091 | 0.557143 | 2.40827 | 84.171429 | 0.746023 | 0.557143 | 0.585714 | 0.4 | 0.385714 | 1.0 | 3.518519 | 1.390244 | 2.571429 |  | 64 |
| silver_bullet | swing_or_fvg | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | sweep_extreme | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 31 | 31 | 13 | 14 | 11.647242 | 9.19118 | 0.225806 | 4.350119 | 77.548387 | 0.521575 | 0.225806 | 0.258065 | 0.193548 | 0.193548 | 8.217391 | 1.166667 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | conservative | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | conservative | 28 | 28 | 26 |  | 24.866026 | 16.874769 | 0.214286 | 5.217411 | 94.892857 | -0.139175 | 0.214286 | 0.285714 | 0.285714 | 0.714286 | 2.576923 | 1.2 | 1.0 | 1.0 |  | 18 |
| mitigation_block | conservative | 78 | 78 | 78 |  | 1.947558 | 1.503239 | 0.307692 | 1.13764 | 78.051282 | -0.566923 | 0.307692 | 0.166667 | 0.038462 | 0.692308 | 1.0 | 2.259259 | 3.153846 | 4.666667 |  | 78 |
| reclaimed_ob | conservative | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | conservative | 70 | 70 | 70 |  | 5.799647 | 4.572091 | 0.557143 | 2.40827 | 84.171429 | 0.746023 | 0.557143 | 0.585714 | 0.4 | 0.385714 | 1.0 | 3.518519 | 1.390244 | 2.571429 |  | 64 |
| silver_bullet | conservative | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | conservative | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 382 | 382 | 361 | 15 | 6.191096 | 3.387608 | 0.282723 | 5.478438 | 67.143979 | 0.3537 | 0.282723 | 0.387435 | 0.264398 | 0.594241 | 1.561828 | 2.814978 | 2.0 | 3.267327 |  | 231 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 11 | 11 | 4 | 5 | 14.947163 | 7.548915 | 0.272727 | 8.896761 | 87.454545 | 1.139954 | 0.272727 | 0.272727 | 0.181818 | 0.090909 | 9.0 | 1.0 | 1.0 | 1.0 |  | 11 |
| breaker_block | equilibrium | 9 | 9 | 4 | 4 | 8.657159 | 7.657322 | 0.111111 | 1.312809 | 69.333333 | -0.260286 | 0.111111 | 0.222222 | 0.111111 | 0.333333 | 10.0 | 1.333333 | 1.0 | 1.0 |  | 9 |
| breaker_block | premium | 11 | 11 | 5 | 5 | 11.399371 | 9.19118 | 0.272727 | 2.288548 | 74.363636 | 0.652361 | 0.272727 | 0.272727 | 0.272727 | 0.181818 | 5.875 | 1.0 | 1.0 | 1.0 |  | 11 |
| ict2022_mss_fvg | premium | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | discount | 16 | 16 | 16 |  | 27.914325 | 19.16407 | 0.1875 | 6.018617 | 96.25 | -0.545461 | 0.1875 | 0.25 | 0.25 | 0.8125 | 2.0625 | 1.153846 | 1.0 | 1.0 |  | 9 |
| ifvg_retest | equilibrium | 4 | 4 | 3 |  | 33.615348 | 22.252912 | 0.25 | 2.198264 | 89.75 | 0.285256 | 0.25 | 0.25 | 0.25 | 0.5 | 2.666667 | 1.0 | 1.0 | 1.0 |  | 4 |
| ifvg_retest | premium | 8 | 8 | 7 |  | 14.148776 | 14.106519 | 0.25 | 5.124573 | 94.75 | 0.607578 | 0.25 | 0.375 | 0.375 | 0.625 | 3.714286 | 1.4 | 1.0 | 1.0 |  | 5 |
| mitigation_block | discount | 29 | 29 | 29 |  | 2.138718 | 1.108046 | 0.206897 | 0.669736 | 79.724138 | -0.764823 | 0.206897 | 0.034483 |  | 0.793103 | 1.0 | 1.913043 | 1.0 |  |  | 29 |
| mitigation_block | equilibrium | 8 | 8 | 8 |  | 1.587113 | 1.697434 | 0.25 | 3.18027 | 74.5 | -0.669768 | 0.25 | 0.125 |  | 0.75 | 1.0 | 3.5 | 1.0 |  |  | 8 |
| mitigation_block | premium | 41 | 41 | 41 |  | 1.882679 | 1.503239 | 0.390244 | 1.070034 | 77.560976 | -0.406878 | 0.390244 | 0.268293 | 0.073171 | 0.609756 | 1.0 | 2.28 | 3.545455 | 4.666667 |  | 41 |
| reclaimed_ob | discount | 2 | 2 | 1 | 1 | 3.084666 | 3.084666 |  | 12.671515 | 87.0 | -1.0 |  | 0.5 | 0.5 | 0.5 | 2.0 | 5.0 | 1.0 | 1.0 |  | 1 |
| reclaimed_ob | equilibrium | 2 | 2 | 2 |  | 6.244573 | 6.244573 | 0.5 | 92.143824 | 82.0 | 0.191532 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 3 | 3 | 3 |  | 9.246231 | 10.039977 | 1.0 | 0.985693 | 81.333333 | 0.985693 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 3 |
| rejection_block | discount | 37 | 37 | 37 |  | 6.157147 | 6.811205 | 0.486486 | 2.432299 | 84.594595 | 0.454059 | 0.486486 | 0.540541 | 0.324324 | 0.486486 | 1.0 | 4.388889 | 1.25 | 1.666667 |  | 36 |
| rejection_block | equilibrium | 6 | 6 | 6 |  | 7.923078 | 3.008577 | 0.666667 | 3.451538 | 75.333333 | 1.914874 | 0.666667 | 0.5 | 0.5 | 0.166667 | 1.0 | 3.0 | 1.0 | 1.333333 |  | 6 |
| rejection_block | premium | 27 | 27 | 27 |  | 4.837866 | 2.891235 | 0.62963 | 2.143504 | 85.555556 | 0.886377 | 0.62963 | 0.666667 | 0.481481 | 0.296296 | 1.0 | 1.625 | 1.611111 | 3.692308 |  | 22 |
| silver_bullet | none | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | none | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 31 | 31 | 13 | 14 | 11.647242 | 9.19118 | 0.225806 | 4.350119 | 77.548387 | 0.521575 | 0.225806 | 0.258065 | 0.193548 | 0.193548 | 8.217391 | 1.166667 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | valid | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | strong | 12 | 12 | 11 |  | 27.376121 | 14.106519 | 0.083333 | 3.967149 | 94.75 | -0.868287 | 0.083333 | 0.083333 | 0.083333 | 0.833333 | 3.363636 | 1.0 | 1.0 | 1.0 |  | 9 |
| ifvg_retest | valid | 16 | 16 | 15 |  | 23.02529 | 17.808295 | 0.3125 | 6.155108 | 95.0 | 0.395506 | 0.3125 | 0.4375 | 0.4375 | 0.625 | 2.0 | 1.4 | 1.0 | 1.0 |  | 9 |
| mitigation_block | none | 78 | 78 | 78 |  | 1.947558 | 1.503239 | 0.307692 | 1.13764 | 78.051282 | -0.566923 | 0.307692 | 0.166667 | 0.038462 | 0.692308 | 1.0 | 2.259259 | 3.153846 | 4.666667 |  | 78 |
| reclaimed_ob | none | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | none | 70 | 70 | 70 |  | 5.799647 | 4.572091 | 0.557143 | 2.40827 | 84.171429 | 0.746023 | 0.557143 | 0.585714 | 0.4 | 0.385714 | 1.0 | 3.518519 | 1.390244 | 2.571429 |  | 64 |
| silver_bullet | none | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | none | 165 | 165 | 165 |  | 5.048818 | 3.45309 | 0.169697 | 8.066439 | 47.212121 | 0.693977 | 0.169697 | 0.436364 | 0.309091 | 0.70303 | 1.0 | 3.163793 | 2.444444 | 4.411765 |  | 32 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 21 | 21 | 9 | 9 | 10.809532 | 5.858796 | 0.238095 | 6.002357 | 84.952381 | 0.551514 | 0.238095 | 0.285714 | 0.190476 | 0.190476 | 8.375 | 1.25 | 1.0 | 1.0 |  | 21 |
| breaker_block | medium | 10 | 10 | 4 | 5 | 13.53209 | 13.39355 | 0.2 | 0.880418 | 62.0 | 0.454212 | 0.2 | 0.2 | 0.2 | 0.2 | 7.857143 | 1.0 | 1.0 | 1.0 |  | 10 |
| ict2022_mss_fvg | high | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | high | 28 | 28 | 26 |  | 24.866026 | 16.874769 | 0.214286 | 5.217411 | 94.892857 | -0.139175 | 0.214286 | 0.285714 | 0.285714 | 0.714286 | 2.576923 | 1.2 | 1.0 | 1.0 |  | 18 |
| mitigation_block | high | 71 | 71 | 71 |  | 1.865261 | 1.331764 | 0.267606 | 1.206743 | 79.633803 | -0.62849 | 0.267606 | 0.15493 | 0.014085 | 0.732394 | 1.0 | 2.307692 | 3.545455 | 12.0 |  | 71 |
| mitigation_block | medium | 7 | 7 | 7 |  | 2.782285 | 2.875106 | 0.714286 | 0.436737 | 62.0 | 0.057535 | 0.714286 | 0.285714 | 0.285714 | 0.285714 | 1.0 | 1.0 | 1.0 | 1.0 |  | 7 |
| reclaimed_ob | high | 7 | 7 | 6 | 1 | 7.218751 | 8.297995 | 0.571429 | 30.369679 | 83.142857 | 0.390023 | 0.571429 | 0.714286 | 0.714286 | 0.285714 | 1.285714 | 3.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | high | 65 | 65 | 65 |  | 6.122764 | 5.170654 | 0.553846 | 2.557047 | 85.876923 | 0.826661 | 0.553846 | 0.630769 | 0.430769 | 0.384615 | 1.0 | 3.64 | 1.390244 | 2.571429 |  | 59 |
| rejection_block | medium | 5 | 5 | 5 |  | 1.599131 | 1.295564 | 0.6 | 0.474166 | 62.0 | -0.302271 | 0.6 |  |  | 0.4 | 1.0 | 2.0 |  |  |  | 5 |
| silver_bullet | medium | 2 | 2 | 2 |  | 0.563267 | 0.563267 |  | 2.0 | 68.0 | -1.0 |  |  |  | 1.0 | 1.0 | 9.0 |  |  |  | 2 |
| turtle_soup | low | 32 | 32 | 32 |  | 2.498628 | 2.096625 | 0.375 | 1.964673 | 35.625 | 0.306381 | 0.375 | 0.5 | 0.28125 | 0.53125 | 1.0 | 4.588235 | 4.9375 | 8.333333 |  | 32 |
| turtle_soup | medium | 133 | 133 | 133 |  | 5.662398 | 3.948448 | 0.120301 | 9.534534 | 50.0 | 0.787233 | 0.120301 | 0.421053 | 0.315789 | 0.744361 | 1.0 | 2.919192 | 1.732143 | 3.571429 |  |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | equilibrium;insufficient_displacement | 1 | 1 |  | 1 |  |  |  | 3.10559 | 82.0 |  |  |  |  |  | 19.0 |  |  |  |  | 1 |
| breaker_block | equilibrium;insufficient_displacement;target_rr_below_2 | 7 | 7 | 3 | 3 | 10.970188 | 9.813606 | 0.142857 | 0.840092 | 64.285714 | -0.013714 | 0.142857 | 0.142857 | 0.142857 | 0.285714 | 8.6 | 1.0 | 1.0 | 1.0 |  | 7 |
| breaker_block | equilibrium;insufficient_displacement;target_rr_below_3 | 1 | 1 | 1 |  | 1.718071 | 1.718071 |  | 2.829049 | 92.0 | -1.0 |  | 1.0 |  | 1.0 | 8.0 | 2.0 | 1.0 |  |  | 1 |
| breaker_block | insufficient_displacement | 5 | 5 | 1 | 4 | 40.176395 | 40.176395 | 0.2 | 18.290133 | 97.6 | 5.247313 | 0.2 | 0.2 | 0.2 |  | 10.0 |  | 1.0 | 1.0 |  | 5 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 5 | 5 | 3 | 1 | 8.764409 | 5.858796 | 0.4 | 0.631548 | 77.0 | 0.028593 | 0.4 | 0.4 | 0.2 | 0.2 | 1.5 | 1.0 | 1.0 | 1.0 |  | 5 |
| breaker_block | insufficient_displacement;target_rr_below_3 | 2 | 2 | 1 |  | 5.531025 | 5.531025 | 0.5 | 2.288225 | 97.5 | 2.416918 | 0.5 | 0.5 | 0.5 |  | 1.0 |  | 1.0 | 1.0 |  | 2 |
| breaker_block | poor_pd_location;insufficient_displacement | 2 | 2 |  | 1 |  |  |  | 8.517892 | 86.0 |  |  |  |  |  | 5.0 |  |  |  |  | 2 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_2 | 8 | 8 | 4 | 4 | 11.196216 | 9.215107 | 0.25 | 0.852221 | 67.5 | 0.017903 | 0.25 | 0.25 | 0.25 | 0.25 | 11.0 | 1.0 | 1.0 | 1.0 |  | 8 |
| ict2022_mss_fvg | none | 1 | 1 | 1 |  | 1.675943 | 1.675943 |  | 6.957059 | 100.0 | 1.675943 |  | 1.0 |  |  | 1.0 |  | 1.0 |  |  |  |
| ifvg_retest | equilibrium | 1 | 1 | 1 |  | 75.497647 | 75.497647 |  | 3.038356 | 100.0 | -1.0 |  |  |  | 1.0 | 3.0 | 1.0 |  |  |  | 1 |
| ifvg_retest | equilibrium;target_rr_below_2 | 2 | 2 | 1 |  | 22.252912 | 22.252912 |  | 1.449466 | 79.5 | -1.0 |  |  |  | 0.5 | 3.0 | 1.0 |  |  |  | 2 |
| ifvg_retest | equilibrium;target_rr_below_3 | 1 | 1 | 1 |  | 3.095485 | 3.095485 | 1.0 | 2.855767 | 100.0 | 2.855767 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | none | 10 | 10 | 10 |  | 31.833028 | 18.756415 | 0.2 | 10.350415 | 100.0 | 0.125304 | 0.2 | 0.4 | 0.4 | 0.8 | 2.7 | 1.5 | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 3 | 3 | 3 |  | 14.21375 | 15.941242 |  | 7.177592 | 99.0 | -1.0 |  |  |  | 1.0 | 1.333333 | 1.0 |  |  |  | 3 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 4 | 4 | 4 |  | 18.332342 | 9.659634 | 0.5 | 1.140954 | 83.5 | 0.455945 | 0.5 | 0.5 | 0.5 | 0.5 | 5.25 | 1.0 | 1.0 | 1.0 |  | 4 |
| ifvg_retest | target_rr_below_2 | 7 | 7 | 6 |  | 18.561622 | 16.067113 | 0.142857 | 1.099101 | 95.285714 | -0.758525 | 0.142857 | 0.142857 | 0.142857 | 0.714286 | 1.166667 | 1.0 | 1.0 | 1.0 |  | 7 |
| mitigation_block | equilibrium | 2 | 2 | 2 |  | 1.758225 | 1.758225 |  | 9.786039 | 82.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.5 |  |  |  | 2 |
| mitigation_block | equilibrium;target_rr_below_2 | 4 | 4 | 4 |  | 1.818896 | 1.877271 | 0.5 | 0.382186 | 72.0 | -0.339536 | 0.5 | 0.25 |  | 0.5 | 1.0 | 1.5 | 1.0 |  |  | 4 |
| mitigation_block | equilibrium;target_rr_below_3 | 2 | 2 | 2 |  | 0.952436 | 0.952436 |  | 2.170668 | 72.0 | -1.0 |  |  |  | 1.0 | 1.0 | 7.5 |  |  |  | 2 |
| mitigation_block | poor_pd_location | 1 | 1 | 1 |  | 1.758225 | 1.758225 |  | 9.786039 | 100.0 | -1.0 |  | 1.0 |  | 1.0 | 1.0 | 4.0 | 2.0 |  |  | 1 |
