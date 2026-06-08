# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_reclaim_full_2022-01-01_2026-04-20_btc_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 42 | 42 |  | 74.285714 | 3.786161 | 2.392156 | 1.685918 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 2.487931 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 3 | 35 | target_rr_below_2:31;target_rr_below_3:4 |
| filtered_all | ALL | 0 | model_rules |  | 42 | 42 |  | 74.285714 | 3.786161 | 2.392156 | 1.685918 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 2.487931 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 3 | 35 | target_rr_below_2:31;target_rr_below_3:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 42 | 42 |  | 74.285714 | 3.786161 | 2.392156 | 1.685918 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 2.487931 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 3 | 35 | target_rr_below_2:31;target_rr_below_3:4 |
| filtered_model | turtle_soup | 0 | model_rules |  | 42 | 42 |  | 74.285714 | 3.786161 | 2.392156 | 1.685918 | 0.284158 | 0.494959 | 0.328903 | 0.328903 | 0.166055 |  | 0.166055 | 2.487931 | 0.595238 | 0.619048 | 0.190476 | 0.357143 | 3 | 35 | target_rr_below_2:31;target_rr_below_3:4 |
