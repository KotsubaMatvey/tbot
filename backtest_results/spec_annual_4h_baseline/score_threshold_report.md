# ICT Decision Score Threshold Report

- events: `backtest_results\spec_annual_4h_baseline\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 74 | 21 |  | 96.810811 | 4.108468 | 0.923018 | 15.108066 | -0.196404 | -0.156077 | -0.156077 | 0.040541 | 0.081081 | 0.040541 | 0.22973 |  | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 70 | 4 | 2 |  | 94.25 | 26.202172 | 26.202172 | 5.351396 | 6.153123 | 3.576562 | 3.576562 | 0.5 | 0.5 | 0.5 |  |  | 1 | target_rr_below_2:1 |
| all | ALL | 70 | none |  | 74 | 21 |  | 96.810811 | 4.108468 | 0.923018 | 15.108066 | -0.196404 | -0.156077 | -0.156077 | 0.040541 | 0.081081 | 0.040541 | 0.22973 |  | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 70 | model_rules | 70 | 4 | 2 |  | 94.25 | 26.202172 | 26.202172 | 5.351396 | 6.153123 | 3.576562 | 3.576562 | 0.5 | 0.5 | 0.5 |  |  | 1 | target_rr_below_2:1 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 1 |  |  | 100.0 |  |  | 4.395491 |  |  |  |  |  |  |  |  |  |  |
| model | reclaimed_ob | 0 | none |  | 9 | 3 |  | 97.111111 | 19.940528 | 15.879401 | 8.656466 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 3 | target_rr_below_2:3 |
| model | rejection_block | 0 | none |  | 64 | 18 |  | 96.71875 | 1.469791 | 0.79004 | 16.182707 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 |  | 15 | target_rr_below_2:13;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 0 | model_rules | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 5 | 4 | 2 |  | 94.25 | 26.202172 | 26.202172 | 5.351396 | 6.153123 | 3.576562 | 3.576562 | 0.5 | 0.5 | 0.5 |  |  | 1 | target_rr_below_2:1 |
| filtered_model | rejection_block | 0 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | ifvg_retest | 70 | none |  | 1 |  |  | 100.0 |  |  | 4.395491 |  |  |  |  |  |  |  |  |  |  |
| model | reclaimed_ob | 70 | none |  | 9 | 3 |  | 97.111111 | 19.940528 | 15.879401 | 8.656466 | 3.768749 | 2.051041 | 2.051041 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 3 | target_rr_below_2:3 |
| model | rejection_block | 70 | none |  | 64 | 18 |  | 96.71875 | 1.469791 | 0.79004 | 16.182707 | -0.857263 | -0.52393 | -0.52393 | 0.015625 | 0.0625 | 0.015625 | 0.25 |  | 15 | target_rr_below_2:13;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 70 | model_rules | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 5 | 4 | 2 |  | 94.25 | 26.202172 | 26.202172 | 5.351396 | 6.153123 | 3.576562 | 3.576562 | 0.5 | 0.5 | 0.5 |  |  | 1 | target_rr_below_2:1 |
| filtered_model | rejection_block | 70 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
