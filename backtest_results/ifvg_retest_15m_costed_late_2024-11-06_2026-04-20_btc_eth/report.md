# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ifvg_retest
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 96
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | BTCUSDT | 179 | 179 | 56 |  | 24.796717 | 13.71632 | 0.083799 | 7.248325 | 69.564246 | 0.260837 | 0.085776 | -1.603771 | -1.603771 | 0.527899 | 0.000674 | 0.528573 | 0.083799 | 0.122905 | 0.089385 | 0.22905 | 7.597765 | 1.219512 | 1.045455 | 1.0625 | 32 | 61 |
| ifvg_retest | ETHUSDT | 148 | 148 | 54 |  | 41.118805 | 20.278325 | 0.087838 | 8.200608 | 69.858108 | 0.049971 | -0.014833 | -1.194738 | -1.194738 | 0.430506 |  | 0.430506 | 0.087838 | 0.135135 | 0.094595 | 0.277027 | 5.459459 | 1.243902 | 1.05 | 1.142857 | 29 | 54 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 327 | 327 | 110 |  | 32.809378 | 17.225855 | 0.085627 | 7.679327 | 69.697248 | 0.157321 | 0.036386 | -1.402973 | -1.402973 | 0.483819 | 0.000369 | 0.484188 | 0.085627 | 0.12844 | 0.091743 | 0.250765 | 6.629969 | 1.231707 | 1.047619 | 1.1 | 61 | 115 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 166 | 166 | 55 |  | 28.948721 | 19.948017 | 0.078313 | 7.558066 | 71.975904 | 0.120339 | -0.03983 | -1.365818 | -1.365818 | 0.439333 |  | 0.439333 | 0.078313 | 0.114458 | 0.084337 | 0.253012 | 6.945783 | 1.142857 | 1.0 | 1.0 | 34 | 60 |
| ifvg_retest | valid | 161 | 161 | 55 |  | 36.670035 | 13.552319 | 0.093168 | 7.804355 | 67.347826 | 0.194303 | 0.112603 | -1.440128 | -1.440128 | 0.529687 | 0.000749 | 0.530436 | 0.093168 | 0.142857 | 0.099379 | 0.248447 | 6.304348 | 1.325 | 1.086957 | 1.1875 | 27 | 55 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 212 | 212 | 80 |  | 37.418813 | 20.278325 | 0.066038 | 10.933691 | 75.5 | 0.217461 | 0.008731 | -1.595546 | -1.595546 | 0.604818 | 0.000569 | 0.605387 | 0.066038 | 0.122642 | 0.099057 | 0.311321 | 5.985849 | 1.212121 | 1.038462 | 1.142857 | 52 |  |
| ifvg_retest | medium | 115 | 115 | 30 |  | 20.517552 | 12.498404 | 0.121739 | 1.67998 | 59.0 | -0.003052 | 0.110135 | -0.889446 | -0.889446 | 0.26076 |  | 0.26076 | 0.121739 | 0.13913 | 0.078261 | 0.13913 | 7.817391 | 1.3125 | 1.0625 | 1.0 | 9 | 115 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 212 | 212 | 80 |  | 37.418813 | 20.278325 | 0.066038 | 10.933691 | 75.5 | 0.217461 | 0.008731 | -1.595546 | -1.595546 | 0.604818 | 0.000569 | 0.605387 | 0.066038 | 0.122642 | 0.099057 | 0.311321 | 5.985849 | 1.212121 | 1.038462 | 1.142857 | 52 |  |
| ifvg_retest | target_rr_below_2 | 76 | 76 | 21 |  | 18.727367 | 11.145507 | 0.171053 | 1.249619 | 55.631579 | 0.243855 | 0.305252 | -0.490222 | -0.490222 | 0.219802 |  | 0.219802 | 0.171053 | 0.171053 | 0.105263 | 0.105263 | 8.092105 | 1.25 | 1.0 | 1.0 | 4 | 76 |
| ifvg_retest | target_rr_below_3 | 39 | 39 | 9 |  | 24.694649 | 17.746058 | 0.025641 | 2.518631 | 65.564103 | -0.579168 | -0.345139 | -1.820968 | -1.820968 | 0.340576 |  | 0.340576 | 0.025641 | 0.076923 | 0.025641 | 0.205128 | 7.282051 | 1.375 | 1.333333 | 1.0 | 5 | 39 |
