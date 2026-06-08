# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nypm_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 3 | 3 |  | 83.333333 | 4.683032 | 2.50518 | 3.454448 | -0.288364 | 0.333333 | 0.047554 | 0.047554 | 0.285779 |  | 0.285779 | 1.128801 | 0.333333 | 0.666667 |  | 0.666667 | 1 | 1 | target_rr_below_2:1 |
| filtered_all | ALL | 0 | model_rules | 1 | 2 | 2 |  | 80.0 | 5.771958 | 5.771958 | 3.664097 | 0.067455 |  | -0.294086 | -0.294086 | 0.294086 |  | 0.294086 | 0.46898 | 0.5 | 0.5 |  | 0.5 |  | 1 | target_rr_below_2:1 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 3 | 3 |  | 83.333333 | 4.683032 | 2.50518 | 3.454448 | -0.288364 | 0.333333 | 0.047554 | 0.047554 | 0.285779 |  | 0.285779 | 1.128801 | 0.333333 | 0.666667 |  | 0.666667 | 1 | 1 | target_rr_below_2:1 |
| filtered_model | turtle_soup | 0 | model_rules | 1 | 2 | 2 |  | 80.0 | 5.771958 | 5.771958 | 3.664097 | 0.067455 |  | -0.294086 | -0.294086 | 0.294086 |  | 0.294086 | 0.46898 | 0.5 | 0.5 |  | 0.5 |  | 1 | target_rr_below_2:1 |
