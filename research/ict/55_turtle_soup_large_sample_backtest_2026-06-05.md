# Turtle Soup Large Sample Backtest - 2026-06-05

## Scope

Locked Turtle Soup candidate only:

- Symbols: `BTCUSDT`, `ETHUSDT`
- Timeframes: `15m`, `30m`
- Data: `data/history_crypto_2022-01-01_2026-04-20`
- Costs: `commission_bps=4.0`, `slippage_bps=1.0`, funding-aware rows from the same data directory
- Rules: Asian range, retest entry, `dol_hierarchy` target, ICT kill zones, `strong` quality, `require_no_smt=true`, `min_risk_bps=35`
- Dedupe: one trade per symbol/session, `first`, timeframe priority `30m,15m`

This run did not tune or change the locked strategy rules.

## Commands

```powershell
python -m backtesting.run_ict_batch --config configs\backtests\turtle_soup_btc_eth_is_2022_2023_strong_no_smt_minrisk35_15m_30m.json
python -m backtesting.run_ict_batch --config configs\backtests\turtle_soup_btc_eth_oos_2023_2024_strong_no_smt_minrisk35_15m_30m.json
python -m backtesting.run_ict_batch --config configs\backtests\turtle_soup_btc_eth_external_2023_2026_strong_no_smt_minrisk35_15m_30m.json
python -m backtesting.run_ict_batch --config configs\backtests\turtle_soup_btc_eth_full_2022_2026_strong_no_smt_minrisk35_15m_30m.json
```

## Deduped Results

| Run | Period | Events | Deduped trades | Winrate | Expectancy R | PF | Max DD R | Max losses | Sharpe | Total R | Gate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| IS | 2022-01-01..2023-06-30 | 1386 | 171 | 76.61% | 0.330721 | 2.189534 | 3.011907 | 2 | 4.166283 | 56.553282 | pass |
| OOS | 2023-07-01..2024-12-31 | 1204 | 92 | 79.35% | 0.389537 | 2.572923 | 3.175337 | 2 | 3.706561 | 35.837435 | fail: min_total_trades |
| Late-control | 2025-01-01..2026-04-20 | 956 | 82 | 73.17% | 0.260068 | 1.806924 | 2.977198 | 2 | 2.308363 | 21.325562 | fail: min_managed_expectancy_r;min_phase_trades;min_total_trades |
| External | 2023-07-01..2026-04-20 | 2160 | 174 | 76.44% | 0.328523 | 2.161562 | 3.175337 | 2 | 3.019687 | 57.162997 | pass |
| Full | 2022-01-01..2026-04-20 | 3546 | 345 | 76.52% | 0.329612 | 2.175307 | 3.175337 | 2 | 3.466294 | 113.716279 | pass |

## Full Sample Yearly Breakdown

| Year | Trades | Expectancy R | Total R | PF |
| --- | ---: | ---: | ---: | ---: |
| 2022 | 128 | 0.309382 | 39.600901 | 2.071511 |
| 2023 | 70 | 0.348056 | 24.363922 | 2.288089 |
| 2024 | 65 | 0.437321 | 28.425894 | 2.966706 |
| 2025 | 61 | 0.212511 | 12.963184 | 1.597302 |
| 2026 | 21 | 0.398208 | 8.362378 | 2.769699 |

## Interpretation

The large full sample is positive and passes the configured walk-forward gates, with positive performance in every calendar year covered by the local data.

This is still not a live approval. The strict OOS split remains below the 100-trade minimum, and the late-control split fails standalone phase/sample gates. The next gate remains forward paper/shadow validation with real scanner signals, fill rate, slippage, and net outcome logging.
