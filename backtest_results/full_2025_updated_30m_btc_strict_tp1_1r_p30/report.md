# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: ifvg_retest, reclaimed_ob, rejection_block
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 37 | 37 | 16 |  | 23.110541 | 9.828739 | 0.108108 | 3.309464 | 100.0 | 0.00499 | -0.146507 | -0.146507 | 0.108108 | 0.108108 | 0.081081 | 0.324324 | 3.823529 | 1.0 | 1.5 | 1.0 |  | 22 |
| reclaimed_ob | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 37 | 37 | 16 |  | 23.110541 | 9.828739 | 0.108108 | 3.309464 | 100.0 | 0.00499 | -0.146507 | -0.146507 | 0.108108 | 0.108108 | 0.081081 | 0.324324 | 3.823529 | 1.0 | 1.5 | 1.0 |  | 22 |
| reclaimed_ob | body_edge | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | body_level | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 37 | 37 | 16 |  | 23.110541 | 9.828739 | 0.108108 | 3.309464 | 100.0 | 0.00499 | -0.146507 | -0.146507 | 0.108108 | 0.108108 | 0.081081 | 0.324324 | 3.823529 | 1.0 | 1.5 | 1.0 |  | 22 |
| reclaimed_ob | mean_threshold | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | wick_extreme | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 37 | 37 | 16 |  | 23.110541 | 9.828739 | 0.108108 | 3.309464 | 100.0 | 0.00499 | -0.146507 | -0.146507 | 0.108108 | 0.108108 | 0.081081 | 0.324324 | 3.823529 | 1.0 | 1.5 | 1.0 |  | 22 |
| reclaimed_ob | conservative | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | conservative | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 124 | 124 | 90 | 2 | 7.056012 | 2.816983 | 0.201613 | 3.505869 | 93.556452 | -0.212402 | -0.137739 | -0.137739 | 0.201613 | 0.282258 | 0.129032 | 0.516129 | 1.983471 | 1.796875 | 1.285714 | 1.5625 |  | 90 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 29 | 29 | 11 |  | 19.434948 | 10.46407 | 0.068966 | 2.956569 | 100.0 | -0.419042 | -0.484238 | -0.484238 | 0.068966 | 0.068966 | 0.034483 | 0.310345 | 3.814815 | 1.0 | 2.0 | 1.0 |  | 20 |
| ifvg_retest | premium | 8 | 8 | 5 |  | 31.196846 | 8.333197 | 0.25 | 4.58871 | 100.0 | 0.93786 | 0.596502 | 0.596502 | 0.25 | 0.25 | 0.25 | 0.375 | 3.857143 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | discount | 11 | 11 | 1 | 1 | 2.484971 | 2.484971 |  | 9.874933 | 91.272727 | -1.0 | -1.0 | -1.0 |  |  |  | 0.090909 | 2.636364 | 1.0 |  |  |  | 7 |
| reclaimed_ob | premium | 5 | 5 | 2 | 1 | 1.897621 | 1.897621 | 0.2 | 10.076685 | 94.6 | 0.5 | 0.35 | 0.35 | 0.2 | 0.2 | 0.2 | 0.2 | 2.0 | 1.0 | 1.0 | 2.0 |  | 3 |
| rejection_block | discount | 57 | 57 | 57 |  | 3.492335 | 2.18491 | 0.298246 | 2.077113 | 89.894737 | -0.265313 | -0.261424 | -0.261424 | 0.298246 | 0.333333 | 0.140351 | 0.684211 | 1.0 | 1.769231 | 1.315789 | 2.0 |  | 48 |
| rejection_block | premium | 14 | 14 | 14 |  | 4.280652 | 2.872404 | 0.214286 | 2.491031 | 92.857143 | -0.29094 | 0.367771 | 0.367771 | 0.214286 | 0.785714 | 0.285714 | 0.785714 | 1.0 | 2.909091 | 1.181818 | 1.0 |  | 10 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 14 | 14 | 6 |  | 22.592402 | 13.520444 | 0.071429 | 3.158612 | 100.0 | -0.304053 | -0.412837 | -0.412837 | 0.071429 | 0.071429 | 0.071429 | 0.357143 | 4.083333 | 1.0 | 1.0 | 1.0 |  | 7 |
| ifvg_retest | valid | 23 | 23 | 10 |  | 23.421425 | 8.843601 | 0.130435 | 3.401287 | 100.0 | 0.190416 | 0.013291 | 0.013291 | 0.130435 | 0.130435 | 0.086957 | 0.304348 | 3.681818 | 1.0 | 1.666667 | 1.0 |  | 15 |
| reclaimed_ob | none | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | none | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 37 | 37 | 16 |  | 23.110541 | 9.828739 | 0.108108 | 3.309464 | 100.0 | 0.00499 | -0.146507 | -0.146507 | 0.108108 | 0.108108 | 0.081081 | 0.324324 | 3.823529 | 1.0 | 1.5 | 1.0 |  | 22 |
| reclaimed_ob | high | 16 | 16 | 3 | 2 | 2.093404 | 2.484971 | 0.0625 | 9.93798 | 92.3125 |  | -0.1 | -0.1 | 0.0625 | 0.0625 | 0.0625 | 0.125 | 2.4375 | 1.0 | 1.0 | 2.0 |  | 10 |
| rejection_block | high | 71 | 71 | 71 |  | 3.647778 | 2.406238 | 0.28169 | 2.158731 | 90.478873 | -0.270366 | -0.137358 | -0.137358 | 0.28169 | 0.422535 | 0.169014 | 0.704225 | 1.0 | 2.02 | 1.266667 | 1.666667 |  | 58 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 15 | 15 | 8 |  | 25.779931 | 8.843601 | 0.133333 | 5.822999 | 100.0 | 0.306545 | 0.064581 | 0.064581 | 0.133333 | 0.133333 | 0.133333 | 0.4 | 4.285714 | 1.0 | 1.0 | 1.0 |  |  |
| ifvg_retest | target_rr_below_2 | 15 | 15 | 7 |  | 22.43092 | 14.983192 | 0.066667 | 1.157181 | 100.0 | -0.683592 | -0.6928 | -0.6928 | 0.066667 | 0.066667 |  | 0.4 | 2.714286 | 1.0 | 3.0 |  |  | 15 |
| ifvg_retest | target_rr_below_3 | 7 | 7 | 1 |  | 6.512768 | 6.512768 | 0.142857 | 2.535353 | 100.0 | 2.412625 | 1.988837 | 1.988837 | 0.142857 | 0.142857 | 0.142857 |  | 5.333333 |  | 1.0 | 1.0 |  | 7 |
| reclaimed_ob | none | 6 | 6 |  | 1 |  |  |  | 24.377738 | 99.5 |  |  |  |  |  |  |  | 3.0 |  |  |  |  |  |
| reclaimed_ob | target_rr_below_2 | 6 | 6 | 1 | 1 | 0.753978 | 0.753978 |  | 0.79021 | 83.666667 | -1.0 | -1.0 | -1.0 |  |  |  | 0.166667 | 2.333333 | 1.0 |  |  |  | 6 |
| reclaimed_ob | target_rr_below_3 | 4 | 4 | 2 |  | 2.763118 | 2.763118 | 0.25 | 2.0 | 94.5 | 0.5 | 0.35 | 0.35 | 0.25 | 0.25 | 0.25 | 0.25 | 1.75 | 1.0 | 1.0 | 2.0 |  | 4 |
| rejection_block | none | 13 | 13 | 13 |  | 4.446443 | 2.652439 |  | 5.253387 | 100.0 | -1.0 | -0.5 | -0.5 |  | 0.384615 | 0.076923 | 1.0 | 1.0 | 1.692308 | 1.2 | 1.0 |  |  |
| rejection_block | target_rr_below_2 | 41 | 41 | 41 |  | 3.490682 | 2.406238 | 0.365854 | 1.072149 | 85.658537 | -0.234451 | -0.129189 | -0.129189 | 0.365854 | 0.414634 | 0.121951 | 0.634146 | 1.0 | 1.769231 | 1.294118 | 1.0 |  | 41 |
| rejection_block | target_rr_below_3 | 17 | 17 | 17 |  | 3.415913 | 2.067388 | 0.294118 | 2.412809 | 94.823529 | 0.200971 | 0.120258 | 0.120258 | 0.294118 | 0.470588 | 0.352941 | 0.647059 | 1.0 | 3.0 | 1.25 | 2.333333 |  | 17 |
