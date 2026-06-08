# ICT Decision Score Threshold Report

- events: `backtest_results\ifvg_retest_15m_costed_oos_2022-01-01_2024-11-05_btc_eth\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 513 | 181 |  | 70.660819 | 36.510725 | 16.618559 | 7.446574 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.214813 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 106 | 181 | target_rr_below_2:95;target_rr_below_3:86 |
| filtered_all | ALL | 0 | model_rules | 95 | 418 | 143 |  | 73.980861 | 40.054841 | 20.380942 | 8.838487 | 0.420818 | 0.238381 | -1.435067 | -1.435067 | 0.57241 | 8.5e-05 | 0.572495 | 0.215976 | 0.062201 | 0.141148 | 0.114833 | 0.279904 | 96 | 86 | target_rr_below_3:86 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 513 | 181 |  | 70.660819 | 36.510725 | 16.618559 | 7.446574 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.214813 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 106 | 181 | target_rr_below_2:95;target_rr_below_3:86 |
| filtered_model | ifvg_retest | 0 | model_rules | 95 | 418 | 143 |  | 73.980861 | 40.054841 | 20.380942 | 8.838487 | 0.420818 | 0.238381 | -1.435067 | -1.435067 | 0.57241 | 8.5e-05 | 0.572495 | 0.215976 | 0.062201 | 0.141148 | 0.114833 | 0.279904 | 96 | 86 | target_rr_below_3:86 |
