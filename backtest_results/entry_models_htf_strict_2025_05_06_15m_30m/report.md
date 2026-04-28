# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m, 30m
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
- generated_at: 2026-04-24T15:00:06.534014+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 2051
- warnings: 2
- skipped_outcome_events: 269

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 646 | 567 | 79 | 355 | 291 | 6.20602 | 1.261726 | 3.386303 | 1.341718 | 0.763668 | 0.560847 | 0.342152 | 0.636223 | 0.458554 | 0.252205 | 4.73065 | BTCUSDT | 30m |
| Entry Model 2 | 1225 | 1036 | 189 | 651 | 574 | 3.161238 | 1.553699 | 3.574733 | 1.84486 | 0.783784 | 0.617761 | 0.416023 | 0.71102 | 0.467181 | 0.290541 | 4.822041 | BTCUSDT | 15m |
| Entry Model 3 | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 355 | 312 | 43 | 355 | 0 | 7.725044 | 1.1588 | 3.968971 | 1.295299 | 0.759615 | 0.557692 | 0.326923 | 0.630986 | 0.458333 | 0.233974 | 4.740845 | BTCUSDT | 30m |
| Entry Model 1 | short | 291 | 255 | 36 | 0 | 291 | 4.34745 | 1.436515 | 2.673391 | 1.4 | 0.768627 | 0.564706 | 0.360784 | 0.642612 | 0.458824 | 0.27451 | 4.718213 | ETHUSDT | 15m |
| Entry Model 2 | long | 651 | 543 | 108 | 651 | 0 | 3.23521 | 1.485578 | 3.450346 | 1.840122 | 0.786372 | 0.620626 | 0.410681 | 0.708141 | 0.464088 | 0.281768 | 4.850998 | ETHUSDT | 30m |
| Entry Model 2 | short | 574 | 493 | 81 | 0 | 574 | 3.079765 | 1.598231 | 3.711735 | 1.863607 | 0.780933 | 0.614604 | 0.421907 | 0.714286 | 0.470588 | 0.300203 | 4.789199 | BTCUSDT | 15m |
| Entry Model 3 | long | 95 | 94 | 1 | 95 | 0 | 7.128856 | 3.814786 | 7.759348 | 4.603134 | 0.893617 | 0.829787 | 0.734043 | 0.947368 | 0.553191 | 0.382979 | 4.968421 | ETHUSDT | 30m |
| Entry Model 3 | short | 85 | 85 | 0 | 0 | 85 | 6.70401 | 3.2 | 7.57645 | 5.68973 | 0.835294 | 0.788235 | 0.682353 | 0.894118 | 0.494118 | 0.376471 | 4.988235 | ETHUSDT | 30m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 426 | 365 | 61 | 227 | 199 | 3.952405 | 1.224017 | 2.493673 | 1.346672 | 0.769863 | 0.550685 | 0.339726 | 0.647887 | 0.449315 | 0.252055 | 4.715962 | ETHUSDT | 15m |
| Entry Model 1 | 30m | 220 | 202 | 18 | 128 | 92 | 10.278145 | 1.297194 | 4.999223 | 1.314797 | 0.752475 | 0.579208 | 0.346535 | 0.613636 | 0.475248 | 0.252475 | 4.759091 | BTCUSDT | 30m |
| Entry Model 2 | 15m | 800 | 674 | 126 | 426 | 374 | 3.171085 | 1.510748 | 3.64406 | 1.863607 | 0.775964 | 0.620178 | 0.416914 | 0.70875 | 0.458457 | 0.28635 | 4.80875 | BTCUSDT | 15m |
| Entry Model 2 | 30m | 425 | 362 | 63 | 225 | 200 | 3.142904 | 1.620879 | 3.445653 | 1.840122 | 0.798343 | 0.61326 | 0.414365 | 0.715294 | 0.483425 | 0.298343 | 4.847059 | ETHUSDT | 30m |
| Entry Model 3 | 30m | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 631 | 552 | 79 | 344 | 287 | 5.351613 | 1.222917 | 3.450518 | 1.391028 | 0.757246 | 0.552536 | 0.333333 | 0.641838 | 0.451087 | 0.244565 | 4.77496 | BTCUSDT | 30m |
| Entry Model 1 | low | 2 | 2 | 0 | 2 | 0 | 3.745665 | 3.745665 | 1.556262 | 1.556262 | 1.0 | 1.0 | 1.0 | 0.5 | 0.5 | 0.5 | 2.0 | ETHUSDT | 15m |
| Entry Model 1 | medium | 13 | 13 | 0 | 9 | 4 | 42.863964 | 3.240429 | 0.941191 | 0.6351 | 1.0 | 0.846154 | 0.615385 | 0.384615 | 0.769231 | 0.538462 | 3.0 | ETHUSDT | 15m |
| Entry Model 2 | high | 1220 | 1032 | 188 | 646 | 574 | 3.138785 | 1.539255 | 3.579665 | 1.84486 | 0.782946 | 0.616279 | 0.41376 | 0.711475 | 0.466085 | 0.289729 | 4.829508 | BTCUSDT | 15m |
| Entry Model 2 | medium | 5 | 4 | 1 | 5 | 0 | 8.95425 | 7.205931 | 2.302097 | 2.204855 | 1.0 | 1.0 | 1.0 | 0.6 | 0.75 | 0.5 | 3.0 | ETHUSDT | 30m |
| Entry Model 3 | high | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 203 | 181 | 22 | 0 | 203 | 2.551918 | 1.547981 | 2.719551 | 1.285106 | 0.779006 | 0.59116 | 0.392265 | 0.605911 | 0.491713 | 0.303867 | 4.926108 | BTCUSDT | 15m |
| Entry Model 1 | bullish | 259 | 227 | 32 | 259 | 0 | 2.587904 | 0.992706 | 2.828789 | 1.448911 | 0.687225 | 0.488987 | 0.281938 | 0.671815 | 0.405286 | 0.202643 | 4.930502 | BTCUSDT | 30m |
| Entry Model 1 | neutral | 184 | 159 | 25 | 96 | 88 | 15.531207 | 1.405448 | 4.941257 | 1.2042 | 0.855346 | 0.628931 | 0.371069 | 0.619565 | 0.496855 | 0.264151 | 4.233696 | BTCUSDT | 30m |
| Entry Model 2 | bearish | 384 | 336 | 48 | 0 | 384 | 3.227472 | 1.645731 | 4.110506 | 1.863607 | 0.77381 | 0.616071 | 0.422619 | 0.700521 | 0.473214 | 0.303571 | 4.984375 | BTCUSDT | 15m |
| Entry Model 2 | bullish | 475 | 402 | 73 | 475 | 0 | 3.054123 | 1.372306 | 3.611968 | 1.921902 | 0.761194 | 0.589552 | 0.39801 | 0.736842 | 0.430348 | 0.268657 | 4.953684 | BTCUSDT | 15m |
| Entry Model 2 | neutral | 366 | 298 | 68 | 176 | 190 | 3.231056 | 1.618026 | 2.920409 | 1.794217 | 0.825503 | 0.657718 | 0.432886 | 0.688525 | 0.510067 | 0.305369 | 4.480874 | ETHUSDT | 30m |
| Entry Model 3 | bearish | 85 | 85 | 0 | 0 | 85 | 6.70401 | 3.2 | 7.57645 | 5.68973 | 0.835294 | 0.788235 | 0.682353 | 0.894118 | 0.494118 | 0.376471 | 4.988235 | ETHUSDT | 30m |
| Entry Model 3 | bullish | 95 | 94 | 1 | 95 | 0 | 7.128856 | 3.814786 | 7.759348 | 4.603134 | 0.893617 | 0.829787 | 0.734043 | 0.947368 | 0.553191 | 0.382979 | 4.968421 | ETHUSDT | 30m |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 288 | 241 | 47 | 204 | 84 | 9.291486 | 1.503837 | 4.619121 | 1.346672 | 0.788382 | 0.589212 | 0.377593 | 0.663194 | 0.473029 | 0.278008 | 4.798611 | BTCUSDT | 30m |
| Entry Model 1 | equilibrium | 67 | 64 | 3 | 45 | 22 | 3.058627 | 1.365651 | 2.46034 | 1.483584 | 0.78125 | 0.59375 | 0.28125 | 0.552239 | 0.53125 | 0.234375 | 4.597015 | BTCUSDT | 15m |
| Entry Model 1 | premium | 291 | 262 | 29 | 106 | 185 | 4.136691 | 1.083688 | 2.478488 | 1.305416 | 0.736641 | 0.526718 | 0.324427 | 0.628866 | 0.427481 | 0.232824 | 4.694158 | ETHUSDT | 15m |
| Entry Model 2 | discount | 569 | 468 | 101 | 401 | 168 | 3.020702 | 1.426635 | 3.260509 | 1.796712 | 0.790598 | 0.621795 | 0.401709 | 0.702988 | 0.478632 | 0.297009 | 4.899824 | BTCUSDT | 30m |
| Entry Model 2 | equilibrium | 122 | 110 | 12 | 91 | 31 | 3.880774 | 1.317485 | 4.302525 | 2.203 | 0.745455 | 0.572727 | 0.390909 | 0.762295 | 0.436364 | 0.254545 | 4.745902 | ETHUSDT | 15m |
| Entry Model 2 | premium | 534 | 458 | 76 | 159 | 375 | 3.13203 | 1.63826 | 3.72102 | 1.916146 | 0.786026 | 0.624454 | 0.436681 | 0.707865 | 0.462882 | 0.292576 | 4.756554 | BTCUSDT | 15m |
| Entry Model 3 | discount | 100 | 99 | 1 | 64 | 36 | 6.346194 | 3.802913 | 6.847087 | 4.374022 | 0.828283 | 0.767677 | 0.666667 | 0.92 | 0.545455 | 0.393939 | 4.97 | ETHUSDT | 30m |
| Entry Model 3 | equilibrium | 8 | 8 | 0 | 8 | 0 | 22.396617 | 6.812801 | 7.610622 | 5.202297 | 1.0 | 1.0 | 0.75 | 1.0 | 0.625 | 0.25 | 5.0 | ETHUSDT | 30m |
| Entry Model 3 | premium | 72 | 72 | 0 | 23 | 49 | 6.007043 | 2.990847 | 8.81431 | 6.290208 | 0.902778 | 0.847222 | 0.763889 | 0.916667 | 0.486111 | 0.375 | 4.986111 | ETHUSDT | 30m |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 149 | 129 | 20 | 83 | 66 | 2.515545 | 0.926573 | 2.413429 | 1.18799 | 0.705426 | 0.457364 | 0.294574 | 0.61745 | 0.348837 | 0.20155 | 4.765101 | BTCUSDT | 30m |
| Entry Model 1 | FVG | 53 | 47 | 6 | 34 | 19 | 3.984297 | 1.214898 | 4.250746 | 2.506925 | 0.638298 | 0.531915 | 0.340426 | 0.735849 | 0.404255 | 0.234043 | 4.924528 | BTCUSDT | 15m |
| Entry Model 1 | IFVG | 324 | 280 | 44 | 149 | 175 | 9.826027 | 1.463319 | 4.258141 | 1.331081 | 0.785714 | 0.6 | 0.371429 | 0.648148 | 0.489286 | 0.271429 | 4.62963 | BTCUSDT | 30m |
| Entry Model 1 | Liquidity | 4 | 4 | 0 | 4 | 0 | 2.1267 | 1.914233 | 2.313896 | 2.815747 | 1.0 | 0.75 | 0.5 | 0.75 | 0.25 | 0.25 | 5.0 | ETHUSDT | 15m |
| Entry Model 1 | OB | 9 | 9 | 0 | 1 | 8 | 2.611817 | 1.189883 | 2.712752 | 1.062984 | 0.777778 | 0.555556 | 0.333333 | 0.555556 | 0.555556 | 0.333333 | 4.666667 | ETHUSDT | 15m |
| Entry Model 1 | PD | 107 | 98 | 9 | 84 | 23 | 2.283117 | 1.308788 | 1.867004 | 1.229709 | 0.826531 | 0.591837 | 0.316327 | 0.579439 | 0.540816 | 0.265306 | 4.88785 | BTCUSDT | 15m |
| Entry Model 2 | Breaker | 242 | 200 | 42 | 130 | 112 | 3.174212 | 1.63826 | 3.029491 | 1.881576 | 0.76 | 0.6 | 0.425 | 0.72314 | 0.43 | 0.265 | 4.913223 | BTCUSDT | 30m |
| Entry Model 2 | FVG | 115 | 88 | 27 | 73 | 42 | 3.245325 | 1.340582 | 4.029793 | 2.632679 | 0.727273 | 0.579545 | 0.397727 | 0.8 | 0.409091 | 0.272727 | 4.982609 | BTCUSDT | 15m |
| Entry Model 2 | IFVG | 667 | 563 | 104 | 300 | 367 | 3.244273 | 1.578947 | 3.813353 | 1.832127 | 0.813499 | 0.639432 | 0.419183 | 0.704648 | 0.486679 | 0.294849 | 4.736132 | ETHUSDT | 30m |
| Entry Model 2 | Liquidity | 14 | 13 | 1 | 14 | 0 | 1.942237 | 1.34702 | 2.43732 | 2.419534 | 0.692308 | 0.538462 | 0.307692 | 0.785714 | 0.384615 | 0.076923 | 4.642857 | ETHUSDT | 15m |
| Entry Model 2 | OB | 16 | 15 | 1 | 6 | 10 | 1.228402 | 0.688052 | 3.585563 | 3.213592 | 0.666667 | 0.333333 | 0.266667 | 0.9375 | 0.133333 | 0.066667 | 4.9375 | ETHUSDT | 15m |
| Entry Model 2 | PD | 171 | 157 | 14 | 128 | 43 | 3.085422 | 1.721775 | 3.251697 | 1.347625 | 0.757962 | 0.617834 | 0.426752 | 0.631579 | 0.515924 | 0.356688 | 4.923977 | BTCUSDT | 15m |

