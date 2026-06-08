# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_oos_2022-01-01_2024-11-05\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 58 | 58 |  | 76.896552 | 3.820464 | 2.013803 | 2.611422 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 1.703313 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 10 | 42 | target_rr_below_2:34;target_rr_below_3:8 |
| filtered_all | ALL | 0 | model_rules | 3 | 55 | 55 |  | 77.090909 | 3.958915 | 2.42225 | 2.667072 | 0.080884 | 0.354639 | 0.197372 | 0.197372 | 0.155174 | 0.002092 | 0.157266 | 1.635546 | 0.454545 | 0.545455 | 0.163636 | 0.509091 | 10 | 39 | target_rr_below_2:32;target_rr_below_3:7 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 58 | 58 |  | 76.896552 | 3.820464 | 2.013803 | 2.611422 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 1.703313 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 10 | 42 | target_rr_below_2:34;target_rr_below_3:8 |
| filtered_model | turtle_soup | 0 | model_rules | 3 | 55 | 55 |  | 77.090909 | 3.958915 | 2.42225 | 2.667072 | 0.080884 | 0.354639 | 0.197372 | 0.197372 | 0.155174 | 0.002092 | 0.157266 | 1.635546 | 0.454545 | 0.545455 | 0.163636 | 0.509091 | 10 | 39 | target_rr_below_2:32;target_rr_below_3:7 |
