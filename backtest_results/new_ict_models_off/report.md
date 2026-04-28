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
- context_mode: off
- forward_bars: 20

## Overall Comparison
| model | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 4032 | 10.050475 | 5.17576 | 0.444444 | 0.553075 |  |
| ifvg_retest | 2172 | 18.086109 | 7.125984 | 0.358195 | 0.63582 |  |
| reclaimed_ob | 234 | 11.090451 | 4.750961 | 0.636752 | 0.363248 |  |
| silver_bullet | 167 | 3.095311 | 1.060029 | 0.239521 | 0.520958 |  |
| turtle_soup | 15874 | 5.116203 | 2.85671 | 0.160136 | 0.722502 |  |

## Entry Mode Analysis
| model | entry_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 4032 | 10.050475 | 5.17576 | 0.444444 | 0.553075 |  |
| ifvg_retest | edge | 2172 | 18.086109 | 7.125984 | 0.358195 | 0.63582 |  |
| reclaimed_ob | body_edge | 234 | 11.090451 | 4.750961 | 0.636752 | 0.363248 |  |
| silver_bullet | edge | 167 | 3.095311 | 1.060029 | 0.239521 | 0.520958 |  |
| turtle_soup | close | 15874 | 5.116203 | 2.85671 | 0.160136 | 0.722502 |  |

## Stop Mode Analysis
| model | stop_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 4032 | 10.050475 | 5.17576 | 0.444444 | 0.553075 |  |
| ifvg_retest | ce | 2172 | 18.086109 | 7.125984 | 0.358195 | 0.63582 |  |
| reclaimed_ob | mean_threshold | 234 | 11.090451 | 4.750961 | 0.636752 | 0.363248 |  |
| silver_bullet | swing_or_fvg | 167 | 3.095311 | 1.060029 | 0.239521 | 0.520958 |  |
| turtle_soup | sweep_extreme | 15874 | 5.116203 | 2.85671 | 0.160136 | 0.722502 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 4032 | 10.050475 | 5.17576 | 0.444444 | 0.553075 |  |
| ifvg_retest | conservative | 2172 | 18.086109 | 7.125984 | 0.358195 | 0.63582 |  |
| reclaimed_ob | conservative | 234 | 11.090451 | 4.750961 | 0.636752 | 0.363248 |  |
| silver_bullet | conservative | 167 | 3.095311 | 1.060029 | 0.239521 | 0.520958 |  |
| turtle_soup | conservative | 15874 | 5.116203 | 2.85671 | 0.160136 | 0.722502 |  |

## Model Family
| model_family | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ict | 22479 | 7.301625 | 3.395515 | 0.23582 | 0.6785 |  |
