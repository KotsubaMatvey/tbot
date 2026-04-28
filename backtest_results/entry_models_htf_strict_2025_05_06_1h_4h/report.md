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
- htf_mode: strict
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-24T14:38:58.513430+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 0
- warnings: 8
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

## 7. Warnings / skipped events
- Entry Model 3 BTCUSDT 1h 0: missing optional HTF history 1d; model3 context will be incomplete
- Entry Model 3 BTCUSDT 4h 0: missing optional HTF history 1d; model3 context will be incomplete
- Entry Model 3 ETHUSDT 1h 0: missing optional HTF history 1d; model3 context will be incomplete
- Entry Model 3 ETHUSDT 4h 0: missing optional HTF history 1d; model3 context will be incomplete
- Entry Models BTCUSDT 1h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models BTCUSDT 4h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models ETHUSDT 1h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals
- Entry Models ETHUSDT 4h 0: missing optional HTF history 1d; strict/soft HTF filtering may block signals

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
