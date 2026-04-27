# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 5m, 15m, 30m, 1h, 4h
- models: model1, model2
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: full history
- end: full history
- htf_mode: strict
- require_displacement: True
- model3_fill_threshold: 0.5
- stop_mode: structural
- model3_stop_mode: source_zone_extreme
- stop_buffer_bps: 2.0
- invalidation_confirmation: close
- model3_reaction_bars: 10
- model3_min_rr_to_objective: 1.5
- model3_source_zone: any
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-27T18:48:01.158738+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 264
- warnings: 0
- skipped_outcome_events: 0

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 33 | 33 | 0 | 0 | 33 | 0 | 2.076401 | 1.38184 | 0.940216 | 0.512986 | 0.757576 | 0.636364 | 0.333333 | 0.272727 | 0.545455 | 0.30303 | 4.515152 | ETHUSDT | 5m |
| Entry Model 1 | short | 16 | 16 | 0 | 0 | 0 | 16 | 1.444751 | 1.120831 | 1.164186 | 0.293129 | 0.875 | 0.6875 | 0.3125 | 0.25 | 0.6875 | 0.3125 | 4.75 | ETHUSDT | 4h |
| Entry Model 2 | long | 190 | 190 | 0 | 0 | 190 | 0 | 14.223542 | 7.825001 | 8.972568 | 5.896192 | 0.957895 | 0.931579 | 0.857895 | 0.805263 | 0.721053 | 0.568421 | 4.994737 | SOLUSDT | 1h |
| Entry Model 2 | short | 25 | 25 | 0 | 0 | 0 | 25 | 16.212839 | 5.618679 | 17.84764 | 9.406526 | 0.8 | 0.76 | 0.72 | 0.84 | 0.6 | 0.52 | 4.88 | ETHUSDT | 4h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 4 | 4 | 0 | 0 | 4 | 0 | 2.49592 | 2.546181 | 0.947531 | 0.307473 | 0.75 | 0.5 | 0.5 | 0.25 | 0.5 | 0.5 | 5.0 | SOLUSDT | 15m |
| Entry Model 1 | 1h | 8 | 8 | 0 | 0 | 8 | 0 | 1.089655 | 0.55499 | 1.083342 | 0.75014 | 0.5 | 0.375 | 0.125 | 0.25 | 0.25 | 0.125 | 4.125 | ETHUSDT | 1h |
| Entry Model 1 | 30m | 12 | 12 | 0 | 0 | 12 | 0 | 2.190706 | 1.38184 | 0.945523 | 0.590303 | 0.916667 | 0.833333 | 0.333333 | 0.25 | 0.666667 | 0.25 | 4.666667 | ETHUSDT | 30m |
| Entry Model 1 | 4h | 14 | 14 | 0 | 0 | 6 | 8 | 1.627918 | 1.802953 | 0.430477 | 0.195857 | 0.928571 | 0.857143 | 0.428571 | 0.142857 | 0.857143 | 0.428571 | 4.357143 | BTCUSDT | 4h |
| Entry Model 1 | 5m | 11 | 11 | 0 | 0 | 3 | 8 | 2.168819 | 0.805514 | 1.802207 | 0.896221 | 0.727273 | 0.454545 | 0.272727 | 0.454545 | 0.454545 | 0.272727 | 5.0 | ETHUSDT | 5m |
| Entry Model 2 | 15m | 64 | 64 | 0 | 0 | 64 | 0 | 11.36093 | 5.493009 | 10.279141 | 7.142429 | 0.984375 | 0.9375 | 0.8125 | 0.859375 | 0.734375 | 0.59375 | 5.0 | SOLUSDT | 15m |
| Entry Model 2 | 1h | 29 | 29 | 0 | 0 | 27 | 2 | 22.759264 | 14.59501 | 10.707669 | 7.462818 | 0.965517 | 0.931034 | 0.931034 | 0.896552 | 0.655172 | 0.482759 | 5.0 | SOLUSDT | 1h |
| Entry Model 2 | 30m | 54 | 54 | 0 | 0 | 54 | 0 | 18.335734 | 11.553819 | 8.83434 | 4.643175 | 0.925926 | 0.907407 | 0.888889 | 0.759259 | 0.648148 | 0.555556 | 5.0 | SOLUSDT | 30m |
| Entry Model 2 | 4h | 21 | 21 | 0 | 0 | 3 | 18 | 20.739215 | 11.43998 | 18.688949 | 5.176129 | 0.857143 | 0.857143 | 0.809524 | 0.761905 | 0.714286 | 0.619048 | 4.809524 | ETHUSDT | 4h |
| Entry Model 2 | 5m | 47 | 47 | 0 | 0 | 42 | 5 | 6.277079 | 4.469473 | 6.661045 | 5.675731 | 0.914894 | 0.893617 | 0.787234 | 0.765957 | 0.765957 | 0.553191 | 5.0 | SOLUSDT | 5m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | high | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 16 | 16 | 0 | 0 | 0 | 16 | 1.444751 | 1.120831 | 1.164186 | 0.293129 | 0.875 | 0.6875 | 0.3125 | 0.25 | 0.6875 | 0.3125 | 4.75 | ETHUSDT | 4h |
| Entry Model 1 | bullish | 33 | 33 | 0 | 0 | 33 | 0 | 2.076401 | 1.38184 | 0.940216 | 0.512986 | 0.757576 | 0.636364 | 0.333333 | 0.272727 | 0.545455 | 0.30303 | 4.515152 | ETHUSDT | 5m |
| Entry Model 2 | bearish | 25 | 25 | 0 | 0 | 0 | 25 | 16.212839 | 5.618679 | 17.84764 | 9.406526 | 0.8 | 0.76 | 0.72 | 0.84 | 0.6 | 0.52 | 4.88 | ETHUSDT | 4h |
| Entry Model 2 | bullish | 190 | 190 | 0 | 0 | 190 | 0 | 14.223542 | 7.825001 | 8.972568 | 5.896192 | 0.957895 | 0.931579 | 0.857895 | 0.805263 | 0.721053 | 0.568421 | 4.994737 | SOLUSDT | 1h |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 22 | 22 | 0 | 0 | 10 | 12 | 1.084793 | 1.1204 | 1.389608 | 0.76207 | 0.818182 | 0.545455 | 0.090909 | 0.363636 | 0.545455 | 0.090909 | 4.681818 | ETHUSDT | 1h |
| Entry Model 1 | equilibrium | 4 | 4 | 0 | 0 | 3 | 1 | 2.17189 | 1.898122 | 1.282156 | 0.554388 | 0.75 | 0.75 | 0.5 | 0.25 | 0.5 | 0.5 | 4.75 | ETHUSDT | 15m |
| Entry Model 1 | premium | 23 | 23 | 0 | 0 | 20 | 3 | 2.56888 | 2.060475 | 0.606699 | 0.295912 | 0.782609 | 0.73913 | 0.521739 | 0.173913 | 0.652174 | 0.478261 | 4.478261 | ETHUSDT | 5m |
| Entry Model 2 | discount | 85 | 85 | 0 | 0 | 69 | 16 | 12.687354 | 7.860633 | 9.600325 | 5.921204 | 0.917647 | 0.905882 | 0.835294 | 0.776471 | 0.741176 | 0.588235 | 4.952941 | SOLUSDT | 1h |
| Entry Model 2 | equilibrium | 31 | 31 | 0 | 0 | 30 | 1 | 14.042125 | 6.731275 | 10.332478 | 4.267842 | 0.967742 | 0.935484 | 0.870968 | 0.806452 | 0.612903 | 0.548387 | 5.0 | ETHUSDT | 4h |
| Entry Model 2 | premium | 99 | 99 | 0 | 0 | 91 | 8 | 16.101647 | 7.72194 | 10.248933 | 6.148717 | 0.949495 | 0.909091 | 0.838384 | 0.838384 | 0.707071 | 0.545455 | 5.0 | SOLUSDT | 1h |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 11 | 11 | 0 | 0 | 9 | 2 | 2.49711 | 1.243399 | 1.246158 | 0.694125 | 0.727273 | 0.545455 | 0.363636 | 0.272727 | 0.545455 | 0.363636 | 4.909091 | ETHUSDT | 15m |
| Entry Model 1 | FVG | 15 | 15 | 0 | 0 | 14 | 1 | 2.48668 | 2.060475 | 0.589482 | 0.210383 | 0.933333 | 0.8 | 0.533333 | 0.2 | 0.733333 | 0.466667 | 4.2 | ETHUSDT | 30m |
| Entry Model 1 | IFVG | 5 | 5 | 0 | 0 | 0 | 5 | 1.955963 | 2.137856 | 0.274514 | 0.181332 | 1.0 | 1.0 | 0.6 | 0.0 | 1.0 | 0.6 | 4.4 | BTCUSDT | 4h |
| Entry Model 1 | PD | 18 | 18 | 0 | 0 | 10 | 8 | 0.949391 | 0.962742 | 1.42953 | 0.603555 | 0.666667 | 0.5 | 0.055556 | 0.388889 | 0.388889 | 0.055556 | 4.777778 | SOLUSDT | 30m |
| Entry Model 2 | Breaker | 43 | 43 | 0 | 0 | 41 | 2 | 10.924425 | 7.860633 | 9.861375 | 6.267749 | 0.953488 | 0.953488 | 0.767442 | 0.837209 | 0.697674 | 0.488372 | 5.0 | BTCUSDT | 1h |
| Entry Model 2 | FVG | 75 | 75 | 0 | 0 | 66 | 9 | 15.386573 | 7.72194 | 13.057424 | 8.621489 | 0.906667 | 0.853333 | 0.813333 | 0.866667 | 0.626667 | 0.48 | 4.96 | SOLUSDT | 4h |
| Entry Model 2 | IFVG | 40 | 40 | 0 | 0 | 33 | 7 | 14.573618 | 9.687271 | 8.362735 | 3.724561 | 0.95 | 0.9 | 0.825 | 0.725 | 0.725 | 0.6 | 4.975 | SOLUSDT | 30m |
| Entry Model 2 | Liquidity | 1 | 1 | 0 | 0 | 1 | 0 | 14.288143 | 14.288143 | 11.970905 | 11.970905 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |
| Entry Model 2 | OB | 4 | 4 | 0 | 0 | 2 | 2 | 4.407098 | 4.466298 | 8.108042 | 5.928844 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.5 | 5.0 | ETHUSDT | 15m |
| Entry Model 2 | PD | 52 | 52 | 0 | 0 | 47 | 5 | 16.715182 | 7.655446 | 7.090777 | 3.147938 | 0.961538 | 0.961538 | 0.942308 | 0.75 | 0.807692 | 0.730769 | 5.0 | SOLUSDT | 4h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | aligned | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | has_displacement | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | has_displacement | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | filled | 5 | 5 | 0 | 0 | 4 | 1 | 2.637743 | 2.906005 | 0.380455 | 0.22706 | 1.0 | 1.0 | 0.6 | 0.0 | 1.0 | 0.6 | 4.8 | SOLUSDT | 15m |
| Entry Model 1 | open | 22 | 22 | 0 | 0 | 15 | 7 | 1.831079 | 1.227992 | 1.060102 | 0.63831 | 0.818182 | 0.590909 | 0.318182 | 0.272727 | 0.545455 | 0.318182 | 4.727273 | ETHUSDT | 30m |
| Entry Model 1 | partially_filled | 22 | 22 | 0 | 0 | 14 | 8 | 1.734763 | 1.373053 | 1.110435 | 0.447786 | 0.727273 | 0.636364 | 0.272727 | 0.318182 | 0.545455 | 0.227273 | 4.409091 | ETHUSDT | 5m |
| Entry Model 2 | unknown | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### Risk / stop modes
| model | stop_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | structural | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | structural | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

