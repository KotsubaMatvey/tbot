# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 5
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | discount | 7 | 7 | 7 |  | 5.550603 | 2.074635 |  | 16.160302 | 80.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  |  |
| turtle_soup | premium | 27 | 27 | 27 |  | 2.152795 | 1.714104 | 0.074074 | 6.36635 | 74.259259 | 0.416089 | 0.074074 | 0.407407 | 0.222222 | 0.555556 | 1.0 | 1.733333 | 1.363636 | 1.833333 |  | 10 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 34 | 34 | 34 |  | 2.852344 | 1.771151 | 0.058824 | 8.382752 | 75.441176 | 0.124541 | 0.058824 | 0.323529 | 0.176471 | 0.647059 | 1.0 | 1.5 | 1.363636 | 1.833333 |  | 10 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 26 | 26 | 26 |  | 3.214725 | 2.098601 | 0.038462 | 9.649416 | 79.230769 | 0.208938 | 0.038462 | 0.307692 | 0.230769 | 0.653846 | 1.0 | 1.647059 | 1.125 | 1.833333 |  | 2 |
| turtle_soup | medium | 8 | 8 | 8 |  | 1.674607 | 1.342352 | 0.125 | 4.266095 | 63.125 | -0.149746 | 0.125 | 0.375 |  | 0.625 | 1.0 | 1.0 | 2.0 |  |  | 8 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 24 | 24 | 24 |  | 3.433067 | 2.30481 | 0.041667 | 10.24889 | 80.0 | 0.176797 | 0.041667 | 0.333333 | 0.25 | 0.708333 | 1.0 | 1.647059 | 1.125 | 1.833333 |  |  |
| turtle_soup | poor_pd_location | 5 | 5 | 5 |  | 2.01598 | 1.482026 |  | 5.940588 | 65.0 | -0.43436 |  | 0.2 |  | 0.8 | 1.0 | 1.0 | 2.0 |  |  | 5 |
| turtle_soup | target_rr_below_2 | 3 | 3 | 3 |  | 1.105652 | 1.202677 | 0.333333 | 1.475272 | 60.0 | 0.32461 | 0.333333 | 0.666667 |  | 0.333333 | 1.0 | 1.0 | 2.0 |  |  | 3 |
| turtle_soup | target_rr_below_3 | 2 | 2 | 2 |  | 0.594621 | 0.594621 |  | 2.455727 | 70.0 | 0.594621 |  |  |  |  | 1.0 |  |  |  |  | 2 |
