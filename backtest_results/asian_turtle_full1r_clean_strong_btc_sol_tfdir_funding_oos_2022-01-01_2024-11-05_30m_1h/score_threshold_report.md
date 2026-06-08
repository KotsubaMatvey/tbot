# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_sol_tfdir_funding_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 97 | 97 |  | 74.742268 | 3.385477 | 2.027705 | 2.039364 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 1.375509 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 12 | 78 | target_rr_below_2:70;target_rr_below_3:8 |
| filtered_all | ALL | 0 | model_rules | 56 | 41 | 41 |  | 73.170732 | 4.050666 | 2.572817 | 1.478067 | 0.309447 | 0.479189 | 0.327065 | 0.327065 | 0.15316 | -0.001037 | 0.152124 | 2.593261 | 0.634146 | 0.536585 | 0.097561 | 0.292683 | 3 | 36 | target_rr_below_2:33;target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 97 | 97 |  | 74.742268 | 3.385477 | 2.027705 | 2.039364 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 1.375509 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 12 | 78 | target_rr_below_2:70;target_rr_below_3:8 |
| filtered_model | turtle_soup | 0 | model_rules | 56 | 41 | 41 |  | 73.170732 | 4.050666 | 2.572817 | 1.478067 | 0.309447 | 0.479189 | 0.327065 | 0.327065 | 0.15316 | -0.001037 | 0.152124 | 2.593261 | 0.634146 | 0.536585 | 0.097561 | 0.292683 | 3 | 36 | target_rr_below_2:33;target_rr_below_3:3 |
