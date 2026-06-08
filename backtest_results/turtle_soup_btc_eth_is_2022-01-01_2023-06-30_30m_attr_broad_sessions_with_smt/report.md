# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 30 | 30 | 30 |  | 7.915116 | 6.440746 | 0.433333 | 5.635913 | 84.0 | 0.755373 | 0.866667 | 0.324316 | 0.324316 | 0.54235 |  | 0.54235 | 0.433333 | 0.933333 | 0.766667 | 0.533333 | 1.0 | 4.5 | 1.142857 | 1.391304 | 13 | 11 |
| turtle_soup | ETHUSDT | 31 | 31 | 31 |  | 8.586782 | 6.640101 | 0.451613 | 5.904323 | 84.193548 | 1.277684 | 0.766816 | 0.311169 | 0.311169 | 0.455647 |  | 0.455647 | 0.451613 | 0.83871 | 0.709677 | 0.516129 | 1.0 | 4.75 | 1.0 | 1.136364 | 11 | 12 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 26 | 26 | 26 |  | 6.441539 | 4.808168 | 0.538462 | 3.665145 | 82.307692 | 0.757917 | 0.672533 | 0.332329 | 0.332329 | 0.340203 |  | 0.340203 | 0.538462 | 0.807692 | 0.576923 | 0.461538 | 1.0 | 4.166667 | 1.095238 | 1.466667 | 7 | 13 |
| turtle_soup | valid | 35 | 35 | 35 |  | 9.604678 | 7.080395 | 0.371429 | 7.337646 | 85.428571 | 1.216102 | 0.922441 | 0.306719 | 0.306719 | 0.615722 |  | 0.615722 | 0.371429 | 0.942857 | 0.857143 | 0.571429 | 1.0 | 4.9 | 1.060606 | 1.166667 | 17 | 10 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 61 | 61 | 61 |  | 8.256455 | 6.453464 | 0.442623 | 5.772318 | 84.098361 | 1.02081 | 0.815923 | 0.317635 | 0.317635 | 0.498288 |  | 0.498288 | 0.442623 | 0.885246 | 0.737705 | 0.52459 | 1.0 | 4.625 | 1.074074 | 1.266667 | 24 | 23 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 38 | 38 | 38 |  | 8.73891 | 6.95389 | 0.263158 | 8.275154 | 90.0 | 1.21552 | 0.842105 | 0.266703 | 0.266703 | 0.575403 |  | 0.575403 | 0.263158 | 0.921053 | 0.894737 | 0.684211 | 1.0 | 4.961538 | 1.028571 | 1.235294 | 23 |  |
| turtle_soup | target_rr_below_2 | 13 | 13 | 13 |  | 7.098976 | 3.161458 | 1.0 | 0.978013 | 70.0 | 0.978013 | 0.905485 | 0.523525 | 0.523525 | 0.38196 |  | 0.38196 | 1.0 | 0.846154 | 0.461538 |  | 1.0 |  | 1.090909 | 1.333333 |  | 13 |
| turtle_soup | target_rr_below_3 | 10 | 10 | 10 |  | 7.927848 | 6.372719 | 0.4 | 2.494139 | 80.0 | 0.336549 | 0.6 | 0.243521 | 0.243521 | 0.356479 |  | 0.356479 | 0.4 | 0.8 | 0.5 | 0.6 | 1.0 | 3.166667 | 1.25 | 1.4 | 1 | 10 |
