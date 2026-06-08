# ICT Decision Score Threshold Report

- events: `backtest_results\ifvg_retest_15m_costed_late_2024-11-06_2026-04-20_btc_eth\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 327 | 110 |  | 69.697248 | 32.809378 | 17.225855 | 7.679327 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.180967 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 61 | 115 | target_rr_below_2:76;target_rr_below_3:39 |
| filtered_all | ALL | 0 | model_rules | 76 | 251 | 89 |  | 73.956175 | 36.1321 | 19.948017 | 9.626171 | 0.136903 | -0.027054 | -1.618341 | -1.618341 | 0.563761 | 0.000481 | 0.564241 | 0.167858 | 0.059761 | 0.115538 | 0.087649 | 0.294821 | 57 | 39 | target_rr_below_3:39 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 327 | 110 |  | 69.697248 | 32.809378 | 17.225855 | 7.679327 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.180967 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 61 | 115 | target_rr_below_2:76;target_rr_below_3:39 |
| filtered_model | ifvg_retest | 0 | model_rules | 76 | 251 | 89 |  | 73.956175 | 36.1321 | 19.948017 | 9.626171 | 0.136903 | -0.027054 | -1.618341 | -1.618341 | 0.563761 | 0.000481 | 0.564241 | 0.167858 | 0.059761 | 0.115538 | 0.087649 | 0.294821 | 57 | 39 | target_rr_below_3:39 |
