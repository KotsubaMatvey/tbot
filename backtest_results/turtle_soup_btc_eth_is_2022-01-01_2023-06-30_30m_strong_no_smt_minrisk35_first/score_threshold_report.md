# ICT Decision Score Threshold Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_strong_no_smt_minrisk35_first\events.csv`
- thresholds: 0, 50, 70, 80, 90

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_all | ALL | 0 | model_rules | 548 | 143 | 143 |  | 58.881119 | 3.886768 | 2.997317 | 3.19023 | 0.258488 | 0.538457 | 0.350612 | 0.350612 | 0.187745 | 0.0001 | 0.187845 | 2.313148 | 0.426573 | 0.748252 | 0.363636 | 0.559441 | 31 | 93 | target_rr_below_2:66;target_rr_below_3:27 |
| all | ALL | 50 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_all | ALL | 50 | model_rules | 548 | 143 | 143 |  | 58.881119 | 3.886768 | 2.997317 | 3.19023 | 0.258488 | 0.538457 | 0.350612 | 0.350612 | 0.187745 | 0.0001 | 0.187845 | 2.313148 | 0.426573 | 0.748252 | 0.363636 | 0.559441 | 31 | 93 | target_rr_below_2:66;target_rr_below_3:27 |
| all | ALL | 70 | none |  | 461 | 461 |  | 72.494577 | 11.735978 | 7.715604 | 7.86335 | 0.977721 | 0.381283 | -0.276802 | -0.276802 | 0.657872 | 0.000213 | 0.658084 | 0.514489 | 0.26898 | 0.687636 | 0.59436 | 0.713666 | 257 | 28 | target_rr_below_2:15;target_rr_below_3:13 |
| filtered_all | ALL | 70 | model_rules | 411 | 50 | 50 |  | 70.0 | 4.207604 | 3.156514 | 6.119219 | -0.107099 | 0.48 | 0.279876 | 0.279876 | 0.200621 | -0.000497 | 0.200124 | 1.895315 | 0.14 | 0.74 | 0.46 | 0.84 | 22 |  |  |
| all | ALL | 80 | none |  | 64 | 64 |  | 87.96875 | 9.448711 | 6.95389 | 6.903961 | 0.64395 | 0.40625 | -0.17816 | -0.17816 | 0.58441 |  | 0.58441 | 0.649939 | 0.234375 | 0.703125 | 0.640625 | 0.734375 | 34 | 13 | target_rr_below_3:13 |
| filtered_all | ALL | 80 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 90 | none |  | 51 | 51 |  | 90.0 | 9.995996 | 7.080395 | 8.031311 | 0.800928 | 0.45098 | -0.175045 | -0.175045 | 0.626025 |  | 0.626025 | 0.643599 | 0.215686 | 0.72549 | 0.705882 | 0.745098 | 31 |  |  |
| filtered_all | ALL | 90 | model_rules | 51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_model | turtle_soup | 0 | model_rules | 548 | 143 | 143 |  | 58.881119 | 3.886768 | 2.997317 | 3.19023 | 0.258488 | 0.538457 | 0.350612 | 0.350612 | 0.187745 | 0.0001 | 0.187845 | 2.313148 | 0.426573 | 0.748252 | 0.363636 | 0.559441 | 31 | 93 | target_rr_below_2:66;target_rr_below_3:27 |
| model | turtle_soup | 50 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_model | turtle_soup | 50 | model_rules | 548 | 143 | 143 |  | 58.881119 | 3.886768 | 2.997317 | 3.19023 | 0.258488 | 0.538457 | 0.350612 | 0.350612 | 0.187745 | 0.0001 | 0.187845 | 2.313148 | 0.426573 | 0.748252 | 0.363636 | 0.559441 | 31 | 93 | target_rr_below_2:66;target_rr_below_3:27 |
| model | turtle_soup | 70 | none |  | 461 | 461 |  | 72.494577 | 11.735978 | 7.715604 | 7.86335 | 0.977721 | 0.381283 | -0.276802 | -0.276802 | 0.657872 | 0.000213 | 0.658084 | 0.514489 | 0.26898 | 0.687636 | 0.59436 | 0.713666 | 257 | 28 | target_rr_below_2:15;target_rr_below_3:13 |
| filtered_model | turtle_soup | 70 | model_rules | 411 | 50 | 50 |  | 70.0 | 4.207604 | 3.156514 | 6.119219 | -0.107099 | 0.48 | 0.279876 | 0.279876 | 0.200621 | -0.000497 | 0.200124 | 1.895315 | 0.14 | 0.74 | 0.46 | 0.84 | 22 |  |  |
| model | turtle_soup | 80 | none |  | 64 | 64 |  | 87.96875 | 9.448711 | 6.95389 | 6.903961 | 0.64395 | 0.40625 | -0.17816 | -0.17816 | 0.58441 |  | 0.58441 | 0.649939 | 0.234375 | 0.703125 | 0.640625 | 0.734375 | 34 | 13 | target_rr_below_3:13 |
| filtered_model | turtle_soup | 80 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | turtle_soup | 90 | none |  | 51 | 51 |  | 90.0 | 9.995996 | 7.080395 | 8.031311 | 0.800928 | 0.45098 | -0.175045 | -0.175045 | 0.626025 |  | 0.626025 | 0.643599 | 0.215686 | 0.72549 | 0.705882 | 0.745098 | 31 |  |  |
| filtered_model | turtle_soup | 90 | model_rules | 51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
