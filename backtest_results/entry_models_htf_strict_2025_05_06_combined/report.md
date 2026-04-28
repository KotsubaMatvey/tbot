# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 5m, 15m, 30m, 1h, 4h
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
- generated_at: 2026-04-24T15:34:55.055119+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 6340
- warnings: 8
- skipped_outcome_events: 933

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 2224 | 1912 | 312 | 1247 | 977 | 4.053414 | 1.405759 | 3.947092 | 1.343111 | 0.781381 | 0.608787 | 0.370816 | 0.651529 | 0.493201 | 0.273536 | 4.813849 | BTCUSDT | 30m |
| Entry Model 2 | 3936 | 3316 | 620 | 2190 | 1746 | 3.438013 | 1.622133 | 3.569051 | 1.834632 | 0.785283 | 0.636007 | 0.433957 | 0.723577 | 0.466526 | 0.293426 | 4.86128 | ETHUSDT | 5m |
| Entry Model 3 | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 1247 | 1068 | 179 | 1247 | 0 | 4.829478 | 1.416052 | 4.790391 | 1.306204 | 0.797753 | 0.627341 | 0.375468 | 0.643945 | 0.5103 | 0.276217 | 4.858059 | BTCUSDT | 30m |
| Entry Model 1 | short | 977 | 844 | 133 | 0 | 977 | 3.07138 | 1.385206 | 2.879981 | 1.401311 | 0.760664 | 0.585308 | 0.364929 | 0.661208 | 0.471564 | 0.270142 | 4.757421 | ETHUSDT | 15m |
| Entry Model 2 | long | 2190 | 1843 | 347 | 2190 | 0 | 3.259324 | 1.62201 | 3.336403 | 1.76891 | 0.793814 | 0.648942 | 0.43299 | 0.705936 | 0.478568 | 0.296799 | 4.896804 | ETHUSDT | 30m |
| Entry Model 2 | short | 1746 | 1473 | 273 | 0 | 1746 | 3.661588 | 1.622256 | 3.860136 | 1.899459 | 0.77461 | 0.619823 | 0.435166 | 0.745704 | 0.45146 | 0.289206 | 4.816724 | ETHUSDT | 5m |
| Entry Model 3 | long | 95 | 94 | 1 | 95 | 0 | 7.128856 | 3.814786 | 7.759348 | 4.603134 | 0.893617 | 0.829787 | 0.734043 | 0.947368 | 0.553191 | 0.382979 | 4.968421 | ETHUSDT | 30m |
| Entry Model 3 | short | 85 | 85 | 0 | 0 | 85 | 6.70401 | 3.2 | 7.57645 | 5.68973 | 0.835294 | 0.788235 | 0.682353 | 0.894118 | 0.494118 | 0.376471 | 4.988235 | ETHUSDT | 30m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 426 | 365 | 61 | 227 | 199 | 3.952405 | 1.224017 | 2.493673 | 1.346672 | 0.769863 | 0.550685 | 0.339726 | 0.647887 | 0.449315 | 0.252055 | 4.715962 | ETHUSDT | 15m |
| Entry Model 1 | 30m | 220 | 202 | 18 | 128 | 92 | 10.278145 | 1.297194 | 4.999223 | 1.314797 | 0.752475 | 0.579208 | 0.346535 | 0.613636 | 0.475248 | 0.252475 | 4.759091 | BTCUSDT | 30m |
| Entry Model 1 | 5m | 1578 | 1345 | 233 | 892 | 686 | 3.145958 | 1.438951 | 4.1835 | 1.347368 | 0.788848 | 0.628996 | 0.3829 | 0.657795 | 0.507807 | 0.282528 | 4.847909 | ETHUSDT | 5m |
| Entry Model 2 | 15m | 800 | 674 | 126 | 426 | 374 | 3.171085 | 1.510748 | 3.64406 | 1.863607 | 0.775964 | 0.620178 | 0.416914 | 0.70875 | 0.458457 | 0.28635 | 4.80875 | BTCUSDT | 15m |
| Entry Model 2 | 30m | 425 | 362 | 63 | 225 | 200 | 3.142904 | 1.620879 | 3.445653 | 1.840122 | 0.798343 | 0.61326 | 0.414365 | 0.715294 | 0.483425 | 0.298343 | 4.847059 | ETHUSDT | 30m |
| Entry Model 2 | 5m | 2711 | 2280 | 431 | 1539 | 1172 | 3.563776 | 1.649455 | 3.566469 | 1.818868 | 0.785965 | 0.644298 | 0.442105 | 0.729251 | 0.466228 | 0.294737 | 4.879011 | ETHUSDT | 5m |
| Entry Model 3 | 30m | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 2198 | 1889 | 309 | 1235 | 963 | 3.796594 | 1.388818 | 3.982337 | 1.356204 | 0.780307 | 0.60667 | 0.368978 | 0.653776 | 0.490736 | 0.271572 | 4.836215 | BTCUSDT | 30m |
| Entry Model 1 | low | 2 | 2 | 0 | 2 | 0 | 3.745665 | 3.745665 | 1.556262 | 1.556262 | 1.0 | 1.0 | 1.0 | 0.5 | 0.5 | 0.5 | 2.0 | ETHUSDT | 15m |
| Entry Model 1 | medium | 24 | 21 | 3 | 10 | 14 | 27.1843 | 1.959414 | 1.004493 | 0.524486 | 0.857143 | 0.761905 | 0.47619 | 0.458333 | 0.714286 | 0.428571 | 3.0 | ETHUSDT | 15m |
| Entry Model 2 | high | 3923 | 3304 | 619 | 2181 | 1742 | 3.432694 | 1.618037 | 3.573377 | 1.834632 | 0.784806 | 0.634988 | 0.432809 | 0.723936 | 0.465799 | 0.292676 | 4.867448 | ETHUSDT | 5m |
| Entry Model 2 | medium | 13 | 12 | 1 | 9 | 4 | 4.902738 | 4.022616 | 2.377981 | 2.204855 | 0.916667 | 0.916667 | 0.75 | 0.615385 | 0.666667 | 0.5 | 3.0 | ETHUSDT | 30m |
| Entry Model 3 | high | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 666 | 590 | 76 | 0 | 666 | 2.601907 | 1.349618 | 2.625191 | 1.294999 | 0.750847 | 0.577966 | 0.367797 | 0.636637 | 0.467797 | 0.269492 | 4.957958 | BTCUSDT | 15m |
| Entry Model 1 | bullish | 960 | 832 | 128 | 960 | 0 | 3.220611 | 1.416868 | 4.69707 | 1.374841 | 0.784856 | 0.617788 | 0.371394 | 0.651042 | 0.503606 | 0.272837 | 4.973958 | ETHUSDT | 5m |
| Entry Model 1 | neutral | 598 | 490 | 108 | 287 | 311 | 7.215211 | 1.413472 | 4.265339 | 1.34322 | 0.812245 | 0.630612 | 0.373469 | 0.668896 | 0.506122 | 0.279592 | 4.396321 | BTCUSDT | 30m |
| Entry Model 2 | bearish | 1139 | 985 | 154 | 0 | 1139 | 3.990832 | 1.588467 | 3.776549 | 1.890396 | 0.764467 | 0.612183 | 0.42132 | 0.741001 | 0.445685 | 0.279188 | 4.983319 | BTCUSDT | 5m |
| Entry Model 2 | bullish | 1644 | 1393 | 251 | 1644 | 0 | 3.322986 | 1.615567 | 3.337942 | 1.750455 | 0.786791 | 0.642498 | 0.433597 | 0.704988 | 0.478823 | 0.301508 | 4.982968 | ETHUSDT | 5m |
| Entry Model 2 | neutral | 1153 | 938 | 215 | 546 | 607 | 3.02832 | 1.668979 | 3.694369 | 1.906886 | 0.804904 | 0.651386 | 0.447761 | 0.732871 | 0.470149 | 0.296375 | 4.567216 | ETHUSDT | 30m |
| Entry Model 3 | bearish | 85 | 85 | 0 | 0 | 85 | 6.70401 | 3.2 | 7.57645 | 5.68973 | 0.835294 | 0.788235 | 0.682353 | 0.894118 | 0.494118 | 0.376471 | 4.988235 | ETHUSDT | 30m |
| Entry Model 3 | bullish | 95 | 94 | 1 | 95 | 0 | 7.128856 | 3.814786 | 7.759348 | 4.603134 | 0.893617 | 0.829787 | 0.734043 | 0.947368 | 0.553191 | 0.382979 | 4.968421 | ETHUSDT | 30m |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 963 | 802 | 161 | 677 | 286 | 4.767273 | 1.459382 | 4.81342 | 1.432831 | 0.78803 | 0.630923 | 0.377805 | 0.671859 | 0.5 | 0.274314 | 4.870197 | BTCUSDT | 30m |
| Entry Model 1 | equilibrium | 272 | 246 | 26 | 174 | 98 | 4.013375 | 1.310359 | 5.683992 | 1.561225 | 0.780488 | 0.585366 | 0.357724 | 0.654412 | 0.495935 | 0.284553 | 4.724265 | ETHUSDT | 5m |
| Entry Model 1 | premium | 989 | 864 | 125 | 396 | 593 | 3.40218 | 1.32698 | 2.648398 | 1.229105 | 0.775463 | 0.594907 | 0.368056 | 0.63094 | 0.486111 | 0.269676 | 4.78362 | ETHUSDT | 15m |
| Entry Model 2 | discount | 1738 | 1453 | 285 | 1324 | 414 | 3.627289 | 1.585231 | 3.536859 | 1.818868 | 0.790778 | 0.639367 | 0.422574 | 0.725547 | 0.47488 | 0.292498 | 4.90794 | ETHUSDT | 5m |
| Entry Model 2 | equilibrium | 491 | 426 | 65 | 311 | 180 | 3.392199 | 1.708214 | 4.394623 | 2.032412 | 0.779343 | 0.638498 | 0.448357 | 0.753564 | 0.469484 | 0.295775 | 4.835031 | ETHUSDT | 15m |
| Entry Model 2 | premium | 1707 | 1437 | 270 | 555 | 1152 | 3.260212 | 1.623389 | 3.356859 | 1.761148 | 0.781489 | 0.631872 | 0.441197 | 0.712947 | 0.457203 | 0.293667 | 4.821324 | BTCUSDT | 5m |
| Entry Model 3 | discount | 100 | 99 | 1 | 64 | 36 | 6.346194 | 3.802913 | 6.847087 | 4.374022 | 0.828283 | 0.767677 | 0.666667 | 0.92 | 0.545455 | 0.393939 | 4.97 | ETHUSDT | 30m |
| Entry Model 3 | equilibrium | 8 | 8 | 0 | 8 | 0 | 22.396617 | 6.812801 | 7.610622 | 5.202297 | 1.0 | 1.0 | 0.75 | 1.0 | 0.625 | 0.25 | 5.0 | ETHUSDT | 30m |
| Entry Model 3 | premium | 72 | 72 | 0 | 23 | 49 | 6.007043 | 2.990847 | 8.81431 | 6.290208 | 0.902778 | 0.847222 | 0.763889 | 0.916667 | 0.486111 | 0.375 | 4.986111 | ETHUSDT | 30m |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 272 | 232 | 40 | 149 | 123 | 3.585507 | 1.122855 | 3.735214 | 1.205194 | 0.737069 | 0.530172 | 0.340517 | 0.625 | 0.422414 | 0.25 | 4.808824 | BTCUSDT | 5m |
| Entry Model 1 | FVG | 251 | 198 | 53 | 169 | 82 | 2.931299 | 1.330231 | 3.247775 | 1.896592 | 0.722222 | 0.606061 | 0.368687 | 0.74502 | 0.459596 | 0.252525 | 4.956175 | BTCUSDT | 15m |
| Entry Model 1 | IFVG | 1375 | 1180 | 195 | 707 | 668 | 4.727163 | 1.468525 | 4.552324 | 1.331165 | 0.791525 | 0.620339 | 0.385593 | 0.657455 | 0.501695 | 0.282203 | 4.757091 | BTCUSDT | 30m |
| Entry Model 1 | Liquidity | 4 | 4 | 0 | 4 | 0 | 2.1267 | 1.914233 | 2.313896 | 2.815747 | 1.0 | 0.75 | 0.5 | 0.75 | 0.25 | 0.25 | 5.0 | ETHUSDT | 15m |
| Entry Model 1 | OB | 40 | 38 | 2 | 25 | 15 | 1.819726 | 1.209976 | 3.018845 | 1.847776 | 0.710526 | 0.552632 | 0.315789 | 0.7 | 0.447368 | 0.184211 | 4.925 | ETHUSDT | 15m |
| Entry Model 1 | PD | 282 | 260 | 22 | 193 | 89 | 2.623782 | 1.402881 | 2.082685 | 1.047286 | 0.826923 | 0.634615 | 0.338462 | 0.556738 | 0.553846 | 0.284615 | 4.950355 | BTCUSDT | 5m |
| Entry Model 2 | Breaker | 431 | 357 | 74 | 224 | 207 | 3.092424 | 1.745793 | 2.932284 | 1.652157 | 0.781513 | 0.633053 | 0.453782 | 0.709977 | 0.453782 | 0.294118 | 4.87703 | BTCUSDT | 30m |
| Entry Model 2 | FVG | 491 | 393 | 98 | 337 | 154 | 3.319936 | 1.514047 | 3.39749 | 2.013004 | 0.763359 | 0.641221 | 0.419847 | 0.749491 | 0.452926 | 0.277354 | 4.989817 | BTCUSDT | 15m |
| Entry Model 2 | IFVG | 2498 | 2097 | 401 | 1268 | 1230 | 3.543639 | 1.605457 | 3.749993 | 1.84743 | 0.790653 | 0.635193 | 0.430615 | 0.731385 | 0.463519 | 0.289461 | 4.814652 | ETHUSDT | 5m |
| Entry Model 2 | Liquidity | 15 | 13 | 2 | 14 | 1 | 1.942237 | 1.34702 | 2.43732 | 2.419534 | 0.692308 | 0.538462 | 0.307692 | 0.8 | 0.384615 | 0.076923 | 4.666667 | ETHUSDT | 15m |
| Entry Model 2 | OB | 69 | 64 | 5 | 45 | 24 | 2.680208 | 1.168028 | 4.021546 | 2.682479 | 0.75 | 0.546875 | 0.40625 | 0.811594 | 0.34375 | 0.21875 | 4.971014 | ETHUSDT | 5m |
| Entry Model 2 | PD | 432 | 392 | 40 | 302 | 130 | 3.479409 | 1.768399 | 3.316671 | 1.567322 | 0.790816 | 0.655612 | 0.456633 | 0.645833 | 0.530612 | 0.34949 | 4.958333 | BTCUSDT | 5m |

