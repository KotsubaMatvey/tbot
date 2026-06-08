# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_control_2024-11-06_2026-04-20\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 33 | 33 |  | 78.181818 | 3.7373 | 3.570459 | 2.812664 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 6.16071 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 2 | 21 | target_rr_below_2:18;target_rr_below_3:3 |
| filtered_all | ALL | 0 | model_rules | 3 | 30 | 30 |  | 78.666667 | 3.906948 | 4.015297 | 3.00802 | 1.045304 | 0.745608 | 0.586769 | 0.586769 | 0.161044 | -0.002205 | 0.158839 | 6.144131 | 0.566667 | 0.833333 | 0.466667 | 0.333333 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 33 | 33 |  | 78.181818 | 3.7373 | 3.570459 | 2.812664 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 6.16071 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 2 | 21 | target_rr_below_2:18;target_rr_below_3:3 |
| filtered_model | turtle_soup | 0 | model_rules | 3 | 30 | 30 |  | 78.666667 | 3.906948 | 4.015297 | 3.00802 | 1.045304 | 0.745608 | 0.586769 | 0.586769 | 0.161044 | -0.002205 | 0.158839 | 6.144131 | 0.566667 | 0.833333 | 0.466667 | 0.333333 | 2 | 18 | target_rr_below_2:16;target_rr_below_3:2 |
