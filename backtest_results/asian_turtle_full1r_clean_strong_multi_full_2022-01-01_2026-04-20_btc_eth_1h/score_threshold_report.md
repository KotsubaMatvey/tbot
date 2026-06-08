# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_multi_full_2022-01-01_2026-04-20_btc_eth_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 73 | 73 |  | 75.068493 | 3.625995 | 2.185569 | 2.119005 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 1.748124 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 6 | 59 | target_rr_below_2:50;target_rr_below_3:9 |
| filtered_all | ALL | 0 | model_rules | 37 | 36 | 36 |  | 73.055556 | 3.58461 | 2.103067 | 1.7014 | 0.218602 | 0.360684 | 0.234643 | 0.234643 | 0.126041 |  | 0.126041 | 1.824662 | 0.583333 | 0.555556 | 0.111111 | 0.361111 | 2 | 33 | target_rr_below_2:28;target_rr_below_3:5 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 73 | 73 |  | 75.068493 | 3.625995 | 2.185569 | 2.119005 | 0.086818 | 0.374056 | 0.220339 | 0.220339 | 0.153718 |  | 0.153718 | 1.748124 | 0.506849 | 0.589041 | 0.191781 | 0.465753 | 6 | 59 | target_rr_below_2:50;target_rr_below_3:9 |
| filtered_model | turtle_soup | 0 | model_rules | 37 | 36 | 36 |  | 73.055556 | 3.58461 | 2.103067 | 1.7014 | 0.218602 | 0.360684 | 0.234643 | 0.234643 | 0.126041 |  | 0.126041 | 1.824662 | 0.583333 | 0.555556 | 0.111111 | 0.361111 | 2 | 33 | target_rr_below_2:28;target_rr_below_3:5 |
