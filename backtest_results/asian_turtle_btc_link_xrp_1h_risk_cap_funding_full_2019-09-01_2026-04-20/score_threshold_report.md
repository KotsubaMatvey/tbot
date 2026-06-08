# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_full_2019-09-01_2026-04-20\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 115 | 115 |  | 76.782609 | 3.771628 | 2.699944 | 2.57793 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 2.22439 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 17 | 82 | target_rr_below_2:70;target_rr_below_3:12 |
| filtered_all | ALL | 0 | model_rules | 8 | 107 | 107 |  | 76.915888 | 3.919 | 2.729548 | 2.631684 | 0.249088 | 0.439091 | 0.290168 | 0.290168 | 0.148135 | 0.000788 | 0.148924 | 2.104551 | 0.46729 | 0.607477 | 0.261682 | 0.485981 | 17 | 75 | target_rr_below_2:65;target_rr_below_3:10 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 115 | 115 |  | 76.782609 | 3.771628 | 2.699944 | 2.57793 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 2.22439 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 17 | 82 | target_rr_below_2:70;target_rr_below_3:12 |
| filtered_model | turtle_soup | 0 | model_rules | 8 | 107 | 107 |  | 76.915888 | 3.919 | 2.729548 | 2.631684 | 0.249088 | 0.439091 | 0.290168 | 0.290168 | 0.148135 | 0.000788 | 0.148924 | 2.104551 | 0.46729 | 0.607477 | 0.261682 | 0.485981 | 17 | 75 | target_rr_below_2:65;target_rr_below_3:10 |
