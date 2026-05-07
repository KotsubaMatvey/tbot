# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_debug_2025_btc_30m\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 101 | 101 |  | 62.772277 | 3.458326 | 2.126295 | 2.0 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.584061 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 11 | 101 | target_rr_below_3:101 |
| filtered_all | ALL | 0 | model_rules | 78 | 23 | 23 |  | 62.608696 | 1.35089 | 1.118307 | 2.0 | 0.172122 | 0.165108 | 0.078035 | 0.078035 | 0.087072 | 1.195652 | 0.26087 | 0.521739 | 0.26087 | 0.521739 | 2 | 23 | target_rr_below_3:23 |
| all | ALL | 50 | none |  | 101 | 101 |  | 62.772277 | 3.458326 | 2.126295 | 2.0 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.584061 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 11 | 101 | target_rr_below_3:101 |
| filtered_all | ALL | 50 | model_rules | 78 | 23 | 23 |  | 62.608696 | 1.35089 | 1.118307 | 2.0 | 0.172122 | 0.165108 | 0.078035 | 0.078035 | 0.087072 | 1.195652 | 0.26087 | 0.521739 | 0.26087 | 0.521739 | 2 | 23 | target_rr_below_3:23 |
| all | ALL | 70 | none |  | 14 | 14 |  | 80.0 | 2.292957 | 2.20373 | 2.0 | 0.183327 | -0.088271 | -0.361037 | -0.361037 | 0.272765 | 0.489362 | 0.357143 | 0.428571 | 0.357143 | 0.571429 |  | 14 | target_rr_below_3:14 |
| filtered_all | ALL | 70 | model_rules | 11 | 3 | 3 |  | 80.0 | 2.07436 | 2.586894 | 2.0 | 1.522192 | 0.588068 | 0.502851 | 0.502851 | 0.085217 | 6.312607 | 0.666667 | 0.666667 | 0.666667 |  |  | 3 | target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 101 | 101 |  | 62.772277 | 3.458326 | 2.126295 | 2.0 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.584061 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 11 | 101 | target_rr_below_3:101 |
| filtered_model | turtle_soup | 0 | model_rules | 78 | 23 | 23 |  | 62.608696 | 1.35089 | 1.118307 | 2.0 | 0.172122 | 0.165108 | 0.078035 | 0.078035 | 0.087072 | 1.195652 | 0.26087 | 0.521739 | 0.26087 | 0.521739 | 2 | 23 | target_rr_below_3:23 |
| model | turtle_soup | 50 | none |  | 101 | 101 |  | 62.772277 | 3.458326 | 2.126295 | 2.0 | -0.090799 | 0.017797 | -0.267569 | -0.267569 | 0.285366 | 0.584061 | 0.257426 | 0.49505 | 0.257426 | 0.673267 | 11 | 101 | target_rr_below_3:101 |
| filtered_model | turtle_soup | 50 | model_rules | 78 | 23 | 23 |  | 62.608696 | 1.35089 | 1.118307 | 2.0 | 0.172122 | 0.165108 | 0.078035 | 0.078035 | 0.087072 | 1.195652 | 0.26087 | 0.521739 | 0.26087 | 0.521739 | 2 | 23 | target_rr_below_3:23 |
| model | turtle_soup | 70 | none |  | 14 | 14 |  | 80.0 | 2.292957 | 2.20373 | 2.0 | 0.183327 | -0.088271 | -0.361037 | -0.361037 | 0.272765 | 0.489362 | 0.357143 | 0.428571 | 0.357143 | 0.571429 |  | 14 | target_rr_below_3:14 |
| filtered_model | turtle_soup | 70 | model_rules | 11 | 3 | 3 |  | 80.0 | 2.07436 | 2.586894 | 2.0 | 1.522192 | 0.588068 | 0.502851 | 0.502851 | 0.085217 | 6.312607 | 0.666667 | 0.666667 | 0.666667 |  |  | 3 | target_rr_below_3:3 |
