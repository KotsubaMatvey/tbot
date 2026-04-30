# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_oct_2025_30m_btc_aligned\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 898 | 868 | 25 | 76.296214 | 6.337352 | 3.151998 | 3.906642 | 0.291868 | 0.326281 | 0.41314 | 0.261693 | 0.585746 |  | 711 | poor_pd_location:506;target_rr_below_2:409;target_rr_below_3:113;insufficient_displacement:63 |
| filtered_all | ALL | 0 | model_rules | 569 | 329 | 317 | 7 | 78.100304 | 6.674057 | 3.886251 | 7.638736 | 0.765835 | 0.164134 | 0.452888 | 0.349544 | 0.68997 |  | 168 | poor_pd_location:140;target_rr_below_3:27;insufficient_displacement:24 |
| all | ALL | 50 | none |  | 854 | 824 | 25 | 77.908665 | 6.504662 | 3.16639 | 4.046734 | 0.306862 | 0.318501 | 0.409836 | 0.265808 | 0.588993 |  | 667 | poor_pd_location:462;target_rr_below_2:365;target_rr_below_3:113;insufficient_displacement:63 |
| filtered_all | ALL | 50 | model_rules | 525 | 329 | 317 | 7 | 78.100304 | 6.674057 | 3.886251 | 7.638736 | 0.765835 | 0.164134 | 0.452888 | 0.349544 | 0.68997 |  | 168 | poor_pd_location:140;target_rr_below_3:27;insufficient_displacement:24 |
| all | ALL | 70 | none |  | 647 | 619 | 23 | 82.76507 | 6.936885 | 3.044922 | 3.95652 | 0.18615 | 0.315301 | 0.386399 | 0.24575 | 0.588872 |  | 460 | target_rr_below_2:317;poor_pd_location:276;target_rr_below_3:79;insufficient_displacement:59 |
| filtered_all | ALL | 70 | model_rules | 443 | 204 | 192 | 7 | 86.127451 | 7.070558 | 3.502477 | 8.529086 | 0.60827 | 0.132353 | 0.406863 | 0.303922 | 0.696078 |  | 43 | target_rr_below_3:27;insufficient_displacement:24;poor_pd_location:15 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | breaker_block | 0 | none |  | 63 | 37 | 22 | 81.603175 | 13.161737 | 7.31203 | 2.570787 | 0.911345 | 0.333333 | 0.349206 | 0.349206 | 0.238095 |  | 63 | insufficient_displacement:63;target_rr_below_2:39;poor_pd_location:38;target_rr_below_3:8 |
| model | ict2022_mss_fvg | 0 | none |  | 8 | 8 |  | 100.0 | 5.300305 | 2.498171 | 8.794929 | 4.449634 | 0.125 | 0.75 | 0.625 | 0.125 |  | 5 | poor_pd_location:5 |
| model | ifvg_retest | 0 | none |  | 80 | 79 |  | 97.6875 | 21.298202 | 11.227001 | 4.390243 | 0.059255 | 0.1875 | 0.25 | 0.225 | 0.8 |  | 61 | poor_pd_location:40;target_rr_below_2:34;target_rr_below_3:6 |
| model | mitigation_block | 0 | none |  | 197 | 197 |  | 77.13198 | 2.565884 | 1.484878 | 0.747411 | -0.311927 | 0.431472 | 0.248731 | 0.126904 | 0.563452 |  | 197 | target_rr_below_2:169;poor_pd_location:127;target_rr_below_3:26 |
| model | reclaimed_ob | 0 | none |  | 17 | 14 | 3 | 81.470588 | 10.115386 | 10.696303 | 1.918858 | 0.871072 | 0.529412 | 0.588235 | 0.411765 | 0.294118 |  | 15 | target_rr_below_2:11;poor_pd_location:10;target_rr_below_3:4 |
| model | rejection_block | 0 | none |  | 149 | 149 |  | 81.597315 | 5.929336 | 3.629536 | 2.043127 | 0.465032 | 0.577181 | 0.610738 | 0.281879 | 0.389262 |  | 132 | target_rr_below_2:99;poor_pd_location:74;target_rr_below_3:13 |
| model | silver_bullet | 0 | none |  | 15 | 15 |  | 88.0 | 1.340204 | 0.794534 | 2.0 | -0.156179 | 0.133333 | 0.266667 | 0.133333 | 0.6 |  | 15 | target_rr_below_3:15;poor_pd_location:10 |
| model | turtle_soup | 0 | none |  | 369 | 369 |  | 66.937669 | 4.710591 | 2.959082 | 6.532086 | 0.438078 | 0.200542 | 0.457995 | 0.308943 | 0.712737 |  | 223 | poor_pd_location:202;target_rr_below_2:57;target_rr_below_3:41 |
| filtered_model | breaker_block | 0 | model_rules | 39 | 24 | 14 | 6 | 92.0 | 12.692658 | 8.110042 | 5.517652 | 2.002816 | 0.25 | 0.333333 | 0.333333 | 0.291667 |  | 24 | insufficient_displacement:24;poor_pd_location:13;target_rr_below_3:8 |
| filtered_model | ict2022_mss_fvg | 0 | model_rules | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| filtered_model | ifvg_retest | 0 | model_rules | 61 | 19 | 18 |  | 100.0 | 20.641637 | 10.334024 | 8.250236 | 0.879075 | 0.210526 | 0.315789 | 0.315789 | 0.736842 |  |  |  |
| filtered_model | mitigation_block | 0 | model_rules | 193 | 4 | 4 |  | 97.5 | 1.107536 | 0.577855 | 2.0 | -1.0 |  |  |  | 1.0 |  | 4 | target_rr_below_3:4 |
| filtered_model | reclaimed_ob | 0 | model_rules | 11 | 6 | 5 | 1 | 91.666667 | 11.978287 | 11.612722 | 4.115627 | 2.248354 | 0.5 | 0.5 | 0.5 | 0.333333 |  | 4 | target_rr_below_3:4;poor_pd_location:2 |
| filtered_model | rejection_block | 0 | model_rules | 126 | 23 | 23 |  | 95.304348 | 4.570082 | 3.157619 | 4.511191 | 0.517406 | 0.26087 | 0.608696 | 0.478261 | 0.652174 |  | 6 | target_rr_below_3:6 |
| filtered_model | silver_bullet | 0 | model_rules | 10 | 5 | 5 |  | 98.0 | 0.868201 | 0.794534 | 2.0 | 0.082955 |  | 0.2 |  | 0.4 |  | 5 | target_rr_below_3:5 |
| filtered_model | turtle_soup | 0 | model_rules | 121 | 248 | 248 |  | 72.439516 | 5.615544 | 3.826065 | 8.377076 | 0.723186 | 0.141129 | 0.471774 | 0.350806 | 0.737903 |  | 125 | poor_pd_location:125 |
| model | breaker_block | 50 | none |  | 63 | 37 | 22 | 81.603175 | 13.161737 | 7.31203 | 2.570787 | 0.911345 | 0.333333 | 0.349206 | 0.349206 | 0.238095 |  | 63 | insufficient_displacement:63;target_rr_below_2:39;poor_pd_location:38;target_rr_below_3:8 |
| model | ict2022_mss_fvg | 50 | none |  | 8 | 8 |  | 100.0 | 5.300305 | 2.498171 | 8.794929 | 4.449634 | 0.125 | 0.75 | 0.625 | 0.125 |  | 5 | poor_pd_location:5 |
| model | ifvg_retest | 50 | none |  | 80 | 79 |  | 97.6875 | 21.298202 | 11.227001 | 4.390243 | 0.059255 | 0.1875 | 0.25 | 0.225 | 0.8 |  | 61 | poor_pd_location:40;target_rr_below_2:34;target_rr_below_3:6 |
| model | mitigation_block | 50 | none |  | 197 | 197 |  | 77.13198 | 2.565884 | 1.484878 | 0.747411 | -0.311927 | 0.431472 | 0.248731 | 0.126904 | 0.563452 |  | 197 | target_rr_below_2:169;poor_pd_location:127;target_rr_below_3:26 |
| model | reclaimed_ob | 50 | none |  | 17 | 14 | 3 | 81.470588 | 10.115386 | 10.696303 | 1.918858 | 0.871072 | 0.529412 | 0.588235 | 0.411765 | 0.294118 |  | 15 | target_rr_below_2:11;poor_pd_location:10;target_rr_below_3:4 |
| model | rejection_block | 50 | none |  | 149 | 149 |  | 81.597315 | 5.929336 | 3.629536 | 2.043127 | 0.465032 | 0.577181 | 0.610738 | 0.281879 | 0.389262 |  | 132 | target_rr_below_2:99;poor_pd_location:74;target_rr_below_3:13 |
| model | silver_bullet | 50 | none |  | 15 | 15 |  | 88.0 | 1.340204 | 0.794534 | 2.0 | -0.156179 | 0.133333 | 0.266667 | 0.133333 | 0.6 |  | 15 | target_rr_below_3:15;poor_pd_location:10 |
| model | turtle_soup | 50 | none |  | 325 | 325 |  | 69.907692 | 4.914548 | 3.021788 | 7.25565 | 0.495888 | 0.163077 | 0.455385 | 0.326154 | 0.738462 |  | 179 | poor_pd_location:158;target_rr_below_3:41;target_rr_below_2:13 |
| filtered_model | breaker_block | 50 | model_rules | 39 | 24 | 14 | 6 | 92.0 | 12.692658 | 8.110042 | 5.517652 | 2.002816 | 0.25 | 0.333333 | 0.333333 | 0.291667 |  | 24 | insufficient_displacement:24;poor_pd_location:13;target_rr_below_3:8 |
| filtered_model | ict2022_mss_fvg | 50 | model_rules | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| filtered_model | ifvg_retest | 50 | model_rules | 61 | 19 | 18 |  | 100.0 | 20.641637 | 10.334024 | 8.250236 | 0.879075 | 0.210526 | 0.315789 | 0.315789 | 0.736842 |  |  |  |
| filtered_model | mitigation_block | 50 | model_rules | 193 | 4 | 4 |  | 97.5 | 1.107536 | 0.577855 | 2.0 | -1.0 |  |  |  | 1.0 |  | 4 | target_rr_below_3:4 |
| filtered_model | reclaimed_ob | 50 | model_rules | 11 | 6 | 5 | 1 | 91.666667 | 11.978287 | 11.612722 | 4.115627 | 2.248354 | 0.5 | 0.5 | 0.5 | 0.333333 |  | 4 | target_rr_below_3:4;poor_pd_location:2 |
| filtered_model | rejection_block | 50 | model_rules | 126 | 23 | 23 |  | 95.304348 | 4.570082 | 3.157619 | 4.511191 | 0.517406 | 0.26087 | 0.608696 | 0.478261 | 0.652174 |  | 6 | target_rr_below_3:6 |
| filtered_model | silver_bullet | 50 | model_rules | 10 | 5 | 5 |  | 98.0 | 0.868201 | 0.794534 | 2.0 | 0.082955 |  | 0.2 |  | 0.4 |  | 5 | target_rr_below_3:5 |
| filtered_model | turtle_soup | 50 | model_rules | 77 | 248 | 248 |  | 72.439516 | 5.615544 | 3.826065 | 8.377076 | 0.723186 | 0.141129 | 0.471774 | 0.350806 | 0.737903 |  | 125 | poor_pd_location:125 |
| model | breaker_block | 70 | none |  | 59 | 35 | 20 | 82.847458 | 13.672103 | 8.190713 | 2.720512 | 0.990479 | 0.338983 | 0.372881 | 0.372881 | 0.237288 |  | 59 | insufficient_displacement:59;poor_pd_location:35;target_rr_below_2:35;target_rr_below_3:8 |
| model | ict2022_mss_fvg | 70 | none |  | 8 | 8 |  | 100.0 | 5.300305 | 2.498171 | 8.794929 | 4.449634 | 0.125 | 0.75 | 0.625 | 0.125 |  | 5 | poor_pd_location:5 |
| model | ifvg_retest | 70 | none |  | 80 | 79 |  | 97.6875 | 21.298202 | 11.227001 | 4.390243 | 0.059255 | 0.1875 | 0.25 | 0.225 | 0.8 |  | 61 | poor_pd_location:40;target_rr_below_2:34;target_rr_below_3:6 |
| model | mitigation_block | 70 | none |  | 186 | 186 |  | 77.946237 | 2.628378 | 1.484878 | 0.764695 | -0.315443 | 0.419355 | 0.258065 | 0.134409 | 0.575269 |  | 186 | target_rr_below_2:158;poor_pd_location:119;target_rr_below_3:26 |
| model | reclaimed_ob | 70 | none |  | 17 | 14 | 3 | 81.470588 | 10.115386 | 10.696303 | 1.918858 | 0.871072 | 0.529412 | 0.588235 | 0.411765 | 0.294118 |  | 15 | target_rr_below_2:11;poor_pd_location:10;target_rr_below_3:4 |
| model | rejection_block | 70 | none |  | 129 | 129 |  | 84.51938 | 5.85815 | 3.629402 | 2.226773 | 0.459761 | 0.534884 | 0.620155 | 0.317829 | 0.426357 |  | 112 | target_rr_below_2:79;poor_pd_location:57;target_rr_below_3:13 |
| model | silver_bullet | 70 | none |  | 15 | 15 |  | 88.0 | 1.340204 | 0.794534 | 2.0 | -0.156179 | 0.133333 | 0.266667 | 0.133333 | 0.6 |  | 15 | target_rr_below_3:15;poor_pd_location:10 |
| model | turtle_soup | 70 | none |  | 153 | 153 |  | 78.039216 | 4.471567 | 2.230167 | 9.710275 | 0.194724 | 0.065359 | 0.392157 | 0.254902 | 0.823529 |  | 7 | target_rr_below_3:7 |
| filtered_model | breaker_block | 70 | model_rules | 35 | 24 | 14 | 6 | 92.0 | 12.692658 | 8.110042 | 5.517652 | 2.002816 | 0.25 | 0.333333 | 0.333333 | 0.291667 |  | 24 | insufficient_displacement:24;poor_pd_location:13;target_rr_below_3:8 |
| filtered_model | ict2022_mss_fvg | 70 | model_rules | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| filtered_model | ifvg_retest | 70 | model_rules | 61 | 19 | 18 |  | 100.0 | 20.641637 | 10.334024 | 8.250236 | 0.879075 | 0.210526 | 0.315789 | 0.315789 | 0.736842 |  |  |  |
| filtered_model | mitigation_block | 70 | model_rules | 182 | 4 | 4 |  | 97.5 | 1.107536 | 0.577855 | 2.0 | -1.0 |  |  |  | 1.0 |  | 4 | target_rr_below_3:4 |
| filtered_model | reclaimed_ob | 70 | model_rules | 11 | 6 | 5 | 1 | 91.666667 | 11.978287 | 11.612722 | 4.115627 | 2.248354 | 0.5 | 0.5 | 0.5 | 0.333333 |  | 4 | target_rr_below_3:4;poor_pd_location:2 |
| filtered_model | rejection_block | 70 | model_rules | 106 | 23 | 23 |  | 95.304348 | 4.570082 | 3.157619 | 4.511191 | 0.517406 | 0.26087 | 0.608696 | 0.478261 | 0.652174 |  | 6 | target_rr_below_3:6 |
| filtered_model | silver_bullet | 70 | model_rules | 10 | 5 | 5 |  | 98.0 | 0.868201 | 0.794534 | 2.0 | 0.082955 |  | 0.2 |  | 0.4 |  | 5 | target_rr_below_3:5 |
| filtered_model | turtle_soup | 70 | model_rules | 30 | 123 | 123 |  | 80.0 | 5.158748 | 2.803523 | 10.604099 | 0.433887 | 0.065041 | 0.414634 | 0.276423 | 0.796748 |  |  |  |
