# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_30m_btc_strict_ce_mt\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 124 | 90 | 2 | 93.556452 | 7.056012 | 2.816983 | 3.505869 | -0.212402 | 0.201613 | 0.282258 | 0.129032 | 0.516129 |  | 90 | target_rr_below_2:62;target_rr_below_3:28 |
| filtered_all | ALL | 0 | model_rules | 69 | 55 | 40 | 1 | 97.945455 | 8.190999 | 2.856708 | 6.380422 | -0.153279 | 0.145455 | 0.290909 | 0.181818 | 0.563636 |  | 21 | target_rr_below_3:21 |
| all | ALL | 50 | none |  | 124 | 90 | 2 | 93.556452 | 7.056012 | 2.816983 | 3.505869 | -0.212402 | 0.201613 | 0.282258 | 0.129032 | 0.516129 |  | 90 | target_rr_below_2:62;target_rr_below_3:28 |
| filtered_all | ALL | 50 | model_rules | 69 | 55 | 40 | 1 | 97.945455 | 8.190999 | 2.856708 | 6.380422 | -0.153279 | 0.145455 | 0.290909 | 0.181818 | 0.563636 |  | 21 | target_rr_below_3:21 |
| all | ALL | 70 | none |  | 124 | 90 | 2 | 93.556452 | 7.056012 | 2.816983 | 3.505869 | -0.212402 | 0.201613 | 0.282258 | 0.129032 | 0.516129 |  | 90 | target_rr_below_2:62;target_rr_below_3:28 |
| filtered_all | ALL | 70 | model_rules | 69 | 55 | 40 | 1 | 97.945455 | 8.190999 | 2.856708 | 6.380422 | -0.153279 | 0.145455 | 0.290909 | 0.181818 | 0.563636 |  | 21 | target_rr_below_3:21 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 0 | none |  | 16 | 3 | 2 | 92.3125 | 2.093404 | 2.484971 | 9.93798 |  | 0.0625 | 0.0625 | 0.0625 | 0.125 |  | 10 | target_rr_below_2:6;target_rr_below_3:4 |
| model | rejection_block | 0 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 0 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 6 | 10 | 2 | 1 | 97.5 | 2.763118 | 2.763118 | 15.426643 | 0.5 | 0.1 | 0.1 | 0.1 | 0.1 |  | 4 | target_rr_below_3:4 |
| filtered_model | rejection_block | 0 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
| model | ifvg_retest | 50 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 50 | none |  | 16 | 3 | 2 | 92.3125 | 2.093404 | 2.484971 | 9.93798 |  | 0.0625 | 0.0625 | 0.0625 | 0.125 |  | 10 | target_rr_below_2:6;target_rr_below_3:4 |
| model | rejection_block | 50 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 50 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 6 | 10 | 2 | 1 | 97.5 | 2.763118 | 2.763118 | 15.426643 | 0.5 | 0.1 | 0.1 | 0.1 | 0.1 |  | 4 | target_rr_below_3:4 |
| filtered_model | rejection_block | 50 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
| model | ifvg_retest | 70 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 70 | none |  | 16 | 3 | 2 | 92.3125 | 2.093404 | 2.484971 | 9.93798 |  | 0.0625 | 0.0625 | 0.0625 | 0.125 |  | 10 | target_rr_below_2:6;target_rr_below_3:4 |
| model | rejection_block | 70 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 70 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 6 | 10 | 2 | 1 | 97.5 | 2.763118 | 2.763118 | 15.426643 | 0.5 | 0.1 | 0.1 | 0.1 | 0.1 |  | 4 | target_rr_below_3:4 |
| filtered_model | rejection_block | 70 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
