# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_hyperliquid_recent_2026-02-10_2026-05-25
- models: ict2022_mss_fvg
- symbols: XYZ100
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 32
- commission_bps: 9.0
- slippage_bps: 2.0
- commission_points: 0.0
- slippage_points: 0.0
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
