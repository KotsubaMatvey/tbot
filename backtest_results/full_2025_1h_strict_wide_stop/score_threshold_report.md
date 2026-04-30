# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_1h_strict_wide_stop\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 119 | 106 | 1 | 96.285714 | 6.583829 | 2.891235 | 5.488715 | 0.22426 | 0.294118 | 0.428571 | 0.310924 | 0.571429 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_all | ALL | 0 | model_rules | 41 | 78 | 68 |  | 98.679487 | 7.67642 | 2.90636 | 7.754581 | 0.328982 | 0.205128 | 0.435897 | 0.346154 | 0.628205 |  | 27 | target_rr_below_3:27 |
| all | ALL | 50 | none |  | 119 | 106 | 1 | 96.285714 | 6.583829 | 2.891235 | 5.488715 | 0.22426 | 0.294118 | 0.428571 | 0.310924 | 0.571429 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_all | ALL | 50 | model_rules | 41 | 78 | 68 |  | 98.679487 | 7.67642 | 2.90636 | 7.754581 | 0.328982 | 0.205128 | 0.435897 | 0.346154 | 0.628205 |  | 27 | target_rr_below_3:27 |
| all | ALL | 70 | none |  | 119 | 106 | 1 | 96.285714 | 6.583829 | 2.891235 | 5.488715 | 0.22426 | 0.294118 | 0.428571 | 0.310924 | 0.571429 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_all | ALL | 70 | model_rules | 41 | 78 | 68 |  | 98.679487 | 7.67642 | 2.90636 | 7.754581 | 0.328982 | 0.205128 | 0.435897 | 0.346154 | 0.628205 |  | 27 | target_rr_below_3:27 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 0 | none |  | 10 | 5 | 1 | 93.6 | 15.033828 | 1.911688 | 13.857714 | 0.857595 | 0.3 | 0.3 | 0.2 | 0.2 |  | 5 | target_rr_below_2:4;target_rr_below_3:1 |
| model | rejection_block | 0 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 0 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 4 | 6 | 3 |  | 98.166667 | 23.647793 | 1.911688 | 22.756932 | 1.173422 | 0.166667 | 0.333333 | 0.166667 | 0.333333 |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 0 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.421195 | 0.254237 | 0.525424 | 0.423729 | 0.694915 |  | 26 | target_rr_below_3:26 |
| model | ifvg_retest | 50 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 50 | none |  | 10 | 5 | 1 | 93.6 | 15.033828 | 1.911688 | 13.857714 | 0.857595 | 0.3 | 0.3 | 0.2 | 0.2 |  | 5 | target_rr_below_2:4;target_rr_below_3:1 |
| model | rejection_block | 50 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 50 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 4 | 6 | 3 |  | 98.166667 | 23.647793 | 1.911688 | 22.756932 | 1.173422 | 0.166667 | 0.333333 | 0.166667 | 0.333333 |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 50 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.421195 | 0.254237 | 0.525424 | 0.423729 | 0.694915 |  | 26 | target_rr_below_3:26 |
| model | ifvg_retest | 70 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 70 | none |  | 10 | 5 | 1 | 93.6 | 15.033828 | 1.911688 | 13.857714 | 0.857595 | 0.3 | 0.3 | 0.2 | 0.2 |  | 5 | target_rr_below_2:4;target_rr_below_3:1 |
| model | rejection_block | 70 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.292209 | 0.333333 | 0.505747 | 0.356322 | 0.632184 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 70 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 4 | 6 | 3 |  | 98.166667 | 23.647793 | 1.911688 | 22.756932 | 1.173422 | 0.166667 | 0.333333 | 0.166667 | 0.333333 |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 70 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.421195 | 0.254237 | 0.525424 | 0.423729 | 0.694915 |  | 26 | target_rr_below_3:26 |
