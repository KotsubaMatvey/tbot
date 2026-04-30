# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob, rejection_block, mitigation_block
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 24 | 24 | 14 | 9 | 16.529494 | 9.821366 | 0.291667 | 3.315362 | 81.083333 | 1.618258 | 0.291667 | 0.291667 | 0.291667 | 0.291667 | 7.1 | 1.142857 | 1.0 | 1.0 |  | 24 |
| ict2022_mss_fvg | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | 27 | 27 | 26 |  | 17.34036 | 8.102736 | 0.111111 | 4.63422 | 96.481481 | -0.738586 | 0.111111 | 0.148148 | 0.111111 | 0.851852 | 3.576923 | 1.130435 | 1.0 | 1.333333 |  | 21 |
| mitigation_block | 56 | 56 | 56 |  | 2.074087 | 1.192588 | 0.517857 | 0.725712 | 72.678571 | -0.287414 | 0.517857 | 0.303571 | 0.232143 | 0.482143 | 1.0 | 2.666667 | 4.941176 | 6.846154 |  | 56 |
| reclaimed_ob | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | 57 | 57 | 57 |  | 6.022033 | 3.934155 | 0.578947 | 2.056392 | 75.245614 | 0.395593 | 0.578947 | 0.649123 | 0.175439 | 0.350877 | 1.0 | 2.6 | 2.162162 | 2.0 |  | 50 |
| silver_bullet | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 24 | 24 | 14 | 9 | 16.529494 | 9.821366 | 0.291667 | 3.315362 | 81.083333 | 1.618258 | 0.291667 | 0.291667 | 0.291667 | 0.291667 | 7.1 | 1.142857 | 1.0 | 1.0 |  | 24 |
| ict2022_mss_fvg | edge | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | edge | 27 | 27 | 26 |  | 17.34036 | 8.102736 | 0.111111 | 4.63422 | 96.481481 | -0.738586 | 0.111111 | 0.148148 | 0.111111 | 0.851852 | 3.576923 | 1.130435 | 1.0 | 1.333333 |  | 21 |
| mitigation_block | body_zone_retest | 56 | 56 | 56 |  | 2.074087 | 1.192588 | 0.517857 | 0.725712 | 72.678571 | -0.287414 | 0.517857 | 0.303571 | 0.232143 | 0.482143 | 1.0 | 2.666667 | 4.941176 | 6.846154 |  | 56 |
| reclaimed_ob | body_edge | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | body_level | 57 | 57 | 57 |  | 6.022033 | 3.934155 | 0.578947 | 2.056392 | 75.245614 | 0.395593 | 0.578947 | 0.649123 | 0.175439 | 0.350877 | 1.0 | 2.6 | 2.162162 | 2.0 |  | 50 |
| silver_bullet | edge | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | close | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 24 | 24 | 14 | 9 | 16.529494 | 9.821366 | 0.291667 | 3.315362 | 81.083333 | 1.618258 | 0.291667 | 0.291667 | 0.291667 | 0.291667 | 7.1 | 1.142857 | 1.0 | 1.0 |  | 24 |
| ict2022_mss_fvg | sweep_extreme | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | ce | 27 | 27 | 26 |  | 17.34036 | 8.102736 | 0.111111 | 4.63422 | 96.481481 | -0.738586 | 0.111111 | 0.148148 | 0.111111 | 0.851852 | 3.576923 | 1.130435 | 1.0 | 1.333333 |  | 21 |
| mitigation_block | block_extreme | 56 | 56 | 56 |  | 2.074087 | 1.192588 | 0.517857 | 0.725712 | 72.678571 | -0.287414 | 0.517857 | 0.303571 | 0.232143 | 0.482143 | 1.0 | 2.666667 | 4.941176 | 6.846154 |  | 56 |
| reclaimed_ob | mean_threshold | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | wick_extreme | 57 | 57 | 57 |  | 6.022033 | 3.934155 | 0.578947 | 2.056392 | 75.245614 | 0.395593 | 0.578947 | 0.649123 | 0.175439 | 0.350877 | 1.0 | 2.6 | 2.162162 | 2.0 |  | 50 |
| silver_bullet | swing_or_fvg | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | sweep_extreme | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 24 | 24 | 14 | 9 | 16.529494 | 9.821366 | 0.291667 | 3.315362 | 81.083333 | 1.618258 | 0.291667 | 0.291667 | 0.291667 | 0.291667 | 7.1 | 1.142857 | 1.0 | 1.0 |  | 24 |
| ict2022_mss_fvg | conservative | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | conservative | 27 | 27 | 26 |  | 17.34036 | 8.102736 | 0.111111 | 4.63422 | 96.481481 | -0.738586 | 0.111111 | 0.148148 | 0.111111 | 0.851852 | 3.576923 | 1.130435 | 1.0 | 1.333333 |  | 21 |
| mitigation_block | conservative | 56 | 56 | 56 |  | 2.074087 | 1.192588 | 0.517857 | 0.725712 | 72.678571 | -0.287414 | 0.517857 | 0.303571 | 0.232143 | 0.482143 | 1.0 | 2.666667 | 4.941176 | 6.846154 |  | 56 |
| reclaimed_ob | conservative | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | conservative | 57 | 57 | 57 |  | 6.022033 | 3.934155 | 0.578947 | 2.056392 | 75.245614 | 0.395593 | 0.578947 | 0.649123 | 0.175439 | 0.350877 | 1.0 | 2.6 | 2.162162 | 2.0 |  | 50 |
| silver_bullet | conservative | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | conservative | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 291 | 291 | 280 | 9 | 6.224314 | 3.512161 | 0.333333 | 3.777754 | 66.058419 | 0.175986 | 0.333333 | 0.443299 | 0.250859 | 0.580756 | 1.695804 | 2.87574 | 2.55814 | 4.191781 |  | 188 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | discount | 8 | 8 | 5 | 3 | 23.532599 | 16.018189 | 0.25 | 4.371356 | 95.0 | 3.62341 | 0.25 | 0.375 | 0.375 | 0.375 | 7.166667 | 1.333333 | 1.0 | 1.0 |  | 8 |
| breaker_block | premium | 14 | 14 | 8 | 5 | 13.320472 | 5.670591 | 0.357143 | 2.591743 | 73.714286 | 0.69232 | 0.357143 | 0.285714 | 0.285714 | 0.214286 | 6.666667 | 1.0 | 1.0 | 1.0 |  | 14 |
| breaker_block | unknown | 2 | 2 | 1 | 1 | 7.186145 | 7.186145 |  | 4.15672 | 77.0 | -1.0 |  |  |  | 0.5 | 9.5 | 1.0 |  |  |  | 2 |
| ict2022_mss_fvg | discount | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | discount | 10 | 10 | 10 |  | 16.714285 | 5.662569 | 0.1 | 4.869006 | 100.0 | -0.765693 | 0.1 | 0.2 | 0.1 | 0.9 | 4.8 | 1.333333 | 1.0 | 1.0 |  | 5 |
| ifvg_retest | equilibrium | 1 | 1 | 1 |  | 8.549972 | 8.549972 |  | 0.58218 | 85.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| ifvg_retest | premium | 16 | 16 | 15 |  | 18.34377 | 9.176501 | 0.125 | 4.740732 | 95.0 | -0.703088 | 0.125 | 0.125 | 0.125 | 0.8125 | 2.933333 | 1.0 | 1.0 | 1.5 |  | 15 |
| mitigation_block | discount | 10 | 10 | 10 |  | 1.879711 | 0.027391 | 0.2 | 0.895406 | 77.4 | -0.718536 | 0.2 | 0.1 |  | 0.8 | 1.0 | 1.75 | 2.0 |  |  | 10 |
| mitigation_block | equilibrium | 2 | 2 | 2 |  | 0.674168 | 0.674168 |  | 4.048443 | 85.0 | -1.0 |  |  |  | 1.0 | 1.0 | 3.5 |  |  |  | 2 |
| mitigation_block | premium | 41 | 41 | 41 |  | 2.335437 | 2.017137 | 0.658537 | 0.496783 | 71.341463 | -0.095361 | 0.658537 | 0.390244 | 0.317073 | 0.341463 | 1.0 | 3.428571 | 5.125 | 6.846154 |  | 41 |
| mitigation_block | unknown | 3 | 3 | 3 |  | 0.083494 |  |  | 1.073597 | 67.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 3 |
| reclaimed_ob | discount | 2 | 2 | 2 |  | 11.898319 | 11.898319 | 0.5 | 2.484812 | 87.5 | 0.750966 | 0.5 | 0.5 | 0.5 | 0.5 | 2.5 | 1.0 | 1.0 | 1.0 |  | 2 |
| reclaimed_ob | premium | 5 | 5 | 5 |  | 11.572328 | 13.034875 | 0.8 | 0.95876 | 70.0 | 0.404391 | 0.8 | 1.0 | 0.6 | 0.2 | 2.4 | 3.0 | 1.0 | 1.0 |  | 5 |
| rejection_block | discount | 12 | 12 | 12 |  | 5.343797 | 3.785139 | 0.5 | 2.277674 | 89.166667 | 0.922053 | 0.5 | 0.833333 | 0.333333 | 0.25 | 1.0 | 1.333333 | 3.3 | 1.5 |  | 10 |
| rejection_block | equilibrium | 2 | 2 | 2 |  | 8.344201 | 8.344201 | 0.5 | 4.584483 | 80.0 | 0.345349 | 0.5 | 1.0 | 1.0 | 0.5 | 1.0 | 4.0 | 1.0 | 1.0 |  | 2 |
| rejection_block | premium | 33 | 33 | 33 |  | 7.311538 | 6.750655 | 0.666667 | 1.66532 | 68.454545 | 0.351973 | 0.666667 | 0.575758 | 0.090909 | 0.30303 | 1.0 | 2.4 | 1.421053 | 3.666667 |  | 33 |
| rejection_block | unknown | 10 | 10 | 10 |  | 2.116119 | 2.059705 | 0.4 | 2.575775 | 80.0 | -0.082163 | 0.4 | 0.6 | 0.1 | 0.6 | 1.0 | 3.333333 | 3.0 | 1.0 |  | 5 |
| silver_bullet | none | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | none | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | none | 24 | 24 | 14 | 9 | 16.529494 | 9.821366 | 0.291667 | 3.315362 | 81.083333 | 1.618258 | 0.291667 | 0.291667 | 0.291667 | 0.291667 | 7.1 | 1.142857 | 1.0 | 1.0 |  | 24 |
| ict2022_mss_fvg | strong | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | strong | 12 | 12 | 12 |  | 17.325083 | 6.200782 | 0.166667 | 4.692718 | 97.5 | -0.58772 | 0.166667 | 0.25 | 0.166667 | 0.833333 | 3.666667 | 1.3 | 1.0 | 1.5 |  | 10 |
| ifvg_retest | valid | 15 | 15 | 14 |  | 17.353455 | 8.102736 | 0.066667 | 4.587422 | 95.666667 | -0.8679 | 0.066667 | 0.066667 | 0.066667 | 0.866667 | 3.5 | 1.0 | 1.0 | 1.0 |  | 11 |
| mitigation_block | none | 56 | 56 | 56 |  | 2.074087 | 1.192588 | 0.517857 | 0.725712 | 72.678571 | -0.287414 | 0.517857 | 0.303571 | 0.232143 | 0.482143 | 1.0 | 2.666667 | 4.941176 | 6.846154 |  | 56 |
| reclaimed_ob | none | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | none | 57 | 57 | 57 |  | 6.022033 | 3.934155 | 0.578947 | 2.056392 | 75.245614 | 0.395593 | 0.578947 | 0.649123 | 0.175439 | 0.350877 | 1.0 | 2.6 | 2.162162 | 2.0 |  | 50 |
| silver_bullet | none | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | none | 113 | 113 | 113 |  | 4.350611 | 2.843218 | 0.159292 | 6.130359 | 46.725664 | 0.189722 | 0.159292 | 0.469027 | 0.292035 | 0.769912 | 1.0 | 3.367816 | 2.584906 | 4.727273 |  | 23 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | high | 20 | 20 | 12 | 7 | 18.579353 | 12.549805 | 0.3 | 3.905966 | 84.65 | 1.966884 | 0.3 | 0.35 | 0.35 | 0.3 | 6.6875 | 1.166667 | 1.0 | 1.0 |  | 20 |
| breaker_block | medium | 4 | 4 | 2 | 2 | 4.230338 | 4.230338 | 0.25 | 0.362342 | 63.25 | -0.473498 | 0.25 |  |  | 0.25 | 8.75 | 1.0 |  |  |  | 4 |
| ict2022_mss_fvg | high | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | high | 27 | 27 | 26 |  | 17.34036 | 8.102736 | 0.111111 | 4.63422 | 96.481481 | -0.738586 | 0.111111 | 0.148148 | 0.111111 | 0.851852 | 3.576923 | 1.130435 | 1.0 | 1.333333 |  | 21 |
| mitigation_block | high | 45 | 45 | 45 |  | 2.21218 | 0.762836 | 0.488889 | 0.791847 | 74.955556 | -0.295952 | 0.488889 | 0.355556 | 0.288889 | 0.511111 | 1.0 | 2.956522 | 5.1875 | 6.846154 |  | 45 |
| mitigation_block | medium | 11 | 11 | 11 |  | 1.50916 | 1.192588 | 0.636364 | 0.45516 | 63.363636 | -0.252486 | 0.636364 | 0.090909 |  | 0.363636 | 1.0 | 1.0 | 1.0 |  |  | 11 |
| reclaimed_ob | high | 7 | 7 | 7 |  | 11.665468 | 13.034875 | 0.714286 | 1.394775 | 75.0 | 0.503412 | 0.714286 | 0.857143 | 0.571429 | 0.285714 | 2.428571 | 2.0 | 1.0 | 1.0 |  | 7 |
| rejection_block | high | 37 | 37 | 37 |  | 5.82395 | 3.811794 | 0.432432 | 2.703842 | 82.0 | 0.339679 | 0.432432 | 0.702703 | 0.243243 | 0.459459 | 1.0 | 2.882353 | 2.384615 | 2.111111 |  | 30 |
| rejection_block | medium | 20 | 20 | 20 |  | 6.388487 | 3.934155 | 0.85 | 0.85861 | 62.75 | 0.499034 | 0.85 | 0.55 | 0.05 | 0.15 | 1.0 | 1.0 | 1.636364 | 1.0 |  | 20 |
| silver_bullet | medium | 6 | 6 | 6 |  | 2.541757 | 2.108015 | 0.333333 | 2.0 | 68.0 | 0.299089 | 0.333333 | 0.666667 | 0.333333 | 0.5 | 1.0 | 10.333333 | 2.75 | 12.5 |  | 6 |
| turtle_soup | low | 23 | 23 | 23 |  | 3.063405 | 3.128466 | 0.347826 | 1.717063 | 33.913043 | -0.022767 | 0.347826 | 0.521739 | 0.347826 | 0.608696 | 1.0 | 3.785714 | 3.166667 | 4.875 |  | 23 |
| turtle_soup | medium | 90 | 90 | 90 |  | 4.679563 | 2.583977 | 0.111111 | 7.258201 | 50.0 | 0.244025 | 0.111111 | 0.455556 | 0.277778 | 0.811111 | 1.0 | 3.287671 | 2.414634 | 4.68 |  |  |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | insufficient_displacement | 6 | 6 | 5 | 1 | 21.76619 | 12.456588 | 0.333333 | 8.091252 | 97.833333 | 3.62341 | 0.333333 | 0.5 | 0.5 | 0.5 | 4.0 | 1.333333 | 1.0 | 1.0 |  | 6 |
| breaker_block | insufficient_displacement;target_rr_below_2 | 4 | 4 | 1 | 3 | 16.018189 | 16.018189 |  | 0.698506 | 84.25 | -1.0 |  |  |  | 0.25 | 14.0 | 1.0 |  |  |  | 4 |
| breaker_block | poor_pd_location;insufficient_displacement | 2 | 2 |  | 1 |  |  |  | 6.800344 | 90.0 |  |  |  |  |  |  |  |  |  |  | 2 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_2 | 9 | 9 | 5 | 4 | 14.875259 | 5.039347 | 0.333333 | 0.786289 | 67.333333 | 0.287749 | 0.333333 | 0.222222 | 0.222222 | 0.222222 | 5.555556 | 1.0 | 1.0 | 1.0 |  | 9 |
| breaker_block | poor_pd_location;insufficient_displacement;target_rr_below_3 | 3 | 3 | 3 |  | 10.729159 | 12.643023 | 0.666667 | 2.51662 | 78.666667 | 1.366605 | 0.666667 | 0.666667 | 0.666667 | 0.333333 | 10.0 | 1.0 | 1.0 | 1.0 |  | 3 |
| ict2022_mss_fvg | poor_pd_location | 1 | 1 | 1 |  | 12.613144 | 12.613144 |  | 22.285479 | 100.0 | 12.613144 |  | 1.0 | 1.0 |  | 1.0 |  | 1.0 | 1.0 |  | 1 |
| ifvg_retest | equilibrium;target_rr_below_2 | 1 | 1 | 1 |  | 8.549972 | 8.549972 |  | 0.58218 | 85.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| ifvg_retest | none | 6 | 6 | 5 |  | 19.159692 | 7.6555 |  | 9.260165 | 100.0 | -1.0 |  | 0.166667 | 0.166667 | 0.833333 | 5.0 | 1.4 | 1.0 | 1.0 |  |  |
| ifvg_retest | poor_pd_location | 8 | 8 | 8 |  | 26.142128 | 19.765201 |  | 7.089026 | 98.875 | -1.0 |  |  |  | 1.0 | 3.5 | 1.0 |  |  |  | 8 |
| ifvg_retest | poor_pd_location;target_rr_below_2 | 6 | 6 | 6 |  | 10.904316 | 7.499549 | 0.333333 | 1.055469 | 88.166667 | -0.257719 | 0.333333 | 0.333333 | 0.333333 | 0.666667 | 2.5 | 1.0 | 1.0 | 1.5 |  | 6 |
| ifvg_retest | target_rr_below_2 | 6 | 6 | 6 |  | 11.98967 | 1.342104 | 0.166667 | 0.989293 | 100.0 | -0.609488 | 0.166667 | 0.166667 |  | 0.833333 | 4.0 | 1.2 | 1.0 |  |  | 6 |
| mitigation_block | equilibrium | 1 | 1 | 1 |  | 0.623866 | 0.623866 |  | 5.846346 | 90.0 | -1.0 |  |  |  | 1.0 | 1.0 | 1.0 |  |  |  | 1 |
| mitigation_block | equilibrium;target_rr_below_3 | 1 | 1 | 1 |  | 0.724469 | 0.724469 |  | 2.25054 | 80.0 | -1.0 |  |  |  | 1.0 | 1.0 | 6.0 |  |  |  | 1 |
| mitigation_block | poor_pd_location | 1 | 1 | 1 |  | 2.86229 | 2.86229 |  | 3.880602 | 82.0 | -1.0 |  | 1.0 | 1.0 | 1.0 | 1.0 | 17.0 | 2.0 | 12.0 |  | 1 |
| mitigation_block | poor_pd_location;target_rr_below_2 | 39 | 39 | 39 |  | 2.332197 | 2.017137 | 0.666667 | 0.380982 | 69.692308 | -0.125893 | 0.666667 | 0.358974 | 0.282051 | 0.333333 | 1.0 | 2.615385 | 5.214286 | 6.0 |  | 39 |
| mitigation_block | poor_pd_location;target_rr_below_3 | 4 | 4 | 4 |  | 0.524828 | 0.027391 | 0.25 | 2.0 | 80.0 | -0.25 | 0.25 | 0.25 | 0.25 | 0.75 | 1.0 | 2.0 | 7.0 | 11.0 |  | 4 |
| mitigation_block | target_rr_below_2 | 10 | 10 | 10 |  | 1.888324 |  | 0.2 | 0.580406 | 78.0 | -0.718536 | 0.2 | 0.1 |  | 0.8 | 1.0 | 1.0 | 2.0 |  |  | 10 |
| reclaimed_ob | poor_pd_location;target_rr_below_2 | 5 | 5 | 5 |  | 11.572328 | 13.034875 | 0.8 | 0.95876 | 70.0 | 0.404391 | 0.8 | 1.0 | 0.6 | 0.2 | 2.4 | 3.0 | 1.0 | 1.0 |  | 5 |
| reclaimed_ob | poor_pd_location;target_rr_below_3 | 1 | 1 | 1 |  | 20.751717 | 20.751717 | 1.0 | 2.501932 | 80.0 | 2.501932 | 1.0 | 1.0 | 1.0 |  | 3.0 |  | 1.0 | 1.0 |  | 1 |
| reclaimed_ob | target_rr_below_3 | 1 | 1 | 1 |  | 3.044922 | 3.044922 |  | 2.467692 | 95.0 | -1.0 |  |  |  | 1.0 | 2.0 | 1.0 |  |  |  | 1 |
