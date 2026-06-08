# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: None
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 46 | 46 | 46 |  | 3.539862 | 1.941838 | 0.652174 | 1.426051 | 73.478261 | 0.429609 | 0.459775 | 0.26442 | 0.26442 | 0.195356 |  | 0.195356 | 0.652174 | 0.565217 | 0.108696 | 0.26087 | 1.0 | 4.5 | 5.576923 | 3.4 | 3 | 41 |
| turtle_soup | valid | 48 | 48 | 48 |  | 3.585833 | 1.783 | 0.416667 | 2.143274 | 75.833333 | -0.126723 | 0.266529 | 0.042536 | 0.042536 | 0.223993 |  | 0.223993 | 0.416667 | 0.5 | 0.208333 | 0.5625 | 1.0 | 3.37037 | 2.666667 | 3.2 | 8 | 35 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 94 | 94 | 94 |  | 3.563336 | 1.936007 | 0.531915 | 1.792293 | 74.680851 | 0.145525 | 0.361096 | 0.151117 | 0.151117 | 0.209979 |  | 0.209979 | 0.531915 | 0.531915 | 0.159574 | 0.414894 | 1.0 | 3.717949 | 4.18 | 3.266667 | 11 | 76 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 18 | 18 | 18 |  | 6.179403 | 3.995654 | 0.111111 | 4.886192 | 90.0 | 0.079448 | 0.666667 | 0.343841 | 0.343841 | 0.322826 |  | 0.322826 | 0.111111 | 0.833333 | 0.555556 | 0.777778 | 1.0 | 3.285714 | 2.333333 | 3.5 | 9 |  |
| turtle_soup | target_rr_below_2 | 68 | 68 | 68 |  | 3.087206 | 1.634934 | 0.705882 | 0.882212 | 70.0 | 0.261439 | 0.352104 | 0.17136 | 0.17136 | 0.180743 |  | 0.180743 | 0.705882 | 0.470588 | 0.058824 | 0.264706 | 1.0 | 4.0 | 4.65625 | 2.75 | 1 | 68 |
| turtle_soup | target_rr_below_3 | 8 | 8 | 8 |  | 1.724293 | 1.1187 |  | 2.566705 | 80.0 | -0.691073 | -0.25 | -0.454575 | -0.454575 | 0.204575 |  | 0.204575 |  | 0.375 | 0.125 | 0.875 | 1.0 | 3.857143 | 8.333333 | 3.0 | 1 | 8 |
