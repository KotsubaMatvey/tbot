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
| turtle_soup | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 11 | 11 | 11 |  | 4.377282 | 4.514163 | 0.909091 | 1.767983 | 74.545455 | 1.123658 | 0.851659 | 0.641891 | 0.641891 | 0.21202 | -0.002252 | 0.209768 | 0.909091 | 0.818182 | 0.636364 | 0.090909 | 1.0 | 22.0 | 1.444444 | 1.571429 |  | 9 |
| turtle_soup | LINKUSDT | 11 | 11 | 11 |  | 3.649006 | 3.570459 | 0.636364 | 2.448662 | 75.454545 | 1.091941 | 0.763846 | 0.648021 | 0.648021 | 0.1158 | 2.5e-05 | 0.115825 | 0.636364 | 0.818182 | 0.363636 | 0.272727 | 1.0 | 6.333333 | 1.555556 | 3.5 |  | 8 |
| turtle_soup | XRPUSDT | 11 | 11 | 11 |  | 3.185612 | 2.699944 | 0.181818 | 4.221347 | 84.545455 | 0.723881 | 0.457913 | 0.339496 | 0.339496 | 0.122653 | -0.004236 | 0.118417 | 0.181818 | 0.636364 | 0.272727 | 0.545455 | 1.0 | 2.833333 | 1.571429 | 4.666667 | 2 | 4 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 15 | 15 | 15 |  | 3.315135 | 2.699944 | 0.533333 | 2.171903 | 78.666667 | 0.286859 | 0.694861 | 0.568626 | 0.568626 | 0.129416 | -0.003181 | 0.126235 | 0.533333 | 0.733333 | 0.2 | 0.4 | 1.0 | 2.666667 | 1.545455 | 3.666667 | 2 | 9 |
| turtle_soup | valid | 18 | 18 | 18 |  | 4.089104 | 4.436725 | 0.611111 | 3.346632 | 77.777778 | 1.557299 | 0.688038 | 0.521894 | 0.521894 | 0.167443 | -0.001299 | 0.166144 | 0.611111 | 0.777778 | 0.611111 | 0.222222 | 1.0 | 10.5 | 1.5 | 2.545455 |  | 12 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 33 | 33 | 33 |  | 3.7373 | 3.570459 | 0.575758 | 2.812664 | 78.181818 | 0.979827 | 0.691139 | 0.543136 | 0.543136 | 0.150158 | -0.002154 | 0.148003 | 0.575758 | 0.757576 | 0.424242 | 0.30303 | 1.0 | 5.8 | 1.52 | 2.785714 | 2 | 21 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 12 | 12 | 12 |  | 3.884943 | 3.827768 | 0.25 | 5.621035 | 90.0 | 1.542393 | 0.833333 | 0.694787 | 0.694787 | 0.140636 | -0.002089 | 0.138546 | 0.25 | 0.916667 | 0.583333 | 0.5 | 1.0 | 6.333333 | 1.636364 | 4.0 | 1 |  |
| turtle_soup | target_rr_below_2 | 18 | 18 | 18 |  | 3.852702 | 3.618424 | 0.833333 | 1.007996 | 70.0 | 0.640594 | 0.601401 | 0.452745 | 0.452745 | 0.149537 | -0.00088 | 0.148656 | 0.833333 | 0.666667 | 0.333333 | 0.166667 | 1.0 | 6.0 | 1.5 | 1.666667 |  | 18 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 2.454313 | 2.480546 | 0.333333 | 2.407191 | 80.0 | 0.764961 | 0.660792 | 0.478878 | 0.478878 | 0.191973 | -0.01006 | 0.181913 | 0.333333 | 0.666667 | 0.333333 | 0.333333 | 1.0 | 2.0 | 1.0 | 1.0 | 1 | 3 |
