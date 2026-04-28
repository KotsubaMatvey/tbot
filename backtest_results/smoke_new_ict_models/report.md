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

## Overall Comparison
| model | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 249 | 12.677055 | 8.185262 | 0.389558 | 0.606426 |  |
| silver_bullet | 18 | 6.566115 | 1.912519 | 0.333333 | 0.666667 |  |
| turtle_soup | 1904 | 4.268743 | 2.568085 | 0.174895 | 0.727416 |  |

## Entry Mode Analysis
| model | entry_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 249 | 12.677055 | 8.185262 | 0.389558 | 0.606426 |  |
| silver_bullet | edge | 18 | 6.566115 | 1.912519 | 0.333333 | 0.666667 |  |
| turtle_soup | close | 1904 | 4.268743 | 2.568085 | 0.174895 | 0.727416 |  |

## Stop Mode Analysis
| model | stop_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | ce | 249 | 12.677055 | 8.185262 | 0.389558 | 0.606426 |  |
| silver_bullet | swing_or_fvg | 18 | 6.566115 | 1.912519 | 0.333333 | 0.666667 |  |
| turtle_soup | sweep_extreme | 1904 | 4.268743 | 2.568085 | 0.174895 | 0.727416 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 249 | 12.677055 | 8.185262 | 0.389558 | 0.606426 |  |
| silver_bullet | conservative | 18 | 6.566115 | 1.912519 | 0.333333 | 0.666667 |  |
| turtle_soup | conservative | 1904 | 4.268743 | 2.568085 | 0.174895 | 0.727416 |  |

## Model Family
| model_family | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ict | 2171 | 5.252172 | 2.782168 | 0.200829 | 0.713035 |  |
