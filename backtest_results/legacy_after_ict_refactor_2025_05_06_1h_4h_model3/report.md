# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1h, 4h
- models: model3
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
- generated_at: 2026-04-24T22:13:52.340205+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 20
- warnings: 0
- skipped_outcome_events: 1

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 20 | 19 | 1 | 6 | 14 | 9.894489 | 9.884615 | 13.644525 | 5.0 | 0.947368 | 0.947368 | 0.947368 | 0.7 | 0.631579 | 0.631579 | 3.2 | BTCUSDT | 4h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | long | 6 | 6 | 0 | 6 | 0 | 9.712423 | 7.988974 | 6.994601 | 7.463489 | 1.0 | 1.0 | 1.0 | 0.666667 | 0.666667 | 0.666667 | 3.166667 | ETHUSDT | 1h |
| Entry Model 3 | short | 14 | 13 | 1 | 0 | 14 | 9.97852 | 10.340983 | 16.713721 | 5.0 | 0.923077 | 0.923077 | 0.923077 | 0.714286 | 0.615385 | 0.615385 | 3.214286 | BTCUSDT | 4h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 1h | 17 | 16 | 1 | 6 | 11 | 8.785232 | 6.253959 | 15.944396 | 10.508268 | 0.9375 | 0.9375 | 0.9375 | 0.705882 | 0.625 | 0.625 | 3.235294 | BTCUSDT | 1h |
| Entry Model 3 | 4h | 3 | 3 | 0 | 0 | 3 | 15.810529 | 13.214292 | 1.378545 | 1.882765 | 1.0 | 1.0 | 1.0 | 0.666667 | 0.666667 | 0.666667 | 3.0 | BTCUSDT | 4h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | high | 4 | 4 | 0 | 1 | 3 | 4.778513 | 4.559793 | 3.93506 | 2.633452 | 1.0 | 1.0 | 1.0 | 0.5 | 0.5 | 0.5 | 4.0 | SOLUSDT | 1h |
| Entry Model 3 | medium | 16 | 15 | 1 | 5 | 11 | 11.25875 | 10.665195 | 16.233716 | 10.753644 | 0.933333 | 0.933333 | 0.933333 | 0.75 | 0.666667 | 0.666667 | 3.0 | BTCUSDT | 4h |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | bearish | 14 | 13 | 1 | 0 | 14 | 9.97852 | 10.340983 | 16.713721 | 5.0 | 0.923077 | 0.923077 | 0.923077 | 0.714286 | 0.615385 | 0.615385 | 3.214286 | BTCUSDT | 4h |
| Entry Model 3 | bullish | 6 | 6 | 0 | 6 | 0 | 9.712423 | 7.988974 | 6.994601 | 7.463489 | 1.0 | 1.0 | 1.0 | 0.666667 | 0.666667 | 0.666667 | 3.166667 | ETHUSDT | 1h |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | discount | 11 | 11 | 0 | 5 | 6 | 10.272608 | 9.884615 | 13.037328 | 4.173333 | 1.0 | 1.0 | 1.0 | 0.545455 | 0.818182 | 0.818182 | 3.181818 | ETHUSDT | 1h |
| Entry Model 3 | equilibrium | 2 | 2 | 0 | 1 | 1 | 9.319082 | 9.319082 | 9.712397 | 9.712397 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 3.5 | ETHUSDT | 1h |
| Entry Model 3 | premium | 7 | 6 | 1 | 0 | 7 | 9.393073 | 7.78526 | 16.068428 | 6.257881 | 0.833333 | 0.833333 | 0.833333 | 0.857143 | 0.5 | 0.5 | 3.142857 | BTCUSDT | 4h |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | Breaker | 1 | 1 | 0 | 0 | 1 | 0.0 | 0.0 | 22.538462 | 22.538462 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 3.0 | SOLUSDT | 1h |
| Entry Model 3 | FVG | 9 | 9 | 0 | 4 | 5 | 9.089877 | 6.414585 | 9.104742 | 0.310467 | 1.0 | 1.0 | 1.0 | 0.444444 | 0.777778 | 0.777778 | 3.222222 | ETHUSDT | 1h |
| Entry Model 3 | IFVG | 4 | 4 | 0 | 0 | 4 | 15.193611 | 13.278575 | 13.71248 | 2.067818 | 1.0 | 1.0 | 1.0 | 0.75 | 0.75 | 0.75 | 3.0 | BTCUSDT | 4h |
| Entry Model 3 | PD | 6 | 5 | 1 | 2 | 4 | 9.082391 | 4.905325 | 19.982982 | 10.753644 | 1.0 | 1.0 | 1.0 | 1.0 | 0.4 | 0.4 | 3.333333 | BTCUSDT | 1h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | aligned | 20 | 19 | 1 | 6 | 14 | 9.894489 | 9.884615 | 13.644525 | 5.0 | 0.947368 | 0.947368 | 0.947368 | 0.7 | 0.631579 | 0.631579 | 3.2 | BTCUSDT | 4h |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | has_displacement | 4 | 4 | 0 | 1 | 3 | 4.778513 | 4.559793 | 3.93506 | 2.633452 | 1.0 | 1.0 | 1.0 | 0.5 | 0.5 | 0.5 | 4.0 | SOLUSDT | 1h |
| Entry Model 3 | weak_or_none | 16 | 15 | 1 | 5 | 11 | 11.25875 | 10.665195 | 16.233716 | 10.753644 | 0.933333 | 0.933333 | 0.933333 | 0.75 | 0.666667 | 0.666667 | 3.0 | BTCUSDT | 4h |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | filled | 17 | 16 | 1 | 4 | 13 | 8.956986 | 6.253959 | 13.879486 | 3.213102 | 0.9375 | 0.9375 | 0.9375 | 0.647059 | 0.625 | 0.625 | 3.235294 | BTCUSDT | 4h |
| Entry Model 3 | partially_filled | 3 | 3 | 0 | 2 | 1 | 14.894506 | 16.951965 | 12.391401 | 12.038462 | 1.0 | 1.0 | 1.0 | 1.0 | 0.666667 | 0.666667 | 3.0 | BTCUSDT | 1h |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 50 | 20 | 19 | 1 | 6 | 14 | 9.894489 | 9.884615 | 13.644525 | 5.0 | 0.947368 | 0.947368 | 0.947368 | 0.7 | 0.631579 | 0.631579 | 3.2 | BTCUSDT | 4h |

## 7. Warnings / skipped events
- 321fbfab5ecdcb64: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
