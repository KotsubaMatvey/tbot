# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_full_2019-09-01_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 215 | 215 |  | 75.906977 | 3.868786 | 2.442512 | 2.194183 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 1.762051 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 27 | 165 | target_rr_below_2:138;target_rr_below_3:27 |
| filtered_all | ALL | 0 | model_rules | 131 | 84 | 84 |  | 75.47619 | 3.853042 | 2.667325 | 1.882787 | 0.333552 | 0.474937 | 0.331925 | 0.331925 | 0.144332 | -0.00132 | 0.143012 | 2.500805 | 0.547619 | 0.583333 | 0.202381 | 0.369048 | 9 | 66 | target_rr_below_2:56;target_rr_below_3:10 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 215 | 215 |  | 75.906977 | 3.868786 | 2.442512 | 2.194183 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 1.762051 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 27 | 165 | target_rr_below_2:138;target_rr_below_3:27 |
| filtered_model | turtle_soup | 0 | model_rules | 131 | 84 | 84 |  | 75.47619 | 3.853042 | 2.667325 | 1.882787 | 0.333552 | 0.474937 | 0.331925 | 0.331925 | 0.144332 | -0.00132 | 0.143012 | 2.500805 | 0.547619 | 0.583333 | 0.202381 | 0.369048 | 9 | 66 | target_rr_below_2:56;target_rr_below_3:10 |
