# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
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
| turtle_soup | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 312 | 312 | 312 |  | 3.149547 | 1.975561 | 0.24359 | 2.0 | 62.403846 | -0.092569 | 0.028188 | -0.167621 | -0.167621 | 0.195808 | 0.24359 | 0.471154 | 0.24359 | 0.669872 | 1.0 | 3.84689 | 3.265306 | 5.118421 | 31 | 312 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 38 | 38 | 38 |  | 2.712057 | 1.958606 | 0.236842 | 2.0 | 80.0 | -0.248248 | -0.274564 | -0.478869 | -0.478869 | 0.204305 | 0.236842 | 0.342105 | 0.236842 | 0.736842 | 1.0 | 2.714286 | 2.307692 | 4.333333 | 2 | 38 |
| turtle_soup | medium | 274 | 274 | 274 |  | 3.210221 | 1.975561 | 0.244526 | 2.0 | 59.963504 | -0.070978 | 0.070175 | -0.124455 | -0.124455 | 0.19463 | 0.244526 | 0.489051 | 0.244526 | 0.660584 | 1.0 | 4.022099 | 3.358209 | 5.223881 | 29 | 274 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_2 | 1 | 1 | 1 |  | 0.038426 | 0.038426 |  | 2.0 | 50.0 | -1.0 | -1.0 | -1.147823 | -1.147823 | 0.147823 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| turtle_soup | target_rr_below_3 | 311 | 311 | 311 |  | 3.159551 | 1.97928 | 0.244373 | 2.0 | 62.44373 | -0.089651 | 0.031494 | -0.164469 | -0.164469 | 0.195963 | 0.244373 | 0.472669 | 0.244373 | 0.66881 | 1.0 | 3.860577 | 3.265306 | 5.118421 | 31 | 311 |
