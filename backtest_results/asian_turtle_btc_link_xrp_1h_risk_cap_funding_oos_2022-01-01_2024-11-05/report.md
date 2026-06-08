# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2019-09-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, LINKUSDT, XRPUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2019-09-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.216078 | 0.216078 | 0.149745 | 0.002564 | 0.15231 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |
| turtle_soup | LINKUSDT | 16 | 16 | 16 |  | 2.679932 | 2.684082 | 0.5 | 3.098861 | 76.875 | 0.326794 | 0.252959 | 0.152411 | 0.152411 | 0.105155 | -0.004607 | 0.100548 | 0.5 | 0.4375 | 0.1875 | 0.4375 | 1.0 | 3.571429 | 1.857143 | 2.0 | 2 | 12 |
| turtle_soup | XRPUSDT | 11 | 11 | 11 |  | 6.167213 | 2.822024 | 0.272727 | 4.592722 | 84.545455 | 0.162855 | 0.484406 | 0.261453 | 0.261453 | 0.212265 | 0.010689 | 0.222953 | 0.272727 | 0.636364 | 0.454545 | 0.636364 | 1.0 | 6.285714 | 1.571429 | 2.6 | 5 | 4 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 30 | 30 | 30 |  | 4.196376 | 2.013803 | 0.6 | 1.682603 | 73.666667 | 0.474484 | 0.42254 | 0.29688 | 0.29688 | 0.123705 | 0.001955 | 0.125659 | 0.6 | 0.5 | 0.066667 | 0.266667 | 1.0 | 5.5 | 5.0 | 2.5 | 1 | 27 |
| turtle_soup | valid | 28 | 28 | 28 |  | 3.417701 | 1.983325 | 0.285714 | 3.606584 | 80.357143 | -0.272858 | 0.289987 | 0.110949 | 0.110949 | 0.176727 | 0.002312 | 0.179038 | 0.285714 | 0.571429 | 0.25 | 0.714286 | 1.0 | 3.95 | 1.6875 | 2.142857 | 9 | 15 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 58 | 58 | 58 |  | 3.820464 | 2.013803 | 0.448276 | 2.611422 | 76.896552 | 0.113698 | 0.358549 | 0.20712 | 0.20712 | 0.149302 | 0.002127 | 0.151429 | 0.448276 | 0.534483 | 0.155172 | 0.482759 | 1.0 | 4.392857 | 3.290323 | 2.222222 | 10 | 42 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 16 | 16 | 16 |  | 5.795956 | 3.751715 | 0.1875 | 6.22685 | 90.0 | -0.043881 | 0.625 | 0.392255 | 0.392255 | 0.2302 | 0.002544 | 0.232745 | 0.1875 | 0.8125 | 0.4375 | 0.8125 | 1.0 | 3.384615 | 1.384615 | 2.428571 | 8 |  |
| turtle_soup | target_rr_below_2 | 34 | 34 | 34 |  | 3.193389 | 1.462477 | 0.647059 | 0.905279 | 70.0 | 0.191465 | 0.258701 | 0.135803 | 0.135803 | 0.120662 | 0.002236 | 0.122898 | 0.647059 | 0.382353 |  | 0.294118 | 1.0 | 4.6 | 4.307692 |  | 1 | 34 |
| turtle_soup | target_rr_below_3 | 8 | 8 | 8 |  | 2.534543 | 1.700225 | 0.125 | 2.631671 | 80.0 | 0.098348 | 0.25 | 0.139949 | 0.139949 | 0.109221 | 0.000831 | 0.110051 | 0.125 | 0.625 | 0.25 | 0.625 | 1.0 | 6.6 | 5.6 | 1.5 | 1 | 8 |
