# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-10-31
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 64 | 64 | 30 | 28 | 11.457118 | 6.585681 | 0.328125 | 6.273518 | 79.59375 | 0.679432 | 0.328125 | 0.296875 | 0.265625 | 0.140625 | 6.411765 | 1.0 | 1.0 | 1.0 |  | 64 |
| ict2022_mss_fvg | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | 67 | 67 | 65 |  | 27.368231 | 14.106519 | 0.238806 | 5.848423 | 95.865672 | 0.544192 | 0.238806 | 0.313433 | 0.298507 | 0.731343 | 2.184615 | 1.244898 | 1.0 | 1.0 |  | 46 |
| mitigation_block | 190 | 190 | 190 |  | 1.983735 | 1.299914 | 0.426316 | 0.775361 | 77.731579 | -0.320837 | 0.426316 | 0.210526 | 0.057895 | 0.563158 | 1.0 | 2.336449 | 3.2 | 9.181818 |  | 189 |
| reclaimed_ob | 10 | 10 | 9 | 1 | 18.78602 | 6.556014 | 0.7 | 19.824721 | 78.9 | 0.730458 | 0.7 | 0.8 | 0.8 | 0.2 | 1.4 | 3.0 | 1.0 | 1.0 |  | 9 |
| rejection_block | 161 | 161 | 161 |  | 5.621072 | 4.450242 | 0.583851 | 2.115813 | 83.583851 | 0.610994 | 0.583851 | 0.627329 | 0.42236 | 0.403727 | 1.0 | 2.461538 | 1.405941 | 2.382353 |  | 144 |
| silver_bullet | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | 448 | 448 | 448 |  | 4.130861 | 2.810172 | 0.142857 | 7.682441 | 70.747768 | 0.260201 | 0.142857 | 0.430804 | 0.294643 | 0.75 | 1.0 | 3.738095 | 2.979275 | 5.189394 |  | 233 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 64 | 64 | 30 | 28 | 11.457118 | 6.585681 | 0.328125 | 6.273518 | 79.59375 | 0.679432 | 0.328125 | 0.296875 | 0.265625 | 0.140625 | 6.411765 | 1.0 | 1.0 | 1.0 |  | 64 |
| ict2022_mss_fvg | edge | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | edge | 67 | 67 | 65 |  | 27.368231 | 14.106519 | 0.238806 | 5.848423 | 95.865672 | 0.544192 | 0.238806 | 0.313433 | 0.298507 | 0.731343 | 2.184615 | 1.244898 | 1.0 | 1.0 |  | 46 |
| mitigation_block | body_zone_retest | 190 | 190 | 190 |  | 1.983735 | 1.299914 | 0.426316 | 0.775361 | 77.731579 | -0.320837 | 0.426316 | 0.210526 | 0.057895 | 0.563158 | 1.0 | 2.336449 | 3.2 | 9.181818 |  | 189 |
| reclaimed_ob | body_edge | 10 | 10 | 9 | 1 | 18.78602 | 6.556014 | 0.7 | 19.824721 | 78.9 | 0.730458 | 0.7 | 0.8 | 0.8 | 0.2 | 1.4 | 3.0 | 1.0 | 1.0 |  | 9 |
| rejection_block | body_level | 161 | 161 | 161 |  | 5.621072 | 4.450242 | 0.583851 | 2.115813 | 83.583851 | 0.610994 | 0.583851 | 0.627329 | 0.42236 | 0.403727 | 1.0 | 2.461538 | 1.405941 | 2.382353 |  | 144 |
| silver_bullet | edge | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | close | 448 | 448 | 448 |  | 4.130861 | 2.810172 | 0.142857 | 7.682441 | 70.747768 | 0.260201 | 0.142857 | 0.430804 | 0.294643 | 0.75 | 1.0 | 3.738095 | 2.979275 | 5.189394 |  | 233 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 64 | 64 | 30 | 28 | 11.457118 | 6.585681 | 0.328125 | 6.273518 | 79.59375 | 0.679432 | 0.328125 | 0.296875 | 0.265625 | 0.140625 | 6.411765 | 1.0 | 1.0 | 1.0 |  | 64 |
| ict2022_mss_fvg | sweep_extreme | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | ce | 67 | 67 | 65 |  | 27.368231 | 14.106519 | 0.238806 | 5.848423 | 95.865672 | 0.544192 | 0.238806 | 0.313433 | 0.298507 | 0.731343 | 2.184615 | 1.244898 | 1.0 | 1.0 |  | 46 |
| mitigation_block | block_extreme | 190 | 190 | 190 |  | 1.983735 | 1.299914 | 0.426316 | 0.775361 | 77.731579 | -0.320837 | 0.426316 | 0.210526 | 0.057895 | 0.563158 | 1.0 | 2.336449 | 3.2 | 9.181818 |  | 189 |
| reclaimed_ob | mean_threshold | 10 | 10 | 9 | 1 | 18.78602 | 6.556014 | 0.7 | 19.824721 | 78.9 | 0.730458 | 0.7 | 0.8 | 0.8 | 0.2 | 1.4 | 3.0 | 1.0 | 1.0 |  | 9 |
| rejection_block | wick_extreme | 161 | 161 | 161 |  | 5.621072 | 4.450242 | 0.583851 | 2.115813 | 83.583851 | 0.610994 | 0.583851 | 0.627329 | 0.42236 | 0.403727 | 1.0 | 2.461538 | 1.405941 | 2.382353 |  | 144 |
| silver_bullet | swing_or_fvg | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | sweep_extreme | 448 | 448 | 448 |  | 4.130861 | 2.810172 | 0.142857 | 7.682441 | 70.747768 | 0.260201 | 0.142857 | 0.430804 | 0.294643 | 0.75 | 1.0 | 3.738095 | 2.979275 | 5.189394 |  | 233 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 64 | 64 | 30 | 28 | 11.457118 | 6.585681 | 0.328125 | 6.273518 | 79.59375 | 0.679432 | 0.328125 | 0.296875 | 0.265625 | 0.140625 | 6.411765 | 1.0 | 1.0 | 1.0 |  | 64 |
| ict2022_mss_fvg | conservative | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | conservative | 67 | 67 | 65 |  | 27.368231 | 14.106519 | 0.238806 | 5.848423 | 95.865672 | 0.544192 | 0.238806 | 0.313433 | 0.298507 | 0.731343 | 2.184615 | 1.244898 | 1.0 | 1.0 |  | 46 |
| mitigation_block | conservative | 190 | 190 | 190 |  | 1.983735 | 1.299914 | 0.426316 | 0.775361 | 77.731579 | -0.320837 | 0.426316 | 0.210526 | 0.057895 | 0.563158 | 1.0 | 2.336449 | 3.2 | 9.181818 |  | 189 |
| reclaimed_ob | conservative | 10 | 10 | 9 | 1 | 18.78602 | 6.556014 | 0.7 | 19.824721 | 78.9 | 0.730458 | 0.7 | 0.8 | 0.8 | 0.2 | 1.4 | 3.0 | 1.0 | 1.0 |  | 9 |
| rejection_block | conservative | 161 | 161 | 161 |  | 5.621072 | 4.450242 | 0.583851 | 2.115813 | 83.583851 | 0.610994 | 0.583851 | 0.627329 | 0.42236 | 0.403727 | 1.0 | 2.461538 | 1.405941 | 2.382353 |  | 144 |
| silver_bullet | conservative | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | conservative | 448 | 448 | 448 |  | 4.130861 | 2.810172 | 0.142857 | 7.682441 | 70.747768 | 0.260201 | 0.142857 | 0.430804 | 0.294643 | 0.75 | 1.0 | 3.738095 | 2.979275 | 5.189394 |  | 233 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 951 | 951 | 914 | 29 | 5.966449 | 3.076181 | 0.298633 | 5.237277 | 77.009464 | 0.259347 | 0.298633 | 0.407992 | 0.272345 | 0.601472 | 1.38141 | 3.127622 | 2.332474 | 3.857143 |  | 694 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 33 | 33 | 16 | 14 | 13.092166 | 7.579207 | 0.363636 | 10.119365 | 85.848485 | 1.072164 | 0.363636 | 0.333333 | 0.30303 | 0.121212 | 6.296296 | 1.0 | 1.0 | 1.0 |  | 33 |
| breaker_block | premium | 31 | 31 | 14 | 14 | 9.588492 | 6.585681 | 0.290323 | 2.179552 | 72.935484 | 0.230596 | 0.290323 | 0.258065 | 0.225806 | 0.16129 | 6.541667 | 1.0 | 1.0 | 1.0 |  | 31 |
| ict2022_mss_fvg | discount | 1 | 1 | 1 |  | 13.865035 | 13.865035 |  | 29.527775 | 100.0 | 13.865035 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  |  |
| ict2022_mss_fvg | premium | 2 | 2 | 2 |  | 3.505492 | 3.505492 |  | 6.913929 | 100.0 | 3.505492 |  | 1.0 | 0.5 |  | 1.0 |  | 1.0 | 2.0 |  | 1 |
| ifvg_retest | discount | 40 | 40 | 39 |  | 26.336568 | 17.603333 | 0.2 | 4.548864 | 97.125 | -0.445425 | 0.2 | 0.25 | 0.25 | 0.775 | 2.076923 | 1.258065 | 1.0 | 1.0 |  | 27 |
| ifvg_retest | premium | 27 | 27 | 26 |  | 28.915726 | 14.014738 | 0.296296 | 7.773697 | 94.0 | 2.028617 | 0.296296 | 0.407407 | 0.37037 | 0.666667 | 2.346154 | 1.222222 | 1.0 | 1.0 |  | 19 |
| mitigation_block | discount | 91 | 91 | 91 |  | 2.02165 | 1.108046 | 0.43956 | 0.744883 | 78.736264 | -0.263791 | 0.43956 | 0.175824 | 0.065934 | 0.549451 | 1.0 | 2.14 | 2.8125 | 11.666667 |  | 90 |
| mitigation_block | premium | 99 | 99 | 99 |  | 1.948883 | 1.503239 | 0.414141 | 0.803375 | 76.808081 | -0.373272 | 0.414141 | 0.242424 | 0.050505 | 0.575758 | 1.0 | 2.508772 | 3.458333 | 6.2 |  | 99 |
| reclaimed_ob | discount | 4 | 4 | 3 | 1 | 41.169622 | 3.70286 | 0.5 | 7.090366 | 84.75 | 0.672811 | 0.5 | 0.75 | 0.75 | 0.25 | 1.5 | 5.0 | 1.0 | 1.0 |  | 3 |
| reclaimed_ob | premium | 6 | 6 | 6 |  | 7.594219 | 8.297995 | 0.833333 | 28.314292 | 75.0 | 0.759281 | 0.833333 | 0.833333 | 0.833333 | 0.166667 | 1.333333 | 1.0 | 1.0 | 1.0 |  | 6 |
| rejection_block | discount | 89 | 89 | 89 |  | 5.906278 | 4.844295 | 0.573034 | 2.336698 | 83.955056 | 0.710695 | 0.573034 | 0.617978 | 0.438202 | 0.404494 | 1.0 | 3.083333 | 1.363636 | 2.128205 |  | 85 |
| rejection_block | premium | 72 | 72 | 72 |  | 5.268526 | 3.734383 | 0.597222 | 1.842775 | 83.125 | 0.487753 | 0.597222 | 0.638889 | 0.402778 | 0.402778 | 1.0 | 1.689655 | 1.456522 | 2.724138 |  | 59 |
| silver_bullet | discount | 2 | 2 | 2 |  | 1.47392 | 1.47392 | 0.5 | 2.0 | 90.5 | 1.419311 | 0.5 | 0.5 | 0.5 |  | 1.0 |  | 2.0 | 3.0 |  | 2 |
| silver_bullet | premium | 6 | 6 | 6 |  | 0.876604 | 0.680992 |  | 2.0 | 88.0 | -0.497059 |  | 0.333333 |  | 0.666667 | 1.0 | 11.75 | 3.5 |  |  | 6 |
| turtle_soup | discount | 258 | 258 | 258 |  | 4.543903 | 3.14116 | 0.143411 | 8.17519 | 70.988372 | 0.477017 | 0.143411 | 0.468992 | 0.341085 | 0.713178 | 1.0 | 3.744565 | 3.024793 | 5.784091 |  | 138 |
| turtle_soup | premium | 190 | 190 | 190 |  | 3.569992 | 2.316942 | 0.142105 | 7.01334 | 70.421053 | -0.034212 | 0.142105 | 0.378947 | 0.231579 | 0.8 | 1.0 | 3.730263 | 2.902778 | 4.0 |  | 95 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 64 | 64 | 30 | 28 | 11.457118 | 6.585681 | 0.328125 | 6.273518 | 79.59375 | 0.679432 | 0.328125 | 0.296875 | 0.265625 | 0.140625 | 6.411765 | 1.0 | 1.0 | 1.0 |  | 64 |
| ict2022_mss_fvg | valid | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | strong | 25 | 25 | 24 |  | 20.383276 | 13.863593 | 0.24 | 3.753333 | 96.0 | -0.364915 | 0.24 | 0.2 | 0.16 | 0.72 | 2.583333 | 1.0 | 1.0 | 1.0 |  | 17 |
| ifvg_retest | valid | 42 | 42 | 41 |  | 31.456985 | 15.941242 | 0.238095 | 7.095501 | 95.785714 | 1.076352 | 0.238095 | 0.380952 | 0.380952 | 0.738095 | 1.95122 | 1.387097 | 1.0 | 1.0 |  | 29 |
| mitigation_block | none | 190 | 190 | 190 |  | 1.983735 | 1.299914 | 0.426316 | 0.775361 | 77.731579 | -0.320837 | 0.426316 | 0.210526 | 0.057895 | 0.563158 | 1.0 | 2.336449 | 3.2 | 9.181818 |  | 189 |
| reclaimed_ob | none | 10 | 10 | 9 | 1 | 18.78602 | 6.556014 | 0.7 | 19.824721 | 78.9 | 0.730458 | 0.7 | 0.8 | 0.8 | 0.2 | 1.4 | 3.0 | 1.0 | 1.0 |  | 9 |
| rejection_block | none | 161 | 161 | 161 |  | 5.621072 | 4.450242 | 0.583851 | 2.115813 | 83.583851 | 0.610994 | 0.583851 | 0.627329 | 0.42236 | 0.403727 | 1.0 | 2.461538 | 1.405941 | 2.382353 |  | 144 |
| silver_bullet | none | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | none | 448 | 448 | 448 |  | 4.130861 | 2.810172 | 0.142857 | 7.682441 | 70.747768 | 0.260201 | 0.142857 | 0.430804 | 0.294643 | 0.75 | 1.0 | 3.738095 | 2.979275 | 5.189394 |  | 233 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 47 | 47 | 21 | 21 | 12.512315 | 5.91938 | 0.340426 | 8.34897 | 85.957447 | 0.995742 | 0.340426 | 0.319149 | 0.276596 | 0.106383 | 6.297297 | 1.0 | 1.0 | 1.0 |  | 47 |
| breaker_block | medium | 17 | 17 | 9 | 7 | 8.994993 | 6.761767 | 0.294118 | 0.535503 | 62.0 | -0.058623 | 0.294118 | 0.235294 | 0.235294 | 0.235294 | 6.714286 | 1.0 | 1.0 | 1.0 |  | 17 |
| ict2022_mss_fvg | high | 3 | 3 | 3 |  | 6.958673 | 5.33504 |  | 14.451878 | 100.0 | 6.958673 |  | 1.0 | 0.666667 |  | 1.0 |  | 1.0 | 1.5 |  | 1 |
| ifvg_retest | high | 67 | 67 | 65 |  | 27.368231 | 14.106519 | 0.238806 | 5.848423 | 95.865672 | 0.544192 | 0.238806 | 0.313433 | 0.298507 | 0.731343 | 2.184615 | 1.244898 | 1.0 | 1.0 |  | 46 |
| mitigation_block | high | 160 | 160 | 160 |  | 2.075902 | 1.299914 | 0.39375 | 0.851204 | 80.68125 | -0.350751 | 0.39375 | 0.21875 | 0.05 | 0.59375 | 1.0 | 2.273684 | 3.142857 | 10.5 |  | 159 |
| mitigation_block | medium | 30 | 30 | 30 |  | 1.492176 | 0.580818 | 0.6 | 0.37086 | 62.0 | -0.161294 | 0.6 | 0.166667 | 0.1 | 0.4 | 1.0 | 2.833333 | 3.6 | 5.666667 |  | 30 |
| reclaimed_ob | high | 8 | 8 | 7 | 1 | 21.83854 | 6.556014 | 0.625 | 24.456075 | 83.125 | 0.56793 | 0.625 | 0.75 | 0.75 | 0.25 | 1.25 | 3.0 | 1.0 | 1.0 |  | 7 |
| reclaimed_ob | medium | 2 | 2 | 2 |  | 8.102202 | 8.102202 | 1.0 | 1.299305 | 62.0 | 1.299305 | 1.0 | 1.0 | 1.0 |  | 2.0 |  | 1.0 | 1.0 |  | 2 |
| rejection_block | high | 141 | 141 | 141 |  | 5.860983 | 4.450242 | 0.574468 | 2.318609 | 86.64539 | 0.702826 | 0.574468 | 0.64539 | 0.446809 | 0.411348 | 1.0 | 2.62069 | 1.450549 | 2.492063 |  | 124 |
| rejection_block | medium | 20 | 20 | 20 |  | 3.929698 | 4.240162 | 0.65 | 0.686103 | 62.0 | -0.03642 | 0.65 | 0.5 | 0.25 | 0.35 | 1.0 | 1.142857 | 1.0 | 1.0 |  | 20 |
| silver_bullet | high | 8 | 8 | 8 |  | 1.025933 | 0.794425 | 0.125 | 2.0 | 88.625 | -0.017967 | 0.125 | 0.375 | 0.125 | 0.5 | 1.0 | 11.75 | 3.0 | 3.0 |  | 8 |
| turtle_soup | high | 238 | 238 | 238 |  | 4.565177 | 3.039943 | 0.12605 | 8.701378 | 79.033613 | 0.418571 | 0.12605 | 0.415966 | 0.298319 | 0.747899 | 1.0 | 3.297753 | 3.191919 | 5.591549 |  | 23 |
| turtle_soup | low | 21 | 21 | 21 |  | 1.15945 | 0.582756 | 0.095238 | 1.300883 | 45.0 | -0.839903 | 0.095238 | 0.142857 | 0.095238 | 0.904762 | 1.0 | 6.157895 | 3.333333 | 4.0 |  | 21 |
| turtle_soup | medium | 189 | 189 | 189 |  | 3.914101 | 2.984539 | 0.169312 | 7.108397 | 63.174603 | 0.183006 | 0.169312 | 0.481481 | 0.312169 | 0.73545 | 1.0 | 3.971223 | 2.736264 | 4.745763 |  | 189 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | insufficient_displacement | 10 | 10 | 3 | 7 | 36.036954 | 35.179976 | 0.3 | 16.361174 | 97.9 | 4.079624 | 0.3 | 0.3 | 0.3 |  | 6.0 |  | 1.0 | 1.0 |  | 10 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 16 | 16 | 9 | 6 | 9.558334 | 5.858796 | 0.4375 | 0.819843 | 81.25 | 0.310841 | 0.4375 | 0.375 | 0.25 | 0.125 | 3.916667 | 1.0 | 1.0 | 1.0 |  | 16 |
| breaker_block | insufficient_displacement;target_rr_below_3 | 4 | 4 | 2 | 1 | 10.086401 | 10.086401 | 0.25 | 2.454399 | 94.25 | 0.708459 | 0.25 | 0.25 | 0.25 | 0.25 | 6.666667 | 1.0 | 1.0 | 1.0 |  | 4 |
| breaker_block | poor_pd_location;insufficient_displacement | 6 | 6 | 1 | 3 | 16.338683 | 16.338683 | 0.166667 | 32.565653 | 87.0 | 4.720064 | 0.166667 | 0.166667 | 0.166667 |  | 7.25 |  | 1.0 | 1.0 |  | 6 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_2 | 28 | 28 | 15 | 11 | 7.537747 | 5.91938 | 0.321429 | 0.698728 | 68.428571 | -0.052697 | 0.321429 | 0.285714 | 0.285714 | 0.214286 | 7.625 | 1.0 | 1.0 | 1.0 |  | 28 |
| ict2022_mss_fvg | none | 2 | 2 | 2 |  | 7.770489 | 7.770489 |  | 18.242417 | 100.0 | 7.770489 |  | 1.0 | 0.5 |  | 1.0 |  | 1.0 | 1.0 |  |  |
| ict2022_mss_fvg | poor_pd_location | 1 | 1 | 1 |  | 5.33504 | 5.33504 |  | 6.870799 | 100.0 | 5.33504 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 2.0 |  | 1 |
| ifvg_retest | none | 21 | 21 | 20 |  | 40.958945 | 24.816638 | 0.190476 | 12.393201 | 100.0 | 2.457493 | 0.190476 | 0.380952 | 0.380952 | 0.761905 | 2.55 | 1.375 | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 13 | 13 | 13 |  | 24.794832 | 17.495589 | 0.153846 | 7.199431 | 98.846154 | -0.273789 | 0.153846 | 0.384615 | 0.384615 | 0.846154 | 1.538462 | 1.363636 | 1.0 | 1.0 |  | 13 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 13 | 13 | 13 |  | 21.566719 | 6.706761 | 0.384615 | 0.769512 | 84.692308 | -0.219791 | 0.384615 | 0.307692 | 0.230769 | 0.615385 | 3.153846 | 1.0 | 1.0 | 1.0 |  | 13 |
| ifvg_retest | poor_pd_location;target_rr_below_3 | 2 | 2 | 2 |  | 11.001815 | 11.001815 | 0.5 | 2.213827 | 97.5 | 0.703023 | 0.5 | 0.5 | 0.5 | 0.5 | 1.5 | 3.0 | 1.0 | 1.0 |  | 2 |
| ifvg_retest | target_rr_below_2 | 15 | 15 | 14 |  | 23.121505 | 16.067113 | 0.2 | 1.021773 | 96.133333 | -0.687333 | 0.2 | 0.133333 | 0.133333 | 0.733333 | 1.642857 | 1.0 | 1.0 | 1.0 |  | 15 |
| ifvg_retest | target_rr_below_3 | 3 | 3 | 3 |  | 3.783754 | 3.095485 | 0.333333 | 2.745545 | 100.0 | 0.285256 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.333333 | 1.0 | 1.0 | 1.0 |  | 3 |
| mitigation_block | none | 1 | 1 | 1 |  | 2.414773 | 2.414773 |  | 3.17894 | 100.0 | 2.414773 |  | 1.0 | 1.0 |  | 1.0 |  | 2.0 | 13.0 |  |  |
| mitigation_block | poor_pd_location | 1 | 1 | 1 |  | 1.758225 | 1.758225 |  | 9.786039 | 100.0 | -1.0 |  | 1.0 |  | 1.0 | 1.0 | 4.0 | 2.0 |  |  | 1 |
| mitigation_block | poor_pd_location;target_rr_below_2 | 60 | 60 | 60 |  | 1.501854 | 1.108046 | 0.6 | 0.411181 | 68.2 | -0.156151 | 0.6 | 0.166667 | 0.066667 | 0.4 | 1.0 | 2.75 | 4.0 | 4.5 |  | 60 |
| mitigation_block | poor_pd_location;target_rr_below_3 | 8 | 8 | 8 |  | 1.785905 | 1.378291 | 0.25 | 2.036701 | 84.0 | 0.066548 | 0.25 | 0.75 | 0.25 | 0.625 | 1.0 | 4.6 | 5.333333 | 7.0 |  | 8 |
| mitigation_block | target_rr_below_2 | 99 | 99 | 99 |  | 2.322416 | 1.394567 | 0.40404 | 0.488331 | 79.939394 | -0.44412 | 0.40404 | 0.161616 | 0.010101 | 0.59596 | 1.0 | 1.423729 | 1.75 | 2.0 |  | 99 |
| mitigation_block | target_rr_below_3 | 21 | 21 | 21 |  | 1.82947 | 1.693435 | 0.142857 | 2.144967 | 90.047619 | -0.455677 | 0.142857 | 0.285714 | 0.142857 | 0.857143 | 1.0 | 4.055556 | 4.0 | 18.0 |  | 21 |
| reclaimed_ob | none | 1 | 1 | 1 |  | 3.084666 | 3.084666 |  | 24.138766 | 97.0 | -1.0 |  | 1.0 | 1.0 | 1.0 | 1.0 | 5.0 | 1.0 | 1.0 |  |  |
