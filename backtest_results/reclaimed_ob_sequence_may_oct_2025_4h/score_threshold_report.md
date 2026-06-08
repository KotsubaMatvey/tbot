# ICT Decision Score Threshold Report

- events: `backtest_results\reclaimed_ob_sequence_may_oct_2025_4h\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 4 | 1 |  | 96.0 | 16.696845 | 16.696845 | 16.105903 | -1.0 | 0.5 | 0.5 |  | 0.25 | 0.25 | 0.25 | 1 | 1 | target_rr_below_3:1 |
| filtered_all | ALL | 0 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 70 | none |  | 4 | 1 |  | 96.0 | 16.696845 | 16.696845 | 16.105903 | -1.0 | 0.5 | 0.5 |  | 0.25 | 0.25 | 0.25 | 1 | 1 | target_rr_below_3:1 |
| filtered_all | ALL | 70 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | reclaimed_ob | 0 | none |  | 4 | 1 |  | 96.0 | 16.696845 | 16.696845 | 16.105903 | -1.0 | 0.5 | 0.5 |  | 0.25 | 0.25 | 0.25 | 1 | 1 | target_rr_below_3:1 |
| filtered_model | reclaimed_ob | 0 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | reclaimed_ob | 70 | none |  | 4 | 1 |  | 96.0 | 16.696845 | 16.696845 | 16.105903 | -1.0 | 0.5 | 0.5 |  | 0.25 | 0.25 | 0.25 | 1 | 1 | target_rr_below_3:1 |
| filtered_model | reclaimed_ob | 70 | model_rules | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
