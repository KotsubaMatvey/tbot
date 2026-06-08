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
- timeframes: 15m, 30m
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
| turtle_soup | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 696 | 696 | 696 |  | 9.094421 | 6.060659 | 0.373563 | 5.724809 | 66.752874 | 0.938101 | 0.475921 | -0.175152 | -0.175152 | 0.650961 | 0.000112 | 0.651074 | 0.373563 | 0.722701 | 0.533046 | 0.610632 | 1.0 | 3.437647 | 1.151093 | 1.382749 | 296 | 235 |
| turtle_soup | ETHUSDT | 690 | 690 | 690 |  | 9.778197 | 5.771289 | 0.336232 | 6.300905 | 66.376812 | 0.81302 | 0.44294 | -0.12692 | -0.12692 | 0.569718 | 0.000143 | 0.56986 | 0.336232 | 0.713043 | 0.536232 | 0.646377 | 1.0 | 3.587444 | 1.292683 | 1.502703 | 317 | 234 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 615 | 615 | 615 |  | 5.939371 | 3.945035 | 0.360976 | 4.149689 | 64.536585 | 0.320592 | 0.537034 | 0.126942 | 0.126942 | 0.409859 | 0.000233 | 0.410092 | 0.360976 | 0.752846 | 0.439024 | 0.626016 | 1.0 | 4.033766 | 1.349892 | 1.974074 | 224 | 287 |
| turtle_soup | valid | 771 | 771 | 771 |  | 12.223035 | 7.90106 | 0.350195 | 7.4968 | 68.184176 | 1.318726 | 0.397657 | -0.372958 | -0.372958 | 0.770572 | 4.3e-05 | 0.770615 | 0.350195 | 0.690013 | 0.610895 | 0.63035 | 1.0 | 3.102881 | 1.109023 | 1.138004 | 389 | 182 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1386 | 1386 | 1386 |  | 9.434829 | 5.925903 | 0.354978 | 6.01161 | 66.565657 | 0.875831 | 0.459502 | -0.151141 | -0.151141 | 0.610515 | 0.000127 | 0.610643 | 0.354978 | 0.717893 | 0.534632 | 0.628427 | 1.0 | 3.514351 | 1.221106 | 1.442645 | 613 | 469 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 958 | 958 | 958 |  | 11.048179 | 7.728883 | 0.273486 | 7.906698 | 72.212944 | 1.087369 | 0.455295 | -0.282841 | -0.282841 | 0.738033 | 0.000102 | 0.738136 | 0.273486 | 0.72547 | 0.61691 | 0.705637 | 1.0 | 3.523669 | 1.126619 | 1.27242 | 541 | 41 |
| turtle_soup | medium | 428 | 428 | 428 |  | 5.823638 | 3.311524 | 0.537383 | 1.769802 | 53.925234 | 0.402342 | 0.468918 | 0.143646 | 0.143646 | 0.325089 | 0.000183 | 0.325272 | 0.537383 | 0.700935 | 0.350467 | 0.455607 | 1.0 | 3.482051 | 1.44 | 2.113333 | 72 | 428 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 917 | 917 | 917 |  | 11.252745 | 7.841852 | 0.25627 | 8.185724 | 72.137405 | 1.109487 | 0.454744 | -0.300068 | -0.300068 | 0.754705 | 0.000107 | 0.754812 | 0.25627 | 0.727372 | 0.627045 | 0.721919 | 1.0 | 3.554381 | 1.086957 | 1.257391 | 537 |  |
| turtle_soup | target_rr_below_2 | 285 | 285 | 285 |  | 5.34707 | 2.8194 | 0.631579 | 1.26595 | 51.754386 | 0.380236 | 0.464622 | 0.196857 | 0.196857 | 0.267438 | 0.000327 | 0.267765 | 0.631579 | 0.677193 | 0.270175 | 0.361404 | 1.0 | 3.737864 | 1.699482 | 2.038961 | 23 | 285 |
| turtle_soup | target_rr_below_3 | 184 | 184 | 184 |  | 6.706472 | 4.214784 | 0.418478 | 2.527102 | 61.73913 | 0.478994 | 0.475286 | 0.05205 | 0.05205 | 0.423316 | -8e-05 | 0.423236 | 0.418478 | 0.733696 | 0.483696 | 0.576087 | 1.0 | 3.04717 | 1.2 | 2.123596 | 53 | 184 |
