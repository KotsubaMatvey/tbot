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
- htf_mode: off
- require_displacement: False
- model3_fill_threshold: 0.5
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-24T22:04:50.149134+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 772
- warnings: 0
- skipped_outcome_events: 97

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 223 | 189 | 33 | 223 | 0 | 2.429688 | 1.285221 | 2.06195 | 1.317125 | 0.751323 | 0.566138 | 0.365079 | 0.654709 | 0.455026 | 0.26455 | 3.008969 | BTCUSDT | 1h |
| Entry Model 1 | short | 230 | 207 | 23 | 0 | 230 | 2.117181 | 1.444906 | 2.001101 | 1.2334 | 0.777778 | 0.618357 | 0.342995 | 0.604348 | 0.52657 | 0.280193 | 2.743478 | SOLUSDT | 4h |
| Entry Model 2 | long | 153 | 136 | 16 | 153 | 0 | 2.135055 | 1.024131 | 2.084405 | 1.299545 | 0.720588 | 0.5 | 0.338235 | 0.575163 | 0.419118 | 0.257353 | 3.503268 | SOLUSDT | 1h |
| Entry Model 2 | short | 166 | 141 | 25 | 0 | 166 | 2.098793 | 1.013072 | 1.625127 | 0.942149 | 0.737589 | 0.503546 | 0.297872 | 0.566265 | 0.425532 | 0.241135 | 3.427711 | BTCUSDT | 1h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 1h | 365 | 316 | 49 | 182 | 183 | 2.220418 | 1.45778 | 2.019184 | 1.266667 | 0.765823 | 0.617089 | 0.367089 | 0.643836 | 0.506329 | 0.275316 | 2.926027 | BTCUSDT | 1h |
| Entry Model 1 | 4h | 88 | 80 | 7 | 41 | 47 | 2.447695 | 0.997119 | 2.073429 | 1.269556 | 0.7625 | 0.5 | 0.3 | 0.568182 | 0.4375 | 0.2625 | 2.659091 | SOLUSDT | 4h |
| Entry Model 2 | 1h | 258 | 222 | 36 | 124 | 134 | 2.205778 | 1.019388 | 1.862936 | 0.970469 | 0.734234 | 0.504505 | 0.337838 | 0.562016 | 0.432432 | 0.27027 | 3.531008 | BTCUSDT | 1h |
| Entry Model 2 | 4h | 61 | 55 | 5 | 29 | 32 | 1.756627 | 0.944518 | 1.800914 | 1.629384 | 0.709091 | 0.490909 | 0.236364 | 0.606557 | 0.381818 | 0.163636 | 3.180328 | SOLUSDT | 4h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 52 | 46 | 6 | 35 | 17 | 3.240075 | 1.946753 | 1.67027 | 1.192181 | 0.826087 | 0.717391 | 0.5 | 0.596154 | 0.608696 | 0.456522 | 4.0 | BTCUSDT | 1h |
| Entry Model 1 | low | 102 | 84 | 18 | 33 | 69 | 1.610576 | 1.424618 | 1.708446 | 1.158508 | 0.821429 | 0.642857 | 0.22619 | 0.607843 | 0.535714 | 0.166667 | 1.931373 | BTCUSDT | 4h |
| Entry Model 1 | medium | 299 | 266 | 32 | 155 | 144 | 2.305021 | 1.29275 | 2.193964 | 1.359841 | 0.736842 | 0.556391 | 0.368421 | 0.64214 | 0.458647 | 0.274436 | 3.0 | SOLUSDT | 4h |
| Entry Model 2 | high | 153 | 132 | 21 | 79 | 74 | 2.767164 | 1.261866 | 2.373839 | 1.31506 | 0.734848 | 0.560606 | 0.393939 | 0.614379 | 0.439394 | 0.287879 | 4.0 | SOLUSDT | 4h |
| Entry Model 2 | low | 5 | 4 | 1 | 2 | 3 | 2.883941 | 2.754717 | 0.698514 | 0.003165 | 1.0 | 1.0 | 0.75 | 0.4 | 0.75 | 0.75 | 2.0 | SOLUSDT | 4h |
| Entry Model 2 | medium | 161 | 141 | 19 | 72 | 89 | 1.485785 | 0.854509 | 1.393484 | 0.943297 | 0.716312 | 0.432624 | 0.234043 | 0.534161 | 0.397163 | 0.198582 | 3.0 | ETHUSDT | 1h |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | none | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | unknown | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | unknown | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | None | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | None | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | no_htf | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | no_htf | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | has_displacement | 164 | 153 | 10 | 81 | 83 | 2.411646 | 1.305578 | 1.703883 | 1.266667 | 0.784314 | 0.581699 | 0.339869 | 0.609756 | 0.490196 | 0.281046 | 3.195122 | BTCUSDT | 4h |
| Entry Model 1 | weak_or_none | 289 | 243 | 46 | 142 | 147 | 2.174838 | 1.456623 | 2.235565 | 1.25 | 0.753086 | 0.600823 | 0.36214 | 0.640138 | 0.493827 | 0.26749 | 2.692042 | BTCUSDT | 1h |
| Entry Model 2 | has_displacement | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | filled | 46 | 41 | 5 | 24 | 22 | 2.209785 | 1.458937 | 1.600216 | 1.302571 | 0.731707 | 0.560976 | 0.317073 | 0.630435 | 0.390244 | 0.195122 | 2.73913 | SOLUSDT | 1h |
| Entry Model 1 | open | 346 | 299 | 46 | 179 | 167 | 2.32622 | 1.354344 | 2.209229 | 1.349615 | 0.759197 | 0.598662 | 0.361204 | 0.650289 | 0.498328 | 0.280936 | 2.945087 | BTCUSDT | 4h |
| Entry Model 1 | partially_filled | 61 | 56 | 5 | 20 | 41 | 1.987975 | 1.546 | 1.388718 | 0.826674 | 0.821429 | 0.589286 | 0.339286 | 0.508197 | 0.535714 | 0.285714 | 2.57377 | BTCUSDT | 1h |
| Entry Model 2 | unknown | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 453 | 396 | 56 | 223 | 230 | 2.266332 | 1.411135 | 2.030142 | 1.266667 | 0.765152 | 0.593434 | 0.353535 | 0.629139 | 0.492424 | 0.272727 | 2.874172 | BTCUSDT | 4h |
| Entry Model 2 | none | 319 | 277 | 41 | 153 | 166 | 2.116596 | 1.013072 | 1.850621 | 1.049913 | 0.729242 | 0.501805 | 0.31769 | 0.570533 | 0.422383 | 0.249097 | 3.46395 | BTCUSDT | 1h |