_Showing 12 of 18 rows._

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 1626 | 1422 | 204 | 960 | 666 | 2.963905 | 1.392364 | 3.83743 | 1.343111 | 0.770745 | 0.601266 | 0.369902 | 0.645141 | 0.488748 | 0.271449 | 4.967405 | ETHUSDT | 5m |
| Entry Model 1 | neutral | 598 | 490 | 108 | 287 | 311 | 7.215211 | 1.413472 | 4.265339 | 1.34322 | 0.812245 | 0.630612 | 0.373469 | 0.668896 | 0.506122 | 0.279592 | 4.396321 | BTCUSDT | 30m |
| Entry Model 2 | aligned | 2783 | 2378 | 405 | 1644 | 1139 | 3.599617 | 1.607558 | 3.519619 | 1.80513 | 0.777544 | 0.629941 | 0.428511 | 0.719727 | 0.465097 | 0.292262 | 4.983112 | ETHUSDT | 5m |
| Entry Model 2 | neutral | 1153 | 938 | 215 | 546 | 607 | 3.02832 | 1.668979 | 3.694369 | 1.906886 | 0.804904 | 0.651386 | 0.447761 | 0.732871 | 0.470149 | 0.296375 | 4.567216 | ETHUSDT | 30m |
| Entry Model 3 | aligned | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 7. Warnings / skipped events
- Entry Model 3 BTCUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- Entry Model 3 ETHUSDT 5m 0: missing optional LTF history 1m; model3 context will be incomplete
- Entry Model 3 BTCUSDT 15m 0: missing optional LTF history 3m; model3 context will be incomplete
- Entry Model 3 ETHUSDT 15m 0: missing optional LTF history 3m; model3 context will be incomplete
- Entry Models BTCUSDT 1h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models BTCUSDT 4h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models ETHUSDT 1h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models ETHUSDT 4h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
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