_Showing 12 of 18 rows._

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 462 | 408 | 54 | 259 | 203 | 2.57194 | 1.2009 | 2.780328 | 1.397995 | 0.727941 | 0.534314 | 0.330882 | 0.642857 | 0.443627 | 0.247549 | 4.928571 | BTCUSDT | 30m |
| Entry Model 1 | neutral | 184 | 159 | 25 | 96 | 88 | 15.531207 | 1.405448 | 4.941257 | 1.2042 | 0.855346 | 0.628931 | 0.371069 | 0.619565 | 0.496855 | 0.264151 | 4.233696 | BTCUSDT | 30m |
| Entry Model 2 | aligned | 859 | 738 | 121 | 475 | 384 | 3.133046 | 1.495532 | 3.838944 | 1.881576 | 0.766938 | 0.601626 | 0.409214 | 0.720605 | 0.449864 | 0.284553 | 4.967404 | BTCUSDT | 15m |
| Entry Model 2 | neutral | 366 | 298 | 68 | 176 | 190 | 3.231056 | 1.618026 | 2.920409 | 1.794217 | 0.825503 | 0.657718 | 0.432886 | 0.688525 | 0.510067 | 0.305369 | 4.480874 | ETHUSDT | 30m |
| Entry Model 3 | aligned | 180 | 179 | 1 | 95 | 85 | 6.927113 | 3.444268 | 7.672497 | 4.927746 | 0.865922 | 0.810056 | 0.709497 | 0.922222 | 0.52514 | 0.379888 | 4.977778 | ETHUSDT | 30m |

