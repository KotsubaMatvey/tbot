# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: silver_bullet, ifvg_retest
- symbols: BTCUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 10 | 10 | 3 |  | 13.448039 | 8.878048 | 0.1 | 3.281745 | 69.0 | 0.523537 | 0.095102 | 0.095102 | 0.1 | 0.1 | 0.1 | 0.2 | 5.5 | 1.0 | 1.0 | 1.0 | 2 | 5 |
| silver_bullet | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 10 | 10 | 3 |  | 13.448039 | 8.878048 | 0.1 | 3.281745 | 69.0 | 0.523537 | 0.095102 | 0.095102 | 0.1 | 0.1 | 0.1 | 0.2 | 5.5 | 1.0 | 1.0 | 1.0 | 2 | 5 |
| silver_bullet | edge | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 10 | 10 | 3 |  | 13.448039 | 8.878048 | 0.1 | 3.281745 | 69.0 | 0.523537 | 0.095102 | 0.095102 | 0.1 | 0.1 | 0.1 | 0.2 | 5.5 | 1.0 | 1.0 | 1.0 | 2 | 5 |
| silver_bullet | swing_or_fvg | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 10 | 10 | 3 |  | 13.448039 | 8.878048 | 0.1 | 3.281745 | 69.0 | 0.523537 | 0.095102 | 0.095102 | 0.1 | 0.1 | 0.1 | 0.2 | 5.5 | 1.0 | 1.0 | 1.0 | 2 | 5 |
| silver_bullet | conservative | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 87 | 87 | 76 |  | 2.022498 | 1.15541 | 0.195402 | 2.147327 | 76.965517 | -0.089337 | -0.01497 | -0.01497 | 0.195402 | 0.367816 | 0.195402 | 0.586207 | 1.724138 | 6.196078 | 5.4375 | 6.588235 | 3 | 5 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 10 | 10 | 3 |  | 13.448039 | 8.878048 | 0.1 | 3.281745 | 69.0 | 0.523537 | 0.095102 | 0.095102 | 0.1 | 0.1 | 0.1 | 0.2 | 5.5 | 1.0 | 1.0 | 1.0 | 2 | 5 |
| silver_bullet | none | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 6 | 6 | 3 |  | 13.448039 | 8.878048 | 0.166667 | 2.596192 | 73.0 | 0.523537 | 0.095102 | 0.095102 | 0.166667 | 0.166667 | 0.166667 | 0.333333 | 3.333333 | 1.0 | 1.0 | 1.0 | 2 | 3 |
| ifvg_retest | valid | 4 | 4 |  |  |  |  |  | 4.310076 | 63.0 |  |  |  |  |  |  |  | 8.75 |  |  |  |  | 2 |
| silver_bullet | none | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 6 | 6 | 2 |  | 6.405555 | 6.405555 | 0.166667 | 4.49066 | 76.333333 | 1.285306 | 0.642653 | 0.642653 | 0.166667 | 0.166667 | 0.166667 | 0.166667 | 5.166667 | 1.0 | 1.0 | 1.0 | 1 | 1 |
| ifvg_retest | medium | 4 | 4 | 1 |  | 27.533007 | 27.533007 |  | 1.468374 | 58.0 | -1.0 | -1.0 | -1.0 |  |  |  | 0.25 | 6.0 | 1.0 |  |  | 1 | 4 |
| silver_bullet | high | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | managed_expectancy | avg_managed_outcome_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 5 | 5 | 2 |  | 6.405555 | 6.405555 | 0.2 | 5.11819 | 76.0 | 1.285306 | 0.642653 | 0.642653 | 0.2 | 0.2 | 0.2 | 0.2 | 5.6 | 1.0 | 1.0 | 1.0 | 1 |  |
| ifvg_retest | target_rr_below_2 | 4 | 4 | 1 |  | 27.533007 | 27.533007 |  | 1.222004 | 60.5 | -1.0 | -1.0 | -1.0 |  |  |  | 0.25 | 5.75 | 1.0 |  |  | 1 | 4 |
| ifvg_retest | target_rr_below_3 | 1 | 1 |  |  |  |  |  | 2.338486 | 68.0 |  |  |  |  |  |  |  | 4.0 |  |  |  |  | 1 |
| silver_bullet | none | 77 | 77 | 73 |  | 1.552955 | 1.123624 | 0.207792 | 2.0 | 78.0 | -0.114523 | -0.019493 | -0.019493 | 0.207792 | 0.402597 | 0.207792 | 0.636364 | 1.233766 | 6.408163 | 5.580645 | 6.9375 | 1 |  |
