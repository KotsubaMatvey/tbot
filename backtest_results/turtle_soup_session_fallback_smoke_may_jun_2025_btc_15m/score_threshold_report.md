# ICT Decision Score Threshold Report

- events: `backtest_results\turtle_soup_session_fallback_smoke_may_jun_2025_btc_15m\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 434 | 434 |  | 59.700461 | 5.753539 | 3.495033 | 2.464828 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 63 | 324 | target_rr_below_2:247;target_rr_below_3:77 |
| filtered_all | ALL | 0 | model_rules | 247 | 187 | 187 |  | 68.663102 | 7.797645 | 5.439492 | 4.397716 | -0.3561 | -0.083127 | -0.083127 | 0.149733 | 0.454545 | 0.283422 | 0.834225 | 48 | 77 | target_rr_below_3:77 |
| all | ALL | 50 | none |  | 434 | 434 |  | 59.700461 | 5.753539 | 3.495033 | 2.464828 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 63 | 324 | target_rr_below_2:247;target_rr_below_3:77 |
| filtered_all | ALL | 50 | model_rules | 247 | 187 | 187 |  | 68.663102 | 7.797645 | 5.439492 | 4.397716 | -0.3561 | -0.083127 | -0.083127 | 0.149733 | 0.454545 | 0.283422 | 0.834225 | 48 | 77 | target_rr_below_3:77 |
| all | ALL | 70 | none |  | 157 | 157 |  | 72.611465 | 7.743865 | 5.25808 | 4.44427 | -0.497131 | -0.173359 | -0.173359 | 0.146497 | 0.414013 | 0.229299 | 0.840764 | 43 | 47 | target_rr_below_2:36;target_rr_below_3:11 |
| filtered_all | ALL | 70 | model_rules | 36 | 121 | 121 |  | 73.38843 | 8.40453 | 5.45307 | 5.437514 | -0.516761 | -0.126669 | -0.126669 | 0.090909 | 0.454545 | 0.272727 | 0.892562 | 41 | 11 | target_rr_below_3:11 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 434 | 434 |  | 59.700461 | 5.753539 | 3.495033 | 2.464828 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 63 | 324 | target_rr_below_2:247;target_rr_below_3:77 |
| filtered_model | turtle_soup | 0 | model_rules | 247 | 187 | 187 |  | 68.663102 | 7.797645 | 5.439492 | 4.397716 | -0.3561 | -0.083127 | -0.083127 | 0.149733 | 0.454545 | 0.283422 | 0.834225 | 48 | 77 | target_rr_below_3:77 |
| model | turtle_soup | 50 | none |  | 434 | 434 |  | 59.700461 | 5.753539 | 3.495033 | 2.464828 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 63 | 324 | target_rr_below_2:247;target_rr_below_3:77 |
| filtered_model | turtle_soup | 50 | model_rules | 247 | 187 | 187 |  | 68.663102 | 7.797645 | 5.439492 | 4.397716 | -0.3561 | -0.083127 | -0.083127 | 0.149733 | 0.454545 | 0.283422 | 0.834225 | 48 | 77 | target_rr_below_3:77 |
| model | turtle_soup | 70 | none |  | 157 | 157 |  | 72.611465 | 7.743865 | 5.25808 | 4.44427 | -0.497131 | -0.173359 | -0.173359 | 0.146497 | 0.414013 | 0.229299 | 0.840764 | 43 | 47 | target_rr_below_2:36;target_rr_below_3:11 |
| filtered_model | turtle_soup | 70 | model_rules | 36 | 121 | 121 |  | 73.38843 | 8.40453 | 5.45307 | 5.437514 | -0.516761 | -0.126669 | -0.126669 | 0.090909 | 0.454545 | 0.272727 | 0.892562 | 41 | 11 | target_rr_below_3:11 |
