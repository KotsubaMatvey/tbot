# ICT Decision Score Threshold Report

- events: `backtest_results\session_open_baseline_may_oct_2025_btc_silver_15m\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 369 | 352 |  | 78.0 | 3.696643 | 2.195372 | 2.0 | -0.102621 | 0.054086 | 0.054086 | 0.257453 | 0.468835 | 0.257453 | 0.653117 | 14 |  |  |
| filtered_all | ALL | 0 | model_rules | 369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 70 | none |  | 369 | 352 |  | 78.0 | 3.696643 | 2.195372 | 2.0 | -0.102621 | 0.054086 | 0.054086 | 0.257453 | 0.468835 | 0.257453 | 0.653117 | 14 |  |  |
| filtered_all | ALL | 70 | model_rules | 369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | silver_bullet | 0 | none |  | 369 | 352 |  | 78.0 | 3.696643 | 2.195372 | 2.0 | -0.102621 | 0.054086 | 0.054086 | 0.257453 | 0.468835 | 0.257453 | 0.653117 | 14 |  |  |
| filtered_model | silver_bullet | 0 | model_rules | 369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | silver_bullet | 70 | none |  | 369 | 352 |  | 78.0 | 3.696643 | 2.195372 | 2.0 | -0.102621 | 0.054086 | 0.054086 | 0.257453 | 0.468835 | 0.257453 | 0.653117 | 14 |  |  |
| filtered_model | silver_bullet | 70 | model_rules | 369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
