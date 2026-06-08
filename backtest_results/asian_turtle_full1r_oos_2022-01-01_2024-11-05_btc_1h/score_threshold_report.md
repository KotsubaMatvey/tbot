# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_oos_2022-01-01_2024-11-05_btc_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 40 | 40 |  | 74.0 | 3.586636 | 1.763138 | 1.62759 | 0.081656 | 0.406279 | 0.259288 | 0.259288 | 0.146991 |  | 0.146991 | 1.994182 | 0.525 | 0.525 | 0.025 | 0.4 | 3 | 34 | target_rr_below_2:30;target_rr_below_3:4 |
| filtered_all | ALL | 0 | model_rules |  | 40 | 40 |  | 74.0 | 3.586636 | 1.763138 | 1.62759 | 0.081656 | 0.406279 | 0.259288 | 0.259288 | 0.146991 |  | 0.146991 | 1.994182 | 0.525 | 0.525 | 0.025 | 0.4 | 3 | 34 | target_rr_below_2:30;target_rr_below_3:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 40 | 40 |  | 74.0 | 3.586636 | 1.763138 | 1.62759 | 0.081656 | 0.406279 | 0.259288 | 0.259288 | 0.146991 |  | 0.146991 | 1.994182 | 0.525 | 0.525 | 0.025 | 0.4 | 3 | 34 | target_rr_below_2:30;target_rr_below_3:4 |
| filtered_model | turtle_soup | 0 | model_rules |  | 40 | 40 |  | 74.0 | 3.586636 | 1.763138 | 1.62759 | 0.081656 | 0.406279 | 0.259288 | 0.259288 | 0.146991 |  | 0.146991 | 1.994182 | 0.525 | 0.525 | 0.025 | 0.4 | 3 | 34 | target_rr_below_2:30;target_rr_below_3:4 |
