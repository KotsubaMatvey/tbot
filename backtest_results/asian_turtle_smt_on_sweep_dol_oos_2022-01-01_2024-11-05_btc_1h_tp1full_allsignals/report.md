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
- timeframes: 1h
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
| turtle_soup | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 32 | 32 | 32 |  | 4.207668 | 2.566325 | 0.59375 | 1.926604 | 74.375 | 0.007701 | 0.504452 | 0.318196 | 0.318196 | 0.186256 |  | 0.186256 | 0.59375 | 0.59375 | 0.125 | 0.40625 | 1.0 | 3.923077 | 2.368421 | 1.5 | 4 | 26 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 6 | 6 | 6 |  | 4.627946 | 3.995654 |  | 6.176733 | 90.0 | -1.0 | 1.0 | 0.611678 | 0.611678 | 0.388322 |  | 0.388322 |  | 1.0 | 0.5 | 1.0 | 1.0 | 4.5 | 1.5 | 1.333333 | 4 |  |
| turtle_soup | target_rr_below_2 | 24 | 24 | 24 |  | 4.214589 | 2.088505 | 0.791667 | 0.79352 | 70.0 | 0.343601 | 0.422602 | 0.282659 | 0.282659 | 0.139944 |  | 0.139944 | 0.791667 | 0.5 | 0.041667 | 0.208333 | 1.0 | 2.8 | 2.916667 | 2.0 |  | 24 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.86379 | 2.86379 |  | 2.773225 | 80.0 | -1.0 |  | -0.13581 | -0.13581 | 0.135811 |  | 0.135811 |  | 0.5 |  | 1.0 | 1.0 | 5.0 | 1.0 |  |  | 2 |
