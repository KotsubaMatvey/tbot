# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_oct_2025_4h_aligned\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 271 | 255 | 10 | 78.070111 | 6.918853 | 2.573175 | 5.001371 | 0.263838 | 0.291513 | 0.405904 | 0.225092 | 0.605166 |  | 174 | poor_pd_location:123;target_rr_below_2:117;insufficient_displacement:26;target_rr_below_3:18 |
| filtered_all | ALL | 0 | model_rules | 137 | 134 | 128 | 4 | 80.164179 | 6.495728 | 3.824357 | 8.400808 | 0.321432 | 0.11194 | 0.432836 | 0.291045 | 0.768657 |  | 37 | poor_pd_location:31;insufficient_displacement:8;target_rr_below_3:4 |
| all | ALL | 50 | none |  | 267 | 251 | 10 | 78.565543 | 7.012623 | 2.721903 | 5.057015 | 0.275621 | 0.29588 | 0.40824 | 0.228464 | 0.602996 |  | 170 | poor_pd_location:119;target_rr_below_2:113;insufficient_displacement:26;target_rr_below_3:18 |
| filtered_all | ALL | 50 | model_rules | 133 | 134 | 128 | 4 | 80.164179 | 6.495728 | 3.824357 | 8.400808 | 0.321432 | 0.11194 | 0.432836 | 0.291045 | 0.768657 |  | 37 | poor_pd_location:31;insufficient_displacement:8;target_rr_below_3:4 |
| all | ALL | 70 | none |  | 209 | 197 | 6 | 83.119617 | 7.831442 | 2.846721 | 5.373596 | 0.27089 | 0.277512 | 0.382775 | 0.23445 | 0.626794 |  | 112 | target_rr_below_2:88;poor_pd_location:66;insufficient_displacement:19;target_rr_below_3:10 |
| filtered_all | ALL | 70 | model_rules | 100 | 109 | 103 | 4 | 83.642202 | 6.928097 | 3.537406 | 8.59681 | 0.23633 | 0.100917 | 0.412844 | 0.275229 | 0.779817 |  | 12 | insufficient_displacement:8;poor_pd_location:6;target_rr_below_3:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | breaker_block | 0 | none |  | 26 | 11 | 10 | 80.615385 | 8.660527 | 5.273829 | 2.679307 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 |  | 26 | insufficient_displacement:26;poor_pd_location:18;target_rr_below_2:18;target_rr_below_3:1 |
| model | ifvg_retest | 0 | none |  | 24 | 23 |  | 98.875 | 35.123343 | 9.722848 | 6.69314 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 |  | 18 | target_rr_below_2:12;poor_pd_location:10;target_rr_below_3:1 |
| model | mitigation_block | 0 | none |  | 45 | 45 |  | 75.244444 | 1.979989 | 0.774549 | 0.883132 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 |  | 43 | target_rr_below_2:39;poor_pd_location:32;target_rr_below_3:4 |
| model | reclaimed_ob | 0 | none |  | 5 | 5 |  | 83.2 | 12.860001 | 12.01518 | 4.364048 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 |  | 4 | poor_pd_location:2;target_rr_below_2:2;target_rr_below_3:1 |
| model | rejection_block | 0 | none |  | 44 | 44 |  | 80.704545 | 4.985211 | 2.965326 | 1.437243 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 |  | 40 | target_rr_below_2:37;poor_pd_location:24;target_rr_below_3:2 |
| model | turtle_soup | 0 | none |  | 127 | 127 |  | 73.503937 | 3.84611 | 2.991057 | 7.876176 | 0.112573 | 0.102362 | 0.456693 | 0.267717 | 0.811024 |  | 43 | poor_pd_location:37;target_rr_below_2:9;target_rr_below_3:9 |
| filtered_model | breaker_block | 0 | model_rules | 18 | 8 | 2 | 4 | 94.625 | 10.681674 | 10.681674 | 6.765281 | 1.903158 | 0.125 | 0.25 | 0.125 | 0.125 |  | 8 | insufficient_displacement:8;poor_pd_location:5;target_rr_below_3:1 |
| filtered_model | ifvg_retest | 0 | model_rules | 18 | 6 | 6 |  | 100.0 | 44.096741 | 35.555607 | 7.589857 | 1.494599 | 0.166667 | 0.166667 | 0.166667 | 0.833333 |  |  |  |
| filtered_model | mitigation_block | 0 | model_rules | 43 | 2 | 2 |  | 98.5 | 3.46526 | 3.46526 | 3.458389 | 1.175986 | 0.5 | 0.5 | 0.5 | 0.5 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 2 | 3 | 3 |  | 92.333333 | 15.777816 | 12.01518 | 6.782091 | 3.266568 | 0.666667 | 0.666667 | 0.666667 | 0.333333 |  | 2 | target_rr_below_3:1;poor_pd_location:1 |
| filtered_model | rejection_block | 0 | model_rules | 38 | 6 | 6 |  | 94.333333 | 6.16315 | 5.671791 | 5.658848 | -1.0 |  | 0.166667 | 0.166667 | 1.0 |  | 2 | target_rr_below_3:2 |
| filtered_model | turtle_soup | 0 | model_rules | 18 | 109 | 109 |  | 76.559633 | 4.167583 | 3.358089 | 8.851658 | 0.203832 | 0.091743 | 0.46789 | 0.302752 | 0.816514 |  | 25 | poor_pd_location:25 |
| model | breaker_block | 50 | none |  | 26 | 11 | 10 | 80.615385 | 8.660527 | 5.273829 | 2.679307 | 0.73721 | 0.346154 | 0.307692 | 0.269231 | 0.076923 |  | 26 | insufficient_displacement:26;poor_pd_location:18;target_rr_below_2:18;target_rr_below_3:1 |
| model | ifvg_retest | 50 | none |  | 24 | 23 |  | 98.875 | 35.123343 | 9.722848 | 6.69314 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 |  | 18 | target_rr_below_2:12;poor_pd_location:10;target_rr_below_3:1 |
| model | mitigation_block | 50 | none |  | 45 | 45 |  | 75.244444 | 1.979989 | 0.774549 | 0.883132 | -0.5216 | 0.288889 | 0.2 | 0.022222 | 0.711111 |  | 43 | target_rr_below_2:39;poor_pd_location:32;target_rr_below_3:4 |
| model | reclaimed_ob | 50 | none |  | 5 | 5 |  | 83.2 | 12.860001 | 12.01518 | 4.364048 | 2.254734 | 0.8 | 0.8 | 0.6 | 0.2 |  | 4 | poor_pd_location:2;target_rr_below_2:2;target_rr_below_3:1 |
| model | rejection_block | 50 | none |  | 44 | 44 |  | 80.704545 | 4.985211 | 2.965326 | 1.437243 | 0.285839 | 0.704545 | 0.477273 | 0.227273 | 0.295455 |  | 40 | target_rr_below_2:37;poor_pd_location:24;target_rr_below_3:2 |
| model | turtle_soup | 50 | none |  | 123 | 123 |  | 74.430894 | 3.937535 | 3.076718 | 8.090454 | 0.131698 | 0.105691 | 0.463415 | 0.276423 | 0.813008 |  | 39 | poor_pd_location:33;target_rr_below_3:9;target_rr_below_2:5 |
| filtered_model | breaker_block | 50 | model_rules | 18 | 8 | 2 | 4 | 94.625 | 10.681674 | 10.681674 | 6.765281 | 1.903158 | 0.125 | 0.25 | 0.125 | 0.125 |  | 8 | insufficient_displacement:8;poor_pd_location:5;target_rr_below_3:1 |
| filtered_model | ifvg_retest | 50 | model_rules | 18 | 6 | 6 |  | 100.0 | 44.096741 | 35.555607 | 7.589857 | 1.494599 | 0.166667 | 0.166667 | 0.166667 | 0.833333 |  |  |  |
| filtered_model | mitigation_block | 50 | model_rules | 43 | 2 | 2 |  | 98.5 | 3.46526 | 3.46526 | 3.458389 | 1.175986 | 0.5 | 0.5 | 0.5 | 0.5 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 2 | 3 | 3 |  | 92.333333 | 15.777816 | 12.01518 | 6.782091 | 3.266568 | 0.666667 | 0.666667 | 0.666667 | 0.333333 |  | 2 | target_rr_below_3:1;poor_pd_location:1 |
| filtered_model | rejection_block | 50 | model_rules | 38 | 6 | 6 |  | 94.333333 | 6.16315 | 5.671791 | 5.658848 | -1.0 |  | 0.166667 | 0.166667 | 1.0 |  | 2 | target_rr_below_3:2 |
| filtered_model | turtle_soup | 50 | model_rules | 14 | 109 | 109 |  | 76.559633 | 4.167583 | 3.358089 | 8.851658 | 0.203832 | 0.091743 | 0.46789 | 0.302752 | 0.816514 |  | 25 | poor_pd_location:25 |
| model | breaker_block | 70 | none |  | 19 | 8 | 6 | 87.473684 | 7.479246 | 6.032545 | 3.372441 | 0.730312 | 0.315789 | 0.315789 | 0.263158 | 0.105263 |  | 19 | insufficient_displacement:19;target_rr_below_2:11;poor_pd_location:11;target_rr_below_3:1 |
| model | ifvg_retest | 70 | none |  | 24 | 23 |  | 98.875 | 35.123343 | 9.722848 | 6.69314 | 1.934527 | 0.375 | 0.416667 | 0.25 | 0.541667 |  | 18 | target_rr_below_2:12;poor_pd_location:10;target_rr_below_3:1 |
| model | mitigation_block | 70 | none |  | 39 | 39 |  | 77.282051 | 2.081548 | 0.553648 | 0.944453 | -0.580266 | 0.230769 | 0.153846 | 0.025641 | 0.769231 |  | 37 | target_rr_below_2:33;poor_pd_location:26;target_rr_below_3:4 |
| model | reclaimed_ob | 70 | none |  | 4 | 4 |  | 88.5 | 12.810196 | 9.397534 | 5.196088 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 |  | 3 | target_rr_below_3:1;target_rr_below_2:1;poor_pd_location:1 |
| model | rejection_block | 70 | none |  | 38 | 38 |  | 83.657895 | 5.371843 | 2.965326 | 1.622806 | 0.2896 | 0.657895 | 0.447368 | 0.263158 | 0.342105 |  | 34 | target_rr_below_2:31;poor_pd_location:18;target_rr_below_3:2 |
| model | turtle_soup | 70 | none |  | 85 | 85 |  | 79.882353 | 3.983199 | 3.003668 | 9.165708 | 0.051958 | 0.070588 | 0.447059 | 0.282353 | 0.847059 |  | 1 | target_rr_below_3:1 |
| filtered_model | breaker_block | 70 | model_rules | 11 | 8 | 2 | 4 | 94.625 | 10.681674 | 10.681674 | 6.765281 | 1.903158 | 0.125 | 0.25 | 0.125 | 0.125 |  | 8 | insufficient_displacement:8;poor_pd_location:5;target_rr_below_3:1 |
| filtered_model | ifvg_retest | 70 | model_rules | 18 | 6 | 6 |  | 100.0 | 44.096741 | 35.555607 | 7.589857 | 1.494599 | 0.166667 | 0.166667 | 0.166667 | 0.833333 |  |  |  |
| filtered_model | mitigation_block | 70 | model_rules | 37 | 2 | 2 |  | 98.5 | 3.46526 | 3.46526 | 3.458389 | 1.175986 | 0.5 | 0.5 | 0.5 | 0.5 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 1 | 3 | 3 |  | 92.333333 | 15.777816 | 12.01518 | 6.782091 | 3.266568 | 0.666667 | 0.666667 | 0.666667 | 0.333333 |  | 2 | target_rr_below_3:1;poor_pd_location:1 |
| filtered_model | rejection_block | 70 | model_rules | 32 | 6 | 6 |  | 94.333333 | 6.16315 | 5.671791 | 5.658848 | -1.0 |  | 0.166667 | 0.166667 | 1.0 |  | 2 | target_rr_below_3:2 |
| filtered_model | turtle_soup | 70 | model_rules | 1 | 84 | 84 |  | 80.0 | 4.004849 | 3.040193 | 9.240176 | 0.064481 | 0.071429 | 0.452381 | 0.285714 | 0.845238 |  |  |  |
