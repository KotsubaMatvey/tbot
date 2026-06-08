# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
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
| turtle_soup | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 7 | 7 | 7 |  | 3.689183 | 4.514163 | 0.857143 | 1.060677 | 71.428571 | 0.585851 | 0.766893 | 0.622188 | 0.622188 | 0.144704 |  | 0.144704 | 0.857143 | 0.714286 | 0.285714 | 0.142857 | 1.0 | 12.0 | 1.6 | 1.0 |  | 7 |
| turtle_soup | valid | 18 | 18 | 18 |  | 3.337206 | 2.621973 | 0.611111 | 1.651044 | 72.777778 | 0.553722 | 0.709122 | 0.470932 | 0.470932 | 0.23819 |  | 0.23819 | 0.611111 | 0.833333 | 0.388889 | 0.333333 | 1.0 | 6.333333 | 2.333333 | 1.571429 | 2 | 16 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 25 | 25 | 25 |  | 3.435759 | 2.773947 | 0.68 | 1.485741 | 72.4 | 0.562718 | 0.725298 | 0.513284 | 0.513284 | 0.212014 |  | 0.212014 | 0.68 | 0.8 | 0.36 | 0.28 | 1.0 | 7.142857 | 2.15 | 1.444444 | 2 | 23 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2 | 2 | 2 |  | 6.07309 | 6.07309 | 0.5 | 4.581823 | 90.0 | 1.038037 | 1.0 | 0.672486 | 0.672486 | 0.327514 |  | 0.327514 | 0.5 | 1.0 | 1.0 | 0.5 | 1.0 | 22.0 | 1.5 | 2.0 |  |  |
| turtle_soup | target_rr_below_2 | 21 | 21 | 21 |  | 3.230624 | 2.469999 | 0.714286 | 1.089496 | 70.0 | 0.486437 | 0.672974 | 0.467784 | 0.467784 | 0.20519 |  | 0.20519 | 0.714286 | 0.761905 | 0.285714 | 0.238095 | 1.0 | 3.2 | 2.25 | 1.333333 | 2 | 21 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.952352 | 2.952352 | 0.5 | 2.550238 | 80.0 | 0.888347 | 1.0 | 0.831829 | 0.831829 | 0.168171 |  | 0.168171 | 0.5 | 1.0 | 0.5 | 0.5 | 1.0 | 12.0 | 2.0 | 1.0 |  | 2 |
