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

## Overall Comparison
| model | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 379 | 7.009109 | 3.378596 | 0.414248 | 0.583113 |  |
| ict2022_mss_fvg | 72 | 2.220082 | 1.082953 | 0.638889 | 0.236111 |  |
| ifvg_retest | 351 | 14.361654 | 6.655925 | 0.37037 | 0.618234 |  |
| reclaimed_ob | 27 | 4.272258 | 2.399652 | 0.703704 | 0.296296 |  |
| silver_bullet | 50 | 2.861442 | 0.767643 | 0.3 | 0.36 |  |
| turtle_soup | 2200 | 4.749691 | 2.643124 | 0.151364 | 0.742727 |  |

## Entry Mode Analysis
| model | entry_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 379 | 7.009109 | 3.378596 | 0.414248 | 0.583113 |  |
| ict2022_mss_fvg | edge | 72 | 2.220082 | 1.082953 | 0.638889 | 0.236111 |  |
| ifvg_retest | edge | 351 | 14.361654 | 6.655925 | 0.37037 | 0.618234 |  |
| reclaimed_ob | body_edge | 27 | 4.272258 | 2.399652 | 0.703704 | 0.296296 |  |
| silver_bullet | edge | 50 | 2.861442 | 0.767643 | 0.3 | 0.36 |  |
| turtle_soup | close | 2200 | 4.749691 | 2.643124 | 0.151364 | 0.742727 |  |

## Stop Mode Analysis
| model | stop_mode | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 379 | 7.009109 | 3.378596 | 0.414248 | 0.583113 |  |
| ict2022_mss_fvg | sweep_extreme | 72 | 2.220082 | 1.082953 | 0.638889 | 0.236111 |  |
| ifvg_retest | ce | 351 | 14.361654 | 6.655925 | 0.37037 | 0.618234 |  |
| reclaimed_ob | mean_threshold | 27 | 4.272258 | 2.399652 | 0.703704 | 0.296296 |  |
| silver_bullet | swing_or_fvg | 50 | 2.861442 | 0.767643 | 0.3 | 0.36 |  |
| turtle_soup | sweep_extreme | 2200 | 4.749691 | 2.643124 | 0.151364 | 0.742727 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 379 | 7.009109 | 3.378596 | 0.414248 | 0.583113 |  |
| ict2022_mss_fvg | conservative | 72 | 2.220082 | 1.082953 | 0.638889 | 0.236111 |  |
| ifvg_retest | conservative | 351 | 14.361654 | 6.655925 | 0.37037 | 0.618234 |  |
| reclaimed_ob | conservative | 27 | 4.272258 | 2.399652 | 0.703704 | 0.296296 |  |
| silver_bullet | conservative | 50 | 2.861442 | 0.767643 | 0.3 | 0.36 |  |
| turtle_soup | conservative | 2200 | 4.749691 | 2.643124 | 0.151364 | 0.742727 |  |

## Model Family
| model_family | count | avg_mfe_r | median_mfe_r | target_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- |
| ict | 3079 | 6.029549 | 2.800845 | 0.227347 | 0.686911 |  |
