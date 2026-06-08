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
| turtle_soup | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 139 | 139 | 139 |  | 6.353344 | 3.968481 | 0.251799 | 2.0 | 80.0 | -0.244604 | -0.079137 | -0.743898 | -0.743898 | 0.664761 | 0.251799 | 0.446043 | 0.251799 | 0.748201 | 1.0 | 3.451923 | 2.693548 | 5.542857 | 24 | 139 |
| turtle_soup | low | 71 | 71 | 71 |  | 7.602148 | 5.091363 | 0.15493 | 2.0 | 40.0 | -0.535211 | -0.253521 | -1.029673 | -1.029673 | 0.776151 | 0.15493 | 0.394366 | 0.15493 | 0.84507 | 1.0 | 3.733333 | 2.928571 | 3.818182 | 9 | 71 |
| turtle_soup | medium | 1375 | 1375 | 1375 |  | 6.664029 | 4.07536 | 0.249455 | 2.0 | 60.0 | -0.246222 | -0.050351 | -0.757932 | -0.757932 | 0.707581 | 0.249455 | 0.465455 | 0.249455 | 0.747636 | 1.0 | 3.790856 | 2.814062 | 4.38484 | 173 | 1375 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 1585 | 1585 | 1585 |  | 6.678805 | 4.105723 | 0.245426 | 2.0 | 60.858044 | -0.259026 | -0.061976 | -0.768873 | -0.768873 | 0.706897 | 0.245426 | 0.460568 | 0.245426 | 0.75205 | 1.0 | 3.758389 | 2.808219 | 4.473008 | 206 | 1585 |
