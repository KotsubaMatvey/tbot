# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h, 4h
- models: model1, model2
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: 2025-05-01
- end: 2025-06-30
- htf_mode: strict
- require_displacement: True
- model3_fill_threshold: 0.5
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-24T22:06:21.129315+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 54
- warnings: 0
- skipped_outcome_events: 6

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 21 | 19 | 2 | 18 | 3 | 2.745599 | 1.164921 | 1.588221 | 1.208745 | 0.631579 | 0.578947 | 0.368421 | 0.571429 | 0.473684 | 0.263158 | 3.904762 | BTCUSDT | 1h |
| Entry Model 2 | 33 | 29 | 4 | 31 | 2 | 1.92171 | 0.966903 | 1.8773 | 1.31831 | 0.724138 | 0.448276 | 0.37931 | 0.606061 | 0.344828 | 0.310345 | 3.878788 | ETHUSDT | 1h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 18 | 16 | 2 | 18 | 0 | 1.714348 | 0.869529 | 1.470955 | 1.292062 | 0.5625 | 0.5 | 0.25 | 0.611111 | 0.4375 | 0.1875 | 3.833333 | ETHUSDT | 1h |
| Entry Model 1 | short | 3 | 3 | 0 | 0 | 3 | 8.245601 | 4.785537 | 2.213639 | 0.642231 | 1.0 | 1.0 | 1.0 | 0.333333 | 0.666667 | 0.666667 | 4.333333 | BTCUSDT | 1h |
| Entry Model 2 | long | 31 | 27 | 4 | 31 | 0 | 1.801198 | 0.944518 | 2.002339 | 1.349882 | 0.703704 | 0.407407 | 0.333333 | 0.645161 | 0.296296 | 0.259259 | 3.83871 | ETHUSDT | 1h |
| Entry Model 2 | short | 2 | 2 | 0 | 0 | 2 | 3.548621 | 3.548621 | 0.189279 | 0.189279 | 1.0 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | 4.5 | BTCUSDT | 1h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 1h | 17 | 15 | 2 | 15 | 2 | 3.18585 | 1.266862 | 1.753749 | 1.208745 | 0.666667 | 0.6 | 0.4 | 0.588235 | 0.466667 | 0.266667 | 3.941176 | BTCUSDT | 1h |
| Entry Model 1 | 4h | 4 | 4 | 0 | 3 | 1 | 1.094657 | 0.715871 | 0.967487 | 0.936932 | 0.5 | 0.5 | 0.25 | 0.5 | 0.5 | 0.25 | 3.75 | BTCUSDT | 4h |
| Entry Model 2 | 1h | 26 | 22 | 4 | 25 | 1 | 2.224248 | 1.203435 | 2.082713 | 1.252488 | 0.727273 | 0.5 | 0.454545 | 0.615385 | 0.363636 | 0.363636 | 4.038462 | ETHUSDT | 1h |
| Entry Model 2 | 4h | 7 | 7 | 0 | 6 | 1 | 0.970876 | 0.531484 | 1.231716 | 1.440002 | 0.714286 | 0.285714 | 0.142857 | 0.571429 | 0.285714 | 0.142857 | 3.285714 | BTCUSDT | 4h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 18 | 17 | 1 | 15 | 3 | 2.994699 | 1.266862 | 1.68066 | 1.375378 | 0.647059 | 0.588235 | 0.411765 | 0.555556 | 0.470588 | 0.294118 | 4.055556 | BTCUSDT | 1h |
| Entry Model 1 | medium | 3 | 2 | 1 | 3 | 0 | 0.628251 | 0.628251 | 0.802486 | 0.802486 | 0.5 | 0.5 | 0.0 | 0.666667 | 0.5 | 0.0 | 3.0 | SOLUSDT | 4h |
| Entry Model 2 | high | 26 | 23 | 3 | 24 | 2 | 2.053154 | 0.995602 | 2.037454 | 1.31831 | 0.73913 | 0.478261 | 0.434783 | 0.576923 | 0.347826 | 0.347826 | 4.153846 | ETHUSDT | 1h |
| Entry Model 2 | low | 1 | 0 | 1 | 1 | 0 |  |  |  |  |  |  |  | 1.0 |  |  | 2.0 |  |  |
| Entry Model 2 | medium | 6 | 6 | 0 | 6 | 0 | 1.417844 | 0.738001 | 1.263375 | 1.313334 | 0.666667 | 0.333333 | 0.166667 | 0.666667 | 0.333333 | 0.166667 | 3.0 | SOLUSDT | 1h |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 3 | 3 | 0 | 0 | 3 | 8.245601 | 4.785537 | 2.213639 | 0.642231 | 1.0 | 1.0 | 1.0 | 0.333333 | 0.666667 | 0.666667 | 4.333333 | BTCUSDT | 1h |
| Entry Model 1 | bullish | 15 | 14 | 1 | 15 | 0 | 1.874905 | 0.91048 | 1.554548 | 1.307751 | 0.571429 | 0.5 | 0.285714 | 0.6 | 0.428571 | 0.214286 | 3.933333 | ETHUSDT | 1h |
| Entry Model 1 | neutral | 3 | 2 | 1 | 3 | 0 | 0.59045 | 0.59045 | 0.885802 | 0.885802 | 0.5 | 0.5 | 0.0 | 0.666667 | 0.5 | 0.0 | 3.333333 | SOLUSDT | 4h |
| Entry Model 2 | bearish | 2 | 2 | 0 | 0 | 2 | 3.548621 | 3.548621 | 0.189279 | 0.189279 | 1.0 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | 4.5 | BTCUSDT | 1h |
| Entry Model 2 | bullish | 27 | 24 | 3 | 27 | 0 | 1.736144 | 0.881335 | 2.166822 | 1.513256 | 0.666667 | 0.416667 | 0.333333 | 0.666667 | 0.291667 | 0.25 | 4.0 | ETHUSDT | 1h |
| Entry Model 2 | neutral | 4 | 3 | 1 | 4 | 0 | 2.32163 | 0.944518 | 0.68647 | 0.436372 | 1.0 | 0.333333 | 0.333333 | 0.5 | 0.333333 | 0.333333 | 2.75 | SOLUSDT | 1h |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 12 | 11 | 1 | 12 | 0 | 1.206287 | 0.656039 | 1.132175 | 0.977549 | 0.545455 | 0.454545 | 0.181818 | 0.5 | 0.454545 | 0.181818 | 3.833333 | ETHUSDT | 1h |
| Entry Model 1 | equilibrium | 4 | 4 | 0 | 4 | 0 | 2.419314 | 0.783873 | 1.478449 | 1.671054 | 0.5 | 0.5 | 0.25 | 0.75 | 0.25 | 0.0 | 4.0 | ETHUSDT | 1h |
| Entry Model 1 | premium | 5 | 4 | 1 | 2 | 3 | 7.30499 | 4.634347 | 2.952118 | 2.904892 | 1.0 | 1.0 | 1.0 | 0.6 | 0.75 | 0.75 | 4.0 | BTCUSDT | 1h |
| Entry Model 2 | discount | 20 | 18 | 2 | 20 | 0 | 1.605581 | 0.95571 | 1.187217 | 0.970469 | 0.777778 | 0.388889 | 0.333333 | 0.5 | 0.277778 | 0.277778 | 3.95 | SOLUSDT | 1h |
| Entry Model 2 | equilibrium | 6 | 6 | 0 | 6 | 0 | 2.471582 | 0.411827 | 4.702472 | 2.390904 | 0.333333 | 0.333333 | 0.333333 | 1.0 | 0.166667 | 0.166667 | 3.666667 | ETHUSDT | 1h |
| Entry Model 2 | premium | 7 | 5 | 2 | 5 | 2 | 2.399928 | 3.131116 | 0.97139 | 0.589903 | 1.0 | 0.8 | 0.6 | 0.571429 | 0.8 | 0.6 | 3.857143 | BTCUSDT | 1h |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 1 | 0 | 1 | 1 | 0 |  |  |  |  |  |  |  | 1.0 |  |  | 3.0 |  |  |
| Entry Model 1 | FVG | 7 | 6 | 1 | 7 | 0 | 1.15185 | 0.96145 | 0.889131 | 0.784128 | 0.666667 | 0.5 | 0.166667 | 0.285714 | 0.5 | 0.166667 | 4.0 | SOLUSDT | 1h |
| Entry Model 1 | IFVG | 13 | 13 | 0 | 10 | 3 | 3.481175 | 1.164921 | 1.910877 | 1.406756 | 0.615385 | 0.615385 | 0.461538 | 0.692308 | 0.461538 | 0.307692 | 3.923077 | BTCUSDT | 1h |
| Entry Model 2 | Breaker | 3 | 2 | 1 | 3 | 0 | 0.226829 | 0.226829 | 10.307317 | 10.307317 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 3.333333 | SOLUSDT | 1h |
| Entry Model 2 | FVG | 10 | 9 | 1 | 10 | 0 | 1.876854 | 1.411268 | 1.22334 | 0.973392 | 0.777778 | 0.555556 | 0.444444 | 0.5 | 0.333333 | 0.333333 | 4.2 | SOLUSDT | 1h |
| Entry Model 2 | IFVG | 17 | 17 | 0 | 15 | 2 | 2.223072 | 0.995602 | 1.300023 | 1.349882 | 0.764706 | 0.470588 | 0.411765 | 0.588235 | 0.411765 | 0.352941 | 3.764706 | ETHUSDT | 1h |
| Entry Model 2 | PD | 3 | 1 | 2 | 3 | 0 | 0.592028 | 0.592028 | 0.716611 | 0.716611 | 1.0 | 0.0 | 0.0 | 0.666667 | 0.0 | 0.0 | 4.0 | ETHUSDT | 1h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 18 | 17 | 1 | 15 | 3 | 2.999146 | 1.266862 | 1.670858 | 1.208745 | 0.647059 | 0.588235 | 0.411765 | 0.555556 | 0.470588 | 0.294118 | 4.0 | BTCUSDT | 1h |
| Entry Model 1 | neutral | 3 | 2 | 1 | 3 | 0 | 0.59045 | 0.59045 | 0.885802 | 0.885802 | 0.5 | 0.5 | 0.0 | 0.666667 | 0.5 | 0.0 | 3.333333 | SOLUSDT | 4h |
| Entry Model 2 | aligned | 29 | 26 | 3 | 27 | 2 | 1.875565 | 0.981252 | 2.014703 | 1.394942 | 0.692308 | 0.461538 | 0.384615 | 0.62069 | 0.346154 | 0.307692 | 4.034483 | ETHUSDT | 1h |
| Entry Model 2 | neutral | 4 | 3 | 1 | 4 | 0 | 2.32163 | 0.944518 | 0.68647 | 0.436372 | 1.0 | 0.333333 | 0.333333 | 0.5 | 0.333333 | 0.333333 | 2.75 | SOLUSDT | 1h |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | has_displacement | 19 | 18 | 1 | 16 | 3 | 2.649068 | 1.12397 | 1.389369 | 1.093147 | 0.611111 | 0.555556 | 0.333333 | 0.526316 | 0.444444 | 0.222222 | 3.947368 | BTCUSDT | 1h |
| Entry Model 1 | weak_or_none | 2 | 1 | 1 | 2 | 0 | 4.483156 | 4.483156 | 5.167553 | 5.167553 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 3.5 | BTCUSDT | 1h |
| Entry Model 2 | has_displacement | 33 | 29 | 4 | 31 | 2 | 1.92171 | 0.966903 | 1.8773 | 1.31831 | 0.724138 | 0.448276 | 0.37931 | 0.606061 | 0.344828 | 0.310345 | 3.878788 | ETHUSDT | 1h |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | filled | 1 | 1 | 0 | 1 | 0 | 4.483156 | 4.483156 | 5.167553 | 5.167553 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 4.0 | BTCUSDT | 1h |
| Entry Model 1 | open | 16 | 14 | 2 | 13 | 3 | 3.274579 | 1.519823 | 1.487123 | 0.885478 | 0.714286 | 0.642857 | 0.428571 | 0.5 | 0.5 | 0.285714 | 3.9375 | BTCUSDT | 1h |
| Entry Model 1 | partially_filled | 4 | 4 | 0 | 4 | 0 | 0.459778 | 0.237184 | 1.047229 | 1.292062 | 0.25 | 0.25 | 0.0 | 0.75 | 0.25 | 0.0 | 3.75 | BTCUSDT | 1h |
| Entry Model 2 | unknown | 33 | 29 | 4 | 31 | 2 | 1.92171 | 0.966903 | 1.8773 | 1.31831 | 0.724138 | 0.448276 | 0.37931 | 0.606061 | 0.344828 | 0.310345 | 3.878788 | ETHUSDT | 1h |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 21 | 19 | 2 | 18 | 3 | 2.745599 | 1.164921 | 1.588221 | 1.208745 | 0.631579 | 0.578947 | 0.368421 | 0.571429 | 0.473684 | 0.263158 | 3.904762 | BTCUSDT | 1h |
| Entry Model 2 | none | 33 | 29 | 4 | 31 | 2 | 1.92171 | 0.966903 | 1.8773 | 1.31831 | 0.724138 | 0.448276 | 0.37931 | 0.606061 | 0.344828 | 0.310345 | 3.878788 | ETHUSDT | 1h |

## 7. Warnings / skipped events
- 4a03a2038c52d535: invalid risk (risk is not positive; R metrics are skipped)
- d03115ea72a32259: invalid risk (risk is not positive; R metrics are skipped)
- 8d4996b96804212c: invalid risk (risk is not positive; R metrics are skipped)
- 5c2cb3335699b638: invalid risk (risk is not positive; R metrics are skipped)
- 3be449e2501ab2a3: invalid risk (risk is not positive; R metrics are skipped)
- 3bc08c0707beadce: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
