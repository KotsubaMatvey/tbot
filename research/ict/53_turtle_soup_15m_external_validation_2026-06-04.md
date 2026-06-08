# Turtle Soup 15m and External Validation

Date: 2026-06-04

Status: Locked-rule IS, OOS, and late-control diagnostics.

## Locked Candidate

Rules were frozen before OOS:

- model: `turtle_soup`
- symbols: BTCUSDT, ETHUSDT
- timeframes: `15m`, `30m`
- entry: retest
- range source: Asian range
- sessions: `02:00-05:00,07:00-10:00,13:00-16:00`
- model filters:
  - `allowed_turtle_qualities=["strong"]`
  - `require_no_smt=true`
  - `min_risk_bps=35`
- session dedupe: first trade per symbol/session
- costs: commission `4.0` bps, slippage `1.0` bps, funding-aware

No OOS filter changes were made after seeing OOS.

## Data

BTCUSDT/ETHUSDT `15m` was downloaded from the official Binance public archive
because Python DNS still failed on `fapi.binance.com`.

Coverage:

- `2022-01-01` through `2026-04-20`
- BTCUSDT `15m`: `150816` candles, `100.0%` coverage, max gap `1.0`
- ETHUSDT `15m`: `150816` candles, `100.0%` coverage, max gap `1.0`

Coverage reports:

- `backtest_results/data_coverage_btc_eth_15m_2022_2026`
- `backtest_results/data_coverage_btc_eth_30m_2025_2026`

## IS Results

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_strong_no_smt_minrisk35_15m_30m.json`

### 15m only

Period: `2022-01-01` through `2023-06-30`

Walk-forward:

| Phase | Trades | Net exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | --- |
| overall | 106 | `+0.409487R` | `2.726334` | `3.373316R` | true |
| train | 33 | `+0.382030R` | `2.535377` | `2.248657R` | true |
| validation | 37 | `+0.307365R` | `2.058272` | `3.373316R` | true |
| test | 38 | `+0.555579R` | `4.412904` | `1.689779R` | true |

Raw filtered P&L:

- `115` trades
- `+0.437971R`
- PF `3.003188`
- max DD `3.632205R`

### 15m + 30m combined

Period: `2022-01-01` through `2023-06-30`

Walk-forward:

| Phase | Trades | Net exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | --- |
| overall | 171 | `+0.330721R` | `2.189534` | `3.011907R` | true |
| train | 55 | `+0.303526R` | `2.011600` | `2.708161R` | true |
| validation | 60 | `+0.281893R` | `1.942309` | `3.011907R` | true |
| test | 58 | `+0.423535R` | `2.876510` | `2.926277R` | true |

Raw filtered P&L:

- `258` trades
- `+0.389551R`
- PF `2.587131`
- max DD `3.688448R`

Timeframe attribution:

- `15m`: `115` trades, `+0.437971R`, PF `3.003188`
- `30m`: `143` trades, `+0.350612R`, PF `2.313148`

## Locked OOS

Config:

- `configs/backtests/turtle_soup_btc_eth_oos_2023_2024_strong_no_smt_minrisk35_15m_30m.json`

Period: `2023-07-01` through `2024-12-31`

Walk-forward:

| Phase | Trades | Net exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | --- |
| overall | 92 | `+0.389537R` | `2.572923` | `3.175337R` | false |
| train | 30 | `+0.260057R` | `1.813771` | `3.175337R` | true |
| validation | 32 | `+0.511899R` | `3.704463` | `1.272268R` | true |
| test | 33 | `+0.431856R` | `2.995988` | `2.375650R` | true |

Failure:

- `min_total_trades`

Interpretation:

The locked OOS is positive and stable across internal phases, but the deduped
sample is `92`, below the `100` trade gate. Raw filtered sample is `128` trades,
but the formal gate is applied after session dedupe.

## Late-Control

Config:

- `configs/backtests/turtle_soup_btc_eth_external_2023_2026_strong_no_smt_minrisk35_15m_30m.json`

Period: `2025-01-01` through `2026-04-20`

Walk-forward:

| Phase | Trades | Net exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | --- |
| overall | 82 | `+0.260068R` | `1.806924` | `2.977198R` | false |
| train | 27 | `+0.052021R` | `1.116413` | `2.977198R` | false |
| validation | 26 | `+0.341206R` | `2.224706` | `1.702068R` | false |
| test | 29 | `+0.381022R` | `2.552096` | `2.393861R` | false |

Failure:

- `min_total_trades`
- `min_phase_trades`
- train `min_managed_expectancy_r`

Interpretation:

Late-control is positive overall, but not gate-clean as a standalone period.
It is mainly sample-limited and has one weak early phase.

## Full External Period

Period: `2023-07-01` through `2026-04-20`

Walk-forward:

| Phase | Trades | Net exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | --- |
| overall | 174 | `+0.328523R` | `2.161562` | `3.175337R` | true |
| train | 59 | `+0.365868R` | `2.379835` | `3.175337R` | true |
| validation | 61 | `+0.234811R` | `1.700915` | `2.977198R` | true |
| test | 57 | `+0.380709R` | `2.510874` | `2.393861R` | true |

Raw filtered P&L:

- `247` trades
- `+0.374591R`
- PF `2.459296`
- max DD `5.218327R`

Timeframe attribution:

- `15m`: `104` trades, `+0.320855R`, PF `2.109296`
- `30m`: `143` trades, `+0.413672R`, PF `2.775257`

## Decision

This is now a credible research candidate, not just an IS artifact.

Live promotion should still wait for a final review because:

- the original locked OOS `2023-07-01..2024-12-31` missed the deduped `100`
  trade gate by `8` trades;
- late-control standalone did not pass phase gates;
- the full external period passes only when `2023-2026` is pooled.

The current best locked candidate is:

- `15m + 30m`
- `strong`
- `require_no_smt`
- `min_risk_bps=35`
- first session dedupe

SMT remains metadata, not a hard gate.

## Next Step

Do not tune filters from OOS.

Next work should be operational validation:

1. Build a forward-paper/live-shadow config for the locked candidate only.
2. Keep live execution disabled until paper fill assumptions are checked.
3. Audit whether retest limit entries are realistically fillable with maker or
   taker costs.
4. If a live gate is needed, promote with small risk only after a forward log
   confirms fills, slippage, and alert timing.
