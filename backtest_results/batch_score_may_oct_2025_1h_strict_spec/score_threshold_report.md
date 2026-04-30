# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_oct_2025_1h_strict_spec\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 117 | 115 | 1 | 91.931624 | 7.57703 | 4.012932 | 5.090434 | 0.309998 | 0.452991 | 0.598291 | 0.376068 | 0.521368 |  | 83 | target_rr_below_2:50;target_rr_below_3:33 |
| filtered_all | ALL | 0 | model_rules | 53 | 64 | 63 |  | 96.328125 | 9.478536 | 4.070896 | 8.458078 | 0.352977 | 0.3125 | 0.625 | 0.46875 | 0.671875 |  | 30 | target_rr_below_3:30 |
| all | ALL | 50 | none |  | 117 | 115 | 1 | 91.931624 | 7.57703 | 4.012932 | 5.090434 | 0.309998 | 0.452991 | 0.598291 | 0.376068 | 0.521368 |  | 83 | target_rr_below_2:50;target_rr_below_3:33 |
| filtered_all | ALL | 50 | model_rules | 53 | 64 | 63 |  | 96.328125 | 9.478536 | 4.070896 | 8.458078 | 0.352977 | 0.3125 | 0.625 | 0.46875 | 0.671875 |  | 30 | target_rr_below_3:30 |
| all | ALL | 70 | none |  | 117 | 115 | 1 | 91.931624 | 7.57703 | 4.012932 | 5.090434 | 0.309998 | 0.452991 | 0.598291 | 0.376068 | 0.521368 |  | 83 | target_rr_below_2:50;target_rr_below_3:33 |
| filtered_all | ALL | 70 | model_rules | 53 | 64 | 63 |  | 96.328125 | 9.478536 | 4.070896 | 8.458078 | 0.352977 | 0.3125 | 0.625 | 0.46875 | 0.671875 |  | 30 | target_rr_below_3:30 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 21 | 20 |  | 98.952381 | 15.215602 | 10.539107 | 6.654852 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 |  | 10 | target_rr_below_2:7;target_rr_below_3:3 |
| model | reclaimed_ob | 0 | none |  | 9 | 8 | 1 | 87.444444 | 19.508529 | 5.801969 | 25.888825 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 |  | 5 | target_rr_below_2:5 |
| model | rejection_block | 0 | none |  | 87 | 87 |  | 90.701149 | 4.723887 | 2.891235 | 2.561259 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_model | ifvg_retest | 0 | model_rules | 10 | 11 | 10 |  | 100.0 | 22.036961 | 11.737836 | 11.547798 | 0.495703 | 0.272727 | 0.454545 | 0.454545 | 0.636364 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 5 | 4 | 4 |  | 98.5 | 31.282771 | 3.393763 | 56.945436 | 1.612486 | 0.25 | 0.75 | 0.75 | 0.75 |  |  |  |
| filtered_model | rejection_block | 0 | model_rules | 38 | 49 | 49 |  | 95.326531 | 5.135655 | 3.026662 | 3.806315 | 0.221032 | 0.326531 | 0.653061 | 0.44898 | 0.673469 |  | 30 | target_rr_below_3:30 |
| model | ifvg_retest | 50 | none |  | 21 | 20 |  | 98.952381 | 15.215602 | 10.539107 | 6.654852 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 |  | 10 | target_rr_below_2:7;target_rr_below_3:3 |
| model | reclaimed_ob | 50 | none |  | 9 | 8 | 1 | 87.444444 | 19.508529 | 5.801969 | 25.888825 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 |  | 5 | target_rr_below_2:5 |
| model | rejection_block | 50 | none |  | 87 | 87 |  | 90.701149 | 4.723887 | 2.891235 | 2.561259 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_model | ifvg_retest | 50 | model_rules | 10 | 11 | 10 |  | 100.0 | 22.036961 | 11.737836 | 11.547798 | 0.495703 | 0.272727 | 0.454545 | 0.454545 | 0.636364 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 5 | 4 | 4 |  | 98.5 | 31.282771 | 3.393763 | 56.945436 | 1.612486 | 0.25 | 0.75 | 0.75 | 0.75 |  |  |  |
| filtered_model | rejection_block | 50 | model_rules | 38 | 49 | 49 |  | 95.326531 | 5.135655 | 3.026662 | 3.806315 | 0.221032 | 0.326531 | 0.653061 | 0.44898 | 0.673469 |  | 30 | target_rr_below_3:30 |
| model | ifvg_retest | 70 | none |  | 21 | 20 |  | 98.952381 | 15.215602 | 10.539107 | 6.654852 | 0.065078 | 0.285714 | 0.333333 | 0.333333 | 0.666667 |  | 10 | target_rr_below_2:7;target_rr_below_3:3 |
| model | reclaimed_ob | 70 | none |  | 9 | 8 | 1 | 87.444444 | 19.508529 | 5.801969 | 25.888825 | 1.30792 | 0.555556 | 0.777778 | 0.777778 | 0.333333 |  | 5 | target_rr_below_2:5 |
| model | rejection_block | 70 | none |  | 87 | 87 |  | 90.701149 | 4.723887 | 2.891235 | 2.561259 | 0.274539 | 0.482759 | 0.643678 | 0.344828 | 0.505747 |  | 68 | target_rr_below_2:38;target_rr_below_3:30 |
| filtered_model | ifvg_retest | 70 | model_rules | 10 | 11 | 10 |  | 100.0 | 22.036961 | 11.737836 | 11.547798 | 0.495703 | 0.272727 | 0.454545 | 0.454545 | 0.636364 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 5 | 4 | 4 |  | 98.5 | 31.282771 | 3.393763 | 56.945436 | 1.612486 | 0.25 | 0.75 | 0.75 | 0.75 |  |  |  |
| filtered_model | rejection_block | 70 | model_rules | 38 | 49 | 49 |  | 95.326531 | 5.135655 | 3.026662 | 3.806315 | 0.221032 | 0.326531 | 0.653061 | 0.44898 | 0.673469 |  | 30 | target_rr_below_3:30 |
