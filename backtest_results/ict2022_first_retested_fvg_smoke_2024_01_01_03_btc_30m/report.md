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
| ict2022_mss_fvg | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | target_rr_below_3 | 2 | 2 | 2 |  | 1.472791 | 1.472791 | 0.5 | 2.066136 | 88.0 | 0.566136 | 0.283068 | 0.236272 | 0.236272 | 0.031938 | 0.014858 | 0.046796 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | 7.0 | 6.0 | 8.0 |  | 2 |
