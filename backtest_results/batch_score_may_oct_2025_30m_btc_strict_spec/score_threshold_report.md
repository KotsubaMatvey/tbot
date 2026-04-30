# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_oct_2025_30m_btc_strict_spec\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 55 | 53 | 2 | 94.327273 | 8.790077 | 5.182974 | 3.402272 | 0.133262 | 0.381818 | 0.436364 | 0.327273 | 0.563636 |  | 38 | target_rr_below_2:30;target_rr_below_3:8 |
| filtered_all | ALL | 0 | model_rules | 33 | 22 | 21 | 1 | 98.863636 | 7.844507 | 6.496171 | 6.789606 | 0.132346 | 0.227273 | 0.454545 | 0.409091 | 0.681818 |  | 5 | target_rr_below_3:5 |
| all | ALL | 50 | none |  | 55 | 53 | 2 | 94.327273 | 8.790077 | 5.182974 | 3.402272 | 0.133262 | 0.381818 | 0.436364 | 0.327273 | 0.563636 |  | 38 | target_rr_below_2:30;target_rr_below_3:8 |
| filtered_all | ALL | 50 | model_rules | 33 | 22 | 21 | 1 | 98.863636 | 7.844507 | 6.496171 | 6.789606 | 0.132346 | 0.227273 | 0.454545 | 0.409091 | 0.681818 |  | 5 | target_rr_below_3:5 |
| all | ALL | 70 | none |  | 55 | 53 | 2 | 94.327273 | 8.790077 | 5.182974 | 3.402272 | 0.133262 | 0.381818 | 0.436364 | 0.327273 | 0.563636 |  | 38 | target_rr_below_2:30;target_rr_below_3:8 |
| filtered_all | ALL | 70 | model_rules | 33 | 22 | 21 | 1 | 98.863636 | 7.844507 | 6.496171 | 6.789606 | 0.132346 | 0.227273 | 0.454545 | 0.409091 | 0.681818 |  | 5 | target_rr_below_3:5 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 17 | 17 |  | 100.0 | 15.22715 | 9.193407 | 3.197427 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 |  | 11 | target_rr_below_2:8;target_rr_below_3:3 |
| model | reclaimed_ob | 0 | none |  | 10 | 8 | 2 | 94.0 | 8.871101 | 7.701916 | 7.175258 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 |  | 6 | target_rr_below_3:3;target_rr_below_2:3 |
| model | rejection_block | 0 | none |  | 28 | 28 |  | 91.0 | 4.858705 | 3.238299 | 2.179148 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 |  | 21 | target_rr_below_2:19;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 0 | model_rules | 11 | 6 | 6 |  | 100.0 | 11.484027 | 8.843601 | 6.315378 | 0.046112 | 0.166667 | 0.333333 | 0.333333 | 0.833333 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 3 | 7 | 6 | 1 | 97.857143 | 8.883027 | 7.701916 | 9.951567 | 0.238425 | 0.285714 | 0.571429 | 0.571429 | 0.571429 |  | 3 | target_rr_below_3:3 |
| filtered_model | rejection_block | 0 | model_rules | 19 | 9 | 9 |  | 98.888889 | 4.725813 | 2.652439 | 4.646456 | 0.119116 | 0.222222 | 0.444444 | 0.333333 | 0.666667 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 50 | none |  | 17 | 17 |  | 100.0 | 15.22715 | 9.193407 | 3.197427 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 |  | 11 | target_rr_below_2:8;target_rr_below_3:3 |
| model | reclaimed_ob | 50 | none |  | 10 | 8 | 2 | 94.0 | 8.871101 | 7.701916 | 7.175258 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 |  | 6 | target_rr_below_3:3;target_rr_below_2:3 |
| model | rejection_block | 50 | none |  | 28 | 28 |  | 91.0 | 4.858705 | 3.238299 | 2.179148 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 |  | 21 | target_rr_below_2:19;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 50 | model_rules | 11 | 6 | 6 |  | 100.0 | 11.484027 | 8.843601 | 6.315378 | 0.046112 | 0.166667 | 0.333333 | 0.333333 | 0.833333 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 3 | 7 | 6 | 1 | 97.857143 | 8.883027 | 7.701916 | 9.951567 | 0.238425 | 0.285714 | 0.571429 | 0.571429 | 0.571429 |  | 3 | target_rr_below_3:3 |
| filtered_model | rejection_block | 50 | model_rules | 19 | 9 | 9 |  | 98.888889 | 4.725813 | 2.652439 | 4.646456 | 0.119116 | 0.222222 | 0.444444 | 0.333333 | 0.666667 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 70 | none |  | 17 | 17 |  | 100.0 | 15.22715 | 9.193407 | 3.197427 | 0.034228 | 0.294118 | 0.411765 | 0.352941 | 0.705882 |  | 11 | target_rr_below_2:8;target_rr_below_3:3 |
| model | reclaimed_ob | 70 | none |  | 10 | 8 | 2 | 94.0 | 8.871101 | 7.701916 | 7.175258 | 0.081085 | 0.3 | 0.5 | 0.4 | 0.5 |  | 6 | target_rr_below_3:3;target_rr_below_2:3 |
| model | rejection_block | 70 | none |  | 28 | 28 |  | 91.0 | 4.858705 | 3.238299 | 2.179148 | 0.208298 | 0.464286 | 0.428571 | 0.285714 | 0.5 |  | 21 | target_rr_below_2:19;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 70 | model_rules | 11 | 6 | 6 |  | 100.0 | 11.484027 | 8.843601 | 6.315378 | 0.046112 | 0.166667 | 0.333333 | 0.333333 | 0.833333 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 3 | 7 | 6 | 1 | 97.857143 | 8.883027 | 7.701916 | 9.951567 | 0.238425 | 0.285714 | 0.571429 | 0.571429 | 0.571429 |  | 3 | target_rr_below_3:3 |
| filtered_model | rejection_block | 70 | model_rules | 19 | 9 | 9 |  | 98.888889 | 4.725813 | 2.652439 | 4.646456 | 0.119116 | 0.222222 | 0.444444 | 0.333333 | 0.666667 |  | 2 | target_rr_below_3:2 |