## 7. Warnings / skipped events
- 4865ae4c1bb68176: invalid risk (risk is not positive; R metrics are skipped)
- 7d1a3645dabd6dab: invalid risk (risk is not positive; R metrics are skipped)
- e027b3e64e5d442d: invalid risk (risk is not positive; R metrics are skipped)
- cf238665e4b400de: invalid risk (risk is not positive; R metrics are skipped)
- fac6c274d5c2db09: invalid risk (risk is not positive; R metrics are skipped)
- 9bc3778fb168e022: invalid risk (risk is not positive; R metrics are skipped)
- aa650cfe59360bdb: invalid risk (risk is not positive; R metrics are skipped)
- 4a6ba9eebd9aa33e: invalid risk (risk is not positive; R metrics are skipped)
- 8e061af7606fe7f2: invalid risk (risk is not positive; R metrics are skipped)
- 67184942ebfc6fe6: invalid risk (risk is not positive; R metrics are skipped)
- 1fbb2d3d188916d8: invalid risk (risk is not positive; R metrics are skipped)
- aaa164bb84953040: invalid risk (risk is not positive; R metrics are skipped)
- 389d6ca6fce5ff88: invalid risk (risk is not positive; R metrics are skipped)
- 599d9d8b35572c4f: invalid risk (risk is not positive; R metrics are skipped)
- f8cd180fbb436650: invalid risk (risk is not positive; R metrics are skipped)
- 086d0abd7849704c: invalid risk (risk is not positive; R metrics are skipped)
- fe4dedb87b6709ae: invalid risk (risk is not positive; R metrics are skipped)
- a4f96e990a00f39f: invalid risk (risk is not positive; R metrics are skipped)
- 132f17191fa462fc: invalid risk (risk is not positive; R metrics are skipped)
- cf40ad7357ab9de5: invalid risk (risk is not positive; R metrics are skipped)
- 52a6deb3a8d287a3: invalid risk (risk is not positive; R metrics are skipped)
- 2e117b8cc3c6138c: invalid risk (risk is not positive; R metrics are skipped)
- 8835622c1e7be8af: invalid risk (risk is not positive; R metrics are skipped)
- 3ab213345cb0d5bd: invalid risk (risk is not positive; R metrics are skipped)
- 4a03a2038c52d535: invalid risk (risk is not positive; R metrics are skipped)
- b00bd4062a64ab59: invalid risk (risk is not positive; R metrics are skipped)
- ec75636d5738c6cf: invalid risk (risk is not positive; R metrics are skipped)
- b0a3de23a3df5907: invalid risk (risk is not positive; R metrics are skipped)
- 9cd0b04ad8991b84: invalid risk (risk is not positive; R metrics are skipped)
- 846ba4c326fffb84: invalid risk (risk is not positive; R metrics are skipped)
- aee502aa883145e2: invalid risk (risk is not positive; R metrics are skipped)
- 77bb1868d101bcd5: invalid risk (risk is not positive; R metrics are skipped)
- 24d4d67afc728fb7: invalid risk (risk is not positive; R metrics are skipped)
- 738d410fdcb39c16: invalid risk (risk is not positive; R metrics are skipped)
- 78ca9a9731c86819: invalid risk (risk is not positive; R metrics are skipped)
- dd04814a9ea5b37f: invalid risk (risk is not positive; R metrics are skipped)
- 197d8210b29268a0: invalid risk (risk is not positive; R metrics are skipped)
- 663d790339db9910: invalid risk (risk is not positive; R metrics are skipped)
- df6b22024c5c3dbf: invalid risk (risk is not positive; R metrics are skipped)
- 0d3ba9dbb4bc77e3: invalid risk (risk is not positive; R metrics are skipped)
- dfbfc2a9e66878d2: invalid risk (risk is not positive; R metrics are skipped)
- e3ffff1270a72f5c: invalid risk (risk is not positive; R metrics are skipped)
- e1245f96db198fca: invalid risk (risk is not positive; R metrics are skipped)
- c7e366314c80b032: invalid risk (risk is not positive; R metrics are skipped)
- 7f55a61bf2165789: invalid risk (risk is not positive; R metrics are skipped)
- c2f87d5636f4bac8: invalid risk (risk is not positive; R metrics are skipped)
- 35acda2593463c37: invalid risk (risk is not positive; R metrics are skipped)
- 80b135732b4f70fe: invalid risk (risk is not positive; R metrics are skipped)
- d40c3a63c0e1f304: invalid risk (risk is not positive; R metrics are skipped)
- 015fe92b814d124a: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
