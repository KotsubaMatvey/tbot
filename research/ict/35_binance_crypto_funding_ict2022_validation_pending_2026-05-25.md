# Binance Crypto Funding And ICT2022 Validation Result - 2026-05-25

## Goal And Evidence Boundary

The next crypto candidate selected for validation is `ict2022_mss_fvg`,
because the project rule map links its sequence to the retrieved ICT 2022
Mentorship text:

- official Episode 2: <https://www.youtube.com/watch?v=tmeCWULSTHc>
- official Episode 3: <https://www.youtube.com/watch?v=nQfHZ2DEJ8c>

The source-backed sequence is liquidity sweep, MSS/displacement, then FVG
retest. The configured same-session requirement below is an internal
operational constraint for clean testing and runtime control, not a claimed
verbatim ICT rule.

For Binance USD-M perpetual validation, funding must be included. The official
funding-history endpoint supplies `fundingRate`, `fundingTime`, and
`markPrice`:
<https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History>.

## Correctness Change

- `backtesting/download_history.py`
  - adds `--include-funding` for Binance USD-M history;
  - downloads paged `fundingRate` rows and writes `SYMBOL_funding.csv`;
  - retains optional settlement `mark_price` where Binance returns it.
- `backtesting/data.py`
  - loads optional `mark_price` in funding rows.
- `backtesting/run_ict_models.py`
  - values funding settlements using their `mark_price` when available;
  - explicitly reports `entry_proxy`, `settlement_mark_price`, or mixed
    notional-price mode when historical rows omit mark price.
- `tests/test_new_ict_models.py`
  - covers Binance response normalization, empty historical `markPrice`, and
    settlement-price funding calculation.

This extends the funding-aware cost path previously added for Hyperliquid;
it does not enable or loosen any live strategy.

## Multi-Year Crypto Dataset

New dataset:
`data/history_crypto_2022-01-01_2026-04-20`

| Symbol | OHLCV timeframes | Date coverage | Funding rows | Rows with mark price |
| --- | --- | --- | ---: | ---: |
| `BTCUSDT` | `30m`, `1h`, `4h`, `1d` | `2022-01-01` through `2026-04-20` | 4713 | 2708 |
| `ETHUSDT` | `30m`, `1h`, `4h`, `1d` | `2022-01-01` through `2026-04-20` | 4713 | 2708 |

OHLCV coverage verification:

```powershell
python -m backtesting.data_coverage_report --data-dir data/history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT ETHUSDT --timeframes 30m 1h 4h 1d --required-start 2022-01-01 --required-end 2026-04-20 --min-coverage-pct 99.9 --max-gap-bars 1 --out-dir backtest_results/data_coverage_crypto_2022-01-01_2026-04-20
```

Result: passed for all eight OHLCV series. Binance returned empty historical
`markPrice` on older funding rows; those rows are retained and explicitly
use the existing entry-price proxy rather than silently dropping funding.

## Predeclared Validation Profile

Added `configs/backtests/crypto_ict2022_funding_validation.json`:

- BTCUSDT and ETHUSDT, independently evaluated on `30m` and `1h`;
- early OOS interval: `2022-01-01` through `2024-11-05`;
- late control interval: `2024-11-06` through `2026-04-20`;
- strict HTF directional context with daily/4h input available;
- strong displacement, edge entry, FVG retest within three bars;
- sweep, MSS, FVG, and retest constrained to the same configured NY session;
- commission `4 bps` and slippage `1 bps` per side, plus downloaded funding;
- existing walk-forward promotion gates unchanged.

## Verification State

Passed:

```powershell
python -m unittest tests.test_new_ict_models.NewICTModelTests.test_binance_funding_costs_use_settlement_mark_price tests.test_new_ict_models.NewICTModelTests.test_binance_funding_uses_official_history_response_shape tests.test_new_ict_models.NewICTModelTests.test_hyperliquid_funding_costs_apply_direction_and_partial_close
```

Completed:

```powershell
python -m backtesting.run_ict_batch --config configs/backtests/crypto_ict2022_funding_validation.json
```

The unconstrained initial run timed out after approximately 20 minutes before
writing a report. The predeclared same-session/session-window preset completed
later and generated all four expected reports:

| Interval | Timeframe | Activated trades | Gate |
| --- | --- | ---: | --- |
| `2022-01-01` through `2024-11-05` | `1h` | 0 | Fail: `min_total_trades` |
| `2022-01-01` through `2024-11-05` | `30m` | 0 | Fail: `min_total_trades` |
| `2024-11-06` through `2026-04-20` | `1h` | 0 | Fail: `min_total_trades` |
| `2024-11-06` through `2026-04-20` | `30m` | 0 | Fail: `min_total_trades` |

Follow-up attempts to diagnose the zero-frequency profile without HTF context
timed out after five minutes without writing reports. Multi-year ICT2022
iteration is therefore also limited by replay performance.

## Decision

The strict source-aligned ICT2022 crypto profile is rejected for live use
because it produces no tradable sample. No profitability result is asserted
from zero trades, and all live models remain disabled. The next required
research step is a bounded attribution run identifying which rule removes
frequency, after optimizing the multi-year replay path enough to produce
timely diagnostic reports.
