# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- models: ifvg_retest
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 5m, 15m, 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20

## Overall Comparison
| model | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 1384 | 19.485975 | 10.457074 | 0.380058 | 0.618497 |  |

## Entry Mode Analysis
| model | entry_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 1384 | 19.485975 | 10.457074 | 0.380058 | 0.618497 |  |

## Stop Mode Analysis
| model | stop_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 1384 | 19.485975 | 10.457074 | 0.380058 | 0.618497 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 1384 | 19.485975 | 10.457074 | 0.380058 | 0.618497 |  |

## Model Family
| model_family | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ict | 1384 | 19.485975 | 10.457074 | 0.380058 | 0.618497 |  |
