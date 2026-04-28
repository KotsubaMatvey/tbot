# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 1h, 4h
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: 2025-05-01
- end: 2025-06-30
- generated_at: 2026-04-24T11:19:04.165033+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 1134
- warnings: 2
- skipped_outcome_events: 114

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 334 | 301 | 33 | 172 | 162 | 2.164518 | 1.387946 | 2.148816 | 1.349713 | 0.767442 | 0.591362 | 0.362126 | 0.622754 | 0.488372 | 0.282392 | 3.571856 | BTCUSDT | 1h |
| Entry Model 2 | 570 | 499 | 71 | 275 | 295 | 3.396077 | 1.779556 | 2.810444 | 1.648441 | 0.843687 | 0.675351 | 0.468938 | 0.659649 | 0.541082 | 0.344689 | 4.229825 | ETHUSDT | 4h |
| Entry Model 3 | 230 | 220 | 10 | 110 | 120 | 20.663959 | 4.541361 | 7.039785 | 3.252954 | 0.904545 | 0.854545 | 0.759091 | 0.813043 | 0.568182 | 0.431818 | 3.895652 | ETHUSDT | 1h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 172 | 150 | 22 | 172 | 0 | 2.503205 | 1.442212 | 2.139089 | 1.419238 | 0.78 | 0.606667 | 0.393333 | 0.639535 | 0.493333 | 0.28 | 3.662791 | BTCUSDT | 1h |
| Entry Model 1 | short | 162 | 151 | 11 | 0 | 162 | 1.828073 | 1.305578 | 2.158478 | 1.349615 | 0.754967 | 0.576159 | 0.331126 | 0.604938 | 0.483444 | 0.284768 | 3.475309 | BTCUSDT | 1h |
| Entry Model 2 | long | 275 | 246 | 29 | 275 | 0 | 3.820463 | 2.016137 | 2.549809 | 1.463716 | 0.865854 | 0.719512 | 0.504065 | 0.621818 | 0.565041 | 0.361789 | 4.218182 | ETHUSDT | 4h |
| Entry Model 2 | short | 295 | 253 | 42 | 0 | 295 | 2.983433 | 1.687116 | 3.063867 | 1.839591 | 0.822134 | 0.632411 | 0.434783 | 0.694915 | 0.517787 | 0.328063 | 4.240678 | ETHUSDT | 1h |
| Entry Model 3 | long | 110 | 105 | 5 | 110 | 0 | 7.035798 | 4.612777 | 5.085955 | 3.195435 | 0.933333 | 0.885714 | 0.790476 | 0.836364 | 0.619048 | 0.428571 | 3.936364 | ETHUSDT | 1h |
| Entry Model 3 | short | 120 | 115 | 5 | 0 | 120 | 33.107062 | 4.539321 | 8.823717 | 3.314692 | 0.878261 | 0.826087 | 0.730435 | 0.791667 | 0.521739 | 0.434783 | 3.858333 | ETHUSDT | 1h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 1h | 265 | 234 | 31 | 137 | 128 | 2.260306 | 1.452355 | 2.114826 | 1.273523 | 0.760684 | 0.628205 | 0.371795 | 0.607547 | 0.525641 | 0.286325 | 3.69434 | BTCUSDT | 1h |
| Entry Model 1 | 4h | 69 | 67 | 2 | 35 | 34 | 1.829972 | 0.969626 | 2.267528 | 1.559652 | 0.791045 | 0.462687 | 0.328358 | 0.681159 | 0.358209 | 0.268657 | 3.101449 | BTCUSDT | 4h |
| Entry Model 2 | 1h | 455 | 392 | 63 | 219 | 236 | 3.294847 | 1.85275 | 2.664033 | 1.514504 | 0.844388 | 0.665816 | 0.466837 | 0.650549 | 0.545918 | 0.354592 | 4.305495 | ETHUSDT | 1h |
| Entry Model 2 | 4h | 115 | 107 | 8 | 56 | 59 | 3.766939 | 1.527623 | 3.346828 | 1.992618 | 0.841121 | 0.71028 | 0.476636 | 0.695652 | 0.523364 | 0.308411 | 3.930435 | ETHUSDT | 4h |
| Entry Model 3 | 1h | 230 | 220 | 10 | 110 | 120 | 20.663959 | 4.541361 | 7.039785 | 3.252954 | 0.904545 | 0.854545 | 0.759091 | 0.813043 | 0.568182 | 0.431818 | 3.895652 | ETHUSDT | 1h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 203 | 179 | 24 | 119 | 84 | 2.647466 | 1.576676 | 2.349974 | 1.417189 | 0.75419 | 0.653631 | 0.446927 | 0.635468 | 0.541899 | 0.340782 | 4.0 | BTCUSDT | 4h |
| Entry Model 1 | low | 12 | 11 | 1 | 5 | 7 | 0.910194 | 0.607508 | 1.791895 | 1.80602 | 0.727273 | 0.181818 | 0.090909 | 0.75 | 0.181818 | 0.090909 | 2.0 | BTCUSDT | 4h |
| Entry Model 1 | medium | 119 | 111 | 8 | 48 | 71 | 1.510011 | 1.231811 | 1.859796 | 1.226214 | 0.792793 | 0.531532 | 0.252252 | 0.588235 | 0.432432 | 0.207207 | 3.0 | BTCUSDT | 1h |
| Entry Model 2 | high | 547 | 480 | 67 | 259 | 288 | 3.345517 | 1.70242 | 2.834595 | 1.673647 | 0.839583 | 0.666667 | 0.458333 | 0.667276 | 0.53125 | 0.333333 | 4.281536 | ETHUSDT | 4h |
| Entry Model 2 | medium | 23 | 19 | 4 | 16 | 7 | 4.673392 | 3.166784 | 2.20031 | 0.881181 | 0.947368 | 0.894737 | 0.736842 | 0.478261 | 0.789474 | 0.631579 | 3.0 | ETHUSDT | 4h |
| Entry Model 3 | high | 208 | 198 | 10 | 103 | 105 | 22.528831 | 5.052832 | 7.459636 | 3.275233 | 0.914141 | 0.873737 | 0.782828 | 0.822115 | 0.570707 | 0.434343 | 4.0 | ETHUSDT | 1h |
| Entry Model 3 | low | 2 | 2 | 0 | 0 | 2 | 1.642299 | 1.642299 | 3.900986 | 3.900986 | 1.0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 2.0 | ETHUSDT | 1h |
| Entry Model 3 | medium | 20 | 20 | 0 | 7 | 13 | 4.103893 | 2.170525 | 3.197144 | 1.680038 | 0.8 | 0.7 | 0.55 | 0.75 | 0.55 | 0.4 | 3.0 | ETHUSDT | 1h |

