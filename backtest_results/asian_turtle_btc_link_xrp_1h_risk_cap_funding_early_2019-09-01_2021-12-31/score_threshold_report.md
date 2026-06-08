# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_early_2019-09-01_2021-12-31\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 24 | 24 |  | 74.583333 | 3.700812 | 2.522187 | 2.174235 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 1.597195 | 0.375 | 0.5 | 0.25 | 0.583333 | 5 | 19 | target_rr_below_2:18;target_rr_below_3:1 |
| filtered_all | ALL | 0 | model_rules | 2 | 22 | 22 |  | 74.090909 | 3.835646 | 2.522187 | 2.030031 | -0.416149 | 0.232245 | 0.117699 | 0.117699 | 0.112936 | 0.00161 | 0.114546 | 1.340414 | 0.363636 | 0.454545 | 0.227273 | 0.636364 | 5 | 18 | target_rr_below_2:17;target_rr_below_3:1 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 24 | 24 |  | 74.583333 | 3.700812 | 2.522187 | 2.174235 | -0.199463 | 0.296224 | 0.189275 | 0.189275 | 0.105474 | 0.001476 | 0.106949 | 1.597195 | 0.375 | 0.5 | 0.25 | 0.583333 | 5 | 19 | target_rr_below_2:18;target_rr_below_3:1 |
| filtered_model | turtle_soup | 0 | model_rules | 2 | 22 | 22 |  | 74.090909 | 3.835646 | 2.522187 | 2.030031 | -0.416149 | 0.232245 | 0.117699 | 0.117699 | 0.112936 | 0.00161 | 0.114546 | 1.340414 | 0.363636 | 0.454545 | 0.227273 | 0.636364 | 5 | 18 | target_rr_below_2:17;target_rr_below_3:1 |
