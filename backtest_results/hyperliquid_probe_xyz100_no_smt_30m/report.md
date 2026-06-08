# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_hyperliquid_recent_2026-02-10_2026-05-25
- models: turtle_soup
- symbols: XYZ100
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 9.0
- slippage_bps: 2.0
- commission_points: 0.0
- slippage_points: 0.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | medium | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 11 | 11 | 11 |  | 2.909467 | 2.575092 | 0.181818 | 2.0 | 60.0 | -0.454545 |  | -1.351898 | -1.351898 | 1.351898 | 0.181818 | 0.545455 | 0.181818 | 0.818182 | 1.0 | 3.888889 | 3.333333 | 3.0 | 3 | 11 |
