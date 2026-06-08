# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ict2022_mss_fvg
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | BTCUSDT | 29 | 29 | 28 |  | 1.579592 | 0.865454 | 0.344828 | 1.196731 | 83.172414 | -0.191819 | -0.241651 | -0.310477 | -0.310477 | 0.064135 | 0.002317 | 0.066452 | 0.344828 | 0.172414 | 0.103448 | 0.482759 | 1.344828 | 4.214286 | 3.4 | 3.666667 | 2 | 28 |
| ict2022_mss_fvg | ETHUSDT | 31 | 31 | 31 |  | 1.190821 | 0.872943 | 0.322581 | 0.830131 | 81.225806 | -0.564325 | -0.565821 | -0.609914 | -0.609914 | 0.043542 | 0.00055 | 0.044093 | 0.322581 | 0.064516 |  | 0.645161 | 1.16129 | 3.35 | 10.0 |  | 2 | 31 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | edge | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | sweep_extreme | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | conservative | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | unknown | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | strong | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | high | 60 | 60 | 59 |  | 1.375322 | 0.872943 | 0.333333 | 1.007321 | 82.166667 | -0.387543 | -0.411978 | -0.467808 | -0.467808 | 0.053495 | 0.001404 | 0.0549 | 0.333333 | 0.116667 | 0.05 | 0.566667 | 1.25 | 3.705882 | 5.285714 | 3.666667 | 4 | 59 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict2022_mss_fvg | none | 1 | 1 | 1 |  | 1.003058 | 1.003058 |  | 3.329711 | 98.0 | -1.0 | -1.0 | -1.161556 | -1.161556 | 0.161556 |  | 0.161556 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  |  |
| ict2022_mss_fvg | target_rr_below_2 | 36 | 36 | 36 |  | 1.45191 | 0.829989 | 0.527778 | 0.288625 | 78.0 | -0.314512 | -0.298181 | -0.357212 | -0.357212 | 0.058678 | 0.000352 | 0.05903 | 0.527778 | 0.111111 | 0.055556 | 0.444444 | 1.194444 | 1.6875 | 1.5 | 1.0 | 4 | 36 |
| ict2022_mss_fvg | target_rr_below_3 | 23 | 23 | 22 |  | 1.266917 | 0.841552 | 0.043478 | 2.031265 | 88.0 | -0.47921 | -0.571462 | -0.617249 | -0.617249 | 0.040685 | 0.003112 | 0.043797 | 0.043478 | 0.130435 | 0.043478 | 0.73913 | 1.347826 | 5.764706 | 10.333333 | 9.0 |  | 23 |
