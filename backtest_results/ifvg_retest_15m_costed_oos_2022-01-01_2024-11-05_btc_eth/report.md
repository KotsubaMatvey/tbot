# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ifvg_retest
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 96
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | BTCUSDT | 242 | 242 | 87 |  | 31.89029 | 14.305889 | 0.090909 | 8.26041 | 71.202479 | 0.203568 | 0.182244 | -1.489491 | -1.489491 | 0.600848 | 0.000147 | 0.600995 | 0.090909 | 0.169421 | 0.14876 | 0.268595 | 6.735537 | 1.815385 | 1.243902 | 1.444444 | 53 | 74 |
| ifvg_retest | ETHUSDT | 271 | 271 | 94 |  | 40.787085 | 18.847895 | 0.092251 | 6.719828 | 70.177122 | 0.550227 | 0.280433 | -1.145359 | -1.145359 | 0.494555 |  | 0.494555 | 0.092251 | 0.147601 | 0.114391 | 0.254613 | 6.228782 | 1.449275 | 1.05 | 1.096774 | 53 | 107 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 513 | 513 | 181 |  | 36.510725 | 16.618559 | 0.091618 | 7.446574 | 70.660819 | 0.383601 | 0.233237 | -1.310771 | -1.310771 | 0.544697 | 6.9e-05 | 0.544767 | 0.091618 | 0.157895 | 0.130604 | 0.261209 | 6.467836 | 1.626866 | 1.148148 | 1.283582 | 106 | 181 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 312 | 312 | 101 |  | 41.034895 | 14.305889 | 0.086538 | 7.096865 | 72.487179 | 0.468396 | 0.298555 | -1.132851 | -1.132851 | 0.463258 | 0.000114 | 0.463372 | 0.086538 | 0.150641 | 0.128205 | 0.237179 | 7.0 | 1.594595 | 1.085106 | 1.05 | 58 | 114 |
| ifvg_retest | valid | 201 | 201 | 80 |  | 30.798961 | 17.438307 | 0.099502 | 7.989407 | 67.825871 | 0.276546 | 0.150773 | -1.535394 | -1.535394 | 0.671111 |  | 0.671111 | 0.099502 | 0.169154 | 0.134328 | 0.298507 | 5.641791 | 1.666667 | 1.235294 | 1.62963 | 48 | 67 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 332 | 332 | 115 |  | 46.865816 | 24.383283 | 0.060241 | 10.484457 | 75.981928 | 0.588421 | 0.320298 | -1.517949 | -1.517949 | 0.636635 | 0.000107 | 0.636742 | 0.060241 | 0.141566 | 0.123494 | 0.286145 | 7.331325 | 1.642105 | 1.191489 | 1.365854 | 84 |  |
| ifvg_retest | medium | 181 | 181 | 66 |  | 18.467763 | 9.564488 | 0.149171 | 1.874325 | 60.900552 | 0.026717 | 0.08154 | -0.949778 | -0.949778 | 0.376061 |  | 0.376061 | 0.149171 | 0.187845 | 0.143646 | 0.21547 | 4.883978 | 1.589744 | 1.088235 | 1.153846 | 22 | 181 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 332 | 332 | 115 |  | 46.865816 | 24.383283 | 0.060241 | 10.484457 | 75.981928 | 0.588421 | 0.320298 | -1.517949 | -1.517949 | 0.636635 | 0.000107 | 0.636742 | 0.060241 | 0.141566 | 0.123494 | 0.286145 | 7.331325 | 1.642105 | 1.191489 | 1.365854 | 84 |  |
| ifvg_retest | target_rr_below_2 | 95 | 95 | 38 |  | 23.173657 | 12.065523 | 0.221053 | 1.322159 | 56.052632 | 0.243549 | 0.21388 | -0.843023 | -0.843023 | 0.422761 |  | 0.422761 | 0.221053 | 0.231579 | 0.2 | 0.178947 | 4.6 | 1.705882 | 1.136364 | 1.157895 | 10 | 95 |
| ifvg_retest | target_rr_below_3 | 86 | 86 | 28 |  | 12.081194 | 7.150782 | 0.069767 | 2.484276 | 66.255814 | -0.267556 | -0.098064 | -1.094658 | -1.094658 | 0.324473 |  | 0.324473 | 0.069767 | 0.139535 | 0.081395 | 0.255814 | 5.197674 | 1.5 | 1.0 | 1.142857 | 12 | 86 |
