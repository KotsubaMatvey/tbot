# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
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
| turtle_soup | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 18 | 18 | 18 |  | 2.365009 | 2.068201 | 0.277778 | 2.0 | 80.0 | -0.079635 | -0.246301 | -0.498008 | -0.498008 | 0.251707 | 0.277778 | 0.333333 | 0.277778 | 0.666667 | 1.0 | 3.083333 | 1.5 | 3.0 |  | 18 |
| turtle_soup | medium | 125 | 125 | 125 |  | 3.382917 | 2.057234 | 0.256 | 2.0 | 60.0 | -0.078612 | -0.011572 | -0.286348 | -0.286348 | 0.274776 | 0.256 | 0.456 | 0.256 | 0.664 | 1.0 | 3.325301 | 3.491228 | 6.03125 | 15 | 125 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 143 | 143 | 143 |  | 3.254789 | 2.057234 | 0.258741 | 2.0 | 62.517483 | -0.078741 | -0.041118 | -0.31299 | -0.31299 | 0.271872 | 0.258741 | 0.440559 | 0.258741 | 0.664336 | 1.0 | 3.294737 | 3.301587 | 5.621622 | 15 | 143 |
