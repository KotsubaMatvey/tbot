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
| turtle_soup | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 15 | 15 | 15 |  | 2.553912 | 2.286835 | 0.266667 | 2.0 | 80.0 | -0.095562 | -0.228895 | -0.5313 | -0.5313 | 0.302405 | 0.266667 | 0.333333 | 0.266667 | 0.666667 | 1.0 | 2.9 | 1.6 | 3.5 |  | 15 |
| turtle_soup | medium | 92 | 92 | 92 |  | 3.376118 | 2.062311 | 0.23913 | 2.0 | 60.0 | -0.149318 | 0.074374 | -0.206144 | -0.206144 | 0.280519 | 0.23913 | 0.51087 | 0.23913 | 0.695652 | 1.0 | 3.671875 | 3.680851 | 6.454545 | 12 | 92 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 107 | 107 | 107 |  | 3.260855 | 2.067388 | 0.242991 | 2.0 | 62.803738 | -0.141782 | 0.03186 | -0.251727 | -0.251727 | 0.283587 | 0.242991 | 0.485981 | 0.242991 | 0.691589 | 1.0 | 3.567568 | 3.480769 | 6.0 | 12 | 107 |
