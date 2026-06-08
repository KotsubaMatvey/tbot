# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nyopen_tfdir_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 19 | 19 |  | 72.105263 | 3.381471 | 2.469999 | 1.433191 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 4.352202 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 15 | 4 | 4 |  | 70.0 | 4.427052 | 4.785893 | 0.956625 | 0.956625 | 0.837184 | 0.68693 | 0.68693 | 0.150253 |  | 0.150253 |  | 1.0 | 0.75 | 0.25 |  |  | 4 | target_rr_below_2:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 19 | 19 |  | 72.105263 | 3.381471 | 2.469999 | 1.433191 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 4.352202 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_model | turtle_soup | 0 | model_rules | 15 | 4 | 4 |  | 70.0 | 4.427052 | 4.785893 | 0.956625 | 0.956625 | 0.837184 | 0.68693 | 0.68693 | 0.150253 |  | 0.150253 |  | 1.0 | 0.75 | 0.25 |  |  | 4 | target_rr_below_2:4 |
