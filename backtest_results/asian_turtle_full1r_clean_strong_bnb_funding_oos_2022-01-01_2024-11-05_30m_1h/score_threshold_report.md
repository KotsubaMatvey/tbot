# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_bnb_funding_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 31 | 31 |  | 77.419355 | 3.397381 | 2.602292 | 2.371333 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 1.130933 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 5 | 22 | target_rr_below_2:17;target_rr_below_3:5 |
| filtered_all | ALL | 0 | model_rules | 15 | 16 | 16 |  | 76.25 | 2.944759 | 2.748511 | 2.073235 | -0.209391 | 0.350457 | 0.183697 | 0.183697 | 0.166742 | 1.7e-05 | 0.166759 | 1.889569 | 0.375 | 0.4375 | 0.1875 | 0.5 | 4 | 12 | target_rr_below_2:10;target_rr_below_3:2 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 31 | 31 |  | 77.419355 | 3.397381 | 2.602292 | 2.371333 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 1.130933 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 5 | 22 | target_rr_below_2:17;target_rr_below_3:5 |
| filtered_model | turtle_soup | 0 | model_rules | 15 | 16 | 16 |  | 76.25 | 2.944759 | 2.748511 | 2.073235 | -0.209391 | 0.350457 | 0.183697 | 0.183697 | 0.166742 | 1.7e-05 | 0.166759 | 1.889569 | 0.375 | 0.4375 | 0.1875 | 0.5 | 4 | 12 | target_rr_below_2:10;target_rr_below_3:2 |
