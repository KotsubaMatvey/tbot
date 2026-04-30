# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- data_dir: tests/fixtures
- models: silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup, breaker_block
- symbols: BTCUSDT
- timeframes: 5m, 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
_No rows._

## Entry Mode Analysis
_No rows._

## Stop Mode Analysis
_No rows._

## Same-Bar Conservative Impact
_No rows._

## Model Family
_No rows._

## HTF Location
_No rows._

## Displacement
_No rows._

## Decision Score Buckets
_No rows._

## No-Trade Reasons
_No rows._
