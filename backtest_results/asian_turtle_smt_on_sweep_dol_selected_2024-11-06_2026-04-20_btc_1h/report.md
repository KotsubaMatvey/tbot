# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 8 | 8 | 8 |  | 4.323379 | 4.518039 | 0.875 | 2.131558 | 76.25 | 1.245612 | 1.124026 | 0.897895 | 0.897895 | 0.22613 | 0.875 | 0.875 | 0.75 | 0.125 | 1.0 | 22.0 | 1.142857 | 1.666667 |  | 6 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 6.07309 | 6.07309 | 0.5 | 4.581823 | 90.0 | 1.038037 | 1.269018 | 0.941504 | 0.941504 | 0.327514 | 0.5 | 1.0 | 1.0 | 0.5 | 1.0 | 22.0 | 1.5 | 2.0 |  |  |
| turtle_soup | target_rr_below_2 | 5 | 5 | 5 |  | 3.61533 | 3.666389 | 1.0 | 1.022426 | 70.0 | 1.022426 | 0.913164 | 0.725914 | 0.725914 | 0.18725 | 1.0 | 0.8 | 0.6 |  | 1.0 |  | 1.0 | 1.666667 |  | 5 |
| turtle_soup | target_rr_below_3 | 1 | 1 | 1 |  | 4.364205 | 4.364205 | 1.0 | 2.776694 | 80.0 | 2.776694 | 1.888347 | 1.670583 | 1.670583 | 0.217764 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
