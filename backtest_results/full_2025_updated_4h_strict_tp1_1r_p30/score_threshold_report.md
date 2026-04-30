# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_updated_4h_strict_tp1_1r_p30\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 49 | 33 |  | 94.428571 | 5.35022 | 2.038557 | 2.410096 | 0.309496 | 0.307646 | 0.307646 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 35 | target_rr_below_2:33;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 33 | 16 | 9 |  | 98.875 | 8.163376 | 7.250988 | 5.478067 | 1.668128 | 1.212134 | 1.212134 | 0.1875 | 0.25 | 0.25 | 0.375 |  | 2 | target_rr_below_3:2 |
| all | ALL | 50 | none |  | 49 | 33 |  | 94.428571 | 5.35022 | 2.038557 | 2.410096 | 0.309496 | 0.307646 | 0.307646 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 35 | target_rr_below_2:33;target_rr_below_3:2 |
| filtered_all | ALL | 50 | model_rules | 33 | 16 | 9 |  | 98.875 | 8.163376 | 7.250988 | 5.478067 | 1.668128 | 1.212134 | 1.212134 | 0.1875 | 0.25 | 0.25 | 0.375 |  | 2 | target_rr_below_3:2 |
| all | ALL | 70 | none |  | 49 | 33 |  | 94.428571 | 5.35022 | 2.038557 | 2.410096 | 0.309496 | 0.307646 | 0.307646 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 35 | target_rr_below_2:33;target_rr_below_3:2 |
| filtered_all | ALL | 70 | model_rules | 33 | 16 | 9 |  | 98.875 | 8.163376 | 7.250988 | 5.478067 | 1.668128 | 1.212134 | 1.212134 | 0.1875 | 0.25 | 0.25 | 0.375 |  | 2 | target_rr_below_3:2 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 0 | none |  | 9 | 3 |  | 92.111111 | 19.940528 | 15.879401 | 2.418917 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 6 | target_rr_below_2:6 |
| model | rejection_block | 0 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 0 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 5.73094 | 5.73094 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 6 | 3 |  |  | 100.0 |  |  | 5.607857 |  |  |  |  |  |  |  |  |  |  |
| filtered_model | rejection_block | 0 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | -0.078954 | -0.078954 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 50 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 50 | none |  | 9 | 3 |  | 92.111111 | 19.940528 | 15.879401 | 2.418917 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 6 | target_rr_below_2:6 |
| model | rejection_block | 50 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 50 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 5.73094 | 5.73094 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 6 | 3 |  |  | 100.0 |  |  | 5.607857 |  |  |  |  |  |  |  |  |  |  |
| filtered_model | rejection_block | 50 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | -0.078954 | -0.078954 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 70 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 2.273349 | 2.273349 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 70 | none |  | 9 | 3 |  | 92.111111 | 19.940528 | 15.879401 | 2.418917 | 0.248319 | 0.273823 | 0.273823 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 6 | target_rr_below_2:6 |
| model | rejection_block | 70 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | -0.081435 | -0.081435 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 70 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 5.73094 | 5.73094 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 6 | 3 |  |  | 100.0 |  |  | 5.607857 |  |  |  |  |  |  |  |  |  |  |
| filtered_model | rejection_block | 70 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | -0.078954 | -0.078954 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
