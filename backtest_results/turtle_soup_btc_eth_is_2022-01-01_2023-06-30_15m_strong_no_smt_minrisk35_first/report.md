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
- timeframes: 15m
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
| turtle_soup | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 356 | 356 | 356 |  | 8.553705 | 5.905627 | 0.384831 | 6.019588 | 67.331461 | 1.103359 | 0.542275 | -0.17663 | -0.17663 | 0.71886 | 4.5e-05 | 0.718905 | 0.384831 | 0.758427 | 0.547753 | 0.598315 | 1.0 | 3.765258 | 1.181481 | 1.461538 | 152 | 107 |
| turtle_soup | ETHUSDT | 339 | 339 | 339 |  | 8.999816 | 5.759587 | 0.321534 | 6.376146 | 66.253687 | 0.837275 | 0.500622 | -0.129552 | -0.129552 | 0.630185 | -1.1e-05 | 0.630174 | 0.321534 | 0.746313 | 0.560472 | 0.654867 | 1.0 | 3.990991 | 1.3083 | 1.6 | 157 | 104 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 316 | 316 | 316 |  | 5.750963 | 3.941873 | 0.363924 | 4.192589 | 64.873418 | 0.409048 | 0.594938 | 0.137308 | 0.137308 | 0.457658 | -2.7e-05 | 0.45763 | 0.363924 | 0.78481 | 0.458861 | 0.620253 | 1.0 | 4.459184 | 1.383065 | 2.227586 | 117 | 134 |
| turtle_soup | valid | 379 | 379 | 379 |  | 11.289584 | 7.994447 | 0.345646 | 7.861818 | 68.416887 | 1.444256 | 0.46111 | -0.396273 | -0.396273 | 0.857328 | 5.5e-05 | 0.857382 | 0.345646 | 0.725594 | 0.633245 | 0.630607 | 1.0 | 3.405858 | 1.116364 | 1.108333 | 192 | 77 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 695 | 695 | 695 |  | 8.771304 | 5.791525 | 0.353957 | 6.193506 | 66.805755 | 0.973571 | 0.521958 | -0.153666 | -0.153666 | 0.675607 | 1.7e-05 | 0.675625 | 0.353957 | 0.752518 | 0.553957 | 0.625899 | 1.0 | 3.88046 | 1.24283 | 1.52987 | 309 | 211 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 497 | 497 | 497 |  | 10.410201 | 7.76249 | 0.277666 | 7.946905 | 71.95171 | 1.189075 | 0.523947 | -0.288442 | -0.288442 | 0.812389 |  | 0.812389 | 0.277666 | 0.760563 | 0.637827 | 0.698189 | 1.0 | 3.821326 | 1.145503 | 1.321767 | 284 | 13 |
| turtle_soup | medium | 198 | 198 | 198 |  | 4.657508 | 2.983564 | 0.545455 | 1.792298 | 53.888889 | 0.432636 | 0.516967 | 0.184635 | 0.184635 | 0.332271 | 6.1e-05 | 0.332332 | 0.545455 | 0.732323 | 0.343434 | 0.444444 | 1.0 | 4.113636 | 1.496552 | 2.5 | 25 | 198 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 484 | 484 | 484 |  | 10.558461 | 7.832211 | 0.264463 | 8.115734 | 71.942149 | 1.193699 | 0.524793 | -0.300579 | -0.300579 | 0.825372 |  | 0.825372 | 0.264463 | 0.762397 | 0.644628 | 0.710744 | 1.0 | 3.840116 | 1.075881 | 1.298077 | 284 |  |
| turtle_soup | target_rr_below_2 | 131 | 131 | 131 |  | 3.883812 | 2.716265 | 0.633588 | 1.317133 | 51.526718 | 0.416609 | 0.498537 | 0.230775 | 0.230775 | 0.267557 | 0.000205 | 0.267762 | 0.633588 | 0.709924 | 0.259542 | 0.358779 | 1.0 | 4.510638 | 1.88172 | 2.588235 | 10 | 131 |
| turtle_soup | target_rr_below_3 | 80 | 80 | 80 |  | 5.962277 | 3.882487 | 0.4375 | 2.549093 | 60.75 | 0.553826 | 0.543158 | 0.105631 | 0.105631 | 0.43771 | -0.000184 | 0.437527 | 0.4375 | 0.7625 | 0.4875 | 0.55 | 1.0 | 3.522727 | 1.278689 | 2.461538 | 15 | 80 |
