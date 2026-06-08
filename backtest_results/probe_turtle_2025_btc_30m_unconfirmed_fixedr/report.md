# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 564 | 564 | 564 |  | 4.791 | 3.061911 | 0.257092 | 2.0 | 80.0 | -0.183372 | -0.013726 | -0.46594 | -0.46594 | 0.452214 | 0.257092 | 0.471631 | 0.257092 | 0.721631 | 1.0 | 2.904177 | 2.646617 | 4.517241 | 74 | 564 |
| turtle_soup | low | 269 | 269 | 269 |  | 5.215164 | 3.389615 | 0.263941 | 2.0 | 40.0 | -0.185192 | 0.000681 | -0.536022 | -0.536022 | 0.536704 | 0.263941 | 0.475836 | 0.263941 | 0.72119 | 1.0 | 3.345361 | 2.617188 | 4.521127 | 43 | 269 |
| turtle_soup | medium | 4101 | 4101 | 4101 |  | 5.11468 | 3.12092 | 0.254084 | 2.0 | 60.0 | -0.205474 | -0.040865 | -0.512559 | -0.512559 | 0.471695 | 0.254084 | 0.462082 | 0.254084 | 0.73031 | 1.0 | 3.248414 | 2.686544 | 3.930902 | 515 | 4101 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 4934 | 4934 | 4934 |  | 5.083159 | 3.148417 | 0.254966 | 2.0 | 61.195784 | -0.201842 | -0.035497 | -0.50851 | -0.50851 | 0.473012 | 0.254966 | 0.463924 | 0.254966 | 0.72882 | 1.0 | 3.214683 | 2.678025 | 4.031797 | 632 | 4934 |
