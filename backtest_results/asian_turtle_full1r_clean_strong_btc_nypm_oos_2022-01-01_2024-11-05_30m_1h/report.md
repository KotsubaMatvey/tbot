# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: None
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 9 | 9 | 9 |  | 1.777513 | 1.020809 | 0.555556 | 0.9256 | 70.0 | 0.16872 | 0.160759 | -0.021368 | -0.021368 | 0.182127 |  | 0.182127 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 10.5 | 5.0 |  | 9 |
| turtle_soup | valid | 9 | 9 | 9 |  | 2.794931 | 2.728408 | 0.555556 | 2.07072 | 76.666667 | 0.297065 | 0.503409 | 0.293075 | 0.293075 | 0.210334 |  | 0.210334 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 1.0 | 6.0 | 2 | 7 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 18 | 18 | 18 |  | 2.286222 | 1.965408 | 0.555556 | 1.49816 | 73.333333 | 0.232893 | 0.332084 | 0.135854 | 0.135854 | 0.196231 |  | 0.196231 | 0.555556 | 0.444444 | 0.111111 | 0.333333 | 1.0 | 3.666667 | 5.75 | 5.5 | 2 | 16 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 3.663583 | 3.663583 |  | 4.887862 | 90.0 | -1.0 |  | -0.427885 | -0.427885 | 0.427885 |  | 0.427885 |  | 0.5 |  | 1.0 | 1.0 | 2.0 | 1.0 |  | 1 |  |
| turtle_soup | target_rr_below_2 | 14 | 14 | 14 |  | 2.0916 | 1.098812 | 0.714286 | 0.836167 | 70.0 | 0.349602 | 0.284108 | 0.115387 | 0.115387 | 0.168721 |  | 0.168721 | 0.714286 | 0.357143 | 0.071429 | 0.214286 | 1.0 | 3.666667 | 8.6 | 5.0 |  | 14 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.271216 | 2.271216 |  | 2.742406 | 80.0 | 0.64882 | 1.0 | 0.842857 | 0.842857 | 0.157143 |  | 0.157143 |  | 1.0 | 0.5 | 0.5 | 1.0 | 7.0 | 1.0 | 6.0 | 1 | 2 |
