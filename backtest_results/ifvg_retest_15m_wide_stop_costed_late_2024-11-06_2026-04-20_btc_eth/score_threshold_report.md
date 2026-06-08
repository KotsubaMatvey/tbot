# ICT Decision Score Threshold Report

- events: `backtest_results\ifvg_retest_15m_wide_stop_costed_late_2024-11-06_2026-04-20_btc_eth\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 327 | 121 |  | 65.752294 | 19.602104 | 8.626381 | 5.046954 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.36085 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 43 | 183 | target_rr_below_2:137;target_rr_below_3:46 |
| filtered_all | ALL | 0 | model_rules | 203 | 124 | 5 |  | 73.120968 | 7.015514 | 3.210011 | 7.798257 | -1.0 | -0.4 | -0.558968 | -0.558968 | 0.00641 |  | 0.00641 | 0.199113 |  | 0.016129 | 0.008065 | 0.040323 | 1 | 30 | target_rr_below_3:30 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 327 | 121 |  | 65.752294 | 19.602104 | 8.626381 | 5.046954 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.36085 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 43 | 183 | target_rr_below_2:137;target_rr_below_3:46 |
| filtered_model | ifvg_retest | 0 | model_rules | 203 | 124 | 5 |  | 73.120968 | 7.015514 | 3.210011 | 7.798257 | -1.0 | -0.4 | -0.558968 | -0.558968 | 0.00641 |  | 0.00641 | 0.199113 |  | 0.016129 | 0.008065 | 0.040323 | 1 | 30 | target_rr_below_3:30 |
