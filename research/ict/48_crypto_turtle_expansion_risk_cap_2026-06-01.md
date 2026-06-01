# Crypto Turtle Expansion and 1h Risk-Cap Lead

Date: 2026-06-01

Status: research lead only. Live remains disabled.

## Purpose

The goal was to move from small positive Turtle samples toward a strategy that
can plausibly survive costs, funding, OOS/control splits, and a meaningful
trade count.

## Infrastructure fixes

### Binance funding limit

The Binance downloader failed while expanding symbols because klines allow
`limit=1500`, but the funding endpoint rejected that value with `illegal
params`.

Fix:

- `backtesting/download_history.py` now caps funding requests separately at
  `1000`.
- Unit coverage added in `tests/test_new_ict_models.py`.

### Event-study performance

The multi-symbol Turtle replay initially timed out:

- 8-symbol batch exceeded 20 minutes before writing reports.
- Single-symbol BNB OOS exceeded 15 minutes before writing reports.

Fixes:

- `_candles_until()` now uses cached candle timestamps plus `bisect_right`
  instead of scanning the secondary SMT history on every bar.
- `turtle_soup` no longer forces accumulated primary snapshots when
  `context_mode=off`; it only needs the visible candle window plus SMT in this
  research mode.

After the fixes:

- BNB OOS completed in about 20 seconds.
- The 8-symbol expansion batch completed in about 226 seconds.
- The extended BTC/LINK/XRP batch completed in about 254 seconds.

## Data added

Expanded local Binance USD-M data:

- `data/history_crypto_2022-01-01_2026-04-20`:
  `BNBUSDT`, `XRPUSDT`, `ADAUSDT`, `DOGEUSDT`, `LINKUSDT`,
  `AVAXUSDT` at `30m`, `1h`, plus funding.
- `data/history_crypto_2019-09-01_2026-04-20`:
  `BTCUSDT`, `ETHUSDT`, `LINKUSDT`, `XRPUSDT` at `30m`, `1h`,
  plus funding.

## 8-symbol crypto expansion

Config:

- `configs/backtests/asian_turtle_full1r_clean_strong_crypto_expansion_funding_research.json`

Rules:

- BTC, SOL, BNB, XRP, ADA, DOGE, LINK, AVAX.
- Same source-aligned Asian Turtle detector settings as the previous BTC lead.
- One trade per symbol/session through session dedupe.
- Funding-aware costs.
- Strict sample gate: `min_total_trades=100`, `min_phase_trades=30`.

Result after model rules:

- OOS 2022-2024: 99 trades, `+0.220119R`, PF `1.81275`.
- Control 2024-2026: 47 trades, `+0.229941R`, PF `1.721375`.

Rejection:

- OOS walk-forward validation phase was negative: `-0.030018R`.
- Control test phase was negative: `-0.382542R`.
- Adding broad symbols increased count but did not create stable phase edge.

## Best strict subset

Read-only subset audit on generated events found the best conservative symbol
subset:

- `BTCUSDT`, `LINKUSDT`, `XRPUSDT`

Config:

- `configs/backtests/asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_research.json`

Strict model-rule result:

- Early 2019-2021: 16 deduped trades, `-0.115738R`, PF `0.75666`.
- OOS 2022-2024: 42 trades, `+0.309618R`, PF `2.344257`.
- Control 2024-2026: 18 trades, `+0.609139R`, PF `9.472112`.
- Full 2019-2026: 76 trades, `+0.291008R`, PF `2.190485`.

Rejection:

- Early regime is negative.
- Full sample remains below 100 trades.
- Full train and validation phases are below the strict `0.3R` expectancy gate.

## Practical 1h risk-cap lead

The most practical lead removes the strong-only/DOL-priority model rules but
keeps the detector itself strict:

- Asian range Turtle Soup.
- NY open `08:30-12:00`.
- SMT required on the sweep.
- Prior failed Asian sweep rejected.
- Funding-aware costs.
- `1h` only.
- `max_risk_bps=220`.
- Symbols: `BTCUSDT`, `LINKUSDT`, `XRPUSDT`.

Config:

- `configs/backtests/asian_turtle_btc_link_xrp_1h_risk_cap_funding_research.json`

Results:

- Early 2019-2021: 22 trades, `+0.117699R`, PF `1.340414`.
- OOS 2022-2024: 54 trades, `+0.22108R`, PF `1.746254`.
- Control 2024-2026: 30 trades, `+0.586769R`, PF `6.144131`.
- Full 2019-2026: 106 deduped trades, `+0.303121R`, PF `2.188874`,
  max drawdown `6.478457R`.
- Full trade P&L report after model rules: 107 trades, `+0.290168R`,
  PF `2.104551`, sample valid.

Rejection for live:

- Full train phase expectancy is `+0.181461R`.
- Full validation phase expectancy is `+0.280305R`.
- Both are below the strict `0.3R` phase gate.
- Early 2020-2021 is positive overall but internally unstable.

## Decision

Do not enable live filters.

The new 1h risk-cap Turtle variant is the strongest practical research lead so
far because it reaches a 100+ full sample after costs/funding and stays net
positive across early/OOS/control windows. It is still not live-grade because
early and full-phase expectancy are below the strict gate.

## Next step

Treat `asian_turtle_btc_link_xrp_1h_risk_cap_funding_research.json` as the
current paper-forward/research candidate. The next work should be rolling
monthly/quarterly stability plus a forward-log/paper-trade harness, not live
promotion.
