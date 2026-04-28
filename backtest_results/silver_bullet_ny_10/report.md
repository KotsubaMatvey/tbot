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

## Overall Comparison
| model | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | 70 | 2.476006 | 0.884531 | 0.2 | 0.471429 |  |

## Entry Mode Analysis
| model | entry_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | edge | 70 | 2.476006 | 0.884531 | 0.2 | 0.471429 |  |

## Stop Mode Analysis
| model | stop_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | swing_or_fvg | 70 | 2.476006 | 0.884531 | 0.2 | 0.471429 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silver_bullet | conservative | 70 | 2.476006 | 0.884531 | 0.2 | 0.471429 |  |

## Model Family
| model_family | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ict | 70 | 2.476006 | 0.884531 | 0.2 | 0.471429 |  |
