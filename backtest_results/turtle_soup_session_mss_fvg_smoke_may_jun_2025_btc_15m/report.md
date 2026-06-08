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
- forward_bars: 32
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 14 | 14 | 14 |  | 1.017031 | 0.811241 | 0.571429 | 0.726529 | 71.428571 | -0.047789 | -0.044053 | -0.044053 | 0.571429 | 0.071429 |  | 0.285714 | 1.0 | 8.75 | 30.0 |  |  | 14 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 8 | 8 | 8 |  | 0.665767 | 0.674434 | 0.5 | 0.993731 | 73.75 | 0.084384 | 0.090921 | 0.090921 | 0.5 | 0.125 |  | 0.25 | 1.0 | 3.0 | 30.0 |  |  | 8 |
| turtle_soup | valid | 6 | 6 | 6 |  | 1.485383 | 1.340118 | 0.666667 | 0.370259 | 68.333333 | -0.224019 | -0.224019 | -0.224019 | 0.666667 |  |  | 0.333333 | 1.0 | 14.5 |  |  |  | 6 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 9 | 9 | 9 |  | 0.800121 | 0.817198 | 0.555556 | 0.91255 | 75.0 | 0.104242 | 0.110052 | 0.110052 | 0.555556 | 0.111111 |  | 0.222222 | 1.0 | 3.0 | 30.0 |  |  | 9 |
| turtle_soup | medium | 5 | 5 | 5 |  | 1.40747 | 0.805285 | 0.6 | 0.39169 | 65.0 | -0.321444 | -0.321444 | -0.321444 | 0.6 |  |  | 0.4 | 1.0 | 14.5 |  |  |  | 5 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_2 | 11 | 11 | 11 |  | 1.172057 | 0.817198 | 0.727273 | 0.379218 | 69.090909 | -0.082324 | -0.07757 | -0.07757 | 0.727273 | 0.090909 |  | 0.272727 | 1.0 | 10.666667 | 30.0 |  |  | 11 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 0.448603 | 0.299674 |  | 2.0 | 80.0 | 0.07884 | 0.07884 | 0.07884 |  |  |  | 0.333333 | 1.0 | 3.0 |  |  |  | 3 |