| model | invalidation_source | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | sweep_extreme | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | ifvg_boundary | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### Displacement grade
| model | displacement_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | strong | 26 | 26 | 0 | 0 | 21 | 5 | 2.111445 | 1.373053 | 1.111102 | 0.578373 | 0.730769 | 0.576923 | 0.307692 | 0.346154 | 0.5 | 0.269231 | 4.615385 | ETHUSDT | 15m |
| Entry Model 1 | valid | 23 | 23 | 0 | 0 | 12 | 11 | 1.597377 | 1.348599 | 0.902845 | 0.293129 | 0.869565 | 0.73913 | 0.347826 | 0.173913 | 0.695652 | 0.347826 | 4.565217 | BTCUSDT | 5m |
| Entry Model 2 | unknown | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### IFVG quality
| model | ifvg_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | strong | 32 | 32 | 0 | 0 | 28 | 4 | 18.140612 | 8.736993 | 8.765323 | 5.300904 | 1.0 | 0.9375 | 0.90625 | 0.8125 | 0.625 | 0.53125 | 5.0 | ETHUSDT | 4h |
| Entry Model 2 | valid | 183 | 183 | 0 | 0 | 162 | 21 | 13.810352 | 7.72194 | 10.221249 | 6.148717 | 0.928962 | 0.907104 | 0.830601 | 0.808743 | 0.721311 | 0.568306 | 4.978142 | SOLUSDT | 1h |

