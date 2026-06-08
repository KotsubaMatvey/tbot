# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2019-09-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, LINKUSDT, XRPUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2019-09-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 64 | 64 | 64 |  | 3.492889 | 1.638643 | 0.578125 | 1.571255 | 73.75 | 0.189194 | 0.342792 | 0.151911 | 0.151911 | 0.189034 | 0.001847 | 0.190881 | 0.578125 | 0.484375 | 0.09375 | 0.375 | 1.0 | 3.875 | 4.903226 | 2.166667 | 6 | 55 |
| turtle_soup | LINKUSDT | 38 | 38 | 38 |  | 3.438044 | 2.53652 | 0.526316 | 2.369164 | 76.052632 | 0.25053 | 0.362302 | 0.23869 | 0.23869 | 0.12643 | -0.002818 | 0.123612 | 0.526316 | 0.578947 | 0.236842 | 0.447368 | 1.0 | 3.588235 | 2.227273 | 1.888889 | 4 | 30 |
| turtle_soup | XRPUSDT | 22 | 22 | 22 |  | 6.208009 | 2.115775 | 0.272727 | 3.107258 | 80.0 | -0.135934 | 0.274343 | 0.088822 | 0.088822 | 0.177253 | 0.008269 | 0.185521 | 0.272727 | 0.545455 | 0.227273 | 0.681818 | 1.0 | 5.2 | 2.833333 | 2.6 | 6 | 13 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 65 | 65 | 65 |  | 4.573527 | 2.053481 | 0.615385 | 1.62249 | 74.153846 | 0.42134 | 0.493408 | 0.331948 | 0.331948 | 0.160022 | 0.001438 | 0.16146 | 0.615385 | 0.569231 | 0.123077 | 0.307692 | 1.0 | 4.65 | 4.513514 | 2.375 | 4 | 57 |
| turtle_soup | valid | 59 | 59 | 59 |  | 3.27945 | 1.703891 | 0.389831 | 2.601464 | 77.118644 | -0.148291 | 0.163902 | -0.014067 | -0.014067 | 0.176281 | 0.001688 | 0.177969 | 0.389831 | 0.474576 | 0.20339 | 0.610169 | 1.0 | 3.861111 | 2.428571 | 2.0 | 12 | 41 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 124 | 124 | 124 |  | 3.957797 | 1.994614 | 0.508065 | 2.088292 | 75.564516 | 0.150306 | 0.336627 | 0.167312 | 0.167312 | 0.167758 | 0.001557 | 0.169315 | 0.508065 | 0.524194 | 0.16129 | 0.451613 | 1.0 | 4.142857 | 3.615385 | 2.15 | 16 | 98 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 26 | 26 | 26 |  | 5.838223 | 3.817782 | 0.192308 | 5.384448 | 90.0 | -0.030788 | 0.692308 | 0.463661 | 0.463661 | 0.227892 | 0.000755 | 0.228647 | 0.192308 | 0.846154 | 0.5 | 0.807692 | 1.0 | 3.761905 | 1.545455 | 1.923077 | 13 |  |
| turtle_soup | target_rr_below_2 | 81 | 81 | 81 |  | 2.981438 | 1.651242 | 0.691358 | 0.943817 | 70.0 | 0.301257 | 0.305453 | 0.159162 | 0.159162 | 0.144937 | 0.001355 | 0.146291 | 0.691358 | 0.432099 | 0.037037 | 0.271605 | 1.0 | 4.227273 | 4.8 | 3.666667 | 1 | 81 |
| turtle_soup | target_rr_below_3 | 17 | 17 | 17 |  | 5.73391 | 2.129633 | 0.117647 | 2.500199 | 80.0 | -0.291961 | -0.058824 | -0.247098 | -0.247098 | 0.184528 | 0.003746 | 0.188274 | 0.117647 | 0.470588 | 0.235294 | 0.764706 | 1.0 | 4.615385 | 4.125 | 1.75 | 2 | 17 |
