# ICT Decision Score Threshold Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nyopen_tfdir_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- thresholds: 0

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 83 | 83 |  | 74.337349 | 3.744969 | 2.469999 | 1.799331 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 1.796979 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 11 | 69 | target_rr_below_2:61;target_rr_below_3:8 |
| filtered_all | ALL | 0 | model_rules | 52 | 31 | 31 |  | 72.903226 | 4.047282 | 2.314313 | 1.364171 | 0.467763 | 0.550748 | 0.360492 | 0.360492 | 0.190256 |  | 0.190256 | 2.881708 | 0.741935 | 0.612903 | 0.096774 | 0.225806 | 1 | 28 | target_rr_below_2:25;target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 83 | 83 |  | 74.337349 | 3.744969 | 2.469999 | 1.799331 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 1.796979 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 11 | 69 | target_rr_below_2:61;target_rr_below_3:8 |
| filtered_model | turtle_soup | 0 | model_rules | 52 | 31 | 31 |  | 72.903226 | 4.047282 | 2.314313 | 1.364171 | 0.467763 | 0.550748 | 0.360492 | 0.360492 | 0.190256 |  | 0.190256 | 2.881708 | 0.741935 | 0.612903 | 0.096774 | 0.225806 | 1 | 28 | target_rr_below_2:25;target_rr_below_3:3 |
