# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_30m_btc_strict_wide_stop\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 124 | 90 | 1 | 93.516129 | 7.026556 | 2.775737 | 3.014842 | -0.233452 | 0.201613 | 0.290323 | 0.120968 | 0.516129 |  | 91 | target_rr_below_2:62;target_rr_below_3:29 |
| filtered_all | ALL | 0 | model_rules | 69 | 55 | 40 |  | 97.854545 | 8.133883 | 2.672152 | 5.308511 | -0.228279 | 0.127273 | 0.309091 | 0.163636 | 0.581818 |  | 22 | target_rr_below_3:22 |
| all | ALL | 50 | none |  | 124 | 90 | 1 | 93.516129 | 7.026556 | 2.775737 | 3.014842 | -0.233452 | 0.201613 | 0.290323 | 0.120968 | 0.516129 |  | 91 | target_rr_below_2:62;target_rr_below_3:29 |
| filtered_all | ALL | 50 | model_rules | 69 | 55 | 40 |  | 97.854545 | 8.133883 | 2.672152 | 5.308511 | -0.228279 | 0.127273 | 0.309091 | 0.163636 | 0.581818 |  | 22 | target_rr_below_3:22 |
| all | ALL | 70 | none |  | 124 | 90 | 1 | 93.516129 | 7.026556 | 2.775737 | 3.014842 | -0.233452 | 0.201613 | 0.290323 | 0.120968 | 0.516129 |  | 91 | target_rr_below_2:62;target_rr_below_3:29 |
| filtered_all | ALL | 70 | model_rules | 69 | 55 | 40 |  | 97.854545 | 8.133883 | 2.672152 | 5.308511 | -0.228279 | 0.127273 | 0.309091 | 0.163636 | 0.581818 |  | 22 | target_rr_below_3:22 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 0 | none |  | 16 | 3 | 1 | 92.0 | 1.209708 | 1.324589 | 6.13252 | -0.631516 | 0.0625 | 0.125 |  | 0.125 |  | 11 | target_rr_below_2:6;target_rr_below_3:5 |
| model | rejection_block | 0 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 0 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 6 | 10 | 2 |  | 97.0 | 1.620801 | 1.620801 | 9.531132 | -1.0 |  | 0.2 |  | 0.2 |  | 5 | target_rr_below_3:5 |
| filtered_model | rejection_block | 0 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
| model | ifvg_retest | 50 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 50 | none |  | 16 | 3 | 1 | 92.0 | 1.209708 | 1.324589 | 6.13252 | -0.631516 | 0.0625 | 0.125 |  | 0.125 |  | 11 | target_rr_below_2:6;target_rr_below_3:5 |
| model | rejection_block | 50 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 50 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 6 | 10 | 2 |  | 97.0 | 1.620801 | 1.620801 | 9.531132 | -1.0 |  | 0.2 |  | 0.2 |  | 5 | target_rr_below_3:5 |
| filtered_model | rejection_block | 50 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
| model | ifvg_retest | 70 | none |  | 37 | 16 |  | 100.0 | 23.110541 | 9.828739 | 3.309464 | 0.00499 | 0.108108 | 0.108108 | 0.081081 | 0.324324 |  | 22 | target_rr_below_2:15;target_rr_below_3:7 |
| model | reclaimed_ob | 70 | none |  | 16 | 3 | 1 | 92.0 | 1.209708 | 1.324589 | 6.13252 | -0.631516 | 0.0625 | 0.125 |  | 0.125 |  | 11 | target_rr_below_2:6;target_rr_below_3:5 |
| model | rejection_block | 70 | none |  | 71 | 71 |  | 90.478873 | 3.647778 | 2.406238 | 2.158731 | -0.270366 | 0.28169 | 0.422535 | 0.169014 | 0.704225 |  | 58 | target_rr_below_2:41;target_rr_below_3:17 |
| filtered_model | ifvg_retest | 70 | model_rules | 22 | 15 | 8 |  | 100.0 | 25.779931 | 8.843601 | 5.822999 | 0.306545 | 0.133333 | 0.133333 | 0.133333 | 0.4 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 6 | 10 | 2 |  | 97.0 | 1.620801 | 1.620801 | 9.531132 | -1.0 |  | 0.2 |  | 0.2 |  | 5 | target_rr_below_3:5 |
| filtered_model | rejection_block | 70 | model_rules | 41 | 30 | 30 |  | 97.066667 | 3.862476 | 2.317935 | 3.643726 | -0.31945 | 0.166667 | 0.433333 | 0.233333 | 0.8 |  | 17 | target_rr_below_3:17 |
