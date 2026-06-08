# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_oos_2022-01-01_2024-11-05
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
| turtle_soup | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 17 | 17 | 17 |  | 4.300193 | 2.098568 | 0.647059 | 1.417597 | 72.941176 | 0.405206 | 0.618351 | 0.477029 | 0.477029 | 0.141323 |  | 0.141323 | 0.647059 | 0.647059 |  | 0.235294 | 1.0 | 7.25 | 5.909091 |  | 1 | 16 |
| turtle_soup | valid | 14 | 14 | 14 |  | 2.697525 | 1.185319 | 0.285714 | 1.947256 | 75.714286 | -0.522438 | 0.06486 | -0.095113 | -0.095113 | 0.159973 |  | 0.159973 | 0.285714 | 0.428571 | 0.071429 | 0.714286 | 1.0 | 2.5 | 2.166667 | 1.0 | 2 | 10 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 31 | 31 | 31 |  | 3.576408 | 1.481125 | 0.483871 | 1.656798 | 74.193548 | -0.01373 | 0.368387 | 0.218642 | 0.218642 | 0.149745 |  | 0.149745 | 0.483871 | 0.548387 | 0.032258 | 0.451613 | 1.0 | 3.857143 | 4.588235 | 1.0 | 3 | 26 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 5 | 5 | 5 |  | 3.829684 | 3.767721 |  | 4.469805 | 90.0 | -1.0 | 0.6 | 0.364857 | 0.364857 | 0.235143 |  | 0.235143 |  | 0.8 | 0.2 | 1.0 | 1.0 | 2.2 | 1.0 | 1.0 | 2 |  |
| turtle_soup | target_rr_below_2 | 23 | 23 | 23 |  | 3.674836 | 1.279143 | 0.652174 | 0.890481 | 70.0 | 0.221868 | 0.322609 | 0.185611 | 0.185611 | 0.136998 |  | 0.136998 | 0.652174 | 0.478261 |  | 0.304348 | 1.0 | 4.714286 | 4.727273 |  | 1 | 23 |
| turtle_soup | target_rr_below_3 | 3 | 3 | 3 |  | 2.399664 | 1.471412 |  | 2.843547 | 80.0 | -0.176196 | 0.333333 | 0.228187 | 0.228187 | 0.105146 |  | 0.105146 |  | 0.666667 |  | 0.666667 | 1.0 | 5.0 | 11.0 |  |  | 3 |
