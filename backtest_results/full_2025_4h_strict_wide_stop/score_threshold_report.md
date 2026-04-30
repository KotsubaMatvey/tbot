# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_4h_strict_wide_stop\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 49 | 33 |  | 94.020408 | 4.507062 | 2.038557 | 2.199743 | 0.284706 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 37 | target_rr_below_2:34;target_rr_below_3:3 |
| filtered_all | ALL | 0 | model_rules | 34 | 15 | 9 |  | 98.466667 | 8.163376 | 7.250988 | 5.206093 | 1.668128 | 0.2 | 0.266667 | 0.266667 | 0.4 |  | 3 | target_rr_below_3:3 |
| all | ALL | 50 | none |  | 49 | 33 |  | 94.020408 | 4.507062 | 2.038557 | 2.199743 | 0.284706 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 37 | target_rr_below_2:34;target_rr_below_3:3 |
| filtered_all | ALL | 50 | model_rules | 34 | 15 | 9 |  | 98.466667 | 8.163376 | 7.250988 | 5.206093 | 1.668128 | 0.2 | 0.266667 | 0.266667 | 0.4 |  | 3 | target_rr_below_3:3 |
| all | ALL | 70 | none |  | 49 | 33 |  | 94.020408 | 4.507062 | 2.038557 | 2.199743 | 0.284706 | 0.285714 | 0.265306 | 0.163265 | 0.387755 |  | 37 | target_rr_below_2:34;target_rr_below_3:3 |
| filtered_all | ALL | 70 | model_rules | 34 | 15 | 9 |  | 98.466667 | 8.163376 | 7.250988 | 5.206093 | 1.668128 | 0.2 | 0.266667 | 0.266667 | 0.4 |  | 3 | target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 0 | none |  | 9 | 3 |  | 89.888889 | 10.665788 | 8.457824 | 1.273663 | -0.024379 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 8 | target_rr_below_2:7;target_rr_below_3:1 |
| model | rejection_block | 0 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 0 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 7 | 2 |  |  | 97.5 |  |  | 3.632947 |  |  |  |  |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 0 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 50 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 50 | none |  | 9 | 3 |  | 89.888889 | 10.665788 | 8.457824 | 1.273663 | -0.024379 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 8 | target_rr_below_2:7;target_rr_below_3:1 |
| model | rejection_block | 50 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 50 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 7 | 2 |  |  | 97.5 |  |  | 3.632947 |  |  |  |  |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 50 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 70 | none |  | 15 | 5 |  | 99.466667 | 8.982657 | 2.038557 | 2.942714 | 2.790499 | 0.2 | 0.266667 | 0.133333 | 0.133333 |  | 9 | target_rr_below_2:9 |
| model | reclaimed_ob | 70 | none |  | 9 | 3 |  | 89.888889 | 10.665788 | 8.457824 | 1.273663 | -0.024379 | 0.222222 | 0.222222 | 0.222222 | 0.111111 |  | 8 | target_rr_below_2:7;target_rr_below_3:1 |
| model | rejection_block | 70 | none |  | 25 | 25 |  | 92.24 | 2.872896 | 1.357874 | 2.087349 | -0.179363 | 0.36 | 0.28 | 0.16 | 0.64 |  | 20 | target_rr_below_2:18;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 70 | model_rules | 9 | 6 | 2 |  | 100.0 | 20.54824 | 20.54824 | 6.126871 | 7.758486 | 0.333333 | 0.333333 | 0.333333 |  |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 7 | 2 |  |  | 97.5 |  |  | 3.632947 |  |  |  |  |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 70 | model_rules | 18 | 7 | 7 |  | 97.428571 | 4.624843 | 2.922539 | 4.866326 | -0.071975 | 0.142857 | 0.285714 | 0.285714 | 0.857143 |  | 2 | target_rr_below_3:2 |
