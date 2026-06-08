# IFVG 15m Cost-Geometry Rejection - 2026-06-08

## Goal

Re-evaluate the standalone `ifvg_retest` model on current BTCUSDT and ETHUSDT
`15m` history with managed exits, Binance funding, and execution costs.

The old broad IFVG report had enough raw sample and high MFE, but it predated
managed P&L and cost fields. Its positive `5m`/`15m` rows could not support a
profitability conclusion.

## Fixed Parameters

- entry: IFVG edge;
- minimum retest depth: `0.15`;
- retest delay: `1..48` bars;
- maximum source FVG age: `100` bars;
- maximum source touches before inversion: `12`;
- displacement: `valid` or `strong`;
- target: nearest draw on liquidity;
- model-rule target distance: at least `2R`;
- commission: `4` bps;
- slippage: `1` bps;
- forward horizon: `96` bars so the window covers the maximum retest delay
  plus post-entry evaluation.

## Replay Performance Repair

Two no-logic-change optimizations made multi-year validation practical:

1. single-model `ifvg_retest` with `context_mode=off` no longer builds an
   accumulated primitive snapshot that the detector does not read;
2. IFVG source, breach, age, and touch calculations now use candle indices
   instead of repeated full-window timestamp scans.

The January 2025 BTC/ETH `15m` equivalence check retained all `15` events and
matching trade/attribution fields. Runtime fell from about `195` seconds to
`12` seconds.

## CE-Stop Baseline

Config:

`configs/backtests/crypto_ifvg_retest_15m_costed_validation.json`

### Raw

| Period | Trades | Expectancy | PF | Max DD | Avg total cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| OOS `2022-01-01..2024-11-05` | 181 | -1.310771R | 0.214813 | 237.907962R | 1.544007R |
| Late `2024-11-06..2026-04-20` | 110 | -1.402973R | 0.180967 | 154.327029R | 1.439359R |

The CE stop makes risk so small that ordinary execution costs average more than
`1R` per trade.

An economic gate of `max_execution_cost_r=0.20` left only:

- OOS: `4` trades, `+0.755527R`;
- late control: `0` trades.

The positive OOS row is invalid because the tradeable sample disappears
entirely in late control.

## Opposite-Boundary Stop

Config:

`configs/backtests/crypto_ifvg_retest_15m_wide_stop_costed_validation.json`

### Raw

| Period | Trades | Expectancy | PF | Max DD | Avg total cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| OOS | 193 | -0.514703R | 0.457140 | 104.955085R | 0.995579R |
| Late control | 121 | -0.600945R | 0.360850 | 74.085530R | 0.878728R |

The wider stop improves survival and reduces cost in R, but the raw strategy
remains strongly negative.

With `max_execution_cost_r=0.20` and target distance `>=2R`:

| Period | Trades | Expectancy | PF |
| --- | ---: | ---: | ---: |
| OOS | 4 | -0.002255R | 0.991643 |
| Late control | 5 | -0.558968R | 0.199113 |

Both samples are invalid and late control is negative.

## Decision

Reject standalone BTC/ETH `15m ifvg_retest` for live and paper use.

- CE-stop geometry is untradeable after realistic costs.
- The source-aligned opposite-boundary stop improves results but does not
  produce positive OOS or late-control edge.
- A strict cost cap removes almost the entire sample.
- Do not rescue this branch by optimizing depth, age, touches, or DOL filters
  on the already observed OOS/control data.

`ifvg_retest` remains useful as primitive/context metadata, but not as a
standalone trade strategy under the tested crypto execution model.
