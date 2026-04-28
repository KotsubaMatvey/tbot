# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- models: silver_bullet
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1m, 5m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | 60 | 60 | 60 |  | 0.948922 | 0.68244 | 0.1 | 2.0 | 0.024999 | 0.1 | 0.233333 | 0.1 | 0.483333 | 1.166667 | 6.482759 | 7.785714 | 11.666667 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | edge | 60 | 60 | 60 |  | 0.948922 | 0.68244 | 0.1 | 2.0 | 0.024999 | 0.1 | 0.233333 | 0.1 | 0.483333 | 1.166667 | 6.482759 | 7.785714 | 11.666667 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | swing_or_fvg | 60 | 60 | 60 |  | 0.948922 | 0.68244 | 0.1 | 2.0 | 0.024999 | 0.1 | 0.233333 | 0.1 | 0.483333 | 1.166667 | 6.482759 | 7.785714 | 11.666667 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | conservative | 60 | 60 | 60 |  | 0.948922 | 0.68244 | 0.1 | 2.0 | 0.024999 | 0.1 | 0.233333 | 0.1 | 0.483333 | 1.166667 | 6.482759 | 7.785714 | 11.666667 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 60 | 60 | 60 |  | 0.948922 | 0.68244 | 0.1 | 2.0 | 0.024999 | 0.1 | 0.233333 | 0.1 | 0.483333 | 1.166667 | 6.482759 | 7.785714 | 11.666667 |  |
