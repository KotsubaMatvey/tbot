# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
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
| turtle_soup | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 41 | 41 | 41 |  | 3.839102 | 2.098568 | 0.707317 | 1.324789 | 72.926829 | 0.483032 | 0.581667 | 0.397213 | 0.397213 | 0.184454 |  | 0.184454 | 0.707317 | 0.609756 | 0.121951 | 0.219512 | 1.0 | 5.555556 | 5.32 | 2.0 | 3 | 38 |
| turtle_soup | valid | 43 | 43 | 43 |  | 3.300359 | 1.716287 | 0.534884 | 1.789515 | 74.186047 | 0.184743 | 0.307507 | 0.105747 | 0.105747 | 0.20176 |  | 0.20176 | 0.534884 | 0.511628 | 0.232558 | 0.44186 | 1.0 | 4.526316 | 2.636364 | 1.6 | 3 | 35 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 84 | 84 | 84 |  | 3.563317 | 2.076025 | 0.619048 | 1.562684 | 73.571429 | 0.330337 | 0.441323 | 0.248011 | 0.248011 | 0.193313 |  | 0.193313 | 0.619048 | 0.559524 | 0.178571 | 0.333333 | 1.0 | 4.857143 | 4.06383 | 1.733333 | 6 | 73 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 11 | 11 | 11 |  | 6.341808 | 4.798881 | 0.272727 | 4.670416 | 90.0 | 0.270698 | 0.818182 | 0.553671 | 0.553671 | 0.26451 |  | 0.26451 | 0.272727 | 0.909091 | 0.636364 | 0.727273 | 1.0 | 5.5 | 1.1 | 1.571429 | 4 |  |
| turtle_soup | target_rr_below_2 | 65 | 65 | 65 |  | 3.270724 | 1.892161 | 0.738462 | 0.911482 | 70.0 | 0.408038 | 0.431864 | 0.252479 | 0.252479 | 0.179384 |  | 0.179384 | 0.738462 | 0.507692 | 0.107692 | 0.215385 | 1.0 | 4.571429 | 4.666667 | 2.0 | 1 | 65 |
| turtle_soup | target_rr_below_3 | 8 | 8 | 8 |  | 2.120208 | 1.505956 | 0.125 | 2.580574 | 80.0 | -0.218987 |  | -0.208583 | -0.208583 | 0.208583 |  | 0.208583 | 0.125 | 0.5 | 0.125 | 0.75 | 1.0 | 4.666667 | 6.5 | 1.0 | 1 | 8 |
