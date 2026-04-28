# Entry Models Backtest Report

Config:
- symbols: BTCUSDT
- timeframes: 15m
- models: model1
- warmup_bars: 100
- forward_bars: 10
- cooldown_bars: 5
- generated_at: 2026-04-23T22:22:56.437138+00:00

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

## 6. Warnings / skipped events
- none

## 7. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
