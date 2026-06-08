# ICT Decision Score Threshold Report

- events: `backtest_results\reclaimed_ob_sequence_may_oct_2025_30m_btc\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_all | ALL | 0 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |
| all | ALL | 50 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_all | ALL | 50 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |
| all | ALL | 70 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_all | ALL | 70 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | reclaimed_ob | 0 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_model | reclaimed_ob | 0 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |
| model | reclaimed_ob | 50 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_model | reclaimed_ob | 50 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |
| model | reclaimed_ob | 70 | none |  | 10 | 1 | 1 | 97.5 | 1.324589 | 1.324589 | 29.424176 | -1.0 | 0.5 | 0.5 |  | 0.1 |  | 0.1 |  | 3 | target_rr_below_3:2;target_rr_below_2:1 |
| filtered_model | reclaimed_ob | 70 | model_rules | 1 | 9 | 1 | 1 | 98.888889 | 1.324589 | 1.324589 | 32.670927 | -1.0 | 0.5 | 0.5 |  | 0.111111 |  | 0.111111 |  | 2 | target_rr_below_3:2 |
