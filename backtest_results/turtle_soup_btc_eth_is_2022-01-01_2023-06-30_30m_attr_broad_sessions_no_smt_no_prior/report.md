# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
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
| turtle_soup | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 954 | 954 | 954 |  | 8.870291 | 5.707936 | 0.401468 | 5.282104 | 64.989518 | 0.741513 | 0.443052 | -0.152398 | -0.152398 | 0.594978 | 0.000472 | 0.59545 | 0.401468 | 0.699161 | 0.480084 | 0.589099 | 1.0 | 2.94484 | 1.233883 | 1.408297 | 356 | 401 |
| turtle_soup | ETHUSDT | 926 | 926 | 926 |  | 9.542035 | 5.389827 | 0.339093 | 6.226262 | 65.593952 | 0.546607 | 0.376592 | -0.109381 | -0.109381 | 0.485956 | 1.7e-05 | 0.485973 | 0.339093 | 0.668467 | 0.463283 | 0.652268 | 1.0 | 3.153974 | 1.327948 | 1.356643 | 398 | 367 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 1003 | 1003 | 1003 |  | 6.372895 | 4.314322 | 0.377866 | 4.149873 | 63.489531 | 0.268543 | 0.452046 | 0.0704 | 0.0704 | 0.381458 | 0.000189 | 0.381647 | 0.377866 | 0.704885 | 0.384845 | 0.615155 | 1.0 | 3.398703 | 1.367751 | 1.650259 | 323 | 518 |
| turtle_soup | valid | 877 | 877 | 877 |  | 12.435768 | 7.777312 | 0.3626 | 7.573915 | 67.343216 | 1.07664 | 0.362592 | -0.361786 | -0.361786 | 0.724062 | 0.000316 | 0.724378 | 0.3626 | 0.660205 | 0.571266 | 0.625998 | 1.0 | 2.664845 | 1.170984 | 1.177645 | 431 | 250 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |
| turtle_soup | 1 | 274 | 274 | 274 |  | 7.531246 | 4.959743 | 0.354015 | 5.671722 | 65.072993 | 0.508246 | 0.42088 | -0.041095 | -0.041095 | 0.462054 | -7.9e-05 | 0.461975 | 0.354015 | 0.689781 | 0.441606 | 0.635036 | 1.0 | 3.408046 | 1.359788 | 1.471074 | 107 | 115 |
| turtle_soup | 10 | 23 | 23 | 23 |  | 6.423523 | 4.360566 | 0.521739 | 6.970016 | 62.173913 | 1.536592 | 0.447883 | -0.062063 | -0.062063 | 0.508799 | 0.001147 | 0.509946 | 0.521739 | 0.652174 | 0.304348 | 0.478261 | 1.0 | 2.0 | 1.066667 | 1.285714 | 5 | 13 |
| turtle_soup | 11 | 17 | 17 | 17 |  | 8.121552 | 5.676986 | 0.470588 | 3.120799 | 58.235294 | 0.381655 | 0.441577 | -0.19892 | -0.19892 | 0.62812 | 0.012377 | 0.640497 | 0.470588 | 0.647059 | 0.411765 | 0.529412 | 1.0 | 2.333333 | 1.0 | 1.0 | 5 | 10 |
| turtle_soup | 12 | 23 | 23 | 23 |  | 12.197763 | 8.088556 | 0.304348 | 6.231453 | 67.826087 | -0.015713 | 0.642165 | -0.071325 | -0.071325 | 0.71349 |  | 0.71349 | 0.304348 | 0.782609 | 0.521739 | 0.695652 | 1.0 | 2.625 | 1.0 | 1.083333 | 11 | 6 |
| turtle_soup | 13 | 22 | 22 | 22 |  | 10.573119 | 4.544747 | 0.272727 | 4.791507 | 63.636364 | 0.158668 | 0.230166 | -0.227916 | -0.227916 | 0.46172 | -0.003638 | 0.458082 | 0.272727 | 0.590909 | 0.318182 | 0.681818 | 1.0 | 2.066667 | 1.384615 | 1.571429 | 7 | 11 |
| turtle_soup | 14 | 15 | 15 | 15 |  | 3.932123 | 2.673363 | 0.666667 | 2.861483 | 63.333333 | 0.988051 | 0.6 | 0.083815 | 0.083815 | 0.518993 | -0.002807 | 0.516185 | 0.666667 | 0.8 | 0.4 | 0.333333 | 1.0 | 4.8 | 1.333333 | 1.166667 | 2 | 10 |
| turtle_soup | 15 | 16 | 16 | 16 |  | 9.604174 | 3.982921 | 0.5 | 3.359593 | 57.5 | -0.017996 | 0.706756 | 0.345853 | 0.345853 | 0.360903 |  | 0.360903 | 0.5 | 0.8125 | 0.25 | 0.5 | 1.0 | 2.375 | 1.461538 | 1.25 | 4 | 11 |
| turtle_soup | 16 | 10 | 10 | 10 |  | 7.690985 | 3.650444 | 0.5 | 4.75542 | 59.0 | 1.22444 | 0.6 | 0.160915 | 0.160915 | 0.440039 | -0.000954 | 0.439086 | 0.5 | 0.8 | 0.4 | 0.5 | 1.0 | 4.2 | 1.375 | 1.0 | 2 | 6 |
| turtle_soup | 17 | 7 | 7 | 7 |  | 8.257918 | 2.662679 | 0.285714 | 11.931858 | 61.428571 | 0.357874 | -0.488563 | -1.109987 | -1.109987 | 0.620826 | 0.000599 | 0.621425 | 0.285714 | 0.142857 | 0.142857 | 0.714286 | 1.0 | 1.2 | 1.0 | 1.0 | 2 | 3 |
| turtle_soup | 18 | 9 | 9 | 9 |  | 13.080935 | 9.813501 | 0.333333 | 7.943565 | 68.888889 | -0.069451 | -0.333333 | -0.843911 | -0.843911 | 0.510578 |  | 0.510578 | 0.333333 | 0.333333 | 0.222222 | 0.666667 | 1.0 | 1.166667 | 1.666667 | 2.5 | 3 | 5 |
| turtle_soup | 19 | 11 | 11 | 11 |  | 7.750393 | 4.103967 | 0.363636 | 4.938555 | 65.454545 | -0.015927 | 0.584084 | 0.141917 | 0.141917 | 0.440499 | 0.001667 | 0.442166 | 0.363636 | 0.727273 | 0.272727 | 0.636364 | 1.0 | 2.142857 | 1.25 | 1.0 | 5 | 6 |
| turtle_soup | 2 | 200 | 200 | 200 |  | 10.658754 | 6.709408 | 0.34 | 6.494687 | 66.65 | 0.774183 | 0.434432 | -0.139608 | -0.139608 | 0.57432 | -0.00028 | 0.57404 | 0.34 | 0.71 | 0.5 | 0.655 | 1.0 | 3.396947 | 1.338028 | 1.34 | 88 | 67 |
| turtle_soup | 20 | 11 | 11 | 11 |  | 7.173716 | 4.374376 | 0.818182 | 4.686892 | 59.090909 | 1.702315 | 0.745 | 0.546895 | 0.546895 | 0.199066 | -0.00096 | 0.198105 | 0.818182 | 0.818182 | 0.727273 | 0.181818 | 1.0 | 2.5 | 1.111111 | 1.375 | 2 | 7 |
| turtle_soup | 21 | 5 | 5 | 5 |  | 3.358708 | 4.113234 | 0.8 | 2.102521 | 62.0 | 1.438062 | 0.490431 | 0.319826 | 0.319826 | 0.170605 |  | 0.170605 | 0.8 | 0.6 | 0.6 | 0.2 | 1.0 | 2.0 | 1.333333 | 2.333333 |  | 5 |
| turtle_soup | 22 | 2 | 2 | 2 |  | 5.463893 | 5.463893 | 0.5 | 2.434618 | 60.0 | 1.296786 |  | -0.371106 | -0.371106 | 0.359312 | 0.011794 | 0.371106 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 2.0 | 1.0 | 7.0 |  | 1 |
| turtle_soup | 23 | 2 | 2 | 2 |  | 12.273181 | 12.273181 | 0.5 | 2.377293 | 60.0 | 0.07972 | 1.0 | 0.5179 | 0.5179 | 0.4821 |  | 0.4821 | 0.5 | 1.0 | 0.5 | 0.5 | 1.0 | 3.0 | 1.5 | 1.0 |  | 1 |
| turtle_soup | 24 | 5 | 5 | 5 |  | 6.758768 | 2.555797 | 0.4 | 2.388836 | 56.0 | -0.105425 | 0.492408 | 0.094006 | 0.094006 | 0.390606 | 0.007796 | 0.398402 | 0.4 | 0.6 | 0.4 | 0.6 | 1.0 | 4.333333 | 1.0 | 1.0 | 2 | 4 |
| turtle_soup | 25 | 5 | 5 | 5 |  | 5.655313 | 4.512768 | 1.0 | 3.756582 | 62.0 | 3.756582 | 1.0 | 0.314146 | 0.314146 | 0.674945 | 0.010909 | 0.685854 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.8 | 2.0 |  | 3 |
| turtle_soup | 26 | 3 | 3 | 3 |  | 18.786988 | 12.407469 | 0.333333 | 4.623189 | 63.333333 | 2.43244 | -0.333333 | -0.739084 | -0.739084 | 0.405751 |  | 0.405751 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 2.5 | 1.0 | 1.0 |  | 1 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1880 | 1880 | 1880 |  | 9.201161 | 5.570947 | 0.370745 | 5.747152 | 65.287234 | 0.645512 | 0.410317 | -0.13121 | -0.13121 | 0.541279 | 0.000248 | 0.541527 | 0.370745 | 0.684043 | 0.471809 | 0.620213 | 1.0 | 3.053173 | 1.27916 | 1.383315 | 754 | 768 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 1183 | 1183 | 1183 |  | 11.369984 | 7.61017 | 0.254438 | 8.179249 | 72.290786 | 0.807493 | 0.382976 | -0.288851 | -0.288851 | 0.671638 | 0.000189 | 0.671827 | 0.254438 | 0.689772 | 0.553677 | 0.733728 | 1.0 | 2.974654 | 1.143382 | 1.276336 | 650 | 71 |
| turtle_soup | medium | 697 | 697 | 697 |  | 5.520074 | 3.56956 | 0.568149 | 1.619218 | 53.400287 | 0.370586 | 0.456722 | 0.136349 | 0.136349 | 0.320022 | 0.00035 | 0.320372 | 0.568149 | 0.674319 | 0.332855 | 0.427547 | 1.0 | 3.281879 | 1.514894 | 1.685345 | 104 | 697 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1112 | 1112 | 1112 |  | 11.659219 | 7.824304 | 0.235612 | 8.588181 | 72.158273 | 0.833838 | 0.37526 | -0.317653 | -0.317653 | 0.692678 | 0.000235 | 0.692913 | 0.235612 | 0.68705 | 0.563849 | 0.751799 | 1.0 | 2.983254 | 1.128272 | 1.240829 | 641 |  |
| turtle_soup | target_rr_below_2 | 500 | 500 | 500 |  | 5.076485 | 2.922953 | 0.652 | 1.163474 | 51.6 | 0.348776 | 0.472212 | 0.202886 | 0.202886 | 0.268657 | 0.000669 | 0.269326 | 0.652 | 0.658 | 0.266 | 0.342 | 1.0 | 3.432749 | 1.617021 | 1.578947 | 38 | 500 |
| turtle_soup | target_rr_below_3 | 268 | 268 | 268 |  | 6.697345 | 4.720194 | 0.406716 | 2.510643 | 62.313433 | 0.417709 | 0.440299 | 0.019073 | 0.019073 | 0.421707 | -0.000481 | 0.421225 | 0.406716 | 0.720149 | 0.473881 | 0.593284 | 1.0 | 3.012579 | 1.300518 | 1.88189 | 75 | 268 |
