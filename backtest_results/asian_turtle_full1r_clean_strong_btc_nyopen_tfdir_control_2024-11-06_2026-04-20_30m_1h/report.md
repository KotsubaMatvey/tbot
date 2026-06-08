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
| turtle_soup | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 5 | 5 | 5 |  | 3.849741 | 4.514163 | 0.8 | 1.230056 | 72.0 | 0.5653 | 0.869747 | 0.725829 | 0.725829 | 0.143918 |  | 0.143918 | 0.8 | 0.8 | 0.2 | 0.2 | 1.0 | 12.0 | 1.75 | 1.0 |  | 5 |
| turtle_soup | valid | 14 | 14 | 14 |  | 3.214232 | 2.093143 | 0.571429 | 1.505739 | 72.142857 | 0.601151 | 0.626015 | 0.406573 | 0.406573 | 0.219442 |  | 0.219442 | 0.571429 | 0.785714 | 0.357143 | 0.357143 | 1.0 | 3.2 | 1.363636 | 1.8 | 2 | 13 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 19 | 19 | 19 |  | 3.381471 | 2.469999 | 0.631579 | 1.433191 | 72.105263 | 0.591717 | 0.690155 | 0.490587 | 0.490587 | 0.199567 |  | 0.199567 | 0.631579 | 0.789474 | 0.315789 | 0.315789 | 1.0 | 4.666667 | 1.466667 | 1.666667 | 2 | 18 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 1 | 1 | 1 |  | 6.642168 | 6.642168 | 1.0 | 3.076073 | 90.0 | 3.076073 | 1.0 | 0.584652 | 0.584652 | 0.415348 |  | 0.415348 | 1.0 | 1.0 | 1.0 |  | 1.0 |  | 2.0 | 3.0 |  |  |
| turtle_soup | target_rr_below_2 | 16 | 16 | 16 |  | 3.231318 | 2.392156 | 0.625 | 1.19088 | 70.0 | 0.399366 | 0.632059 | 0.442053 | 0.442053 | 0.190005 |  | 0.190005 | 0.625 | 0.75 | 0.25 | 0.3125 | 1.0 | 3.2 | 1.333333 | 1.5 | 2 | 16 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 2.952352 | 2.952352 | 0.5 | 2.550238 | 80.0 | 0.888347 | 1.0 | 0.831829 | 0.831829 | 0.168171 |  | 0.168171 | 0.5 | 1.0 | 0.5 | 0.5 | 1.0 | 12.0 | 2.0 | 1.0 |  | 2 |
