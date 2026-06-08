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
- timeframes: 30m, 1h
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
| turtle_soup | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 20 | 20 | 20 |  | 3.788684 | 4.015297 | 0.75 | 1.535259 | 73.0 | 0.781995 | 0.756623 | 0.551558 | 0.551558 | 0.207006 | -0.001941 | 0.205065 | 0.75 | 0.8 | 0.45 | 0.2 | 1.0 | 10.75 | 2.4375 | 1.444444 |  | 18 |
| turtle_soup | LINKUSDT | 21 | 21 | 21 |  | 3.031591 | 2.795639 | 0.52381 | 1.859083 | 74.285714 | 0.374016 | 0.519548 | 0.38682 | 0.38682 | 0.132491 | 0.000236 | 0.132728 | 0.52381 | 0.666667 | 0.238095 | 0.428571 | 1.0 | 3.555556 | 1.714286 | 3.2 | 2 | 17 |
| turtle_soup | XRPUSDT | 17 | 17 | 17 |  | 4.993655 | 2.699944 | 0.352941 | 3.647997 | 82.941176 | 0.920624 | 0.476039 | 0.335812 | 0.335812 | 0.144259 | -0.004032 | 0.140227 | 0.352941 | 0.647059 | 0.411765 | 0.411765 | 1.0 | 3.428571 | 1.909091 | 3.857143 | 2 | 8 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 25 | 25 | 25 |  | 3.563352 | 2.808628 | 0.52 | 2.040285 | 77.6 | 0.344161 | 0.779142 | 0.648245 | 0.648245 | 0.133033 | -0.002136 | 0.130897 | 0.52 | 0.8 | 0.28 | 0.4 | 1.0 | 3.5 | 1.85 | 3.428571 | 4 | 17 |
| turtle_soup | valid | 33 | 33 | 33 |  | 4.098347 | 2.795639 | 0.575758 | 2.447113 | 75.454545 | 0.925479 | 0.444154 | 0.262335 | 0.262335 | 0.183303 | -0.001485 | 0.181819 | 0.575758 | 0.636364 | 0.424242 | 0.30303 | 1.0 | 6.4 | 2.238095 | 2.285714 |  | 26 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 58 | 58 | 58 |  | 3.867745 | 2.795639 | 0.551724 | 2.271756 | 76.37931 | 0.674911 | 0.588545 | 0.428676 | 0.428676 | 0.161635 | -0.001765 | 0.15987 | 0.551724 | 0.706897 | 0.362069 | 0.344828 | 1.0 | 4.95 | 2.04878 | 2.666667 | 4 | 43 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 15 | 15 | 15 |  | 3.573433 | 3.174917 | 0.2 | 5.333086 | 90.0 | 1.26267 | 0.733333 | 0.602401 | 0.602401 | 0.132603 | -0.001671 | 0.130932 | 0.2 | 0.866667 | 0.6 | 0.533333 | 1.0 | 6.0 | 1.769231 | 3.888889 | 2 |  |
| turtle_soup | target_rr_below_2 | 36 | 36 | 36 |  | 3.365867 | 2.795639 | 0.722222 | 0.97671 | 70.0 | 0.425953 | 0.532035 | 0.365786 | 0.365786 | 0.167514 | -0.001264 | 0.166249 | 0.722222 | 0.638889 | 0.25 | 0.25 | 1.0 | 3.888889 | 2.217391 | 1.555556 | 1 | 36 |
| turtle_soup | target_rr_below_3 | 7 | 7 | 7 |  | 7.079504 | 2.480546 | 0.428571 | 2.371997 | 80.0 | 0.695784 | 0.568911 | 0.37984 | 0.37984 | 0.193614 | -0.004544 | 0.18907 | 0.428571 | 0.714286 | 0.428571 | 0.428571 | 1.0 | 5.333333 | 2.0 | 2.333333 | 1 | 7 |
