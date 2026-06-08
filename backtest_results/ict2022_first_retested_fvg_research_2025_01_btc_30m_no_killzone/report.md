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
| ict2022_mss_fvg | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 4 | 4 | 4 |  | 1.413827 | 1.22513 | 0.5 | 1.043812 | 78.0 | 0.5 | 0.25 | 0.20695 | 0.20695 | 0.046121 | -0.00307 | 0.04305 | 0.5 | 0.5 | 0.5 | 0.5 | 1.0 | 1.5 | 11.5 | 17.5 | 1 | 4 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 3 | 3 | 3 |  | 0.902327 | 0.399018 | 0.333333 | 0.725082 | 81.333333 |  | -0.166667 | -0.205289 | -0.205289 | 0.042716 | -0.004094 | 0.038622 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 1.0 | 1.5 | 20.0 | 21.0 | 1 | 3 |
| ict2022_mss_fvg | medium | 1 | 1 | 1 |  | 2.948328 | 2.948328 | 1.0 | 2.0 | 68.0 | 2.0 | 1.5 | 1.443666 | 1.443666 | 0.056334 |  | 0.056334 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 3.0 | 14.0 |  | 1 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | missing_required_killzone;target_rr_below_3 | 1 | 1 | 1 |  | 2.948328 | 2.948328 | 1.0 | 2.0 | 68.0 | 2.0 | 1.5 | 1.443666 | 1.443666 | 0.056334 |  | 0.056334 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 3.0 | 14.0 |  | 1 |
| ict2022_mss_fvg | target_rr_below_2 | 2 | 2 | 2 |  | 0.327869 | 0.327869 |  | 0.087623 | 78.0 | -1.0 | -1.0 | -1.033322 | -1.033322 | 0.033322 |  | 0.033322 |  |  |  | 1.0 | 1.0 | 1.5 |  |  | 1 | 2 |
| ict2022_mss_fvg | target_rr_below_3 | 1 | 1 | 1 |  | 2.051241 | 2.051241 | 1.0 | 2.0 | 88.0 | 2.0 | 1.5 | 1.450777 | 1.450777 | 0.061505 | -0.012282 | 0.049223 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 20.0 | 21.0 |  | 1 |
