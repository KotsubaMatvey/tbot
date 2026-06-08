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
| turtle_soup | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 434 | 434 | 434 |  | 5.753539 | 3.495033 | 0.324885 | 2.464828 | 59.700461 | -0.252658 | -0.060407 | -0.060407 | 0.324885 | 0.40553 | 0.170507 | 0.665899 | 1.0 | 3.190311 | 2.232955 | 3.459459 | 63 | 324 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 157 | 157 | 157 |  | 7.743865 | 5.25808 | 0.146497 | 4.44427 | 72.611465 | -0.497131 | -0.173359 | -0.173359 | 0.146497 | 0.414013 | 0.229299 | 0.840764 | 1.0 | 3.340909 | 2.092308 | 3.472222 | 43 | 47 |
| turtle_soup | medium | 277 | 277 | 277 |  | 4.625449 | 2.970748 | 0.425993 | 1.342906 | 52.382671 | -0.114094 | 0.003612 | 0.003612 | 0.425993 | 0.400722 | 0.137184 | 0.566787 | 1.0 | 3.063694 | 2.315315 | 3.447368 | 20 | 277 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 110 | 110 | 110 |  | 8.596475 | 5.485946 | 0.090909 | 5.744482 | 72.727273 | -0.499104 | -0.131942 | -0.131942 | 0.090909 | 0.445455 | 0.290909 | 0.890909 | 1.0 | 3.255102 | 1.938776 | 3.75 | 38 |  |
| turtle_soup | target_rr_below_2 | 247 | 247 | 247 |  | 4.205977 | 2.574039 | 0.45749 | 1.001467 | 52.91498 | -0.174344 | -0.043207 | -0.043207 | 0.45749 | 0.368421 | 0.08502 | 0.538462 | 1.0 | 3.428571 | 2.296703 | 3.380952 | 15 | 247 |
| turtle_soup | target_rr_below_3 | 77 | 77 | 77 |  | 6.656459 | 5.267486 | 0.233766 | 2.473765 | 62.857143 | -0.151809 | -0.013391 | -0.013391 | 0.233766 | 0.467532 | 0.272727 | 0.753247 | 1.0 | 2.534483 | 2.472222 | 3.095238 | 10 | 77 |
