# ICT Decision Score Threshold Report

- events: `backtest_results\ict2022_first_retested_fvg_session_fallback_oos_2022-01-01_2024-11-05_btc_eth_30m\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 60 | 59 |  | 82.166667 | 1.375322 | 0.872943 | 1.007321 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.230369 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 4 | 59 | target_rr_below_2:36;target_rr_below_3:23 |
| filtered_all | ALL | 0 | model_rules | 36 | 24 | 23 |  | 88.416667 | 1.255445 | 0.875121 | 2.085366 | -0.501853 | -0.590094 | -0.640915 | -0.640915 | 0.045721 | 0.002982 | 0.048704 | 0.222297 | 0.041667 | 0.125 | 0.041667 | 0.75 |  | 23 | target_rr_below_3:23 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ict2022_mss_fvg | 0 | none |  | 60 | 59 |  | 82.166667 | 1.375322 | 0.872943 | 1.007321 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.230369 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 4 | 59 | target_rr_below_2:36;target_rr_below_3:23 |
| filtered_model | ict2022_mss_fvg | 0 | model_rules | 36 | 24 | 23 |  | 88.416667 | 1.255445 | 0.875121 | 2.085366 | -0.501853 | -0.590094 | -0.640915 | -0.640915 | 0.045721 | 0.002982 | 0.048704 | 0.222297 | 0.041667 | 0.125 | 0.041667 | 0.75 |  | 23 | target_rr_below_3:23 |
