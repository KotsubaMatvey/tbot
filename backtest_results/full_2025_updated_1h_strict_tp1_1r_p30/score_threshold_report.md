# ICT Decision Score Threshold Report

- events: `backtest_results\full_2025_updated_1h_strict_tp1_1r_p30\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 119 | 106 | 1 | 96.327731 | 7.097198 | 2.891235 | 6.516928 | 0.116458 | 0.156159 | 0.156159 | 0.277311 | 0.428571 | 0.310924 | 0.596639 |  | 67 | target_rr_below_2:38;target_rr_below_3:29 |
| filtered_all | ALL | 0 | model_rules | 41 | 78 | 68 |  | 98.74359 | 8.427936 | 3.018402 | 9.300685 | 0.18793 | 0.228446 | 0.228446 | 0.192308 | 0.435897 | 0.346154 | 0.653846 |  | 26 | target_rr_below_3:26 |
| all | ALL | 50 | none |  | 119 | 106 | 1 | 96.327731 | 7.097198 | 2.891235 | 6.516928 | 0.116458 | 0.156159 | 0.156159 | 0.277311 | 0.428571 | 0.310924 | 0.596639 |  | 67 | target_rr_below_2:38;target_rr_below_3:29 |
| filtered_all | ALL | 50 | model_rules | 41 | 78 | 68 |  | 98.74359 | 8.427936 | 3.018402 | 9.300685 | 0.18793 | 0.228446 | 0.228446 | 0.192308 | 0.435897 | 0.346154 | 0.653846 |  | 26 | target_rr_below_3:26 |
| all | ALL | 70 | none |  | 119 | 106 | 1 | 96.327731 | 7.097198 | 2.891235 | 6.516928 | 0.116458 | 0.156159 | 0.156159 | 0.277311 | 0.428571 | 0.310924 | 0.596639 |  | 67 | target_rr_below_2:38;target_rr_below_3:29 |
| filtered_all | ALL | 70 | model_rules | 41 | 78 | 68 |  | 98.74359 | 8.427936 | 3.018402 | 9.300685 | 0.18793 | 0.228446 | 0.228446 | 0.192308 | 0.435897 | 0.346154 | 0.653846 |  | 26 | target_rr_below_3:26 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 0 | none |  | 10 | 5 | 1 | 94.1 | 25.917253 | 3.70286 | 26.093456 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 |  | 4 | target_rr_below_2:4 |
| model | rejection_block | 0 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 0 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 | -0.783333 | -0.783333 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 4 | 6 | 3 |  | 99.0 | 40.68214 | 3.70286 | 42.856281 | -1.0 | -0.133333 | -0.133333 |  | 0.333333 | 0.333333 | 0.5 |  |  |  |
| filtered_model | rejection_block | 0 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.369139 | 0.349734 | 0.349734 | 0.254237 | 0.525424 | 0.40678 | 0.711864 |  | 26 | target_rr_below_3:26 |
| model | ifvg_retest | 50 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 50 | none |  | 10 | 5 | 1 | 94.1 | 25.917253 | 3.70286 | 26.093456 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 |  | 4 | target_rr_below_2:4 |
| model | rejection_block | 50 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 50 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 | -0.783333 | -0.783333 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 4 | 6 | 3 |  | 99.0 | 40.68214 | 3.70286 | 42.856281 | -1.0 | -0.133333 | -0.133333 |  | 0.333333 | 0.333333 | 0.5 |  |  |  |
| filtered_model | rejection_block | 50 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.369139 | 0.349734 | 0.349734 | 0.254237 | 0.525424 | 0.40678 | 0.711864 |  | 26 | target_rr_below_3:26 |
| model | ifvg_retest | 70 | none |  | 22 | 14 |  | 100.0 | 14.529968 | 7.089148 | 10.704277 | -0.424187 | -0.302289 | -0.302289 | 0.136364 | 0.181818 | 0.181818 | 0.5 |  | 9 | target_rr_below_2:6;target_rr_below_3:3 |
| model | reclaimed_ob | 70 | none |  | 10 | 5 | 1 | 94.1 | 25.917253 | 3.70286 | 26.093456 | -0.326239 | 0.181805 | 0.181805 | 0.2 | 0.3 | 0.3 | 0.3 |  | 4 | target_rr_below_2:4 |
| model | rejection_block | 70 | none |  | 87 | 87 |  | 95.655172 | 4.819507 | 2.534978 | 3.207883 | 0.228901 | 0.228458 | 0.228458 | 0.321839 | 0.505747 | 0.344828 | 0.655172 |  | 54 | target_rr_below_2:28;target_rr_below_3:26 |
| filtered_model | ifvg_retest | 70 | model_rules | 9 | 13 | 6 |  | 100.0 | 20.563278 | 4.723579 | 17.027452 | -1.0 | -0.783333 | -0.783333 |  | 0.076923 | 0.076923 | 0.461538 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 4 | 6 | 3 |  | 99.0 | 40.68214 | 3.70286 | 42.856281 | -1.0 | -0.133333 | -0.133333 |  | 0.333333 | 0.333333 | 0.5 |  |  |  |
| filtered_model | rejection_block | 70 | model_rules | 28 | 59 | 59 |  | 98.440678 | 5.553789 | 2.891235 | 4.185744 | 0.369139 | 0.349734 | 0.349734 | 0.254237 | 0.525424 | 0.40678 | 0.711864 |  | 26 | target_rr_below_3:26 |
