# Entry Models Backtest Report

Config:
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 5m, 15m, 30m, 1h, 4h
- models: model2
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: full history
- end: full history
- htf_mode: strict
- require_displacement: True
- model3_fill_threshold: 0.5
- stop_mode: standard
- model3_stop_mode: source_zone_extreme
- stop_buffer_bps: 2.0
- invalidation_confirmation: close
- model3_reaction_bars: 10
- model3_min_rr_to_objective: 1.5
- model3_source_zone: any
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-27T18:54:17.992567+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 0
- warnings: 0
- skipped_outcome_events: 0

## 2. Summary by model
_No rows._

## 3. Summary by direction
_No rows._

## 4. Summary by timeframe
_No rows._

## 5. Score bucket analysis
_No rows._

## 6. HTF Context Analysis
### Events by HTF bias
_No rows._

### Performance by HTF location
_No rows._

### Performance by HTF zone type
_No rows._

### Performance by HTF alignment
_No rows._

### Performance by displacement
_No rows._

### Performance by FVG status
_No rows._

### Risk / stop modes
_No rows._

_No rows._

### Displacement grade
_No rows._

### IFVG quality
_No rows._

### HTF objective and draw
_No rows._

_No rows._

_No rows._

### Score components
_No rows._

_No rows._

_No rows._

### Swing / liquidity quality
_No rows._

_No rows._

### Model 3 fill variants
_No rows._

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
