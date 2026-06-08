# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ict2022_mss_fvg
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 11 | 11 | 11 |  | 2.190972 | 1.34988 | 0.636364 | 0.979037 | 78.454545 | 0.243276 | 0.155124 | 0.063057 | 0.063057 | 0.088789 | 0.003277 | 0.092066 | 0.636364 | 0.181818 | 0.090909 | 0.272727 | 1.454545 | 3.666667 | 6.5 | 8.0 | 1 | 11 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 8 | 8 | 8 |  | 2.054706 | 1.139607 | 0.625 | 1.19583 | 80.5 | 0.364565 | 0.243356 | 0.182138 | 0.182138 | 0.056712 | 0.004507 | 0.061218 | 0.625 | 0.25 | 0.125 | 0.25 | 1.625 | 5.0 | 6.5 | 8.0 |  | 8 |
| ict2022_mss_fvg | valid | 3 | 3 | 3 |  | 2.554348 | 2.102447 | 0.666667 | 0.400921 | 73.0 | -0.080162 | -0.080162 | -0.254491 | -0.254491 | 0.174329 |  | 0.174329 | 0.666667 |  |  | 0.333333 | 1.0 | 1.0 |  |  | 1 | 3 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 10 | 10 | 10 |  | 2.317136 | 1.632519 | 0.6 | 1.058418 | 80.5 | 0.249081 | 0.152114 | 0.057016 | 0.057016 | 0.091493 | 0.003605 | 0.095098 | 0.6 | 0.2 | 0.1 | 0.3 | 1.5 | 3.666667 | 6.5 | 8.0 | 1 | 10 |
| ict2022_mss_fvg | medium | 1 | 1 | 1 |  | 0.929334 | 0.929334 | 1.0 | 0.18522 | 58.0 | 0.18522 | 0.18522 | 0.123473 | 0.123473 | 0.061747 |  | 0.061747 | 1.0 |  |  |  | 1.0 |  |  |  |  | 1 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | missing_required_killzone;target_rr_below_2 | 1 | 1 | 1 |  | 0.929334 | 0.929334 | 1.0 | 0.18522 | 58.0 | 0.18522 | 0.18522 | 0.123473 | 0.123473 | 0.061747 |  | 0.061747 | 1.0 |  |  |  | 1.0 |  |  |  |  | 1 |
| ict2022_mss_fvg | target_rr_below_2 | 6 | 6 | 6 |  | 2.992603 | 2.008802 | 0.833333 | 0.408652 | 75.5 | 0.16811 | 0.16811 | 0.039362 | 0.039362 | 0.128748 |  | 0.128748 | 0.833333 |  |  | 0.166667 | 1.0 | 1.0 |  |  | 1 | 6 |
| ict2022_mss_fvg | target_rr_below_3 | 4 | 4 | 4 |  | 1.303934 | 1.135078 | 0.25 | 2.033068 | 88.0 | 0.370538 | 0.12812 | 0.083496 | 0.083496 | 0.035611 | 0.009013 | 0.044624 | 0.25 | 0.5 | 0.25 | 0.5 | 2.25 | 5.0 | 6.5 | 8.0 |  | 4 |