### HTF objective and draw
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 42 | 42 | 0 | 0 | 29 | 13 | 1.839318 | 1.295999 | 1.107579 | 0.487803 | 0.785714 | 0.642857 | 0.285714 | 0.285714 | 0.571429 | 0.261905 | 4.642857 | ETHUSDT | 15m |
| Entry Model 1 | mixed | 7 | 7 | 0 | 0 | 4 | 3 | 2.055129 | 2.137856 | 0.447969 | 0.131538 | 0.857143 | 0.714286 | 0.571429 | 0.142857 | 0.714286 | 0.571429 | 4.285714 | BTCUSDT | 5m |
| Entry Model 2 | aligned | 192 | 192 | 0 | 0 | 171 | 21 | 14.591287 | 7.755655 | 9.930326 | 5.896192 | 0.947917 | 0.921875 | 0.854167 | 0.8125 | 0.703125 | 0.5625 | 4.979167 | SOLUSDT | 1h |
| Entry Model 2 | mixed | 23 | 23 | 0 | 0 | 19 | 4 | 13.315948 | 6.008295 | 10.624182 | 6.432233 | 0.869565 | 0.826087 | 0.73913 | 0.782609 | 0.73913 | 0.565217 | 5.0 | BTCUSDT | 30m |

| model | objective_unreached | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | True | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | True | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

