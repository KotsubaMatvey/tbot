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
| turtle_soup | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 53 | 53 | 53 |  | 3.559584 | 2.053481 | 0.679245 | 1.377794 | 73.207547 | 0.450245 | 0.500338 | 0.311672 | 0.311672 | 0.188666 |  | 0.188666 | 0.679245 | 0.584906 | 0.132075 | 0.245283 | 1.0 | 5.076923 | 4.935484 | 2.714286 | 3 | 48 |
| turtle_soup | valid | 66 | 66 | 66 |  | 3.518025 | 2.228555 | 0.469697 | 2.009029 | 75.0 | 0.058853 | 0.387236 | 0.159371 | 0.159371 | 0.227865 |  | 0.227865 | 0.469697 | 0.590909 | 0.257576 | 0.5 | 1.0 | 3.909091 | 2.538462 | 2.529412 | 10 | 51 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 119 | 119 | 119 |  | 3.536534 | 2.098568 | 0.563025 | 1.727891 | 74.201681 | 0.23317 | 0.437609 | 0.227203 | 0.227203 | 0.210406 |  | 0.210406 | 0.563025 | 0.588235 | 0.201681 | 0.386555 | 1.0 | 4.23913 | 3.6 | 2.583333 | 13 | 99 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 20 | 20 | 20 |  | 6.168772 | 4.189239 | 0.15 | 4.855755 | 90.0 | 0.175307 | 0.7 | 0.376705 | 0.376705 | 0.323295 |  | 0.323295 | 0.15 | 0.85 | 0.6 | 0.75 | 1.0 | 4.533333 | 2.235294 | 3.25 | 9 |  |
| turtle_soup | target_rr_below_2 | 89 | 89 | 89 |  | 3.121046 | 1.773602 | 0.707865 | 0.931121 | 70.0 | 0.314528 | 0.427815 | 0.241303 | 0.241303 | 0.186512 |  | 0.186512 | 0.707865 | 0.539326 | 0.11236 | 0.258427 | 1.0 | 3.826087 | 3.854167 | 1.9 | 3 | 89 |
| turtle_soup | target_rr_below_3 | 10 | 10 | 10 |  | 1.969905 | 1.505956 | 0.1 | 2.563412 | 80.0 | -0.375189 |  | -0.197294 | -0.197294 | 0.197294 |  | 0.197294 | 0.1 | 0.5 | 0.2 | 0.8 | 1.0 | 4.875 | 5.8 | 2.0 | 1 | 10 |
