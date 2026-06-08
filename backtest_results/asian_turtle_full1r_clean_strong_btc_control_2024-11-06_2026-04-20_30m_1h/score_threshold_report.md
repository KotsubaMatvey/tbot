# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 20 | 20 |  | 73.0 | 3.788684 | 4.015297 | 1.535259 | 0.781995 | 0.756623 | 0.549617 | 0.549617 | 0.207006 |  | 0.207006 | 7.842471 | 0.75 | 0.8 | 0.45 | 0.2 |  | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_all | ALL | 0 | model_rules | 13 | 7 | 7 |  | 71.428571 | 3.689183 | 4.514163 | 1.060677 | 0.585851 | 0.766893 | 0.622188 | 0.622188 | 0.144704 |  | 0.144704 | 128.546139 | 0.857143 | 0.714286 | 0.285714 | 0.142857 |  | 7 | target_rr_below_2:6;target_rr_below_3:1 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 20 | 20 |  | 73.0 | 3.788684 | 4.015297 | 1.535259 | 0.781995 | 0.756623 | 0.549617 | 0.549617 | 0.207006 |  | 0.207006 | 7.842471 | 0.75 | 0.8 | 0.45 | 0.2 |  | 18 | target_rr_below_2:16;target_rr_below_3:2 |
| filtered_model | turtle_soup | 0 | model_rules | 13 | 7 | 7 |  | 71.428571 | 3.689183 | 4.514163 | 1.060677 | 0.585851 | 0.766893 | 0.622188 | 0.622188 | 0.144704 |  | 0.144704 | 128.546139 | 0.857143 | 0.714286 | 0.285714 | 0.142857 |  | 7 | target_rr_below_2:6;target_rr_below_3:1 |
