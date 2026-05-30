# Hyperliquid Free Index Feed - 2026-05-25

## Decision

Use Hyperliquid as the free automated feed for the next recent/forward
research cycle, while retaining Databento/CME only as the route for a later
long-history futures validation.

Historical note: the probe numbers below were generated before hourly
perpetual funding was integrated into the backtester. The strict zero-event
result is unchanged by funding; any traded follow-up profile must use the
funding-aware configuration added later.

This is not a substitution of instruments:

- `xyz:XYZ100` is a HIP-3 synthetic Nasdaq-oriented perpetual market;
- `xyz:SP500` is a HIP-3 S&P 500 perpetual market;
- they are tradeable on Hyperliquid and can be tested with Hyperliquid
  execution assumptions;
- they are not CME `NQ`/`MNQ` or `ES`/`MES`.

## Official API Evidence

Hyperliquid documents:

- HIP-3 builder-deployed perps and the deployer's responsibility for market
  definition/oracles:
  <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals>
- public `POST https://api.hyperliquid.xyz/info` candle snapshots, supported
  `30m` intervals, the `xyz:XYZ100` HIP-3 naming format, and the most-recent
  `5000` candle limit:
  <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint>
- `perpDexs` and `meta` endpoints used to discover HIP-3 market universes:
  <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals>
- HIP-3 user fees are twice normal validator-operated perp fees:
  <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals>

API requests performed on `2026-05-25` returned:

| Endpoint / market | Result |
| --- | --- |
| `perpDexs` | includes `xyz` |
| `meta`, dex `xyz` | includes `xyz:XYZ100`, `xyz:SP500`, `xyz:DXY`, `xyz:EUR`, `xyz:GBP` |
| `xyz:XYZ100`, `30m` | data from `2026-02-10 08:00 UTC` through `2026-05-25` when a longer range was requested |
| `xyz:SP500`, `30m` | data from `2026-03-18 13:00 UTC` through `2026-05-25` |

## Implementation

- Added `backtesting/download_hyperliquid_history.py`.
  - Uses the free public Hyperliquid info endpoint without an API key.
  - Saves `xyz:XYZ100` to local backtest symbol `XYZ100` and
    `xyz:SP500` to `SP500`, avoiding invalid Windows filename characters.
  - Also downloads core crypto perps such as `BTC` and `ETH` so cross-market
    comparison uses one execution venue.
  - With `--include-funding`, downloads paginated hourly `fundingHistory`
    rows to `SYMBOL_funding.csv` for funding-aware validation.
- Added `configs/backtests/hyperliquid_recent_turtle_research.json`.
  - Tests `XYZ100:SP500` same-sweep SMT for the index-perp candidate.
  - Tests `BTC:ETH` on the same recent source as a crypto comparator.
  - Scores signals only on full common days `2026-03-19` through
    `2026-05-24`; `SP500` begins during `2026-03-18` and `2026-05-25` was
    incomplete when downloaded.
  - Assumes `9 bps` HIP-3 commission per side plus `2 bps` slippage; this is
    deliberately conservative and must be replaced by actual user fee tier,
    growth-mode status, and observed execution.

## Limitations

- The public candle history is capped at recent bars and cannot establish
  multi-year profitability.
- HIP-3 oracle behavior and liquidity differ from CME index futures.
- Subsequent Hyperliquid profiles model hourly funding using entry price as a
  notional proxy; this avoids omitting the fee but is still an approximation
  to oracle-price settlement.
- The new source expands the test universe; it does not repair the rejected
  BTC Binance OOS result.

## Download and Probe Results

Downloaded `30m` bars through the public endpoint:

| Local symbol | Hyperliquid market | Returned candles |
| --- | --- | ---: |
| `BTC` | `BTC` | 5001 |
| `ETH` | `ETH` | 5001 |
| `XYZ100` | `xyz:XYZ100` | 5000 |
| `SP500` | `xyz:SP500` | 3268 |

Coverage for the full common window `2026-03-19` through `2026-05-24`
passed for all four markets: `3216` `30m` candles per market, `100%`
coverage, maximum gap `1` bar.

The strict candidate (`Asian range sweep + directional SMT on the sweep
candle`) produced no events on either pair:

| Profile | Events | Gate result |
| --- | ---: | --- |
| `XYZ100:SP500`, strict SMT-on-sweep | 0 | Fail: no sample |
| `BTC:ETH`, strict SMT-on-sweep | 0 | Fail: no sample |

Diagnostics confirm that the source contains actionable-shaped candles but do
not justify loosening the candidate:

| Diagnostic profile | Activated trades | Net managed expectancy | Profit factor | Decision |
| --- | ---: | ---: | ---: | --- |
| `XYZ100`, Asian sweep without SMT | 11 | `-1.351898R` | `0.047747` | Reject |
| `BTC`, Asian sweep without SMT | 13 | `-0.251766R` | `0.562447` | Reject |
| `XYZ100`, directional SMT without same-sweep | 0 | n/a | n/a | No sample |
| `BTC`, directional SMT without same-sweep | 1 | n/a | n/a | No sample |

The very large index net-cost drag is informative: with a narrow stop,
conservative HIP-3 fee/slippage assumptions consume too much of the intended
R outcome. A later index design must address stop distance and execution
costs without optimising to this short window.

## Runbook

```powershell
python -m backtesting.download_hyperliquid_history --out-dir data/history_hyperliquid_recent_2026-02-10_2026-05-25 --coins BTC ETH xyz:XYZ100 xyz:SP500 --timeframes 30m --start 2026-02-10 --end 2026-05-25T23:59:59Z --include-funding
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_recent_turtle_research.json
```

## Live Decision

All live strategy filters remain disabled. Hyperliquid results, even if
positive in this recent window, are only candidate evidence until funding is
modelled and a sufficiently long costed OOS sample passes the existing gates.