| model | draw_direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | down | 16 | 16 | 0 | 0 | 0 | 16 | 1.444751 | 1.120831 | 1.164186 | 0.293129 | 0.875 | 0.6875 | 0.3125 | 0.25 | 0.6875 | 0.3125 | 4.75 | ETHUSDT | 4h |
| Entry Model 1 | up | 33 | 33 | 0 | 0 | 33 | 0 | 2.076401 | 1.38184 | 0.940216 | 0.512986 | 0.757576 | 0.636364 | 0.333333 | 0.272727 | 0.545455 | 0.30303 | 4.515152 | ETHUSDT | 5m |
| Entry Model 2 | down | 25 | 25 | 0 | 0 | 0 | 25 | 16.212839 | 5.618679 | 17.84764 | 9.406526 | 0.8 | 0.76 | 0.72 | 0.84 | 0.6 | 0.52 | 4.88 | ETHUSDT | 4h |
| Entry Model 2 | up | 190 | 190 | 0 | 0 | 190 | 0 | 14.223542 | 7.825001 | 8.972568 | 5.896192 | 0.957895 | 0.931579 | 0.857895 | 0.805263 | 0.721053 | 0.568421 | 4.994737 | SOLUSDT | 1h |

### Score components
| model | objective_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | high | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

| model | poi_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 16 | 16 | 0 | 0 | 9 | 7 | 2.328002 | 1.649619 | 0.942519 | 0.495793 | 0.8125 | 0.6875 | 0.4375 | 0.1875 | 0.6875 | 0.4375 | 4.75 | ETHUSDT | 15m |
| Entry Model 1 | medium | 33 | 33 | 0 | 0 | 24 | 9 | 1.648158 | 1.364265 | 1.04769 | 0.462621 | 0.787879 | 0.636364 | 0.272727 | 0.30303 | 0.545455 | 0.242424 | 4.515152 | ETHUSDT | 30m |
| Entry Model 2 | high | 87 | 87 | 0 | 0 | 76 | 11 | 12.302568 | 7.78937 | 9.091732 | 5.883946 | 0.954023 | 0.931034 | 0.804598 | 0.793103 | 0.724138 | 0.54023 | 4.988506 | SOLUSDT | 30m |
| Entry Model 2 | low | 1 | 1 | 0 | 0 | 1 | 0 | 14.288143 | 14.288143 | 11.970905 | 11.970905 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |
| Entry Model 2 | medium | 127 | 127 | 0 | 0 | 113 | 14 | 15.93057 | 7.72194 | 10.614388 | 5.948339 | 0.929134 | 0.897638 | 0.866142 | 0.818898 | 0.700787 | 0.582677 | 4.976378 | SOLUSDT | 4h |

