# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_split_session_tfdir_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 94 | 94 |  | 74.680851 | 3.563336 | 1.936007 | 1.792293 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 1.484313 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 11 | 76 | target_rr_below_2:68;target_rr_below_3:8 |
| filtered_all | ALL | 0 | model_rules | 56 | 38 | 38 |  | 73.684211 | 3.771852 | 1.941838 | 1.460318 | 0.4998 | 0.535413 | 0.3482 | 0.3482 | 0.187212 |  | 0.187212 | 2.786862 | 0.657895 | 0.605263 | 0.131579 | 0.236842 | 2 | 33 | target_rr_below_2:29;target_rr_below_3:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 94 | 94 |  | 74.680851 | 3.563336 | 1.936007 | 1.792293 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 1.484313 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 11 | 76 | target_rr_below_2:68;target_rr_below_3:8 |
| filtered_model | turtle_soup | 0 | model_rules | 56 | 38 | 38 |  | 73.684211 | 3.771852 | 1.941838 | 1.460318 | 0.4998 | 0.535413 | 0.3482 | 0.3482 | 0.187212 |  | 0.187212 | 2.786862 | 0.657895 | 0.605263 | 0.131579 | 0.236842 | 2 | 33 | target_rr_below_2:29;target_rr_below_3:4 |
