# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 5m
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: 2025-05-01
- end: 2025-06-30
- htf_mode: strict
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-24T15:33:40.113284+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 4289
- warnings: 2
- skipped_outcome_events: 664

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 1578 | 1345 | 233 | 892 | 686 | 3.145958 | 1.438951 | 4.1835 | 1.347368 | 0.788848 | 0.628996 | 0.3829 | 0.657795 | 0.507807 | 0.282528 | 4.847909 | ETHUSDT | 5m |
| Entry Model 2 | 2711 | 2280 | 431 | 1539 | 1172 | 3.563776 | 1.649455 | 3.566469 | 1.818868 | 0.785965 | 0.644298 | 0.442105 | 0.729251 | 0.466228 | 0.294737 | 4.879011 | ETHUSDT | 5m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 892 | 756 | 136 | 892 | 0 | 3.634482 | 1.502817 | 5.129389 | 1.310304 | 0.813492 | 0.656085 | 0.395503 | 0.649103 | 0.531746 | 0.293651 | 4.904709 | BTCUSDT | 5m |
| Entry Model 1 | short | 686 | 589 | 97 | 0 | 686 | 2.518922 | 1.379839 | 2.969421 | 1.402622 | 0.757216 | 0.594228 | 0.366723 | 0.669096 | 0.47708 | 0.268251 | 4.774052 | ETHUSDT | 5m |
| Entry Model 2 | long | 1539 | 1300 | 239 | 1539 | 0 | 3.269396 | 1.655387 | 3.288811 | 1.725968 | 0.796923 | 0.660769 | 0.442308 | 0.705003 | 0.484615 | 0.303077 | 4.916179 | ETHUSDT | 5m |
| Entry Model 2 | short | 1172 | 980 | 192 | 0 | 1172 | 3.95428 | 1.626429 | 3.934791 | 1.919921 | 0.771429 | 0.622449 | 0.441837 | 0.761092 | 0.441837 | 0.283673 | 4.830205 | ETHUSDT | 5m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 5m | 1578 | 1345 | 233 | 892 | 686 | 3.145958 | 1.438951 | 4.1835 | 1.347368 | 0.788848 | 0.628996 | 0.3829 | 0.657795 | 0.507807 | 0.282528 | 4.847909 | ETHUSDT | 5m |
| Entry Model 2 | 5m | 2711 | 2280 | 431 | 1539 | 1172 | 3.563776 | 1.649455 | 3.566469 | 1.818868 | 0.785965 | 0.644298 | 0.442105 | 0.729251 | 0.466228 | 0.294737 | 4.879011 | ETHUSDT | 5m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 1567 | 1337 | 230 | 891 | 676 | 3.154581 | 1.438951 | 4.201906 | 1.350834 | 0.789828 | 0.62902 | 0.383695 | 0.658583 | 0.507105 | 0.282723 | 4.860881 | ETHUSDT | 5m |
| Entry Model 1 | medium | 11 | 8 | 3 | 1 | 10 | 1.704846 | 1.571125 | 1.107358 | 0.521176 | 0.625 | 0.625 | 0.25 | 0.545455 | 0.625 | 0.25 | 3.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 2703 | 2272 | 431 | 1535 | 1168 | 3.566194 | 1.647486 | 3.57052 | 1.818868 | 0.785651 | 0.643486 | 0.441461 | 0.72956 | 0.465669 | 0.294014 | 4.884573 | ETHUSDT | 5m |
| Entry Model 2 | medium | 8 | 8 | 0 | 4 | 4 | 2.876983 | 2.910537 | 2.415922 | 2.370526 | 0.875 | 0.875 | 0.625 | 0.625 | 0.625 | 0.5 | 3.0 | BTCUSDT | 5m |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 463 | 409 | 54 | 0 | 463 | 2.624029 | 1.26358 | 2.583433 | 1.313505 | 0.738386 | 0.572127 | 0.356968 | 0.650108 | 0.457213 | 0.254279 | 4.971922 | ETHUSDT | 5m |
| Entry Model 1 | bullish | 701 | 605 | 96 | 701 | 0 | 3.458007 | 1.571764 | 5.398061 | 1.30459 | 0.821488 | 0.666116 | 0.404959 | 0.643367 | 0.540496 | 0.299174 | 4.990014 | ETHUSDT | 5m |
| Entry Model 1 | neutral | 414 | 331 | 83 | 191 | 223 | 3.220519 | 1.419018 | 3.940653 | 1.405333 | 0.791541 | 0.63142 | 0.374622 | 0.690821 | 0.510574 | 0.287009 | 4.468599 | BTCUSDT | 5m |
| Entry Model 2 | bearish | 755 | 649 | 106 | 0 | 755 | 4.386038 | 1.526071 | 3.603652 | 1.918979 | 0.75963 | 0.610169 | 0.420647 | 0.761589 | 0.431433 | 0.266564 | 4.982781 | ETHUSDT | 5m |
| Entry Model 2 | bullish | 1169 | 991 | 178 | 1169 | 0 | 3.43205 | 1.674452 | 3.226784 | 1.649038 | 0.797175 | 0.663976 | 0.448032 | 0.692044 | 0.498486 | 0.314834 | 4.994867 | ETHUSDT | 5m |
| Entry Model 2 | neutral | 787 | 640 | 147 | 370 | 417 | 2.933921 | 1.683967 | 4.054744 | 1.941645 | 0.795312 | 0.648438 | 0.454688 | 0.753494 | 0.451562 | 0.292187 | 4.60737 | ETHUSDT | 5m |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 675 | 561 | 114 | 473 | 202 | 2.823717 | 1.419169 | 4.896889 | 1.478534 | 0.787879 | 0.648841 | 0.377897 | 0.675556 | 0.511586 | 0.272727 | 4.900741 | BTCUSDT | 5m |
| Entry Model 1 | equilibrium | 205 | 182 | 23 | 129 | 76 | 4.34911 | 1.284519 | 6.817583 | 1.612456 | 0.78022 | 0.582418 | 0.384615 | 0.687805 | 0.483516 | 0.302198 | 4.765854 | ETHUSDT | 5m |
| Entry Model 1 | premium | 698 | 602 | 96 | 290 | 408 | 3.082509 | 1.496525 | 2.722345 | 1.220475 | 0.792359 | 0.624585 | 0.387043 | 0.631805 | 0.511628 | 0.285714 | 4.820917 | BTCUSDT | 5m |
| Entry Model 2 | discount | 1169 | 985 | 184 | 923 | 246 | 3.915496 | 1.625082 | 3.66816 | 1.823762 | 0.790863 | 0.647716 | 0.432487 | 0.736527 | 0.473096 | 0.290355 | 4.911891 | ETHUSDT | 5m |
| Entry Model 2 | equilibrium | 369 | 316 | 53 | 220 | 149 | 3.222126 | 1.825157 | 4.426682 | 2.00625 | 0.791139 | 0.661392 | 0.468354 | 0.750678 | 0.481013 | 0.310127 | 4.864499 | ETHUSDT | 5m |
| Entry Model 2 | premium | 1173 | 979 | 194 | 396 | 777 | 3.320178 | 1.615296 | 3.186496 | 1.678375 | 0.779367 | 0.635342 | 0.443309 | 0.71526 | 0.454545 | 0.294178 | 4.85081 | BTCUSDT | 5m |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 123 | 103 | 20 | 66 | 57 | 4.925558 | 1.358388 | 5.390655 | 1.253606 | 0.776699 | 0.621359 | 0.398058 | 0.634146 | 0.514563 | 0.31068 | 4.861789 | BTCUSDT | 5m |
| Entry Model 1 | FVG | 198 | 151 | 47 | 135 | 63 | 2.603545 | 1.379839 | 2.935591 | 1.799166 | 0.748344 | 0.629139 | 0.377483 | 0.747475 | 0.476821 | 0.258278 | 4.964646 | ETHUSDT | 5m |
| Entry Model 1 | IFVG | 1051 | 900 | 151 | 558 | 493 | 3.14085 | 1.472669 | 4.643847 | 1.336462 | 0.793333 | 0.626667 | 0.39 | 0.660324 | 0.505556 | 0.285556 | 4.796384 | ETHUSDT | 5m |
| Entry Model 1 | OB | 31 | 29 | 2 | 24 | 7 | 1.573905 | 1.230069 | 3.11384 | 1.906376 | 0.689655 | 0.551724 | 0.310345 | 0.741935 | 0.413793 | 0.137931 | 5.0 | ETHUSDT | 5m |
| Entry Model 1 | PD | 175 | 162 | 13 | 109 | 66 | 2.829863 | 1.459531 | 2.213158 | 1.007092 | 0.82716 | 0.660494 | 0.351852 | 0.542857 | 0.561728 | 0.296296 | 4.988571 | BTCUSDT | 5m |
| Entry Model 2 | Breaker | 189 | 157 | 32 | 94 | 95 | 2.988236 | 1.93746 | 2.808453 | 1.451407 | 0.808917 | 0.675159 | 0.490446 | 0.693122 | 0.484076 | 0.33121 | 4.830688 | ETHUSDT | 5m |
| Entry Model 2 | FVG | 376 | 305 | 71 | 264 | 112 | 3.341462 | 1.633527 | 3.215056 | 1.868318 | 0.77377 | 0.659016 | 0.42623 | 0.734043 | 0.465574 | 0.278689 | 4.992021 | BTCUSDT | 5m |
| Entry Model 2 | IFVG | 1831 | 1534 | 297 | 968 | 863 | 3.653511 | 1.611057 | 3.726738 | 1.85608 | 0.782269 | 0.633638 | 0.434811 | 0.741125 | 0.45502 | 0.287484 | 4.843255 | ETHUSDT | 5m |
| Entry Model 2 | Liquidity | 1 | 0 | 1 | 0 | 1 |  |  |  |  |  |  |  | 1.0 |  |  | 5.0 |  |  |
| Entry Model 2 | OB | 53 | 49 | 4 | 39 | 14 | 3.124638 | 1.424181 | 4.155009 | 2.424571 | 0.77551 | 0.612245 | 0.44898 | 0.773585 | 0.408163 | 0.265306 | 4.981132 | ETHUSDT | 5m |
| Entry Model 2 | PD | 261 | 235 | 26 | 174 | 87 | 3.742626 | 1.906606 | 3.360078 | 1.587361 | 0.812766 | 0.680851 | 0.476596 | 0.655172 | 0.540426 | 0.344681 | 4.980843 | BTCUSDT | 5m |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 1164 | 1014 | 150 | 701 | 463 | 3.121619 | 1.443701 | 4.262772 | 1.306204 | 0.787968 | 0.628205 | 0.385602 | 0.646048 | 0.506903 | 0.281065 | 4.982818 | ETHUSDT | 5m |
| Entry Model 1 | neutral | 414 | 331 | 83 | 191 | 223 | 3.220519 | 1.419018 | 3.940653 | 1.405333 | 0.791541 | 0.63142 | 0.374622 | 0.690821 | 0.510574 | 0.287009 | 4.468599 | BTCUSDT | 5m |
| Entry Model 2 | aligned | 1924 | 1640 | 284 | 1169 | 755 | 3.809573 | 1.630109 | 3.375922 | 1.74811 | 0.782317 | 0.642683 | 0.437195 | 0.719335 | 0.471951 | 0.295732 | 4.990125 | ETHUSDT | 5m |
| Entry Model 2 | neutral | 787 | 640 | 147 | 370 | 417 | 2.933921 | 1.683967 | 4.054744 | 1.941645 | 0.795312 | 0.648438 | 0.454688 | 0.753494 | 0.451562 | 0.292187 | 4.60737 | ETHUSDT | 5m |

