# Hyperliquid Funding Cost Integrity - 2026-05-25

## Reason For This Change

Hyperliquid instruments used by the recent ICT research are perpetual
contracts. The official documentation states that:

- funding is paid every hour;
- positive funding is paid by long holders to short holders and negative
  funding reverses that payment;
- the public info endpoint exposes historical `fundingHistory`, including for
  HIP-3 markets.

Official sources:

- <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding>
- <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals>

Ignoring funding would make a later Hyperliquid live-gate decision incomplete,
even though it does not explain the already negative Silver Bullet results.

## Implementation

- `backtesting/download_hyperliquid_history.py`
  - adds `--include-funding`;
  - pages the public `fundingHistory` response beyond its `500`-row response
    limit;
  - saves `SYMBOL_funding.csv` rows with `time`, `funding_rate`, and
    `premium`.
- `backtesting/data.py`
  - loads the hourly funding CSV for a traded symbol.
- `backtesting/run_ict_models.py`
  - records `exit_time` and `tp1_time`;
  - applies funding only for hourly settlements after entry and through exit;
  - reduces funded position size after a partial TP1 close;
  - exports `funding_cost_r` and `total_cost_r`.
- Reports now expose average funding and total costs.
- Hyperliquid research presets require the funding directory.

Funding payment uses entry price as a stable notional-price proxy because the
historical API response supplies rate and premium, not the settlement oracle
price used in the official payment formula. This is more complete than
omitting funding, but remains an approximation for future live promotion.

## Download Coverage

Command:

```powershell
python -m backtesting.download_hyperliquid_history --out-dir data/history_hyperliquid_recent_2026-02-10_2026-05-25 --coins BTC ETH xyz:XYZ100 xyz:SP500 --timeframes 30m --start 2026-02-10 --end 2026-05-25T23:59:59Z --include-funding
```

| Local symbol | Hourly funding rows | Coverage note |
| --- | ---: | --- |
| `BTC` | 2513 | Starts `2026-02-10`; covers test period |
| `ETH` | 2513 | Starts `2026-02-10`; covers paired research period |
| `XYZ100` | 2513 | Starts `2026-02-10`; covers test period |
| `SP500` | 1635 | Starts at market availability on `2026-03-18`; covers test period |

## Funding-Aware Silver Bullet Validation

Command:

```powershell
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_official_silver_bullet_research.json
```

| Market | Activated trades | Gross expectancy | Execution cost | Funding cost | Net expectancy | Profit factor | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `XYZ100` | 68 | `-0.058894R` | `1.415364R` | `0.004229R` | `-1.478487R` | `0.066541` | Fail |
| `SP500` | 81 | `-0.070278R` | `1.512049R` | `0.004126R` | `-1.586453R` | `0.047457` | Fail |
| `BTC` | 60 | `-0.124419R` | `0.357211R` | `0.000759R` | `-0.482389R` | `0.339243` | Fail |

Funding is not the dominant loss source; execution costs and negative gross
expectancy already reject this Silver Bullet profile.

## Turtle Soup Control

The strict Hyperliquid Asian-range Turtle Soup configuration was also rerun
with funding required. It still generates `0` events for both
`XYZ100:SP500` and `BTC:ETH`, so it remains untestable rather than profitable.

## Decision

All live strategies remain disabled. Hyperliquid candidates can now be
evaluated with hourly funding included, but no tested strategy currently meets
the costed walk-forward profitability gates.
