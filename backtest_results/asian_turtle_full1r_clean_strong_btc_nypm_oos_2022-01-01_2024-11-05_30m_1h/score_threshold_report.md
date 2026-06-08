# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nypm_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 18 | 18 |  | 73.333333 | 2.286222 | 1.965408 | 1.49816 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 1.466136 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 2 | 16 | target_rr_below_2:14;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 9 | 9 | 9 |  | 70.0 | 1.777513 | 1.020809 | 0.9256 | 0.16872 | 0.160759 | -0.021368 | -0.021368 | 0.182127 |  | 0.182127 | 0.949445 | 0.555556 | 0.444444 | 0.111111 | 0.333333 |  | 9 | target_rr_below_2:9 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 18 | 18 |  | 73.333333 | 2.286222 | 1.965408 | 1.49816 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 1.466136 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 2 | 16 | target_rr_below_2:14;target_rr_below_3:2 |
| filtered_model | turtle_soup | 0 | model_rules | 9 | 9 | 9 |  | 70.0 | 1.777513 | 1.020809 | 0.9256 | 0.16872 | 0.160759 | -0.021368 | -0.021368 | 0.182127 |  | 0.182127 | 0.949445 | 0.555556 | 0.444444 | 0.111111 | 0.333333 |  | 9 | target_rr_below_2:9 |
