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
| turtle_soup | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 25 | 25 | 25 |  | 4.280546 | 2.530113 | 0.6 | 1.79379 | 73.6 | 0.045822 | 0.407873 | 0.214801 | 0.214801 | 0.193072 |  | 0.193072 | 0.6 | 0.56 | 0.16 | 0.4 | 1.0 | 3.3 | 2.642857 | 1.5 | 3 | 21 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 4 | 4 | 4 |  | 4.35193 | 3.995654 |  | 6.265604 | 90.0 | -1.0 | 1.0 | 0.515397 | 0.515397 | 0.484603 |  | 0.484603 |  | 1.0 | 0.75 | 1.0 | 1.0 | 3.0 | 1.0 | 1.333333 | 3 |  |
| turtle_soup | target_rr_below_2 | 20 | 20 | 20 |  | 4.452699 | 2.077138 | 0.75 | 0.84718 | 70.0 | 0.307277 | 0.359842 | 0.219925 | 0.219925 | 0.139917 |  | 0.139917 | 0.75 | 0.5 | 0.05 | 0.25 | 1.0 | 2.8 | 3.3 | 2.0 |  | 20 |
| turtle_soup | target_rr_below_3 | 1 | 1 | 1 |  | 0.551946 | 0.551946 |  | 2.838739 | 80.0 | -1.0 | -1.0 | -1.090045 | -1.090045 | 0.090045 |  | 0.090045 |  |  |  | 1.0 | 1.0 | 7.0 |  |  |  | 1 |
