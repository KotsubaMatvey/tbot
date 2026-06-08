# ICT Decision Score Threshold Report

- events: `backtest_results\silver_bullet_notebooklm_am_pm_htf_aligned_no_poi_quality_gates_may_jun_2025_multi_15m\events.csv`
- thresholds: 0, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 9 | 9 |  | 100.0 | 1.387409 | 0.932926 | 2.0 |  | -0.166667 | -0.166667 | 0.333333 | 0.333333 | 0.333333 | 0.666667 |  |  |  |
| filtered_all | ALL | 0 | model_rules | 8 | 1 | 1 |  | 100.0 | 2.086688 | 2.086688 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| all | ALL | 70 | none |  | 9 | 9 |  | 100.0 | 1.387409 | 0.932926 | 2.0 |  | -0.166667 | -0.166667 | 0.333333 | 0.333333 | 0.333333 | 0.666667 |  |  |  |
| filtered_all | ALL | 70 | model_rules | 8 | 1 | 1 |  | 100.0 | 2.086688 | 2.086688 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | silver_bullet | 0 | none |  | 9 | 9 |  | 100.0 | 1.387409 | 0.932926 | 2.0 |  | -0.166667 | -0.166667 | 0.333333 | 0.333333 | 0.333333 | 0.666667 |  |  |  |
| filtered_model | silver_bullet | 0 | model_rules | 8 | 1 | 1 |  | 100.0 | 2.086688 | 2.086688 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
| model | silver_bullet | 70 | none |  | 9 | 9 |  | 100.0 | 1.387409 | 0.932926 | 2.0 |  | -0.166667 | -0.166667 | 0.333333 | 0.333333 | 0.333333 | 0.666667 |  |  |  |
| filtered_model | silver_bullet | 70 | model_rules | 8 | 1 | 1 |  | 100.0 | 2.086688 | 2.086688 | 2.0 | 2.0 | 1.5 | 1.5 | 1.0 | 1.0 | 1.0 |  |  |  |  |