| model | risk_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 3 | 3 | 0 | 0 | 0 | 3 | 0.690604 | 0.793124 | 3.045429 | 2.537223 | 0.666667 | 0.333333 | 0.0 | 0.666667 | 0.333333 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | low | 37 | 37 | 0 | 0 | 29 | 8 | 1.708161 | 1.38184 | 0.79658 | 0.295912 | 0.810811 | 0.702703 | 0.324324 | 0.216216 | 0.621622 | 0.297297 | 4.459459 | ETHUSDT | 30m |
| Entry Model 1 | medium | 9 | 9 | 0 | 0 | 4 | 5 | 2.929276 | 1.364265 | 1.227149 | 0.432951 | 0.777778 | 0.555556 | 0.444444 | 0.333333 | 0.555556 | 0.444444 | 5.0 | ETHUSDT | 15m |
| Entry Model 2 | high | 165 | 165 | 0 | 0 | 154 | 11 | 15.876775 | 8.356486 | 11.296783 | 7.151158 | 0.939394 | 0.90303 | 0.836364 | 0.866667 | 0.684848 | 0.545455 | 5.0 | SOLUSDT | 4h |
| Entry Model 2 | low | 8 | 8 | 0 | 0 | 2 | 6 | 7.775996 | 6.159787 | 4.291174 | 1.207959 | 1.0 | 1.0 | 0.875 | 0.625 | 0.75 | 0.625 | 4.5 | BTCUSDT | 4h |
| Entry Model 2 | medium | 42 | 42 | 0 | 0 | 34 | 8 | 10.140909 | 5.782097 | 6.016196 | 2.181978 | 0.928571 | 0.928571 | 0.857143 | 0.619048 | 0.785714 | 0.619048 | 5.0 | ETHUSDT | 4h |

### Swing / liquidity quality
| model | sweep_swing_significance | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | intermediate | 19 | 19 | 0 | 0 | 13 | 6 | 1.264714 | 0.805514 | 1.121381 | 0.717986 | 0.789474 | 0.473684 | 0.210526 | 0.263158 | 0.473684 | 0.210526 | 4.736842 | SOLUSDT | 4h |
| Entry Model 1 | long | 16 | 16 | 0 | 0 | 15 | 1 | 2.990595 | 1.692287 | 0.622792 | 0.307473 | 0.8125 | 0.75 | 0.4375 | 0.3125 | 0.625 | 0.375 | 4.5 | ETHUSDT | 5m |
| Entry Model 1 | short | 14 | 14 | 0 | 0 | 5 | 9 | 1.411299 | 1.38961 | 1.313084 | 0.293129 | 0.785714 | 0.785714 | 0.357143 | 0.214286 | 0.714286 | 0.357143 | 4.5 | ETHUSDT | 4h |
| Entry Model 2 | intermediate | 62 | 62 | 0 | 0 | 55 | 7 | 13.475185 | 6.824597 | 9.885701 | 5.413409 | 0.903226 | 0.903226 | 0.854839 | 0.758065 | 0.693548 | 0.580645 | 4.983871 | ETHUSDT | 1h |
| Entry Model 2 | long | 97 | 97 | 0 | 0 | 91 | 6 | 17.272908 | 8.949302 | 11.187746 | 5.921204 | 0.958763 | 0.927835 | 0.835052 | 0.804124 | 0.731959 | 0.587629 | 4.989691 | SOLUSDT | 4h |
| Entry Model 2 | short | 56 | 56 | 0 | 0 | 44 | 12 | 10.658222 | 7.212025 | 8.086679 | 6.223562 | 0.946429 | 0.892857 | 0.839286 | 0.875 | 0.678571 | 0.5 | 4.964286 | ETHUSDT | 30m |

| model | objective_is_equal_high_low | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | True | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | True | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 49 | 49 | 0 | 0 | 33 | 16 | 1.870148 | 1.364265 | 1.013349 | 0.462621 | 0.795918 | 0.653061 | 0.326531 | 0.265306 | 0.591837 | 0.306122 | 4.591837 | ETHUSDT | 15m |
| Entry Model 2 | none | 215 | 215 | 0 | 0 | 190 | 25 | 14.454856 | 7.72194 | 10.004553 | 5.921204 | 0.939535 | 0.911628 | 0.84186 | 0.809302 | 0.706977 | 0.562791 | 4.981395 | SOLUSDT | 1h |

## 7. Warnings / skipped events
- none

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
