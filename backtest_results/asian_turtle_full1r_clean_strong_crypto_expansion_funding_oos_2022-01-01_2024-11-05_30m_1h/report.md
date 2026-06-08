# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, SOLUSDT, BNBUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, LINKUSDT, AVAXUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | ADAUSDT | 27 | 27 | 27 |  | 3.276518 | 2.414588 | 0.444444 | 2.528877 | 78.148148 | 0.392235 | 0.244877 | 0.101253 | 0.101253 | 0.14101 | 0.002613 | 0.143624 | 0.444444 | 0.518519 | 0.222222 | 0.518519 | 1.0 | 5.071429 | 3.428571 | 3.666667 | 1 | 17 |
| turtle_soup | AVAXUSDT | 27 | 27 | 27 |  | 6.883303 | 2.774765 | 0.333333 | 5.271245 | 80.0 | 0.79567 | 0.555556 | 0.434934 | 0.434934 | 0.12264 | -0.002018 | 0.120621 | 0.333333 | 0.777778 | 0.296296 | 0.62963 | 1.0 | 3.470588 | 3.809524 | 2.0 | 6 | 15 |
| turtle_soup | BNBUSDT | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |
| turtle_soup | BTCUSDT | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.151911 | 0.151911 | 0.189034 | 0.001847 | 0.190881 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |
| turtle_soup | DOGEUSDT | 26 | 26 | 26 |  | 5.168951 | 2.122267 | 0.461538 | 2.423454 | 75.384615 | 0.585634 | -0.074779 | -0.248045 | -0.248045 | 0.17109 | 0.002176 | 0.173266 | 0.461538 | 0.307692 | 0.153846 | 0.5 | 1.0 | 3.307692 | 1.25 | 1.75 | 1 | 20 |
| turtle_soup | LINKUSDT | 37 | 37 | 37 |  | 3.512612 | 2.543938 | 0.540541 | 2.185577 | 75.675676 | 0.284328 | 0.399121 | 0.275121 | 0.275121 | 0.126565 | -0.002566 | 0.124 | 0.540541 | 0.594595 | 0.243243 | 0.432432 | 1.0 | 3.6875 | 2.227273 | 1.888889 | 4 | 30 |
| turtle_soup | SOLUSDT | 33 | 33 | 33 |  | 3.177162 | 2.572817 | 0.30303 | 2.947212 | 76.666667 | -0.362204 | 0.185449 | 0.069389 | 0.069389 | 0.116274 | -0.000213 | 0.11606 | 0.30303 | 0.454545 | 0.181818 | 0.666667 | 1.0 | 4.181818 | 1.533333 | 2.0 | 6 | 23 |
| turtle_soup | XRPUSDT | 22 | 22 | 22 |  | 6.208009 | 2.115775 | 0.272727 | 3.107258 | 80.0 | -0.135934 | 0.274343 | 0.088822 | 0.088822 | 0.177253 | 0.008269 | 0.185521 | 0.272727 | 0.545455 | 0.227273 | 0.681818 | 1.0 | 5.2 | 2.833333 | 2.6 | 6 | 13 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 132 | 132 | 132 |  | 3.927562 | 2.356067 | 0.537879 | 1.705281 | 74.242424 | 0.208682 | 0.334998 | 0.19102 | 0.19102 | 0.14233 | 0.001649 | 0.143979 | 0.537879 | 0.492424 | 0.128788 | 0.393939 | 1.0 | 4.288462 | 4.369231 | 2.588235 | 12 | 112 |
| turtle_soup | valid | 135 | 135 | 135 |  | 4.374242 | 2.389285 | 0.355556 | 3.474605 | 78.814815 | 0.294914 | 0.227982 | 0.062078 | 0.062078 | 0.16674 | -0.000836 | 0.165904 | 0.355556 | 0.533333 | 0.251852 | 0.622222 | 1.0 | 3.904762 | 1.958333 | 2.058824 | 23 | 83 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 267 | 267 | 267 |  | 4.153411 | 2.37782 | 0.445693 | 2.599883 | 76.554307 | 0.252282 | 0.280889 | 0.125824 | 0.125824 | 0.154672 | 0.000393 | 0.155065 | 0.445693 | 0.513109 | 0.191011 | 0.509363 | 1.0 | 4.051471 | 3.10219 | 2.235294 | 35 | 195 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 72 | 72 | 72 |  | 6.284589 | 4.172477 | 0.194444 | 6.315813 | 90.0 | 0.735479 | 0.60072 | 0.400663 | 0.400663 | 0.202092 | -0.002035 | 0.200057 | 0.194444 | 0.791667 | 0.472222 | 0.75 | 1.0 | 3.814815 | 1.736842 | 1.911765 | 28 |  |
| turtle_soup | target_rr_below_2 | 164 | 164 | 164 |  | 3.059073 | 1.689601 | 0.615854 | 0.991533 | 70.0 | 0.155008 | 0.185343 | 0.053929 | 0.053929 | 0.130668 | 0.000746 | 0.131414 | 0.615854 | 0.390244 | 0.060976 | 0.353659 | 1.0 | 4.155172 | 4.25 | 3.2 | 4 | 164 |
| turtle_soup | target_rr_below_3 | 31 | 31 | 31 |  | 4.992983 | 2.539452 | 0.129032 | 2.478027 | 80.0 | -0.355367 | 0.043526 | -0.132159 | -0.132159 | 0.171525 | 0.00416 | 0.175685 | 0.129032 | 0.516129 | 0.225806 | 0.774194 | 1.0 | 4.333333 | 3.375 | 2.428571 | 3 | 31 |
