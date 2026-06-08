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
| ifvg_retest | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | BTCUSDT | 179 | 179 | 62 |  | 15.502215 | 7.840616 | 0.134078 | 4.907992 | 65.26257 | 0.436141 | 0.476691 | -0.575462 | -0.575462 | 0.363973 | 0.00046 | 0.364433 | 0.134078 | 0.201117 | 0.089385 | 0.212291 | 7.597765 | 3.026316 | 1.222222 | 1.25 | 19 | 103 |
| ifvg_retest | ETHUSDT | 148 | 148 | 59 |  | 23.910462 | 9.721344 | 0.128378 | 5.215023 | 66.344595 | -0.083205 | 0.068761 | -0.627723 | -0.627723 | 0.277693 | -4.1e-05 | 0.277652 | 0.128378 | 0.182432 | 0.108108 | 0.263514 | 5.459459 | 3.102564 | 2.259259 | 1.5625 | 24 | 80 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | opposite_boundary | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 327 | 327 | 121 |  | 19.602104 | 8.626381 | 0.131498 | 5.046954 | 65.752294 | 0.182906 | 0.277783 | -0.600945 | -0.600945 | 0.324923 | 0.000233 | 0.325156 | 0.131498 | 0.192661 | 0.097859 | 0.235474 | 6.629969 | 3.064935 | 1.666667 | 1.40625 | 43 | 183 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 166 | 166 | 58 |  | 17.518114 | 10.589814 | 0.120482 | 5.056797 | 68.421687 | 0.234629 | 0.242638 | -0.56868 | -0.56868 | 0.283509 | -3.7e-05 | 0.283473 | 0.120482 | 0.174699 | 0.090361 | 0.222892 | 6.945783 | 2.162162 | 1.413793 | 1.066667 | 24 | 90 |
| ifvg_retest | valid | 161 | 161 | 63 |  | 21.520698 | 7.470159 | 0.142857 | 5.036805 | 63.0 | 0.135288 | 0.310139 | -0.630649 | -0.630649 | 0.367622 | 0.000512 | 0.368134 | 0.142857 | 0.21118 | 0.10559 | 0.248447 | 6.304348 | 3.9 | 1.882353 | 1.705882 | 19 | 93 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 144 | 144 | 53 |  | 32.182305 | 19.033577 | 0.083333 | 9.657181 | 75.638889 | 0.466877 | 0.469288 | -0.822072 | -0.822072 | 0.474594 | 0.000698 | 0.475292 | 0.083333 | 0.208333 | 0.138889 | 0.284722 | 5.527778 | 2.146341 | 1.266667 | 1.55 | 33 |  |
| ifvg_retest | medium | 183 | 183 | 68 |  | 9.796948 | 5.199058 | 0.169399 | 1.419234 | 57.972678 | -0.038424 | 0.128522 | -0.428596 | -0.428596 | 0.207149 | -0.000132 | 0.207016 | 0.169399 | 0.180328 | 0.065574 | 0.196721 | 7.497268 | 4.111111 | 2.030303 | 1.166667 | 10 | 183 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 144 | 144 | 53 |  | 32.182305 | 19.033577 | 0.083333 | 9.657181 | 75.638889 | 0.466877 | 0.469288 | -0.822072 | -0.822072 | 0.474594 | 0.000698 | 0.475292 | 0.083333 | 0.208333 | 0.138889 | 0.284722 | 5.527778 | 2.146341 | 1.266667 | 1.55 | 33 |  |
| ifvg_retest | target_rr_below_2 | 137 | 137 | 50 |  | 9.12306 | 4.944704 | 0.20438 | 1.07592 | 55.518248 | 0.107735 | 0.254786 | -0.262213 | -0.262213 | 0.188862 | -0.000177 | 0.188685 | 0.20438 | 0.189781 | 0.065693 | 0.153285 | 7.59854 | 5.714286 | 2.230769 | 1.222222 | 4 | 137 |
| ifvg_retest | target_rr_below_3 | 46 | 46 | 18 |  | 11.668859 | 7.225852 | 0.065217 | 2.441714 | 65.282609 | -0.444421 | -0.22221 | -0.890771 | -0.890771 | 0.261611 |  | 0.261611 | 0.065217 | 0.152174 | 0.065217 | 0.326087 | 7.195652 | 1.866667 | 1.285714 | 1.0 | 6 | 46 |