## 7. Warnings / skipped events
- Entry Model 3 BTCUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- Entry Model 3 ETHUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- 8c1773cbbae740ca: invalid risk (risk is not positive; R metrics are skipped)
- 6920d4a86b603935: invalid risk (risk is not positive; R metrics are skipped)
- 293d297d4dfe89e1: invalid risk (risk is not positive; R metrics are skipped)
- 0140f0b97f4cc1a1: invalid risk (risk is not positive; R metrics are skipped)
- 8ca3731b6052c380: invalid risk (risk is not positive; R metrics are skipped)
- 6de737e733325756: invalid risk (risk is not positive; R metrics are skipped)
- 7fa27a7260915810: invalid risk (risk is not positive; R metrics are skipped)
- 47e74880dbcdc680: invalid risk (risk is not positive; R metrics are skipped)
- 5dd64cb6f536f135: invalid risk (risk is not positive; R metrics are skipped)
- 1cfbe91cd0e678d0: invalid risk (risk is not positive; R metrics are skipped)
- 81c38ccae508e96f: invalid risk (risk is not positive; R metrics are skipped)
- afa4ce0799399112: invalid risk (risk is not positive; R metrics are skipped)
- 6cb8d26565bcfba1: invalid risk (risk is not positive; R metrics are skipped)
- 7e0c2afc3b3fa7ef: invalid risk (risk is not positive; R metrics are skipped)
- 4a2f79897c1fe1e0: invalid risk (risk is not positive; R metrics are skipped)
- a55f8a9d91bb17be: invalid risk (risk is not positive; R metrics are skipped)
- f067955731e4f888: invalid risk (risk is not positive; R metrics are skipped)
- 77c6a7629a0b960d: invalid risk (risk is not positive; R metrics are skipped)
- fcebf9d4a2581319: invalid risk (risk is not positive; R metrics are skipped)
- 80d3f5ddcfb595f4: invalid risk (risk is not positive; R metrics are skipped)
- b69304189ec34bfa: invalid risk (risk is not positive; R metrics are skipped)
- bb45b0b5afef14c6: invalid risk (risk is not positive; R metrics are skipped)
- 94cf9f43fd698f38: invalid risk (risk is not positive; R metrics are skipped)
- a03bdb4f588016cb: invalid risk (risk is not positive; R metrics are skipped)
- 6f9249c21101fbbe: invalid risk (risk is not positive; R metrics are skipped)
- 2eda7f94f90a1660: invalid risk (risk is not positive; R metrics are skipped)
- 3ca0c90fb38270c5: invalid risk (risk is not positive; R metrics are skipped)
- 15ce0e3cec77f98c: invalid risk (risk is not positive; R metrics are skipped)
- 62048e11c43b9bfd: invalid risk (risk is not positive; R metrics are skipped)
- b550eee07e0d3930: invalid risk (risk is not positive; R metrics are skipped)
- 86a75b5fc0333c08: invalid risk (risk is not positive; R metrics are skipped)
- 7c9e3f78caed674b: invalid risk (risk is not positive; R metrics are skipped)
- b0b4280ad4c0140f: invalid risk (risk is not positive; R metrics are skipped)
- cdd0114d1dd7c5a5: invalid risk (risk is not positive; R metrics are skipped)
- c56b917dd08d0d24: invalid risk (risk is not positive; R metrics are skipped)
- 7ef9522c307c4de9: invalid risk (risk is not positive; R metrics are skipped)
- a55fe5b4f96a1b16: invalid risk (risk is not positive; R metrics are skipped)
- e0fb5314550af2f7: invalid risk (risk is not positive; R metrics are skipped)
- af9a347e9ddefce3: invalid risk (risk is not positive; R metrics are skipped)
- 01ec672827dd75a4: invalid risk (risk is not positive; R metrics are skipped)
- 00a939fe9bdf6993: invalid risk (risk is not positive; R metrics are skipped)
- cda254c4f1f7a11d: invalid risk (risk is not positive; R metrics are skipped)
- 7ed581e4a7a7b614: invalid risk (risk is not positive; R metrics are skipped)
- eb28485376b1e30f: invalid risk (risk is not positive; R metrics are skipped)
- 923a4a9465825ea0: invalid risk (risk is not positive; R metrics are skipped)
- 5e0757fe7f318300: invalid risk (risk is not positive; R metrics are skipped)
- 1e7002a4ef3b3fc6: invalid risk (risk is not positive; R metrics are skipped)
- e5e06ce61c9d2395: invalid risk (risk is not positive; R metrics are skipped)
- e955325d6b2186c5: invalid risk (risk is not positive; R metrics are skipped)
- 23e8c1d05245d41e: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
