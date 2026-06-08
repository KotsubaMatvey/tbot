# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, SOLUSDT
- timeframes: 30m, 1h
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
| turtle_soup | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.151911 | 0.151911 | 0.189034 | 0.001847 | 0.190881 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |
| turtle_soup | SOLUSDT | 33 | 33 | 33 |  | 3.177162 | 2.572817 | 0.30303 | 2.947212 | 76.666667 | -0.362204 | 0.185449 | 0.069389 | 0.069389 | 0.116274 | -0.000213 | 0.11606 | 0.30303 | 0.454545 | 0.181818 | 0.666667 | 1.0 | 4.181818 | 1.533333 | 2.0 | 6 | 23 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 49 | 49 | 49 |  | 3.610774 | 2.053481 | 0.612245 | 1.435815 | 73.061224 | 0.231329 | 0.417362 | 0.252909 | 0.252909 | 0.163122 | 0.00133 | 0.164452 | 0.612245 | 0.510204 | 0.081633 | 0.326531 | 1.0 | 4.625 | 5.4 | 2.25 | 4 | 44 |
| turtle_soup | valid | 48 | 48 | 48 |  | 3.155486 | 1.688112 | 0.354167 | 2.655487 | 76.458333 | -0.232906 | 0.158496 | -0.007925 | -0.007925 | 0.165462 | 0.000958 | 0.166421 | 0.354167 | 0.4375 | 0.166667 | 0.625 | 1.0 | 3.7 | 1.904762 | 2.0 | 8 | 34 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 97 | 97 | 97 |  | 3.385477 | 2.027705 | 0.484536 | 2.039364 | 74.742268 | 0.001605 | 0.289263 | 0.123837 | 0.123837 | 0.16428 | 0.001146 | 0.165426 | 0.484536 | 0.474227 | 0.123711 | 0.474227 | 1.0 | 4.021739 | 3.804348 | 2.083333 | 12 | 78 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 19 | 19 | 19 |  | 5.331884 | 4.635563 | 0.105263 | 6.078278 | 90.0 | -0.156738 | 0.684211 | 0.499652 | 0.499652 | 0.184247 | 0.000311 | 0.184558 | 0.105263 | 0.842105 | 0.526316 | 0.842105 | 1.0 | 3.3125 | 1.0 | 1.8 | 9 |  |
| turtle_soup | target_rr_below_2 | 70 | 70 | 70 |  | 3.01808 | 1.597997 | 0.642857 | 0.879251 | 70.0 | 0.123746 | 0.243693 | 0.087736 | 0.087736 | 0.155243 | 0.000714 | 0.155957 | 0.642857 | 0.385714 | 0.028571 | 0.328571 | 1.0 | 4.73913 | 4.962963 | 3.5 | 2 | 70 |
| turtle_soup | target_rr_below_3 | 8 | 8 | 8 |  | 1.977485 | 1.608822 |  | 2.597939 | 80.0 | -0.691073 | -0.25 | -0.452843 | -0.452843 | 0.195936 | 0.006906 | 0.202843 |  | 0.375 |  | 0.875 | 1.0 | 3.285714 | 8.333333 |  | 1 | 8 |
