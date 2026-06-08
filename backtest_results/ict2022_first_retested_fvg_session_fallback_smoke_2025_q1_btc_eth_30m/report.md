# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ict2022_mss_fvg
- symbols: BTCUSDT, ETHUSDT
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
| ict2022_mss_fvg | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 6 | 6 | 6 |  | 0.803423 | 0.404074 | 0.333333 | 1.034367 | 84.666667 | -0.601952 | -0.601952 | -0.65235 | -0.65235 | 0.050332 | 6.6e-05 | 0.050398 | 0.333333 |  |  | 0.666667 | 1.166667 | 4.0 |  |  | 1 | 6 |
| ict2022_mss_fvg | ETHUSDT | 5 | 5 | 5 |  | 0.711947 | 0.523499 | 0.2 | 0.917827 | 82.0 | -0.742158 | -0.671079 | -0.708976 | -0.708976 | 0.037602 | 0.000295 | 0.037897 | 0.2 | 0.2 |  | 0.8 | 1.0 | 4.5 | 1.0 |  | 1 | 5 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 11 | 11 | 11 |  | 0.761843 | 0.40913 | 0.272727 | 0.981394 | 83.454545 | -0.665682 | -0.633373 | -0.678089 | -0.678089 | 0.044546 | 0.00017 | 0.044716 | 0.272727 | 0.090909 |  | 0.727273 | 1.090909 | 4.25 | 1.0 |  | 2 | 11 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | target_rr_below_2 | 7 | 7 | 7 |  | 1.096272 | 1.138922 | 0.428571 | 0.399333 | 80.857143 | -0.474643 | -0.423872 | -0.481043 | -0.481043 | 0.05717 |  | 0.05717 | 0.428571 | 0.142857 |  | 0.571429 | 1.0 | 2.25 | 1.0 |  | 2 | 7 |
| ict2022_mss_fvg | target_rr_below_3 | 4 | 4 | 4 |  | 0.176592 | 0.170424 |  | 2.0 | 88.0 | -1.0 | -1.0 | -1.022921 | -1.022921 | 0.022452 | 0.000468 | 0.02292 |  |  |  | 1.0 | 1.25 | 6.25 |  |  |  | 4 |
