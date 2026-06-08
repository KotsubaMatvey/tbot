# ICT Decision Score Threshold Report

- events: `backtest_results\turtle_soup_btc_eth_late_control_2025-01-01_2026-04-20_15m_30m_stability_minrisk25\events.csv`
- thresholds: 0, 50, 70, 80, 90

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 956 | 956 |  | 68.828452 | 10.316673 | 6.779519 | 7.585108 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.543008 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 479 | 217 | target_rr_below_2:113;target_rr_below_3:104 |
| filtered_all | ALL | 0 | model_rules | 775 | 181 | 181 |  | 61.823204 | 5.055828 | 3.50706 | 3.496189 | 0.434106 | 0.606548 | 0.362758 | 0.362758 | 0.243847 | -5.7e-05 | 0.24379 | 2.525398 | 0.39779 | 0.790055 | 0.480663 | 0.574586 | 57 | 95 | target_rr_below_2:53;target_rr_below_3:42 |
| all | ALL | 50 | none |  | 956 | 956 |  | 68.828452 | 10.316673 | 6.779519 | 7.585108 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.543008 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 479 | 217 | target_rr_below_2:113;target_rr_below_3:104 |
| filtered_all | ALL | 50 | model_rules | 775 | 181 | 181 |  | 61.823204 | 5.055828 | 3.50706 | 3.496189 | 0.434106 | 0.606548 | 0.362758 | 0.362758 | 0.243847 | -5.7e-05 | 0.24379 | 2.525398 | 0.39779 | 0.790055 | 0.480663 | 0.574586 | 57 | 95 | target_rr_below_2:53;target_rr_below_3:42 |
| all | ALL | 70 | none |  | 758 | 758 |  | 72.506596 | 11.130139 | 8.226545 | 9.081709 | 1.085335 | 0.461741 | -0.350943 | -0.350943 | 0.812705 | -2.1e-05 | 0.812685 | 0.413734 | 0.224274 | 0.730871 | 0.622691 | 0.742744 | 444 | 19 | target_rr_below_3:10;target_rr_below_2:9 |
| filtered_all | ALL | 70 | model_rules | 672 | 86 | 86 |  | 70.0 | 5.186919 | 4.15594 | 5.342532 | 0.373843 | 0.674419 | 0.395076 | 0.395076 | 0.279434 | -9.2e-05 | 0.279342 | 2.914114 | 0.209302 | 0.837209 | 0.581395 | 0.732558 | 44 |  |  |
| all | ALL | 80 | none |  | 100 | 100 |  | 89.0 | 11.847389 | 8.557542 | 9.790743 | 2.198957 | 0.44 | -0.269814 | -0.269814 | 0.709814 |  | 0.709814 | 0.513728 | 0.21 | 0.72 | 0.59 | 0.71 | 53 | 10 | target_rr_below_3:10 |
| filtered_all | ALL | 80 | model_rules | 100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 90 | none |  | 90 | 90 |  | 90.0 | 12.509703 | 9.233127 | 10.597154 | 2.325771 | 0.422222 | -0.339249 | -0.339249 | 0.761471 |  | 0.761471 | 0.424456 | 0.166667 | 0.711111 | 0.577778 | 0.744444 | 52 |  |  |
| filtered_all | ALL | 90 | model_rules | 90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 956 | 956 |  | 68.828452 | 10.316673 | 6.779519 | 7.585108 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.543008 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 479 | 217 | target_rr_below_2:113;target_rr_below_3:104 |
| filtered_model | turtle_soup | 0 | model_rules | 775 | 181 | 181 |  | 61.823204 | 5.055828 | 3.50706 | 3.496189 | 0.434106 | 0.606548 | 0.362758 | 0.362758 | 0.243847 | -5.7e-05 | 0.24379 | 2.525398 | 0.39779 | 0.790055 | 0.480663 | 0.574586 | 57 | 95 | target_rr_below_2:53;target_rr_below_3:42 |
| model | turtle_soup | 50 | none |  | 956 | 956 |  | 68.828452 | 10.316673 | 6.779519 | 7.585108 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.543008 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 479 | 217 | target_rr_below_2:113;target_rr_below_3:104 |
| filtered_model | turtle_soup | 50 | model_rules | 775 | 181 | 181 |  | 61.823204 | 5.055828 | 3.50706 | 3.496189 | 0.434106 | 0.606548 | 0.362758 | 0.362758 | 0.243847 | -5.7e-05 | 0.24379 | 2.525398 | 0.39779 | 0.790055 | 0.480663 | 0.574586 | 57 | 95 | target_rr_below_2:53;target_rr_below_3:42 |
| model | turtle_soup | 70 | none |  | 758 | 758 |  | 72.506596 | 11.130139 | 8.226545 | 9.081709 | 1.085335 | 0.461741 | -0.350943 | -0.350943 | 0.812705 | -2.1e-05 | 0.812685 | 0.413734 | 0.224274 | 0.730871 | 0.622691 | 0.742744 | 444 | 19 | target_rr_below_3:10;target_rr_below_2:9 |
| filtered_model | turtle_soup | 70 | model_rules | 672 | 86 | 86 |  | 70.0 | 5.186919 | 4.15594 | 5.342532 | 0.373843 | 0.674419 | 0.395076 | 0.395076 | 0.279434 | -9.2e-05 | 0.279342 | 2.914114 | 0.209302 | 0.837209 | 0.581395 | 0.732558 | 44 |  |  |
| model | turtle_soup | 80 | none |  | 100 | 100 |  | 89.0 | 11.847389 | 8.557542 | 9.790743 | 2.198957 | 0.44 | -0.269814 | -0.269814 | 0.709814 |  | 0.709814 | 0.513728 | 0.21 | 0.72 | 0.59 | 0.71 | 53 | 10 | target_rr_below_3:10 |
| filtered_model | turtle_soup | 80 | model_rules | 100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | turtle_soup | 90 | none |  | 90 | 90 |  | 90.0 | 12.509703 | 9.233127 | 10.597154 | 2.325771 | 0.422222 | -0.339249 | -0.339249 | 0.761471 |  | 0.761471 | 0.424456 | 0.166667 | 0.711111 | 0.577778 | 0.744444 | 52 |  |  |
| filtered_model | turtle_soup | 90 | model_rules | 90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
