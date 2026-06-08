# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 88 | 88 | 88 |  | 4.2943 | 3.281584 | 0.329545 | 2.0 | 80.0 | -0.011364 | 0.164773 | -0.34788 | -0.34788 | 0.512653 | 0.329545 | 0.556818 | 0.329545 | 0.670455 | 1.0 | 3.491525 | 3.061224 | 5.0 | 14 | 88 |
| turtle_soup | low | 48 | 48 | 48 |  | 5.055609 | 3.064376 | 0.229167 | 2.0 | 40.0 | -0.3125 | 0.010417 | -0.527284 | -0.527284 | 0.5377 | 0.229167 | 0.520833 | 0.229167 | 0.770833 | 1.0 | 3.783784 | 2.6 | 4.727273 | 6 | 48 |
| turtle_soup | medium | 654 | 654 | 654 |  | 4.580682 | 3.276729 | 0.255352 | 2.0 | 60.0 | -0.215932 | -0.052151 | -0.5707 | -0.5707 | 0.518549 | 0.255352 | 0.457187 | 0.255352 | 0.735474 | 1.0 | 3.276507 | 2.745819 | 3.988024 | 82 | 654 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 790 | 790 | 790 |  | 4.577637 | 3.27107 | 0.262025 | 2.0 | 61.012658 | -0.199012 | -0.024186 | -0.543242 | -0.543242 | 0.519056 | 0.262025 | 0.472152 | 0.262025 | 0.73038 | 1.0 | 3.331023 | 2.77748 | 4.169082 | 102 | 790 |
