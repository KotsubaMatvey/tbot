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
| turtle_soup | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 13 | 13 | 13 |  | 1.279493 | 1.067202 | 0.230769 | 2.0 | 80.0 | -0.187186 | -0.325831 | -0.44165 | -0.44165 | 0.115819 | 0.230769 | 0.307692 | 0.230769 | 0.692308 | 1.0 | 3.777778 | 2.0 | 9.333333 |  | 13 |
| turtle_soup | medium | 85 | 85 | 85 |  | 1.82749 | 1.006663 | 0.211765 | 2.0 | 60.0 | 0.029815 | -0.033613 | -0.149754 | -0.149754 | 0.116141 | 0.211765 | 0.447059 | 0.211765 | 0.611765 | 1.0 | 5.846154 | 6.5 | 9.722222 | 3 | 85 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 98 | 98 | 98 |  | 1.754797 | 1.008183 | 0.214286 | 2.0 | 62.653061 | 0.001029 | -0.072377 | -0.188475 | -0.188475 | 0.116099 | 0.214286 | 0.428571 | 0.214286 | 0.622449 | 1.0 | 5.540984 | 6.071429 | 9.666667 | 3 | 98 |
