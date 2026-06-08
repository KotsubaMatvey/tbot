# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: rejection_block
- symbols: ETHUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | body_level | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | wick_extreme | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | conservative | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | discount | 18 | 18 | 7 |  | 2.210779 | 1.470714 |  | 16.143488 | 95.055556 | -0.814746 | -0.54851 | -0.633946 | -0.633946 | 0.033225 |  | 0.111111 |  | 0.333333 | 5.125 | 6.0 | 5.0 |  |  | 3 |
| rejection_block | premium | 38 | 38 | 14 |  | 2.883704 | 2.294107 | 0.052632 | 74.953177 | 99.605263 | 0.356427 | 0.460494 | 0.290468 | 0.290468 | 0.062641 | 0.052632 | 0.236842 | 0.105263 | 0.263158 | 4.628571 | 4.2 | 2.333333 | 2.75 | 4 | 2 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | high | 56 | 56 | 21 |  | 2.659396 | 2.071261 | 0.035714 | 56.050063 | 98.142857 | -0.033964 | 0.124159 | -0.01767 | -0.01767 | 0.053186 | 0.035714 | 0.196429 | 0.071429 | 0.285714 | 4.784314 | 4.875 | 2.818182 | 2.75 | 4 | 5 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 51 | 51 | 18 |  | 2.703217 | 1.977471 |  | 61.407236 | 99.411765 | -0.136976 | 0.060041 | -0.089687 | -0.089687 | 0.052845 |  | 0.176471 | 0.078431 | 0.294118 | 4.787234 | 5.066667 | 2.444444 | 2.75 | 4 |  |
| rejection_block | target_rr_below_2 | 4 | 4 | 3 |  | 2.396474 | 2.891235 | 0.5 | 1.061695 | 84.75 | 0.584104 | 0.508873 | 0.41443 | 0.41443 | 0.070832 | 0.5 | 0.5 |  | 0.25 | 4.666667 | 2.0 | 4.5 |  |  | 4 |
| rejection_block | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.787677 | 87.0 |  |  |  |  |  |  |  |  |  | 5.0 |  |  |  |  | 1 |
