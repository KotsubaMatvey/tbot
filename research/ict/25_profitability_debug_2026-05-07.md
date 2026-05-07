# Profitability Debug - 2026-05-07

## Goal

Improve ICT model profitability/frequency and debug the bot end to end.

Success criteria used in this pass:

- Unit tests pass.
- Compile check passes.
- Offline smoke checks pass.
- Backtests include execution costs.
- No live model is enabled unless it has positive net expectancy, enough trades, and stable walk-forward phases.

## Code Changes

- Added `turtle_soup_range_source=asian_range`.
  - Builds an Asian range from `turtle_soup_asian_range_window`, defaulting to `00:00-08:00` in `UTC`.
  - Trades only configured NY session windows.
  - Detects sweep and reclaim of Asian high/low.
  - Can restrict to the first reclaim after the range.
- Added optional `turtle_soup_min_stop_bps`.
  - Widens Turtle Soup stops to a minimum distance when configured.
  - This is research-only; it did not improve the best BTC Asian-range profile.
- Added event fields for Asian range metadata.
- Added model-filter support for:
  - `min_risk_bps`
  - `max_risk_bps`
  - `max_execution_cost_r`
  - `allowed_directions`
  - `allowed_session_labels`
  - `allowed_session_windows`
  - `allowed_range_sources`
- Fixed a simulator issue:
  - Unresolved trades inside `forward_bars` now close at the last horizon close.
  - Previous behavior used max favorable excursion as the managed result, which overstated model quality.
- Added repeatable config:
  - `configs/backtests/asian_turtle_debug_2025.json`

## Key Backtest Results

### Asian Range Turtle Soup, BTCUSDT 30m, 2025

Command profile:

- Data: `data/history_2025-01-01_2025-12-31`
- Model: `turtle_soup`
- Range source: `asian_range`
- Asian range: `00:00-08:00 UTC`
- Trade session: NY `08:30-12:00`
- Target: fixed `2R`
- TP1: `1R`, full close
- Costs: `4 bps` commission and `1 bps` slippage per side
- Model filter: `min_risk_bps=80`

Result from `backtest_results/asian_turtle_debug_2025_btc_30m`:

- Filtered trades: `23`
- Net managed expectancy: `+0.078035R`
- Profit factor: `1.195652`
- Win rate: `56.52%`
- Walk-forward: failed
  - Too few total trades.
  - Too few phase trades.
  - Validation phase expectancy was negative.
  - Profit factor below strict gate.

### Extended BTCUSDT 30m, 2024-11-06 to 2026-04-20

Best-looking 2025-only Asian Turtle filters did not survive extension:

- `risk_bps >= 80`: `38` trades, net expectancy `-0.0077R`, PF `0.9832`.
- `short` and `risk_bps >= 80`: `21` trades, net expectancy `+0.1420R`, PF `1.3920`, but:
  - 2024 partial sample negative.
  - 2026 partial sample negative.
  - Not enough robust phase coverage.

### Rejection Block 1h, Costed 2025

Re-ran old positive-looking profile with current costed runner and horizon-close fix:

- BTCUSDT: negative net expectancy.
- ETHUSDT: near breakeven but negative after costs.
- SOLUSDT: negative.
- Combined: negative.

## Current Trading Decision

Do not enable a new live model from this pass.

The project is more correct after the simulator fix and Asian-range research implementation, but the honest profitability target is not met yet. The best new profile is a research candidate, not a deployable bot model.

## Verification

Passed:

- `python -m unittest discover` -> 97 tests OK.
- `python -m compileall -q .`
- `python offline_smoke_test.py` -> 5/5 passed.
- `python offline_backtest.py` -> 5/5 scenarios passed.

