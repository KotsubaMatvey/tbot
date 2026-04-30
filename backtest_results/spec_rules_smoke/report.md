# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: ifvg_retest, rejection_block
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: strict
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | body_level | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | wick_extreme | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | conservative | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | discount | 4 | 4 | 1 |  | 1.958823 | 1.958823 | 0.25 | 8.036682 | 89.5 | 1.915226 | 1.457613 | 1.457613 | 0.25 | 0.25 |  |  | 2.0 |  | 5.0 |  |  | 2 |
| rejection_block | premium | 7 | 7 | 1 |  | 1.834568 | 1.834568 |  | 21.36556 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.142857 | 3.0 | 4.0 |  |  |  |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | high | 11 | 11 | 2 |  | 1.896696 | 1.896696 | 0.090909 | 16.518695 | 94.272727 | 0.457613 | 0.228807 | 0.228807 | 0.090909 | 0.090909 |  | 0.090909 | 2.6 | 4.0 | 5.0 |  |  | 2 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rejection_block | none | 9 | 9 | 1 |  | 1.834568 | 1.834568 |  | 19.7345 | 97.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.111111 | 3.0 | 4.0 |  |  |  |  |
| rejection_block | target_rr_below_2 | 1 | 1 | 1 |  | 1.958823 | 1.958823 | 1.0 | 1.915226 | 77.0 | 1.915226 | 1.457613 | 1.457613 | 1.0 | 1.0 |  |  | 2.0 |  | 5.0 |  |  | 1 |
| rejection_block | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.179919 | 87.0 |  |  |  |  |  |  |  | 2.0 |  |  |  |  | 1 |
