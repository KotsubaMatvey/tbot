# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 64 | 64 |  | 73.75 | 3.492889 | 1.638643 | 1.571255 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 1.49883 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 6 | 55 | target_rr_below_2:49;target_rr_below_3:6 |
| filtered_all | ALL | 0 | model_rules | 30 | 34 | 34 |  | 73.235294 | 3.869968 | 1.994614 | 1.379165 | 0.461863 | 0.543532 | 0.350895 | 0.350895 | 0.192637 |  | 0.192637 | 2.755155 | 0.676471 | 0.588235 | 0.088235 | 0.235294 | 3 | 31 | target_rr_below_2:26;target_rr_below_3:5 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 64 | 64 |  | 73.75 | 3.492889 | 1.638643 | 1.571255 | 0.189194 | 0.342792 | 0.153759 | 0.153759 | 0.189034 |  | 0.189034 | 1.49883 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 6 | 55 | target_rr_below_2:49;target_rr_below_3:6 |
| filtered_model | turtle_soup | 0 | model_rules | 30 | 34 | 34 |  | 73.235294 | 3.869968 | 1.994614 | 1.379165 | 0.461863 | 0.543532 | 0.350895 | 0.350895 | 0.192637 |  | 0.192637 | 2.755155 | 0.676471 | 0.588235 | 0.088235 | 0.235294 | 3 | 31 | target_rr_below_2:26;target_rr_below_3:5 |
