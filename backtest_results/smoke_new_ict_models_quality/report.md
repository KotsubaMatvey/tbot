# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- models: turtle_soup, silver_bullet, ifvg_retest
- symbols: BTCUSDT
- timeframes: 5m, 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 249 | 249 | 249 |  | 12.350424 | 7.711615 | 0.353414 | 2.0 | 0.083057 | 0.353414 | 0.465863 | 0.353414 | 0.638554 | 2.120482 | 1.320755 | 1.163793 | 1.625 |  |
| silver_bullet | 10 | 10 | 10 |  | 1.046651 | 0.894116 |  | 2.0 | -0.443002 |  | 0.2 |  | 0.8 | 1.2 | 7.5 | 11.5 |  |  |
| turtle_soup | 1313 | 1313 | 1313 |  | 3.562421 | 2.333024 | 0.163747 | 6.470983 | 0.212729 | 0.163747 | 0.491241 | 0.301599 | 0.723534 | 1.0 | 4.234737 | 2.595349 | 4.462121 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 249 | 249 | 249 |  | 12.350424 | 7.711615 | 0.353414 | 2.0 | 0.083057 | 0.353414 | 0.465863 | 0.353414 | 0.638554 | 2.120482 | 1.320755 | 1.163793 | 1.625 |  |
| silver_bullet | edge | 10 | 10 | 10 |  | 1.046651 | 0.894116 |  | 2.0 | -0.443002 |  | 0.2 |  | 0.8 | 1.2 | 7.5 | 11.5 |  |  |
| turtle_soup | close | 1313 | 1313 | 1313 |  | 3.562421 | 2.333024 | 0.163747 | 6.470983 | 0.212729 | 0.163747 | 0.491241 | 0.301599 | 0.723534 | 1.0 | 4.234737 | 2.595349 | 4.462121 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 249 | 249 | 249 |  | 12.350424 | 7.711615 | 0.353414 | 2.0 | 0.083057 | 0.353414 | 0.465863 | 0.353414 | 0.638554 | 2.120482 | 1.320755 | 1.163793 | 1.625 |  |
| silver_bullet | swing_or_fvg | 10 | 10 | 10 |  | 1.046651 | 0.894116 |  | 2.0 | -0.443002 |  | 0.2 |  | 0.8 | 1.2 | 7.5 | 11.5 |  |  |
| turtle_soup | sweep_extreme | 1313 | 1313 | 1313 |  | 3.562421 | 2.333024 | 0.163747 | 6.470983 | 0.212729 | 0.163747 | 0.491241 | 0.301599 | 0.723534 | 1.0 | 4.234737 | 2.595349 | 4.462121 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 249 | 249 | 249 |  | 12.350424 | 7.711615 | 0.353414 | 2.0 | 0.083057 | 0.353414 | 0.465863 | 0.353414 | 0.638554 | 2.120482 | 1.320755 | 1.163793 | 1.625 |  |
| silver_bullet | conservative | 10 | 10 | 10 |  | 1.046651 | 0.894116 |  | 2.0 | -0.443002 |  | 0.2 |  | 0.8 | 1.2 | 7.5 | 11.5 |  |  |
| turtle_soup | conservative | 1313 | 1313 | 1313 |  | 3.562421 | 2.333024 | 0.163747 | 6.470983 | 0.212729 | 0.163747 | 0.491241 | 0.301599 | 0.723534 | 1.0 | 4.234737 | 2.595349 | 4.462121 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 1572 | 1572 | 1572 |  | 4.93841 | 2.736937 | 0.192748 | 5.734352 | 0.188018 | 0.192748 | 0.485369 | 0.307888 | 0.71056 | 1.178753 | 3.84333 | 2.401048 | 3.946281 |  |
