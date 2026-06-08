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
| turtle_soup | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 1052 | 1052 | 1052 |  | 10.496298 | 6.790979 | 0.318441 | 6.578019 | 67.984791 | 0.802546 | 0.40244 | -0.468736 | -0.468736 | 0.870995 | 0.000181 | 0.871176 | 0.318441 | 0.693916 | 0.546578 | 0.6673 | 1.0 | 3.180912 | 1.126027 | 1.323478 | 500 | 273 |
| turtle_soup | ETHUSDT | 1108 | 1108 | 1108 |  | 10.071887 | 6.082115 | 0.274368 | 7.496253 | 68.456679 | 0.84548 | 0.457167 | -0.202997 | -0.202997 | 0.660498 | -0.000335 | 0.660164 | 0.274368 | 0.725632 | 0.564982 | 0.696751 | 1.0 | 3.404145 | 1.237562 | 1.458466 | 574 | 258 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 923 | 923 | 923 |  | 6.669473 | 4.308735 | 0.317443 | 4.603868 | 65.969664 | 0.408209 | 0.51984 | 0.021382 | 0.021382 | 0.498493 | -3.5e-05 | 0.498458 | 0.317443 | 0.754063 | 0.475623 | 0.658722 | 1.0 | 3.422697 | 1.29023 | 1.722096 | 351 | 355 |
| turtle_soup | valid | 1237 | 1237 | 1237 |  | 12.97157 | 8.94914 | 0.279709 | 8.873529 | 69.911075 | 1.135241 | 0.36386 | -0.596416 | -0.596416 | 0.960396 | -0.00012 | 0.960277 | 0.279709 | 0.677445 | 0.616006 | 0.700081 | 1.0 | 3.210162 | 1.096659 | 1.204724 | 723 | 176 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2160 | 2160 | 2160 |  | 10.278591 | 6.332419 | 0.295833 | 7.049039 | 68.226852 | 0.824569 | 0.430513 | -0.332422 | -0.332422 | 0.763018 | -8.3e-05 | 0.762935 | 0.295833 | 0.710185 | 0.556019 | 0.682407 | 1.0 | 3.297829 | 1.184485 | 1.393838 | 1074 | 531 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 1672 | 1672 | 1672 |  | 11.389275 | 7.621422 | 0.231459 | 8.577981 | 72.254785 | 0.959912 | 0.420506 | -0.449095 | -0.449095 | 0.869834 | -0.000233 | 0.869601 | 0.231459 | 0.70933 | 0.601077 | 0.741627 | 1.0 | 3.325 | 1.065767 | 1.308458 | 983 | 43 |
| turtle_soup | medium | 488 | 488 | 488 |  | 6.473132 | 3.601297 | 0.516393 | 1.810533 | 54.42623 | 0.360853 | 0.464798 | 0.067326 | 0.067326 | 0.397043 | 0.000429 | 0.397472 | 0.516393 | 0.713115 | 0.401639 | 0.479508 | 1.0 | 3.153846 | 1.58908 | 1.831633 | 91 | 488 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1629 | 1629 | 1629 |  | 11.490652 | 7.678726 | 0.220381 | 8.760182 | 72.18539 | 0.970271 | 0.414365 | -0.465206 | -0.465206 | 0.879831 | -0.000261 | 0.87957 | 0.220381 | 0.707182 | 0.604052 | 0.751995 | 1.0 | 3.333061 | 1.049479 | 1.306911 | 977 |  |
| turtle_soup | target_rr_below_2 | 294 | 294 | 294 |  | 6.223018 | 3.314045 | 0.632653 | 1.228433 | 51.496599 | 0.354995 | 0.428257 | 0.072527 | 0.072527 | 0.355247 | 0.000484 | 0.355731 | 0.632653 | 0.676871 | 0.333333 | 0.367347 | 1.0 | 3.25 | 1.733668 | 1.530612 | 33 | 294 |
| turtle_soup | target_rr_below_3 | 237 | 237 | 237 |  | 6.978553 | 4.024713 | 0.396624 | 2.508141 | 61.772152 | 0.405613 | 0.544304 | 0.077916 | 0.077916 | 0.465956 | 0.000432 | 0.466387 | 0.396624 | 0.772152 | 0.50211 | 0.594937 | 1.0 | 3.028369 | 1.437158 | 2.0 | 64 | 237 |
