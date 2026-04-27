# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT
- timeframes: 5m, 15m, 30m, 1h
- models: model3
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
- generated_at: 2026-04-27T19:04:14.908983+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 3
- warnings: 0
- skipped_outcome_events: 0

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | long | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 1h | 1 | 1 | 0 | 0 | 1 | 0 | 3.12895 | 3.12895 | 14.929402 | 14.929402 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 1h |
| Entry Model 3 | 30m | 2 | 2 | 0 | 0 | 2 | 0 | 4.221315 | 4.221315 | 7.678348 | 7.678348 | 1.0 | 0.5 | 0.5 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | high | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | bullish | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | premium | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | FVG | 2 | 2 | 0 | 0 | 2 | 0 | 4.221315 | 4.221315 | 7.678348 | 7.678348 | 1.0 | 0.5 | 0.5 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |
| Entry Model 3 | PD | 1 | 1 | 0 | 0 | 1 | 0 | 3.12895 | 3.12895 | 14.929402 | 14.929402 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 1h |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | aligned | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | has_displacement | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | filled | 1 | 1 | 0 | 0 | 1 | 0 | 7.619142 | 7.619142 | 12.024654 | 12.024654 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |
| Entry Model 3 | partially_filled | 2 | 2 | 0 | 0 | 2 | 0 | 1.976218 | 1.976218 | 9.130723 | 9.130723 | 1.0 | 0.5 | 0.5 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 1h |

### Risk / stop modes
| model | stop_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | source_zone_extreme | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | invalidation_source | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | source_zone_extreme | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Displacement grade
| model | displacement_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | valid | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### IFVG quality
| model | ifvg_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | none | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### HTF objective and draw
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | aligned | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | objective_unreached | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | True | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | draw_direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | up | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Score components
| model | objective_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | high | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | poi_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | medium | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | risk_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | high | 2 | 2 | 0 | 0 | 2 | 0 | 5.374046 | 5.374046 | 13.477028 | 13.477028 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |
| Entry Model 3 | low | 1 | 1 | 0 | 0 | 1 | 0 | 0.823487 | 0.823487 | 3.332043 | 3.332043 | 1.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Swing / liquidity quality
| model | sweep_swing_significance | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | unknown | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

| model | objective_is_equal_high_low | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | True | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 3 | 50 | 3 | 3 | 0 | 0 | 3 | 0 | 3.857193 | 3.12895 | 10.095366 | 12.024654 | 1.0 | 0.666667 | 0.666667 | 1.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 30m |

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
