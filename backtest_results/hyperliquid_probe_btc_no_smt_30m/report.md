# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_hyperliquid_recent_2026-02-10_2026-05-25
- models: turtle_soup
- symbols: BTC
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.5
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 1 | 1 | 1 |  | 1.934512 | 1.934512 |  | 2.0 | 80.0 | -1.0 | 0.5 | 0.222117 | 0.222117 | 0.277883 |  | 1.0 |  | 1.0 | 1.0 | 7.0 | 5.0 |  | 1 | 1 |
| turtle_soup | medium | 12 | 12 | 12 |  | 4.799965 | 3.229185 | 0.25 | 2.0 | 60.0 | -0.083668 | 0.049866 | -0.291257 | -0.291257 | 0.341123 | 0.25 | 0.5 | 0.25 | 0.666667 | 1.0 | 2.25 | 3.166667 | 7.666667 |  | 12 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 13 | 13 | 13 |  | 4.579546 | 2.615719 | 0.230769 | 2.0 | 61.538462 | -0.154155 | 0.084492 | -0.251766 | -0.251766 | 0.336258 | 0.230769 | 0.538462 | 0.230769 | 0.692308 | 1.0 | 2.777778 | 3.428571 | 7.666667 | 1 | 13 |
