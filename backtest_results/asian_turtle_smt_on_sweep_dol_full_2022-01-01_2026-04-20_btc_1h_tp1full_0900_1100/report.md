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
- timeframes: 1h
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
| turtle_soup | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 49 | 49 | 49 |  | 4.025815 | 2.898323 | 0.673469 | 1.554617 | 73.469388 | 0.285987 | 0.512502 | 0.352803 | 0.352803 | 0.159699 |  | 0.159699 | 0.673469 | 0.612245 | 0.183673 | 0.326531 | 1.0 | 6.0 | 2.7 | 1.555556 | 3 | 42 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 7 | 7 | 7 |  | 4.538098 | 4.011702 | 0.142857 | 5.003226 | 90.0 | -0.417704 | 0.714286 | 0.456324 | 0.456324 | 0.257961 |  | 0.257961 | 0.142857 | 0.857143 | 0.428571 | 0.857143 | 1.0 | 7.166667 | 1.666667 | 1.666667 | 2 |  |
| turtle_soup | target_rr_below_2 | 39 | 39 | 39 |  | 3.984781 | 2.314313 | 0.794872 | 0.841807 | 70.0 | 0.414374 | 0.490067 | 0.348269 | 0.348269 | 0.141798 |  | 0.141798 | 0.794872 | 0.564103 | 0.128205 | 0.205128 | 1.0 | 5.375 | 3.136364 | 1.6 | 1 | 39 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 3.363928 | 4.364205 | 0.333333 | 2.774381 | 80.0 | 0.258898 | 0.333333 | 0.170205 | 0.170205 | 0.163128 |  | 0.163128 | 0.333333 | 0.666667 | 0.333333 | 0.666667 | 1.0 | 5.0 | 1.0 | 1.0 |  | 3 |