## 7. Warnings / skipped events
- Entry Model 3 BTCUSDT 15m 0: missing optional LTF history 3m; model3 context will be incomplete
- Entry Model 3 ETHUSDT 15m 0: missing optional LTF history 3m; model3 context will be incomplete
- 6b335f79b6288d0f: invalid risk (risk is not positive; R metrics are skipped)
- 39ec6c64328cb702: invalid risk (risk is not positive; R metrics are skipped)
- b5b31447dee270ad: invalid risk (risk is not positive; R metrics are skipped)
- 350c367c97ecf246: invalid risk (risk is not positive; R metrics are skipped)
- 974048e47fcce172: invalid risk (risk is not positive; R metrics are skipped)
- 77dee9d0b6c454ad: invalid risk (risk is not positive; R metrics are skipped)
- a21f0398eb4a6aed: invalid risk (risk is not positive; R metrics are skipped)
- 8198eaaa8b0d931d: invalid risk (risk is not positive; R metrics are skipped)
- 649dd8c55afeeed5: invalid risk (risk is not positive; R metrics are skipped)
- 31529ae14245c654: invalid risk (risk is not positive; R metrics are skipped)
- 9737f5c5d03e376b: invalid risk (risk is not positive; R metrics are skipped)
- 96666ef213bba9dd: invalid risk (risk is not positive; R metrics are skipped)
- d102de61d0103d04: invalid risk (risk is not positive; R metrics are skipped)
- 9d8c4de08d9299ba: invalid risk (risk is not positive; R metrics are skipped)
- 1c070f30d24b2db5: invalid risk (risk is not positive; R metrics are skipped)
- 2d308866e0407e2e: invalid risk (risk is not positive; R metrics are skipped)
- 78a0f5f77f25ff9d: invalid risk (risk is not positive; R metrics are skipped)
- a96af9734cd2df46: invalid risk (risk is not positive; R metrics are skipped)
- 5d944ab067eb3102: invalid risk (risk is not positive; R metrics are skipped)
- 6ec075b908c4b0f0: invalid risk (risk is not positive; R metrics are skipped)
- 8bbf41b07e132e13: invalid risk (risk is not positive; R metrics are skipped)
- 7cc8123a5abf5fe5: invalid risk (risk is not positive; R metrics are skipped)
- b777e33fe271e8a4: invalid risk (risk is not positive; R metrics are skipped)
- c2a173c5f612a599: invalid risk (risk is not positive; R metrics are skipped)
- 1cb7aa6e52794d94: invalid risk (risk is not positive; R metrics are skipped)
- d29561034581b916: invalid risk (risk is not positive; R metrics are skipped)
- 7ad3322636bd3149: invalid risk (risk is not positive; R metrics are skipped)
- 716bd08ffda2d4e6: invalid risk (risk is not positive; R metrics are skipped)
- 8ddf36051ffe2bf2: invalid risk (risk is not positive; R metrics are skipped)
- 4be8c0451374e816: invalid risk (risk is not positive; R metrics are skipped)
- 471c3c5dc9643b1d: invalid risk (risk is not positive; R metrics are skipped)
- 6e1e3e42a4e70c4e: invalid risk (risk is not positive; R metrics are skipped)
- ec2c86cf38b160fb: invalid risk (risk is not positive; R metrics are skipped)
- 9269d465684e368a: invalid risk (risk is not positive; R metrics are skipped)
- c429b543257ee3f8: invalid risk (risk is not positive; R metrics are skipped)
- 32293cfa69fd4c3a: invalid risk (risk is not positive; R metrics are skipped)
- bc22a20ae4a12093: invalid risk (risk is not positive; R metrics are skipped)
- 708cf96f357e6ac4: invalid risk (risk is not positive; R metrics are skipped)
- 263ef87c4109a596: invalid risk (risk is not positive; R metrics are skipped)
- 5fa687d07d173469: invalid risk (risk is not positive; R metrics are skipped)
- dc7209597e693b0a: invalid risk (risk is not positive; R metrics are skipped)
- de1ac18fa2d8e96c: invalid risk (risk is not positive; R metrics are skipped)
- 0cc1af322c12010d: invalid risk (risk is not positive; R metrics are skipped)
- 41cfbb1cc512a1f1: invalid risk (risk is not positive; R metrics are skipped)
- aa1e6d004527ac67: invalid risk (risk is not positive; R metrics are skipped)
- bc0f28f6a1916513: invalid risk (risk is not positive; R metrics are skipped)
- ebc38ea5109e6981: invalid risk (risk is not positive; R metrics are skipped)
- d80c2183f1cb9813: invalid risk (risk is not positive; R metrics are skipped)
- f228d01b1477d714: invalid risk (risk is not positive; R metrics are skipped)
- 6faa9dcc9c7bb9ef: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
