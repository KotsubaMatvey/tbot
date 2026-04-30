# ICT Decision Score Threshold Report

- events: `backtest_results\notebooklm_smoke_2025_btc_1h\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 32 | 23 |  | 86.46875 | 1.735594 | 1.785091 | 7.416985 | -0.10499 | 0.143253 | 0.143253 | 0.34375 | 0.34375 | 0.09375 | 0.375 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 16 | 16 | 7 |  | 95.9375 | 2.716878 | 1.834568 | 14.115168 | -0.571429 | 0.214286 | 0.214286 | 0.0625 | 0.3125 | 0.1875 | 0.375 | 2 | 2 | target_rr_below_3:2 |
| all | ALL | 50 | none |  | 32 | 23 |  | 86.46875 | 1.735594 | 1.785091 | 7.416985 | -0.10499 | 0.143253 | 0.143253 | 0.34375 | 0.34375 | 0.09375 | 0.375 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 50 | model_rules | 16 | 16 | 7 |  | 95.9375 | 2.716878 | 1.834568 | 14.115168 | -0.571429 | 0.214286 | 0.214286 | 0.0625 | 0.3125 | 0.1875 | 0.375 | 2 | 2 | target_rr_below_3:2 |
| all | ALL | 70 | none |  | 32 | 23 |  | 86.46875 | 1.735594 | 1.785091 | 7.416985 | -0.10499 | 0.143253 | 0.143253 | 0.34375 | 0.34375 | 0.09375 | 0.375 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 70 | model_rules | 16 | 16 | 7 |  | 95.9375 | 2.716878 | 1.834568 | 14.115168 | -0.571429 | 0.214286 | 0.214286 | 0.0625 | 0.3125 | 0.1875 | 0.375 | 2 | 2 | target_rr_below_3:2 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | mitigation_block | 0 | none |  | 17 | 17 |  | 78.764706 | 1.219223 | 0.936841 | 1.192855 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 |  | 16 | target_rr_below_2:15;target_rr_below_3:1 |
| model | reclaimed_ob | 0 | none |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| model | rejection_block | 0 | none |  | 11 | 2 |  | 94.272727 | 1.896696 | 1.896696 | 16.518695 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 |  | 2 | target_rr_below_2:1;target_rr_below_3:1 |
| model | silver_bullet | 0 | none |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| filtered_model | mitigation_block | 0 | model_rules | 15 | 2 | 2 |  | 92.0 | 0.892545 | 0.892545 | 5.346472 | -1.0 | -0.25 | -0.25 |  | 0.5 |  | 1.0 |  | 1 | target_rr_below_3:1 |
| filtered_model | reclaimed_ob | 0 | model_rules |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| filtered_model | rejection_block | 0 | model_rules | 1 | 10 | 1 |  | 96.0 | 1.834568 | 1.834568 | 17.979042 | -1.0 | -1.0 | -1.0 |  |  |  | 0.1 |  | 1 | target_rr_below_3:1 |
| filtered_model | silver_bullet | 0 | model_rules |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| model | mitigation_block | 50 | none |  | 17 | 17 |  | 78.764706 | 1.219223 | 0.936841 | 1.192855 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 |  | 16 | target_rr_below_2:15;target_rr_below_3:1 |
| model | reclaimed_ob | 50 | none |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| model | rejection_block | 50 | none |  | 11 | 2 |  | 94.272727 | 1.896696 | 1.896696 | 16.518695 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 |  | 2 | target_rr_below_2:1;target_rr_below_3:1 |
| model | silver_bullet | 50 | none |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| filtered_model | mitigation_block | 50 | model_rules | 15 | 2 | 2 |  | 92.0 | 0.892545 | 0.892545 | 5.346472 | -1.0 | -0.25 | -0.25 |  | 0.5 |  | 1.0 |  | 1 | target_rr_below_3:1 |
| filtered_model | reclaimed_ob | 50 | model_rules |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| filtered_model | rejection_block | 50 | model_rules | 1 | 10 | 1 |  | 96.0 | 1.834568 | 1.834568 | 17.979042 | -1.0 | -1.0 | -1.0 |  |  |  | 0.1 |  | 1 | target_rr_below_3:1 |
| filtered_model | silver_bullet | 50 | model_rules |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| model | mitigation_block | 70 | none |  | 17 | 17 |  | 78.764706 | 1.219223 | 0.936841 | 1.192855 | -0.137059 | -0.009577 | -0.009577 | 0.529412 | 0.352941 |  | 0.470588 |  | 16 | target_rr_below_2:15;target_rr_below_3:1 |
| model | reclaimed_ob | 70 | none |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| model | rejection_block | 70 | none |  | 11 | 2 |  | 94.272727 | 1.896696 | 1.896696 | 16.518695 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 |  | 2 | target_rr_below_2:1;target_rr_below_3:1 |
| model | silver_bullet | 70 | none |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| filtered_model | mitigation_block | 70 | model_rules | 15 | 2 | 2 |  | 92.0 | 0.892545 | 0.892545 | 5.346472 | -1.0 | -0.25 | -0.25 |  | 0.5 |  | 1.0 |  | 1 | target_rr_below_3:1 |
| filtered_model | reclaimed_ob | 70 | model_rules |  | 3 | 3 |  | 97.0 | 3.936397 | 4.297039 | 11.119776 | -1.0 | 0.5 | 0.5 |  | 1.0 | 0.666667 | 1.0 | 2 |  |  |
| filtered_model | rejection_block | 70 | model_rules | 1 | 10 | 1 |  | 96.0 | 1.834568 | 1.834568 | 17.979042 | -1.0 | -1.0 | -1.0 |  |  |  | 0.1 |  | 1 | target_rr_below_3:1 |
| filtered_model | silver_bullet | 70 | model_rules |  | 1 | 1 |  | 100.0 | 3.589295 | 3.589295 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
