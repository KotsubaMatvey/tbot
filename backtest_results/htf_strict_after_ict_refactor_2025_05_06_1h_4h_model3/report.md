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
- htf_mode: strict
- require_displacement: True
- model3_fill_threshold: 0.5
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-24T22:10:08.341243+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 12
- warnings: 0
- skipped_outcome_events: 1

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 12 | 11 | 1 | 8 | 4 | 18.429536 | 13.214292 | 17.471406 | 10.753644 | 0.909091 | 0.909091 | 0.909091 | 0.833333 | 0.454545 | 0.454545 | 4.25 | ETHUSDT | 1h |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | long | 8 | 7 | 1 | 8 | 0 | 21.796276 | 14.866477 | 17.981347 | 18.650273 | 0.857143 | 0.857143 | 0.857143 | 0.875 | 0.428571 | 0.428571 | 4.25 | ETHUSDT | 1h |
| Entry Model 3 | short | 4 | 4 | 0 | 0 | 4 | 12.537741 | 11.939744 | 16.579009 | 2.067818 | 1.0 | 1.0 | 1.0 | 0.75 | 0.5 | 0.5 | 4.25 | BTCUSDT | 4h |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 1h | 9 | 8 | 1 | 8 | 1 | 19.411663 | 11.043816 | 23.506229 | 19.397686 | 0.875 | 0.875 | 0.875 | 0.888889 | 0.375 | 0.375 | 4.333333 | ETHUSDT | 1h |
| Entry Model 3 | 4h | 3 | 3 | 0 | 0 | 3 | 15.810529 | 13.214292 | 1.378545 | 1.882765 | 1.0 | 1.0 | 1.0 | 0.666667 | 0.666667 | 0.666667 | 4.0 | BTCUSDT | 4h |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | high | 12 | 11 | 1 | 8 | 4 | 18.429536 | 13.214292 | 17.471406 | 10.753644 | 0.909091 | 0.909091 | 0.909091 | 0.833333 | 0.454545 | 0.454545 | 4.25 | ETHUSDT | 1h |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | bearish | 4 | 4 | 0 | 0 | 4 | 12.537741 | 11.939744 | 16.579009 | 2.067818 | 1.0 | 1.0 | 1.0 | 0.75 | 0.5 | 0.5 | 4.25 | BTCUSDT | 4h |
| Entry Model 3 | bullish | 8 | 7 | 1 | 8 | 0 | 21.796276 | 14.866477 | 17.981347 | 18.650273 | 0.857143 | 0.857143 | 0.857143 | 0.875 | 0.428571 | 0.428571 | 4.25 | ETHUSDT | 1h |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | discount | 7 | 6 | 1 | 7 | 0 | 18.812648 | 11.043816 | 17.620722 | 14.701959 | 0.833333 | 0.833333 | 0.833333 | 0.857143 | 0.333333 | 0.333333 | 4.142857 | ETHUSDT | 1h |
| Entry Model 3 | equilibrium | 1 | 1 | 0 | 1 | 0 | 39.698039 | 39.698039 | 20.145098 | 20.145098 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 5.0 | ETHUSDT | 1h |
| Entry Model 3 | premium | 4 | 4 | 0 | 0 | 4 | 12.537741 | 11.939744 | 16.579009 | 2.067818 | 1.0 | 1.0 | 1.0 | 0.75 | 0.5 | 0.5 | 4.25 | BTCUSDT | 4h |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | FVG | 2 | 1 | 1 | 2 | 0 | 4.012358 | 4.012358 | 0.310467 | 0.310467 | 1.0 | 1.0 | 1.0 | 0.5 | 1.0 | 1.0 | 4.0 | BTCUSDT | 1h |
| Entry Model 3 | IFVG | 4 | 4 | 0 | 1 | 3 | 21.782406 | 18.383195 | 6.070183 | 2.067818 | 1.0 | 1.0 | 1.0 | 0.75 | 0.75 | 0.75 | 4.25 | ETHUSDT | 1h |
| Entry Model 3 | PD | 6 | 6 | 0 | 5 | 1 | 18.597151 | 11.043816 | 27.932377 | 21.128908 | 0.833333 | 0.833333 | 0.833333 | 1.0 | 0.166667 | 0.166667 | 4.333333 | ETHUSDT | 1h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | aligned | 12 | 11 | 1 | 8 | 4 | 18.429536 | 13.214292 | 17.471406 | 10.753644 | 0.909091 | 0.909091 | 0.909091 | 0.833333 | 0.454545 | 0.454545 | 4.25 | ETHUSDT | 1h |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | has_displacement | 10 | 9 | 1 | 7 | 3 | 18.256257 | 10.665195 | 16.294594 | 10.753644 | 0.888889 | 0.888889 | 0.888889 | 0.8 | 0.444444 | 0.444444 | 4.3 | ETHUSDT | 1h |
| Entry Model 3 | weak_or_none | 2 | 2 | 0 | 1 | 1 | 19.209288 | 19.209288 | 22.767061 | 22.767061 | 1.0 | 1.0 | 1.0 | 1.0 | 0.5 | 0.5 | 4.0 | BTCUSDT | 4h |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | filled | 8 | 8 | 0 | 4 | 4 | 14.493624 | 11.939744 | 17.396751 | 5.687013 | 1.0 | 1.0 | 1.0 | 0.75 | 0.5 | 0.5 | 4.375 | ETHUSDT | 4h |
| Entry Model 3 | partially_filled | 4 | 3 | 1 | 4 | 0 | 28.9253 | 17.846939 | 17.670486 | 18.650273 | 0.666667 | 0.666667 | 0.666667 | 1.0 | 0.333333 | 0.333333 | 4.0 | ETHUSDT | 1h |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 50 | 12 | 11 | 1 | 8 | 4 | 18.429536 | 13.214292 | 17.471406 | 10.753644 | 0.909091 | 0.909091 | 0.909091 | 0.833333 | 0.454545 | 0.454545 | 4.25 | ETHUSDT | 1h |

## 7. Warnings / skipped events
- 66624bcef1ac6cb5: invalid risk (risk is not positive; R metrics are skipped)

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
