# ICT Decision Score Threshold Report

- events: `backtest_results\session_open_baseline_may_oct_2025_eth_silver_15m\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 359 | 343 |  | 77.888579 | 3.626558 | 2.031776 | 2.0 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 22 | 2 | target_rr_below_2:2 |
| filtered_all | ALL | 0 | model_rules | 359 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 70 | none |  | 357 | 341 |  | 78.0 | 3.646439 | 2.03712 | 2.0 | -0.050031 | 0.103991 | 0.103991 | 0.257703 | 0.490196 | 0.257703 | 0.633053 | 22 |  |  |
| filtered_all | ALL | 70 | model_rules | 357 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | silver_bullet | 0 | none |  | 359 | 343 |  | 77.888579 | 3.626558 | 2.031776 | 2.0 | -0.05557 | 0.097553 | 0.097553 | 0.256267 | 0.487465 | 0.256267 | 0.635097 | 22 | 2 | target_rr_below_2:2 |
| filtered_model | silver_bullet | 0 | model_rules | 359 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | silver_bullet | 70 | none |  | 357 | 341 |  | 78.0 | 3.646439 | 2.03712 | 2.0 | -0.050031 | 0.103991 | 0.103991 | 0.257703 | 0.490196 | 0.257703 | 0.633053 | 22 |  |  |
| filtered_model | silver_bullet | 70 | model_rules | 357 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
