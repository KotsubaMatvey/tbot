# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nyopen_tfdir_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 64 | 64 |  | 75.0 | 3.852882 | 2.405383 | 1.908029 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 1.447287 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 9 | 51 | target_rr_below_2:45;target_rr_below_3:6 |
| filtered_all | ALL | 0 | model_rules | 37 | 27 | 27 |  | 73.333333 | 3.99102 | 1.936007 | 1.424548 | 0.395339 | 0.508313 | 0.312131 | 0.312131 | 0.196183 |  | 0.196183 | 2.419042 | 0.703704 | 0.592593 | 0.074074 | 0.259259 | 1 | 24 | target_rr_below_2:21;target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 64 | 64 |  | 75.0 | 3.852882 | 2.405383 | 1.908029 | 0.032899 | 0.365576 | 0.142001 | 0.142001 | 0.223575 |  | 0.223575 | 1.447287 | 0.515625 | 0.5625 | 0.171875 | 0.453125 | 9 | 51 | target_rr_below_2:45;target_rr_below_3:6 |
| filtered_model | turtle_soup | 0 | model_rules | 37 | 27 | 27 |  | 73.333333 | 3.99102 | 1.936007 | 1.424548 | 0.395339 | 0.508313 | 0.312131 | 0.312131 | 0.196183 |  | 0.196183 | 2.419042 | 0.703704 | 0.592593 | 0.074074 | 0.259259 | 1 | 24 | target_rr_below_2:21;target_rr_below_3:3 |
