# ICT Decision Score Threshold Report

- events: `backtest_results\breaker_research_may_oct_2025_1h\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 4 | 3 | 1 | 97.25 | 9.664197 | 8.145282 | 10.249643 | 2.402492 |  |  | 0.25 | 0.5 | 0.5 | 0.25 |  | 2 | target_rr_below_2:2 |
| filtered_all | ALL | 0 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 70 | none |  | 4 | 3 | 1 | 97.25 | 9.664197 | 8.145282 | 10.249643 | 2.402492 |  |  | 0.25 | 0.5 | 0.5 | 0.25 |  | 2 | target_rr_below_2:2 |
| filtered_all | ALL | 70 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | breaker_block | 0 | none |  | 4 | 3 | 1 | 97.25 | 9.664197 | 8.145282 | 10.249643 | 2.402492 |  |  | 0.25 | 0.5 | 0.5 | 0.25 |  | 2 | target_rr_below_2:2 |
| filtered_model | breaker_block | 0 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | breaker_block | 70 | none |  | 4 | 3 | 1 | 97.25 | 9.664197 | 8.145282 | 10.249643 | 2.402492 |  |  | 0.25 | 0.5 | 0.5 | 0.25 |  | 2 | target_rr_below_2:2 |
| filtered_model | breaker_block | 70 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
