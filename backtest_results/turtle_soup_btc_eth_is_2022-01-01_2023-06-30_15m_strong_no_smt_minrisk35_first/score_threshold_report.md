# ICT Decision Score Threshold Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_15m_strong_no_smt_minrisk35_first\events.csv`
- thresholds: 0, 50, 70, 80, 90

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 695 | 695 |  | 66.805755 | 8.771304 | 5.791525 | 6.193506 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.681964 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 309 | 211 | target_rr_below_2:131;target_rr_below_3:80 |
| filtered_all | ALL | 0 | model_rules | 580 | 115 | 115 |  | 58.521739 | 3.578325 | 2.853124 | 3.527987 | 0.225562 | 0.624304 | 0.437971 | 0.437971 | 0.186409 | -7.5e-05 | 0.186333 | 3.003188 | 0.434783 | 0.791304 | 0.356522 | 0.556522 | 31 | 74 | target_rr_below_2:58;target_rr_below_3:16 |
| all | ALL | 50 | none |  | 695 | 695 |  | 66.805755 | 8.771304 | 5.791525 | 6.193506 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.681964 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 309 | 211 | target_rr_below_2:131;target_rr_below_3:80 |
| filtered_all | ALL | 50 | model_rules | 580 | 115 | 115 |  | 58.521739 | 3.578325 | 2.853124 | 3.527987 | 0.225562 | 0.624304 | 0.437971 | 0.437971 | 0.186409 | -7.5e-05 | 0.186333 | 3.003188 | 0.434783 | 0.791304 | 0.356522 | 0.556522 | 31 | 74 | target_rr_below_2:58;target_rr_below_3:16 |
| all | ALL | 70 | none |  | 497 | 497 |  | 71.95171 | 10.410201 | 7.76249 | 7.946905 | 1.189075 | 0.523947 | -0.288442 | -0.288442 | 0.812389 |  | 0.812389 | 0.473771 | 0.277666 | 0.760563 | 0.637827 | 0.698189 | 284 | 13 | target_rr_below_2:10;target_rr_below_3:3 |
| filtered_all | ALL | 70 | model_rules | 456 | 41 | 41 |  | 70.0 | 4.632453 | 3.640329 | 7.081755 | -0.32484 | 0.609756 | 0.404571 | 0.404571 | 0.205185 |  | 0.205185 | 2.716951 | 0.073171 | 0.804878 | 0.439024 | 0.902439 | 25 |  |  |
| all | ALL | 80 | none |  | 50 | 50 |  | 89.4 | 10.623611 | 6.529974 | 6.965742 | 0.59724 | 0.48 | -0.299432 | -0.299432 | 0.779432 |  | 0.779432 | 0.479349 | 0.24 | 0.74 | 0.58 | 0.76 | 33 | 3 | target_rr_below_3:3 |
| filtered_all | ALL | 80 | model_rules | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 90 | none |  | 47 | 47 |  | 90.0 | 10.977321 | 6.900063 | 7.228434 | 0.53779 | 0.489362 | -0.311522 | -0.311522 | 0.800884 |  | 0.800884 | 0.465233 | 0.212766 | 0.744681 | 0.574468 | 0.787234 | 33 |  |  |
| filtered_all | ALL | 90 | model_rules | 47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 695 | 695 |  | 66.805755 | 8.771304 | 5.791525 | 6.193506 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.681964 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 309 | 211 | target_rr_below_2:131;target_rr_below_3:80 |
| filtered_model | turtle_soup | 0 | model_rules | 580 | 115 | 115 |  | 58.521739 | 3.578325 | 2.853124 | 3.527987 | 0.225562 | 0.624304 | 0.437971 | 0.437971 | 0.186409 | -7.5e-05 | 0.186333 | 3.003188 | 0.434783 | 0.791304 | 0.356522 | 0.556522 | 31 | 74 | target_rr_below_2:58;target_rr_below_3:16 |
| model | turtle_soup | 50 | none |  | 695 | 695 |  | 66.805755 | 8.771304 | 5.791525 | 6.193506 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.681964 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 309 | 211 | target_rr_below_2:131;target_rr_below_3:80 |
| filtered_model | turtle_soup | 50 | model_rules | 580 | 115 | 115 |  | 58.521739 | 3.578325 | 2.853124 | 3.527987 | 0.225562 | 0.624304 | 0.437971 | 0.437971 | 0.186409 | -7.5e-05 | 0.186333 | 3.003188 | 0.434783 | 0.791304 | 0.356522 | 0.556522 | 31 | 74 | target_rr_below_2:58;target_rr_below_3:16 |
| model | turtle_soup | 70 | none |  | 497 | 497 |  | 71.95171 | 10.410201 | 7.76249 | 7.946905 | 1.189075 | 0.523947 | -0.288442 | -0.288442 | 0.812389 |  | 0.812389 | 0.473771 | 0.277666 | 0.760563 | 0.637827 | 0.698189 | 284 | 13 | target_rr_below_2:10;target_rr_below_3:3 |
| filtered_model | turtle_soup | 70 | model_rules | 456 | 41 | 41 |  | 70.0 | 4.632453 | 3.640329 | 7.081755 | -0.32484 | 0.609756 | 0.404571 | 0.404571 | 0.205185 |  | 0.205185 | 2.716951 | 0.073171 | 0.804878 | 0.439024 | 0.902439 | 25 |  |  |
| model | turtle_soup | 80 | none |  | 50 | 50 |  | 89.4 | 10.623611 | 6.529974 | 6.965742 | 0.59724 | 0.48 | -0.299432 | -0.299432 | 0.779432 |  | 0.779432 | 0.479349 | 0.24 | 0.74 | 0.58 | 0.76 | 33 | 3 | target_rr_below_3:3 |
| filtered_model | turtle_soup | 80 | model_rules | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | turtle_soup | 90 | none |  | 47 | 47 |  | 90.0 | 10.977321 | 6.900063 | 7.228434 | 0.53779 | 0.489362 | -0.311522 | -0.311522 | 0.800884 |  | 0.800884 | 0.465233 | 0.212766 | 0.744681 | 0.574468 | 0.787234 | 33 |  |  |
| filtered_model | turtle_soup | 90 | model_rules | 47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
