# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1m, 5m, 15m, 30m, 1h, 4h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 98 | 98 | 62 | 29 | 9.502403 | 4.359622 | 0.438776 | 2.380803 | 0.481367 | 0.438776 | 0.387755 | 0.265306 | 0.163265 | 5.833333 | 1.6875 | 1.052632 | 1.153846 |  |
| ict2022_mss_fvg | 72 | 72 | 72 |  | 2.309943 | 1.206536 | 0.763889 | 0.662582 | 0.245588 | 0.763889 | 0.319444 | 0.138889 | 0.125 | 1.0 | 3.333333 | 2.652174 | 2.3 |  |
| ifvg_retest | 351 | 351 | 351 |  | 13.974376 | 6.727212 | 0.282051 | 2.0 | -0.103222 | 0.282051 | 0.396011 | 0.282051 | 0.695157 | 2.233618 | 2.094262 | 1.633094 | 2.212121 |  |
| reclaimed_ob | 20 | 20 | 19 | 1 | 4.229816 | 3.559393 | 0.75 | 1.640283 | 0.644338 | 0.75 | 0.7 | 0.4 | 0.2 | 2.7 | 5.0 | 1.0 | 1.625 |  |
| silver_bullet | 35 | 35 | 35 |  | 1.150462 | 0.840245 | 0.142857 | 2.0 | 0.207528 | 0.142857 | 0.342857 | 0.142857 | 0.428571 | 1.057143 | 8.6 | 3.666667 | 4.6 |  |
| turtle_soup | 1550 | 1550 | 1550 |  | 3.894137 | 2.335433 | 0.143871 | 6.490352 | 0.199232 | 0.143871 | 0.463871 | 0.280645 | 0.74 | 1.0 | 4.268527 | 2.788595 | 4.583908 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 98 | 98 | 62 | 29 | 9.502403 | 4.359622 | 0.438776 | 2.380803 | 0.481367 | 0.438776 | 0.387755 | 0.265306 | 0.163265 | 5.833333 | 1.6875 | 1.052632 | 1.153846 |  |
| ict2022_mss_fvg | edge | 72 | 72 | 72 |  | 2.309943 | 1.206536 | 0.763889 | 0.662582 | 0.245588 | 0.763889 | 0.319444 | 0.138889 | 0.125 | 1.0 | 3.333333 | 2.652174 | 2.3 |  |
| ifvg_retest | edge | 351 | 351 | 351 |  | 13.974376 | 6.727212 | 0.282051 | 2.0 | -0.103222 | 0.282051 | 0.396011 | 0.282051 | 0.695157 | 2.233618 | 2.094262 | 1.633094 | 2.212121 |  |
| reclaimed_ob | body_edge | 20 | 20 | 19 | 1 | 4.229816 | 3.559393 | 0.75 | 1.640283 | 0.644338 | 0.75 | 0.7 | 0.4 | 0.2 | 2.7 | 5.0 | 1.0 | 1.625 |  |
| silver_bullet | edge | 35 | 35 | 35 |  | 1.150462 | 0.840245 | 0.142857 | 2.0 | 0.207528 | 0.142857 | 0.342857 | 0.142857 | 0.428571 | 1.057143 | 8.6 | 3.666667 | 4.6 |  |
| turtle_soup | close | 1550 | 1550 | 1550 |  | 3.894137 | 2.335433 | 0.143871 | 6.490352 | 0.199232 | 0.143871 | 0.463871 | 0.280645 | 0.74 | 1.0 | 4.268527 | 2.788595 | 4.583908 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 98 | 98 | 62 | 29 | 9.502403 | 4.359622 | 0.438776 | 2.380803 | 0.481367 | 0.438776 | 0.387755 | 0.265306 | 0.163265 | 5.833333 | 1.6875 | 1.052632 | 1.153846 |  |
| ict2022_mss_fvg | sweep_extreme | 72 | 72 | 72 |  | 2.309943 | 1.206536 | 0.763889 | 0.662582 | 0.245588 | 0.763889 | 0.319444 | 0.138889 | 0.125 | 1.0 | 3.333333 | 2.652174 | 2.3 |  |
| ifvg_retest | ce | 351 | 351 | 351 |  | 13.974376 | 6.727212 | 0.282051 | 2.0 | -0.103222 | 0.282051 | 0.396011 | 0.282051 | 0.695157 | 2.233618 | 2.094262 | 1.633094 | 2.212121 |  |
| reclaimed_ob | mean_threshold | 20 | 20 | 19 | 1 | 4.229816 | 3.559393 | 0.75 | 1.640283 | 0.644338 | 0.75 | 0.7 | 0.4 | 0.2 | 2.7 | 5.0 | 1.0 | 1.625 |  |
| silver_bullet | swing_or_fvg | 35 | 35 | 35 |  | 1.150462 | 0.840245 | 0.142857 | 2.0 | 0.207528 | 0.142857 | 0.342857 | 0.142857 | 0.428571 | 1.057143 | 8.6 | 3.666667 | 4.6 |  |
| turtle_soup | sweep_extreme | 1550 | 1550 | 1550 |  | 3.894137 | 2.335433 | 0.143871 | 6.490352 | 0.199232 | 0.143871 | 0.463871 | 0.280645 | 0.74 | 1.0 | 4.268527 | 2.788595 | 4.583908 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 98 | 98 | 62 | 29 | 9.502403 | 4.359622 | 0.438776 | 2.380803 | 0.481367 | 0.438776 | 0.387755 | 0.265306 | 0.163265 | 5.833333 | 1.6875 | 1.052632 | 1.153846 |  |
| ict2022_mss_fvg | conservative | 72 | 72 | 72 |  | 2.309943 | 1.206536 | 0.763889 | 0.662582 | 0.245588 | 0.763889 | 0.319444 | 0.138889 | 0.125 | 1.0 | 3.333333 | 2.652174 | 2.3 |  |
| ifvg_retest | conservative | 351 | 351 | 351 |  | 13.974376 | 6.727212 | 0.282051 | 2.0 | -0.103222 | 0.282051 | 0.396011 | 0.282051 | 0.695157 | 2.233618 | 2.094262 | 1.633094 | 2.212121 |  |
| reclaimed_ob | conservative | 20 | 20 | 19 | 1 | 4.229816 | 3.559393 | 0.75 | 1.640283 | 0.644338 | 0.75 | 0.7 | 0.4 | 0.2 | 2.7 | 5.0 | 1.0 | 1.625 |  |
| silver_bullet | conservative | 35 | 35 | 35 |  | 1.150462 | 0.840245 | 0.142857 | 2.0 | 0.207528 | 0.142857 | 0.342857 | 0.142857 | 0.428571 | 1.057143 | 8.6 | 3.666667 | 4.6 |  |
| turtle_soup | conservative | 1550 | 1550 | 1550 |  | 3.894137 | 2.335433 | 0.143871 | 6.490352 | 0.199232 | 0.143871 | 0.463871 | 0.280645 | 0.74 | 1.0 | 4.268527 | 2.788595 | 4.583908 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 2126 | 2126 | 2089 | 30 | 5.656781 | 2.609247 | 0.206961 | 5.242651 | 0.162571 | 0.206961 | 0.444497 | 0.274224 | 0.674976 | 1.414299 | 3.911498 | 2.530159 | 3.948542 |  |
