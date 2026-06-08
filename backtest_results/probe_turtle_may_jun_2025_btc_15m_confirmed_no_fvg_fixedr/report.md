# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 48
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 19 | 19 | 19 |  | 1.641483 | 1.059851 | 0.157895 | 2.0 | 80.0 | -0.162316 | 0.194826 | 0.078501 | 0.078501 | 0.116325 | 0.157895 | 0.526316 | 0.157895 | 0.631579 | 1.0 | 22.916667 | 15.7 | 22.333333 |  | 19 |
| turtle_soup | valid | 18 | 18 | 18 |  | 1.331595 | 1.221307 | 0.111111 | 2.0 | 76.111111 | -0.327841 | -0.123702 | -0.293095 | -0.293095 | 0.169393 | 0.111111 | 0.388889 | 0.111111 | 0.722222 | 1.0 | 12.538462 | 8.571429 | 24.5 |  | 18 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 37 | 37 | 37 |  | 1.490727 | 1.202998 | 0.135135 | 2.0 | 78.108108 | -0.242842 | 0.039866 | -0.102276 | -0.102276 | 0.142142 | 0.135135 | 0.459459 | 0.135135 | 0.675676 | 1.0 | 17.52 | 12.764706 | 23.2 |  | 37 |
