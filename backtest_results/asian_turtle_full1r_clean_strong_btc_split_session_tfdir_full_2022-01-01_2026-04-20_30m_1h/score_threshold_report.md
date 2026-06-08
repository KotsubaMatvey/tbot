# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_split_session_tfdir_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 119 | 119 |  | 74.201681 | 3.536534 | 2.098568 | 1.727891 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 1.841098 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 13 | 99 | target_rr_below_2:89;target_rr_below_3:10 |
| filtered_all | ALL | 0 | model_rules | 75 | 44 | 44 |  | 73.181818 | 3.809412 | 2.206441 | 1.377115 | 0.547576 | 0.56168 | 0.379671 | 0.379671 | 0.18201 |  | 0.18201 | 3.245638 | 0.704545 | 0.613636 | 0.159091 | 0.204545 | 2 | 39 | target_rr_below_2:35;target_rr_below_3:4 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 119 | 119 |  | 74.201681 | 3.536534 | 2.098568 | 1.727891 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 1.841098 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 13 | 99 | target_rr_below_2:89;target_rr_below_3:10 |
| filtered_model | turtle_soup | 0 | model_rules | 75 | 44 | 44 |  | 73.181818 | 3.809412 | 2.206441 | 1.377115 | 0.547576 | 0.56168 | 0.379671 | 0.379671 | 0.18201 |  | 0.18201 | 3.245638 | 0.704545 | 0.613636 | 0.159091 | 0.204545 | 2 | 39 | target_rr_below_2:35;target_rr_below_3:4 |
