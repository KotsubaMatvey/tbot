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
| turtle_soup | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 37 | 37 | 37 |  | 3.86117 | 2.314313 | 0.702703 | 1.364558 | 72.972973 | 0.362877 | 0.483167 | 0.291893 | 0.291893 | 0.191274 |  | 0.191274 | 0.702703 | 0.567568 | 0.081081 | 0.27027 | 1.0 | 4.6 | 2.666667 | 3.333333 | 2 | 34 |
| turtle_soup | valid | 46 | 46 | 46 |  | 3.651502 | 2.503283 | 0.413043 | 2.14904 | 75.434783 | -0.001703 | 0.405057 | 0.165417 | 0.165417 | 0.23964 |  | 0.23964 | 0.413043 | 0.652174 | 0.304348 | 0.543478 | 1.0 | 3.32 | 2.166667 | 2.857143 | 9 | 35 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 83 | 83 | 83 |  | 3.744969 | 2.469999 | 0.542169 | 1.799331 | 74.337349 | 0.160821 | 0.439877 | 0.221798 | 0.221798 | 0.218079 |  | 0.218079 | 0.542169 | 0.614458 | 0.204819 | 0.421687 | 1.0 | 3.685714 | 2.372549 | 2.941176 | 11 | 69 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 14 | 14 | 14 |  | 5.742076 | 3.995654 | 0.071429 | 5.186564 | 90.0 | -0.028248 | 0.714286 | 0.362259 | 0.362259 | 0.352027 |  | 0.352027 | 0.071429 | 0.857143 | 0.571429 | 0.785714 | 1.0 | 3.636364 | 2.75 | 4.375 | 8 |  |
| turtle_soup | target_rr_below_2 | 61 | 61 | 61 |  | 3.491367 | 1.935747 | 0.704918 | 0.925731 | 70.0 | 0.29454 | 0.434587 | 0.242732 | 0.242732 | 0.191855 |  | 0.191855 | 0.704918 | 0.57377 | 0.114754 | 0.278689 | 1.0 | 3.058824 | 2.285714 | 1.571429 | 2 | 61 |
| turtle_soup | target_rr_below_3 | 8 | 8 | 8 |  | 2.183746 | 1.937407 | 0.125 | 2.532881 | 80.0 | -0.527913 |  | -0.183632 | -0.183632 | 0.183632 |  | 0.183632 | 0.125 | 0.5 | 0.25 | 0.875 | 1.0 | 5.285714 | 2.0 | 2.0 | 1 | 8 |
