# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2024-11-06_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 1h
- same_bar_policy: conservative
- context_mode: aligned_only
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
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
