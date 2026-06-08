# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BNBUSDT
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
| turtle_soup | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BNBUSDT | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 18 | 18 | 18 |  | 2.916112 | 2.748511 | 0.388889 | 1.98242 | 76.111111 | -0.13546 | 0.3038 | 0.146994 | 0.146994 | 0.156402 | 0.000404 | 0.156806 | 0.388889 | 0.388889 | 0.166667 | 0.444444 | 1.0 | 4.0 | 1.285714 | 1.0 | 4 | 14 |
| turtle_soup | valid | 13 | 13 | 13 |  | 4.063755 | 2.539452 | 0.461538 | 2.909828 | 79.230769 | 1.139428 | 0.076923 | -0.094184 | -0.094184 | 0.184431 | -0.013324 | 0.171107 | 0.461538 | 0.538462 | 0.307692 | 0.538462 | 1.0 | 3.428571 | 2.857143 | 2.75 | 1 | 8 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 31 | 31 | 31 |  | 3.397381 | 2.602292 | 0.419355 | 2.371333 | 77.419355 | 0.39917 | 0.208658 | 0.045855 | 0.045855 | 0.168156 | -0.005353 | 0.162803 | 0.419355 | 0.451613 | 0.225806 | 0.483871 | 1.0 | 3.733333 | 2.071429 | 2.0 | 5 | 22 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 9 | 9 | 9 |  | 5.264991 | 4.574512 | 0.333333 | 5.18634 | 90.0 | 1.664807 | 0.472429 | 0.235893 | 0.235893 | 0.255109 | -0.018573 | 0.236536 | 0.333333 | 0.666667 | 0.555556 | 0.555556 | 1.0 | 3.6 | 1.333333 | 1.6 | 3 |  |
| turtle_soup | target_rr_below_2 | 17 | 17 | 17 |  | 2.773498 | 2.453975 | 0.588235 | 0.860074 | 70.0 | 0.058284 | 0.168661 | 0.037179 | 0.037179 | 0.131822 | -0.00034 | 0.131482 | 0.588235 | 0.352941 | 0.058824 | 0.352941 | 1.0 | 3.166667 | 2.5 | 1.0 | 1 | 17 |
| turtle_soup | target_rr_below_3 | 5 | 5 | 5 |  | 2.15689 | 2.539452 |  | 2.442602 | 80.0 | -0.719963 | -0.13014 | -0.266714 | -0.266714 | 0.135174 | 0.0014 | 0.136574 |  | 0.4 | 0.2 | 0.8 | 1.0 | 4.75 | 3.0 | 5.0 | 1 | 5 |
