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
| ict2022_mss_fvg | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 29 | 29 | 29 |  | 1.088247 | 0.929422 | 0.37931 | 0.96474 | 81.103448 | -0.40546 | -0.391828 | -0.472493 | -0.472493 | 0.080439 | 0.000226 | 0.080665 | 0.37931 | 0.172414 |  | 0.586207 | 1.241379 | 5.882353 | 2.6 |  | 3 | 29 |
| ict2022_mss_fvg | ETHUSDT | 18 | 18 | 18 |  | 0.98159 | 0.593108 | 0.5 | 0.635353 | 79.666667 | -0.292705 | -0.300738 | -0.348517 | -0.348517 | 0.047588 | 0.00019 | 0.047778 | 0.5 | 0.111111 | 0.055556 | 0.5 | 1.222222 | 2.888889 | 3.5 | 14.0 | 2 | 18 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 47 | 47 | 47 |  | 1.0474 | 0.784322 | 0.425532 | 0.838592 | 80.553191 | -0.362277 | -0.356943 | -0.425013 | -0.425013 | 0.067858 | 0.000212 | 0.06807 | 0.425532 | 0.148936 | 0.021277 | 0.553191 | 1.234043 | 4.846154 | 2.857143 | 14.0 | 5 | 47 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | target_rr_below_2 | 35 | 35 | 35 |  | 1.106264 | 0.929863 | 0.542857 | 0.440395 | 78.0 | -0.278676 | -0.245279 | -0.32061 | -0.32061 | 0.075105 | 0.000227 | 0.075332 | 0.542857 | 0.171429 |  | 0.457143 | 1.2 | 2.75 | 2.333333 |  | 5 | 35 |
| ict2022_mss_fvg | target_rr_below_3 | 12 | 12 | 12 |  | 0.875711 | 0.432338 | 0.083333 | 2.0 | 88.0 | -0.606112 | -0.682631 | -0.72952 | -0.72952 | 0.046721 | 0.000168 | 0.046889 | 0.083333 | 0.083333 | 0.083333 | 0.833333 | 1.333333 | 8.2 | 6.0 | 14.0 |  | 12 |
