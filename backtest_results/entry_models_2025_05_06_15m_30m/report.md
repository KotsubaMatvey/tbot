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
- generated_at: 2026-04-24T11:36:19.301423+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 5564
- warnings: 0
- skipped_outcome_events: 622

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 1607 | 1419 | 188 | 837 | 770 | 4.21383 | 1.514857 | 2.552064 | 1.118662 | 0.816068 | 0.635659 | 0.400987 | 0.578718 | 0.536293 | 0.306554 | 3.878034 | BTCUSDT | 30m |
| Entry Model 2 | 2827 | 2441 | 386 | 1392 | 1435 | 3.446172 | 1.795042 | 3.009393 | 1.526642 | 0.820565 | 0.681278 | 0.459648 | 0.655819 | 0.535027 | 0.332241 | 4.510081 | BTCUSDT | 15m |
| Entry Model 3 | 1130 | 1082 | 48 | 530 | 600 | 22.17468 | 2.631548 | 11.321556 | 2.716962 | 0.880776 | 0.786506 | 0.597043 | 0.752212 | 0.544362 | 0.360444 | 3.937168 | BTCUSDT | 30m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 837 | 746 | 91 | 837 | 0 | 4.679019 | 1.459802 | 2.827803 | 1.143326 | 0.80563 | 0.623324 | 0.382038 | 0.585424 | 0.534853 | 0.297587 | 3.893668 | BTCUSDT | 30m |
| Entry Model 1 | short | 770 | 673 | 97 | 0 | 770 | 3.698182 | 1.616938 | 2.246417 | 1.062705 | 0.827637 | 0.649331 | 0.421991 | 0.571429 | 0.53789 | 0.316493 | 3.861039 | ETHUSDT | 15m |
| Entry Model 2 | long | 1392 | 1192 | 200 | 1392 | 0 | 3.491 | 1.815202 | 2.926237 | 1.459958 | 0.836409 | 0.697987 | 0.463926 | 0.650862 | 0.547819 | 0.338087 | 4.551724 | ETHUSDT | 15m |
| Entry Model 2 | short | 1435 | 1249 | 186 | 0 | 1435 | 3.40339 | 1.783934 | 3.088753 | 1.547634 | 0.805444 | 0.665332 | 0.455564 | 0.660627 | 0.522818 | 0.326661 | 4.469686 | BTCUSDT | 15m |
| Entry Model 3 | long | 530 | 512 | 18 | 530 | 0 | 41.563137 | 2.650882 | 17.48919 | 2.694926 | 0.888672 | 0.814453 | 0.609375 | 0.732075 | 0.572266 | 0.357422 | 3.941509 | BTCUSDT | 30m |
| Entry Model 3 | short | 600 | 570 | 30 | 0 | 600 | 4.759085 | 2.590189 | 5.781505 | 2.728319 | 0.873684 | 0.761404 | 0.585965 | 0.77 | 0.519298 | 0.363158 | 3.933333 | ETHUSDT | 15m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 1105 | 960 | 145 | 560 | 545 | 3.317382 | 1.506626 | 2.180298 | 1.141473 | 0.816667 | 0.635417 | 0.40625 | 0.59095 | 0.526042 | 0.303125 | 3.898643 | ETHUSDT | 15m |
| Entry Model 1 | 30m | 502 | 459 | 43 | 277 | 225 | 6.088753 | 1.517471 | 3.329616 | 1.067037 | 0.814815 | 0.636166 | 0.389978 | 0.551793 | 0.557734 | 0.313725 | 3.832669 | BTCUSDT | 30m |
| Entry Model 2 | 15m | 1906 | 1636 | 270 | 948 | 958 | 3.583532 | 1.820969 | 3.138921 | 1.562804 | 0.82335 | 0.687042 | 0.466381 | 0.667891 | 0.529951 | 0.328851 | 4.540399 | BTCUSDT | 15m |
| Entry Model 2 | 30m | 921 | 805 | 116 | 444 | 477 | 3.167016 | 1.75087 | 2.746154 | 1.438042 | 0.814907 | 0.669565 | 0.445963 | 0.630836 | 0.545342 | 0.33913 | 4.44734 | ETHUSDT | 30m |
| Entry Model 3 | 15m | 829 | 803 | 26 | 387 | 442 | 5.425133 | 2.751787 | 6.300096 | 2.751773 | 0.879203 | 0.794521 | 0.612702 | 0.755127 | 0.545455 | 0.371108 | 3.960193 | ETHUSDT | 15m |
| Entry Model 3 | 30m | 301 | 279 | 22 | 143 | 158 | 70.382158 | 2.20966 | 25.774 | 2.380888 | 0.885305 | 0.763441 | 0.551971 | 0.744186 | 0.541219 | 0.329749 | 3.873754 | BTCUSDT | 30m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 1413 | 1241 | 172 | 750 | 663 | 4.065982 | 1.548731 | 2.743159 | 1.192135 | 0.818695 | 0.638195 | 0.406124 | 0.601557 | 0.532635 | 0.305399 | 4.0 | BTCUSDT | 30m |
| Entry Model 1 | low | 2 | 2 | 0 | 2 | 0 | 3.18668 | 3.18668 | 3.112525 | 3.112525 | 1.0 | 1.0 | 0.5 | 1.0 | 0.0 | 0.0 | 2.0 | ETHUSDT | 15m |
| Entry Model 1 | medium | 192 | 176 | 16 | 85 | 107 | 5.267995 | 1.430659 | 1.198262 | 0.672156 | 0.795455 | 0.613636 | 0.363636 | 0.40625 | 0.568182 | 0.318182 | 3.0 | ETHUSDT | 15m |
| Entry Model 2 | high | 2825 | 2440 | 385 | 1390 | 1435 | 3.432966 | 1.795042 | 2.987329 | 1.524715 | 0.820492 | 0.681148 | 0.459426 | 0.655575 | 0.534836 | 0.331967 | 4.51115 | BTCUSDT | 15m |
| Entry Model 2 | medium | 2 | 1 | 1 | 2 | 0 | 35.670659 | 35.670659 | 56.844311 | 56.844311 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 3.0 | ETHUSDT | 30m |
| Entry Model 3 | high | 1061 | 1020 | 41 | 499 | 562 | 23.3245 | 2.685008 | 11.781559 | 2.752437 | 0.884314 | 0.792157 | 0.604902 | 0.763431 | 0.536275 | 0.356863 | 4.0 | BTCUSDT | 30m |
| Entry Model 3 | low | 2 | 2 | 0 | 0 | 2 | 1.482259 | 1.482259 | 2.27721 | 2.27721 | 1.0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | ETHUSDT | 30m |
| Entry Model 3 | medium | 67 | 60 | 7 | 31 | 36 | 3.317496 | 1.813047 | 3.802983 | 1.484083 | 0.816667 | 0.7 | 0.466667 | 0.58209 | 0.683333 | 0.416667 | 3.0 | BTCUSDT | 15m |

