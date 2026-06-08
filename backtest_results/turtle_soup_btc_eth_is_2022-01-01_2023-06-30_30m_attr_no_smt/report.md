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
| turtle_soup | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 170 | 170 | 170 |  | 8.484474 | 5.059979 | 0.423529 | 4.160252 | 65.411765 | 0.782244 | 0.493495 | 0.033138 | 0.033138 | 0.459402 | 0.000955 | 0.460357 | 0.423529 | 0.723529 | 0.476471 | 0.564706 | 1.0 | 3.208333 | 1.260163 | 1.518519 | 61 | 75 |
| turtle_soup | ETHUSDT | 176 | 176 | 176 |  | 11.997381 | 5.262135 | 0.4375 | 4.589299 | 64.147727 | 1.250137 | 0.410727 | -0.02188 | -0.02188 | 0.432258 | 0.000349 | 0.432607 | 0.4375 | 0.693182 | 0.517045 | 0.545455 | 1.0 | 2.395833 | 1.114754 | 1.362637 | 67 | 83 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 155 | 155 | 155 |  | 6.029404 | 3.467454 | 0.445161 | 2.829376 | 61.677419 | 0.587217 | 0.539431 | 0.25189 | 0.25189 | 0.287329 | 0.000212 | 0.287541 | 0.445161 | 0.748387 | 0.393548 | 0.522581 | 1.0 | 3.0 | 1.241379 | 1.786885 | 41 | 99 |
| turtle_soup | valid | 191 | 191 | 191 |  | 13.713833 | 7.37645 | 0.418848 | 5.635634 | 67.277487 | 1.371659 | 0.379949 | -0.195081 | -0.195081 | 0.57403 | 0.001 | 0.57503 | 0.418848 | 0.675393 | 0.581152 | 0.581152 | 1.0 | 2.657658 | 1.139535 | 1.243243 | 87 | 59 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 346 | 346 | 346 |  | 10.271386 | 5.1623 | 0.430636 | 4.378495 | 64.768786 | 1.020247 | 0.451393 | 0.005152 | 0.005152 | 0.445594 | 0.000647 | 0.446241 | 0.430636 | 0.708092 | 0.49711 | 0.554913 | 1.0 | 2.802083 | 1.187755 | 1.436047 | 128 | 158 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 199 | 199 | 199 |  | 13.425223 | 7.285928 | 0.356784 | 6.336726 | 72.713568 | 1.483114 | 0.457286 | -0.12184 | -0.12184 | 0.577906 | 0.00122 | 0.579126 | 0.356784 | 0.728643 | 0.59799 | 0.633166 | 1.0 | 2.746032 | 1.137931 | 1.092437 | 103 | 11 |
| turtle_soup | medium | 147 | 147 | 147 |  | 6.001906 | 3.235684 | 0.530612 | 1.727557 | 54.013605 | 0.393646 | 0.443416 | 0.177066 | 0.177066 | 0.266478 | -0.000128 | 0.26635 | 0.530612 | 0.680272 | 0.360544 | 0.44898 | 1.0 | 2.909091 | 1.26 | 2.207547 | 25 | 147 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 188 | 188 | 188 |  | 13.909907 | 7.472549 | 0.351064 | 6.599178 | 72.553191 | 1.562694 | 0.425532 | -0.167914 | -0.167914 | 0.592123 | 0.001323 | 0.593446 | 0.351064 | 0.712766 | 0.611702 | 0.638298 | 1.0 | 2.6 | 1.052239 | 1.086957 | 102 |  |
| turtle_soup | target_rr_below_2 | 93 | 93 | 93 |  | 5.675044 | 2.979508 | 0.602151 | 1.196883 | 51.075269 | 0.289547 | 0.464324 | 0.213665 | 0.213665 | 0.249957 | 0.000702 | 0.250659 | 0.602151 | 0.666667 | 0.268817 | 0.376344 | 1.0 | 3.342857 | 1.258065 | 1.44 | 8 | 93 |
| turtle_soup | target_rr_below_3 | 65 | 65 | 65 |  | 6.323971 | 3.465967 | 0.415385 | 2.507749 | 61.846154 | 0.496787 | 0.507692 | 0.207379 | 0.207379 | 0.3017 | -0.001387 | 0.300313 | 0.415385 | 0.753846 | 0.492308 | 0.569231 | 1.0 | 2.945946 | 1.469388 | 2.6875 | 18 | 65 |
