# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup, ifvg_retest
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 5
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 7 | 7 | 5 |  | 8.833849 | 7.128581 | 0.285714 | 5.341047 | 94.0 | 1.250609 | 0.285714 | 0.285714 | 0.285714 | 0.428571 | 1.8 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 7 | 7 | 5 |  | 8.833849 | 7.128581 | 0.285714 | 5.341047 | 94.0 | 1.250609 | 0.285714 | 0.285714 | 0.285714 | 0.428571 | 1.8 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | close | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 7 | 7 | 5 |  | 8.833849 | 7.128581 | 0.285714 | 5.341047 | 94.0 | 1.250609 | 0.285714 | 0.285714 | 0.285714 | 0.428571 | 1.8 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | sweep_extreme | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 7 | 7 | 5 |  | 8.833849 | 7.128581 | 0.285714 | 5.341047 | 94.0 | 1.250609 | 0.285714 | 0.285714 | 0.285714 | 0.428571 | 1.8 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | conservative | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 41 | 41 | 39 |  | 3.619204 | 2.074635 | 0.097561 | 7.863436 | 78.609756 | 0.268909 | 0.097561 | 0.317073 | 0.195122 | 0.609756 | 1.102564 | 1.44 | 1.307692 | 1.625 |  | 14 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | discount | 1 | 1 | 1 |  | 8.590473 | 8.590473 |  | 17.356968 | 100.0 | -1.0 |  |  |  | 1.0 | 3.0 | 1.0 |  |  |  |  |
| ifvg_retest | premium | 6 | 6 | 4 |  | 8.894694 | 6.891253 | 0.333333 | 3.338393 | 93.0 | 1.813261 | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 1.5 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | discount | 7 | 7 | 7 |  | 5.550603 | 2.074635 |  | 16.160302 | 80.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  |  |
| turtle_soup | premium | 27 | 27 | 27 |  | 2.152795 | 1.714104 | 0.074074 | 6.36635 | 74.259259 | 0.416089 | 0.074074 | 0.407407 | 0.222222 | 0.555556 | 1.0 | 1.733333 | 1.363636 | 1.833333 |  | 10 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 4 | 4 | 2 |  | 7.622199 | 7.622199 |  | 4.834145 | 90.25 | -1.0 |  |  |  | 0.5 | 2.0 | 1.0 |  |  |  | 3 |
| ifvg_retest | valid | 3 | 3 | 3 |  | 9.641616 | 7.128581 | 0.666667 | 6.016915 | 99.0 | 2.751015 | 0.666667 | 0.666667 | 0.666667 | 0.333333 | 1.666667 | 1.0 | 1.0 | 1.0 |  | 1 |
| turtle_soup | none | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 7 | 7 | 5 |  | 8.833849 | 7.128581 | 0.285714 | 5.341047 | 94.0 | 1.250609 | 0.285714 | 0.285714 | 0.285714 | 0.428571 | 1.8 | 1.0 | 1.0 | 1.0 |  | 4 |
| turtle_soup | high | 26 | 26 | 26 |  | 3.214725 | 2.098601 | 0.038462 | 9.649416 | 79.230769 | 0.208938 | 0.038462 | 0.307692 | 0.230769 | 0.653846 | 1.0 | 1.647059 | 1.125 | 1.833333 |  | 2 |
| turtle_soup | medium | 8 | 8 | 8 |  | 1.674607 | 1.342352 | 0.125 | 4.266095 | 63.125 | -0.149746 | 0.125 | 0.375 |  | 0.625 | 1.0 | 1.0 | 2.0 |  |  | 8 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 3 | 3 | 3 |  | 7.19136 | 7.128581 | 0.666667 | 8.870004 | 100.0 | 2.751015 | 0.666667 | 0.666667 | 0.666667 | 0.333333 | 2.333333 | 1.0 | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 1 | 1 | 1 |  | 15.941242 | 15.941242 |  | 8.797701 | 97.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 2 | 2 | 1 |  | 6.653925 | 6.653925 |  | 0.37002 | 82.0 | -1.0 |  |  |  | 0.5 | 1.0 | 1.0 |  |  |  | 2 |
| ifvg_retest | target_rr_below_2 | 1 | 1 |  |  |  |  |  | 1.239574 | 97.0 |  |  |  |  |  |  |  |  |  |  | 1 |
| turtle_soup | none | 24 | 24 | 24 |  | 3.433067 | 2.30481 | 0.041667 | 10.24889 | 80.0 | 0.176797 | 0.041667 | 0.333333 | 0.25 | 0.708333 | 1.0 | 1.647059 | 1.125 | 1.833333 |  |  |
| turtle_soup | poor_pd_location | 5 | 5 | 5 |  | 2.01598 | 1.482026 |  | 5.940588 | 65.0 | -0.43436 |  | 0.2 |  | 0.8 | 1.0 | 1.0 | 2.0 |  |  | 5 |
| turtle_soup | target_rr_below_2 | 3 | 3 | 3 |  | 1.105652 | 1.202677 | 0.333333 | 1.475272 | 60.0 | 0.32461 | 0.333333 | 0.666667 |  | 0.333333 | 1.0 | 1.0 | 2.0 |  |  | 3 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 0.594621 | 0.594621 |  | 2.455727 | 70.0 | 0.594621 |  |  |  |  | 1.0 |  |  |  |  | 2 |