## 6. Warnings / skipped events
- 91d03d39edc18dca: invalid risk (risk is not positive; R metrics are skipped)
- 3af4eb798c2ad9c8: invalid risk (risk is not positive; R metrics are skipped)
- 67f62e89991facab: invalid risk (risk is not positive; R metrics are skipped)
- bf11a3ece18ebe36: invalid risk (risk is not positive; R metrics are skipped)
- 02a88b422e8b3239: invalid risk (risk is not positive; R metrics are skipped)
- 7cc679372c4fba78: invalid risk (risk is not positive; R metrics are skipped)
- b753e8ae91c169ed: invalid risk (risk is not positive; R metrics are skipped)
- e0d8c2a1ec1b148b: invalid risk (risk is not positive; R metrics are skipped)
- 6b335f79b6288d0f: invalid risk (risk is not positive; R metrics are skipped)
- 25bdfda8c4fd6a26: invalid risk (risk is not positive; R metrics are skipped)
- aeff8be46284fc7c: invalid risk (risk is not positive; R metrics are skipped)
- 78e8459cd4680d7e: invalid risk (risk is not positive; R metrics are skipped)
- b24c16c8d7919314: invalid risk (risk is not positive; R metrics are skipped)
- 4c6e548c07196122: invalid risk (risk is not positive; R metrics are skipped)
- 6a5b989584de60e3: invalid risk (risk is not positive; R metrics are skipped)
- 8a1c3c17afafec95: invalid risk (risk is not positive; R metrics are skipped)
- 7fa52ce2ec4253dc: invalid risk (risk is not positive; R metrics are skipped)
- 7df73d5dc8a2d2c6: invalid risk (risk is not positive; R metrics are skipped)
- 93087c40107f02c4: invalid risk (risk is not positive; R metrics are skipped)
- 39ec6c64328cb702: invalid risk (risk is not positive; R metrics are skipped)
- 36353507935ed307: invalid risk (risk is not positive; R metrics are skipped)
- b3aa88ec24635254: invalid risk (risk is not positive; R metrics are skipped)
- 9368c4098eadfe51: invalid risk (risk is not positive; R metrics are skipped)
- 2d280e43ed807488: invalid risk (risk is not positive; R metrics are skipped)
- a624e478783d275d: invalid risk (risk is not positive; R metrics are skipped)
- d9996e633aee981b: invalid risk (risk is not positive; R metrics are skipped)
- 92b0e8a9565f285f: invalid risk (risk is not positive; R metrics are skipped)
- 8f74862c6c78d7a0: invalid risk (risk is not positive; R metrics are skipped)
- 2f555d81c90213e6: invalid risk (risk is not positive; R metrics are skipped)
- 8ea208e36d8f672b: invalid risk (risk is not positive; R metrics are skipped)
- 21090e26f4870a0a: invalid risk (risk is not positive; R metrics are skipped)
- 552c843692ef7d6a: invalid risk (risk is not positive; R metrics are skipped)
- cd827592c09600fc: invalid risk (risk is not positive; R metrics are skipped)
- e6b9df4542708626: invalid risk (risk is not positive; R metrics are skipped)
- 7d23db753500fc97: invalid risk (risk is not positive; R metrics are skipped)
- d9aa10626d4936df: invalid risk (risk is not positive; R metrics are skipped)
- c574f7658090872c: invalid risk (risk is not positive; R metrics are skipped)
- c37e6958088e02de: invalid risk (risk is not positive; R metrics are skipped)
- f514b5845fc1b82b: invalid risk (risk is not positive; R metrics are skipped)
- ebf41f382c6207ef: invalid risk (risk is not positive; R metrics are skipped)
- 8a5b1831c02b933d: invalid risk (risk is not positive; R metrics are skipped)
- dc2ed55d28701672: invalid risk (risk is not positive; R metrics are skipped)
- 6c0e7ecc418a9e7b: invalid risk (risk is not positive; R metrics are skipped)
- 419debfa5bf9f447: invalid risk (risk is not positive; R metrics are skipped)
- d3d69fa15a6fd0db: invalid risk (risk is not positive; R metrics are skipped)
- 49eb17460248fcd6: invalid risk (risk is not positive; R metrics are skipped)
- b5b31447dee270ad: invalid risk (risk is not positive; R metrics are skipped)
- 2ff48b6f4d32102b: invalid risk (risk is not positive; R metrics are skipped)
- bb3801f9f449d825: invalid risk (risk is not positive; R metrics are skipped)
- 1d8b1a70c5d6625b: invalid risk (risk is not positive; R metrics are skipped)

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
