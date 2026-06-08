# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_early_2019-09-01_2021-12-31_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 33 | 33 |  | 76.363636 | 3.536149 | 2.442512 | 2.455734 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 1.179728 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 7 | 24 | target_rr_below_2:21;target_rr_below_3:3 |
| filtered_all | ALL | 0 | model_rules | 16 | 17 | 17 |  | 75.882353 | 2.47318 | 2.390096 | 2.081122 | -0.207534 | 0.037145 | -0.0641 | -0.0641 | 0.101984 | -0.00074 | 0.101245 | 0.856807 | 0.352941 | 0.352941 | 0.294118 | 0.588235 | 3 | 12 | target_rr_below_2:12 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 33 | 33 |  | 76.363636 | 3.536149 | 2.442512 | 2.455734 | -0.417792 | 0.185133 | 0.071396 | 0.071396 | 0.110577 | 0.003159 | 0.113737 | 1.179728 | 0.272727 | 0.484848 | 0.212121 | 0.69697 | 7 | 24 | target_rr_below_2:21;target_rr_below_3:3 |
| filtered_model | turtle_soup | 0 | model_rules | 16 | 17 | 17 |  | 75.882353 | 2.47318 | 2.390096 | 2.081122 | -0.207534 | 0.037145 | -0.0641 | -0.0641 | 0.101984 | -0.00074 | 0.101245 | 0.856807 | 0.352941 | 0.352941 | 0.294118 | 0.588235 | 3 | 12 | target_rr_below_2:12 |
