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
| turtle_soup | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 54 | 54 | 54 |  | 3.433678 | 2.206441 | 0.574074 | 1.757029 | 74.074074 | 0.182021 | 0.41518 | 0.256549 | 0.256549 | 0.157761 | 0.00087 | 0.158631 | 0.574074 | 0.555556 | 0.166667 | 0.388889 | 1.0 | 4.47619 | 3.4 | 1.555556 | 5 | 45 |
| turtle_soup | LINKUSDT | 34 | 34 | 34 |  | 3.811561 | 3.073448 | 0.470588 | 2.733091 | 75.882353 | 0.366833 | 0.454402 | 0.3512 | 0.3512 | 0.105013 | -0.001811 | 0.103202 | 0.470588 | 0.617647 | 0.264706 | 0.470588 | 1.0 | 3.9375 | 1.904762 | 3.222222 | 4 | 26 |
| turtle_soup | XRPUSDT | 27 | 27 | 27 |  | 4.397244 | 2.699944 | 0.259259 | 4.024345 | 83.333333 | 0.438527 | 0.475682 | 0.321652 | 0.321652 | 0.150242 | 0.003788 | 0.15403 | 0.259259 | 0.62963 | 0.407407 | 0.555556 | 1.0 | 4.6 | 2.764706 | 5.181818 | 8 | 11 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 58 | 58 | 58 |  | 3.591231 | 2.432381 | 0.551724 | 1.747864 | 74.827586 | 0.327747 | 0.409148 | 0.291403 | 0.291403 | 0.117774 | -2.9e-05 | 0.117745 | 0.551724 | 0.517241 | 0.155172 | 0.344828 | 1.0 | 3.9 | 4.133333 | 6.0 | 4 | 47 |
| turtle_soup | valid | 57 | 57 | 57 |  | 3.955191 | 2.881517 | 0.385965 | 3.422559 | 78.77193 | 0.265479 | 0.473373 | 0.308381 | 0.308381 | 0.163424 | 0.001567 | 0.164992 | 0.385965 | 0.666667 | 0.350877 | 0.561404 | 1.0 | 4.625 | 1.710526 | 2.3 | 13 | 35 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 115 | 115 | 115 |  | 3.771628 | 2.699944 | 0.469565 | 2.57793 | 76.782609 | 0.296884 | 0.440981 | 0.299818 | 0.299818 | 0.140401 | 0.000762 | 0.141163 | 0.469565 | 0.591304 | 0.252174 | 0.452174 | 1.0 | 4.346154 | 2.779412 | 3.448276 | 17 | 82 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 33 | 33 | 33 |  | 5.238977 | 3.73571 | 0.181818 | 6.028053 | 90.0 | 0.508291 | 0.757576 | 0.569319 | 0.569319 | 0.187317 | 0.00094 | 0.188257 | 0.181818 | 0.878788 | 0.545455 | 0.69697 | 1.0 | 4.347826 | 1.586207 | 3.222222 | 13 |  |
| turtle_soup | target_rr_below_2 | 70 | 70 | 70 |  | 3.290432 | 2.368282 | 0.657143 | 0.959271 | 70.0 | 0.218377 | 0.296149 | 0.174325 | 0.174325 | 0.120679 | 0.001146 | 0.121824 | 0.657143 | 0.442857 | 0.114286 | 0.314286 | 1.0 | 4.0 | 3.580645 | 4.75 | 1 | 70 |
| turtle_soup | target_rr_below_3 | 12 | 12 | 12 |  | 2.5434 | 2.204792 | 0.166667 | 2.532276 | 80.0 | 0.173472 | 0.415198 | 0.290734 | 0.290734 | 0.126426 | -0.001961 | 0.124464 | 0.166667 | 0.666667 | 0.25 | 0.583333 | 1.0 | 5.428571 | 4.0 | 1.333333 | 3 | 12 |