## 6. Warnings / skipped events
- Entry Model 3 BTCUSDT 4h 0: missing optional HTF history 1d; model3 context will be incomplete
- Entry Model 3 ETHUSDT 4h 0: missing optional HTF history 1d; model3 context will be incomplete
- 3a85d1410945d4ed: invalid risk (risk is not positive; R metrics are skipped)
- 4865ae4c1bb68176: invalid risk (risk is not positive; R metrics are skipped)
- 632ab60f34dffa9c: invalid risk (risk is not positive; R metrics are skipped)
- 7d1a3645dabd6dab: invalid risk (risk is not positive; R metrics are skipped)
- fab27e8203631fa0: invalid risk (risk is not positive; R metrics are skipped)
- cf238665e4b400de: invalid risk (risk is not positive; R metrics are skipped)
- 3b2b52773bcd7d55: invalid risk (risk is not positive; R metrics are skipped)
- 9bc3778fb168e022: invalid risk (risk is not positive; R metrics are skipped)
- 00c8b5dc41c1b8a1: invalid risk (risk is not positive; R metrics are skipped)
- aa650cfe59360bdb: invalid risk (risk is not positive; R metrics are skipped)
- 264555a24a2f33f5: invalid risk (risk is not positive; R metrics are skipped)
- 4a6ba9eebd9aa33e: invalid risk (risk is not positive; R metrics are skipped)
- 8e061af7606fe7f2: invalid risk (risk is not positive; R metrics are skipped)
- 67184942ebfc6fe6: invalid risk (risk is not positive; R metrics are skipped)
- 9e9ebfa3d68081bf: invalid risk (risk is not positive; R metrics are skipped)
- 55aec2ad371855e0: invalid risk (risk is not positive; R metrics are skipped)
- 1fbb2d3d188916d8: invalid risk (risk is not positive; R metrics are skipped)
- aaa164bb84953040: invalid risk (risk is not positive; R metrics are skipped)
- c8ac20592feb189b: invalid risk (risk is not positive; R metrics are skipped)
- 389d6ca6fce5ff88: invalid risk (risk is not positive; R metrics are skipped)
- 599d9d8b35572c4f: invalid risk (risk is not positive; R metrics are skipped)
- a29307a225f53e2c: invalid risk (risk is not positive; R metrics are skipped)
- 67061f7f2fde02e5: invalid risk (risk is not positive; R metrics are skipped)
- a56e12305314f6c5: invalid risk (risk is not positive; R metrics are skipped)
- 086d0abd7849704c: invalid risk (risk is not positive; R metrics are skipped)
- da15537c3430ab42: invalid risk (risk is not positive; R metrics are skipped)
- e4d21ee3e8c82b5d: invalid risk (risk is not positive; R metrics are skipped)
- fe4dedb87b6709ae: invalid risk (risk is not positive; R metrics are skipped)
- 7ebf3e3ca31fa6e3: invalid risk (risk is not positive; R metrics are skipped)
- 51e8369fddf7ac5e: invalid risk (risk is not positive; R metrics are skipped)
- 41b097ccffbc0cc8: invalid risk (risk is not positive; R metrics are skipped)
- a4f96e990a00f39f: invalid risk (risk is not positive; R metrics are skipped)
- b476207ae8bd5bd6: invalid risk (risk is not positive; R metrics are skipped)
- be4d2465bfd83702: invalid risk (risk is not positive; R metrics are skipped)
- 4ba64e2782526ed1: invalid risk (risk is not positive; R metrics are skipped)
- 18a9acb6c8fe1144: invalid risk (risk is not positive; R metrics are skipped)
- 7adb676b43bc0417: invalid risk (risk is not positive; R metrics are skipped)
- 2e117b8cc3c6138c: invalid risk (risk is not positive; R metrics are skipped)
- 8835622c1e7be8af: invalid risk (risk is not positive; R metrics are skipped)
- 42c467f693e28805: invalid risk (risk is not positive; R metrics are skipped)
- 3ab213345cb0d5bd: invalid risk (risk is not positive; R metrics are skipped)
- 4a03a2038c52d535: invalid risk (risk is not positive; R metrics are skipped)
- b00bd4062a64ab59: invalid risk (risk is not positive; R metrics are skipped)
- ec75636d5738c6cf: invalid risk (risk is not positive; R metrics are skipped)
- b84709d943ed2453: invalid risk (risk is not positive; R metrics are skipped)
- b7f3553b70ab354d: invalid risk (risk is not positive; R metrics are skipped)
- 9cd0b04ad8991b84: invalid risk (risk is not positive; R metrics are skipped)
- 846ba4c326fffb84: invalid risk (risk is not positive; R metrics are skipped)
- d37fc8c20a5f8f00: invalid risk (risk is not positive; R metrics are skipped)
- 77bb1868d101bcd5: invalid risk (risk is not positive; R metrics are skipped)

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
