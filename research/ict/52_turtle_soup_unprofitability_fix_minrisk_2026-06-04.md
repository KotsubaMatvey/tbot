# Turtle Soup Unprofitability Fix: Min-Risk Cost Gate

Date: 2026-06-04

Status: IS-only diagnostics and candidate refinement. OOS remains untouched.

## Problem

The current Turtle Soup failure is not primarily signal frequency. It is costed
quality.

The broad optional-SMT run generated enough trades but was net-negative after
costs. The strong-quality subset improved the edge, but validation stayed weak.

Core symptoms:

- broad optional SMT: `691` trades, `-0.148600R`, PF `0.706199`
- strong quality, SMT optional: `299` raw trades, `+0.115987R`, PF `1.322423`
- strong no-SMT, first dedupe: `234` WF trades, `+0.133679R`, PF `1.378827`
- strong no-SMT validation: `+0.020566R`, PF `1.048994`

## Root Causes Found

### 1. SMT is not the profitable gate on BTC/ETH 30m IS

For strong-quality trades:

- no-SMT raw bucket: `263` trades, `+0.146863R`, PF `1.433826`
- SMT raw bucket: `36` trades, `-0.109585R`, PF `0.787065`

Decision: use SMT as metadata/confidence only. Do not require SMT and do not let
SMT score dominate session selection.

### 2. Current `decision_score` is not P&L-aligned

In the strong no-SMT raw bucket:

- high score: `126` trades, `-0.022425R`, PF `0.945755`
- medium score: `137` trades, `+0.302559R`, PF `2.121952`

The high-score bucket mostly means larger target distance, but these trades had
tighter stops and higher cost in R. Raising `min_decision_score` would worsen
the strategy.

### 3. Validation is broken by tight-stop cost drag

Strong no-SMT first-dedupe validation:

- all validation: `+0.007298R`, PF `1.017146`
- high score / no score penalty: `-0.210821R`, PF `0.607513`
- average total cost in that bad bucket: `0.562172R`
- medium score validation: `+0.204138R`, PF `1.628019`

The failing trades are not simply "bad pattern shape"; they are mostly too
expensive in R because risk distance is too small.

## Code Changes

Added:

- `require_no_smt` in `strategies/ict_models/model_filters.py`
- `backtesting/phase_attribution_report.py`
- `phase_attribution_report` support in `backtesting/run_ict_batch.py`

This makes the no-SMT base and phase-level P&L attribution reproducible from
JSON configs.

## IS Candidate

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_strong_no_smt_minrisk35_first_30m.json`

Rules:

- model: Turtle Soup
- symbols: BTCUSDT, ETHUSDT
- timeframe: `30m`
- IS: `2022-01-01` through `2023-06-30`
- entry: retest
- range: Asian range
- sessions: London open, NY open, NY PM
- model filter:
  - `allowed_turtle_qualities=["strong"]`
  - `require_no_smt=true`
  - `min_risk_bps=35`
- dedupe: first trade per symbol/session
- costs: commission `4.0` bps, slippage `1.0` bps, funding-aware

## Candidate Results

Walk-forward:

| Phase | Trades | Net exp | Gross exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 133 | `+0.360814R` | `+0.548868R` | `2.390905` | `3.749911R` | true |
| train | 42 | `+0.294590R` | `+0.476190R` | `1.951502` | `3.120560R` | true |
| validation | 44 | `+0.423381R` | `+0.611930R` | `2.932603` | `3.749911R` | true |
| test | 47 | `+0.361419R` | `+0.554776R` | `2.432409` | `2.966217R` | true |

Raw filtered P&L:

- `143` trades
- `+0.350612R`
- PF `2.313148`
- max DD `3.688448R`
- Sharpe `4.175081`
- average total cost down to `0.187845R`

Per-symbol raw filtered report:

- BTCUSDT: `61` trades, `+0.446387R`, PF `3.266925`
- ETHUSDT: `82` trades, `+0.279365R`, PF `1.875367`

## Decision

Do not run OOS yet.

The candidate passes IS walk-forward gates, but it was discovered through IS
diagnostics. Treat it as the first locked OOS candidate, not as a proven edge.

The important algorithmic repair is the min-risk/cost gate:

- Turtle Soup must not take setups where risk distance is so tight that normal
  crypto execution costs consume a large part of R.
- `min_risk_bps=35` is the current IS candidate value.

## Next Step

1. Keep this candidate frozen.
2. Restore BTCUSDT/ETHUSDT `15m` data if Binance DNS/network becomes available.
3. Before OOS, decide whether OOS should test:
   - only this locked `30m` candidate; or
   - the same locked rules on `15m + 30m` after `15m` data is available.
4. Run OOS only once the candidate scope is locked.
