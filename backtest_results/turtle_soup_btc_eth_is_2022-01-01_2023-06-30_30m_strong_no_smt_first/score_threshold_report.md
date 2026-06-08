# ICT Decision Score Threshold Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_strong_no_smt_first\events.csv`
- thresholds: 0, 50, 70, 80, 90

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_all | ALL | 0 | model_rules | 428 | 263 | 263 |  | 61.596958 | 5.892325 | 3.834041 | 4.127498 | 0.22129 | 0.504905 | 0.146863 | 0.146863 | 0.357463 | 0.000578 | 0.358041 | 1.433826 | 0.353612 | 0.73384 | 0.414449 | 0.634981 | 93 | 137 | target_rr_below_2:84;target_rr_below_3:53 |
| all | ALL | 50 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_all | ALL | 50 | model_rules | 428 | 263 | 263 |  | 61.596958 | 5.892325 | 3.834041 | 4.127498 | 0.22129 | 0.504905 | 0.146863 | 0.146863 | 0.357463 | 0.000578 | 0.358041 | 1.433826 | 0.353612 | 0.73384 | 0.414449 | 0.634981 | 93 | 137 | target_rr_below_2:84;target_rr_below_3:53 |
| all | ALL | 70 | none |  | 461 | 461 |  | 72.494577 | 11.735978 | 7.715604 | 7.86335 | 0.977721 | 0.381283 | -0.276802 | -0.276802 | 0.657872 | 0.000213 | 0.658084 | 0.514489 | 0.26898 | 0.687636 | 0.59436 | 0.713666 | 257 | 28 | target_rr_below_2:15;target_rr_below_3:13 |
| filtered_all | ALL | 70 | model_rules | 335 | 126 | 126 |  | 70.0 | 6.797838 | 4.96838 | 6.706613 | 0.084795 | 0.444444 | -0.022425 | -0.022425 | 0.465974 | 0.000896 | 0.46687 | 0.945755 | 0.166667 | 0.722222 | 0.507937 | 0.81746 | 69 |  |  |
| all | ALL | 80 | none |  | 64 | 64 |  | 87.96875 | 9.448711 | 6.95389 | 6.903961 | 0.64395 | 0.40625 | -0.17816 | -0.17816 | 0.58441 |  | 0.58441 | 0.649939 | 0.234375 | 0.703125 | 0.640625 | 0.734375 | 34 | 13 | target_rr_below_3:13 |
| filtered_all | ALL | 80 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all | ALL | 90 | none |  | 51 | 51 |  | 90.0 | 9.995996 | 7.080395 | 8.031311 | 0.800928 | 0.45098 | -0.175045 | -0.175045 | 0.626025 |  | 0.626025 | 0.643599 | 0.215686 | 0.72549 | 0.705882 | 0.745098 | 31 |  |  |
| filtered_all | ALL | 90 | model_rules | 51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | profit_factor | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | turtle_soup | 0 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_model | turtle_soup | 0 | model_rules | 428 | 263 | 263 |  | 61.596958 | 5.892325 | 3.834041 | 4.127498 | 0.22129 | 0.504905 | 0.146863 | 0.146863 | 0.357463 | 0.000578 | 0.358041 | 1.433826 | 0.353612 | 0.73384 | 0.414449 | 0.634981 | 93 | 137 | target_rr_below_2:84;target_rr_below_3:53 |
| model | turtle_soup | 50 | none |  | 691 | 691 |  | 66.324168 | 10.102195 | 6.056164 | 5.828661 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.706199 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 304 | 258 | target_rr_below_2:154;target_rr_below_3:104 |
| filtered_model | turtle_soup | 50 | model_rules | 428 | 263 | 263 |  | 61.596958 | 5.892325 | 3.834041 | 4.127498 | 0.22129 | 0.504905 | 0.146863 | 0.146863 | 0.357463 | 0.000578 | 0.358041 | 1.433826 | 0.353612 | 0.73384 | 0.414449 | 0.634981 | 93 | 137 | target_rr_below_2:84;target_rr_below_3:53 |
| model | turtle_soup | 70 | none |  | 461 | 461 |  | 72.494577 | 11.735978 | 7.715604 | 7.86335 | 0.977721 | 0.381283 | -0.276802 | -0.276802 | 0.657872 | 0.000213 | 0.658084 | 0.514489 | 0.26898 | 0.687636 | 0.59436 | 0.713666 | 257 | 28 | target_rr_below_2:15;target_rr_below_3:13 |
| filtered_model | turtle_soup | 70 | model_rules | 335 | 126 | 126 |  | 70.0 | 6.797838 | 4.96838 | 6.706613 | 0.084795 | 0.444444 | -0.022425 | -0.022425 | 0.465974 | 0.000896 | 0.46687 | 0.945755 | 0.166667 | 0.722222 | 0.507937 | 0.81746 | 69 |  |  |
| model | turtle_soup | 80 | none |  | 64 | 64 |  | 87.96875 | 9.448711 | 6.95389 | 6.903961 | 0.64395 | 0.40625 | -0.17816 | -0.17816 | 0.58441 |  | 0.58441 | 0.649939 | 0.234375 | 0.703125 | 0.640625 | 0.734375 | 34 | 13 | target_rr_below_3:13 |
| filtered_model | turtle_soup | 80 | model_rules | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model | turtle_soup | 90 | none |  | 51 | 51 |  | 90.0 | 9.995996 | 7.080395 | 8.031311 | 0.800928 | 0.45098 | -0.175045 | -0.175045 | 0.626025 |  | 0.626025 | 0.643599 | 0.215686 | 0.72549 | 0.705882 | 0.745098 | 31 |  |  |
| filtered_model | turtle_soup | 90 | model_rules | 51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
