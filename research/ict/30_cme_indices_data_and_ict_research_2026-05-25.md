# CME Index Data and ICT Research - 2026-05-25

## Purpose

The crypto adaptation has not passed costed out-of-sample validation. The next
research track tests an ICT setup on the index futures market shown in an
official ICT example, while retaining Binance crypto as a control. No live
model is enabled by this change.

## Source Check

- Official ICT video title identifies an NQ Turtle Soup example:
  <https://www.youtube.com/watch?v=PFUe6OKmKuk>
- Official ICT channel:
  <https://www.youtube.com/@InnerCircleTrader>
- CME lists Micro E-mini Nasdaq-100 as `MNQ` and Micro E-mini S&P 500 as
  `MES`, including the `0.25` point minimum tick and `$2`/`$5` point
  multipliers:
  <https://www.cmegroup.com/articles/faqs/micro-e-mini-equity-index-futures-frequently-asked-questions.html>
- Databento documents CME Globex dataset `GLBX.MDP3`, OHLCV schemas, and
  continuous futures symbology:
  <https://databento.com/docs/venues-and-datasets/glbx-mdp3>
  <https://databento.com/docs/schemas-and-data-formats>
  <https://databento.com/docs/examples/symbology/continuous>

Inference: the official NQ Turtle Soup example supports testing Nasdaq
futures. Testing the smaller `MNQ` contract and `MNQ:MES` SMT relationship is
a research hypothesis, not a quoted ICT rule.

## Implementation

- Added `backtesting/download_databento_history.py`.
  - Uses Databento's official Python client and `DATABENTO_API_KEY`.
  - Requests volume-based front continuous contracts such as `MNQ.v.0` and
    `MES.v.0`.
  - Writes the existing `time,open,high,low,close,volume` CSV shape so no
    detector is forked by market.
  - Locally aggregates unsupported bar sizes from Databento OHLCV bars.
  - Provides `--estimate-only` using `metadata.get_cost` before a billable
    historical time-series download.
- Added fixed price-point execution costs to `backtesting/run_ict_models.py`.
  - Binance crypto continues to use `commission_bps` and `slippage_bps`.
  - CME runs can use `commission_points` and `slippage_points`.
- Fixed Asian-range handling for windows crossing midnight, enabling a
  New York-time `20:00-00:00` test range without changing prior UTC crypto
  configurations.
- Added `configs/backtests/cme_crypto_turtle_oos_research.json`.

## OOS Experiment

The preset keeps the previously failed BTC/ETH rule as a control and adds two
separate CME tests:

| Run | Primary / SMT reference | Cost model |
| --- | --- | --- |
| crypto control | `BTCUSDT:ETHUSDT` | `4 bps` commission + `1 bps` slippage per side |
| Nasdaq micro | `MNQ:MES` | assumed `0.50` point commission + `0.25` point slippage per side |
| S&P micro | `MES:MNQ` | assumed `0.20` point commission + `0.25` point slippage per side |

The CME commission assumptions represent `$1.00` per side per contract using
the CME point multipliers. Replace them with the actual broker all-in rate
before any execution decision. Slippage assumes one minimum tick per side.

Common admission gates remain:

- at least `30` activated trades overall and `10` per phase;
- net managed expectancy at least `+0.3R`;
- profit factor at least `1.3`;
- maximum drawdown no worse than `8R`;
- no more than one activated trade per session.

## Runbook

```powershell
python -m pip install databento
$env:DATABENTO_API_KEY = "db-..."
python -m backtesting.download_databento_history --estimate-only --symbols MNQ MES --timeframes 30m --start 2022-01-01 --end 2024-11-06
python -m backtesting.download_databento_history --out-dir data/history_cme_oos_2022-01-01_2024-11-06 --symbols MNQ MES --timeframes 30m --start 2022-01-01 --end 2024-11-06
python -m backtesting.run_ict_batch --config configs/backtests/cme_crypto_turtle_oos_research.json
```

Databento continuous prices are original, unadjusted contract prices and may
jump at roll transitions. Any apparently profitable result must be inspected
around roll dates before it is considered a candidate. Historical downloads
are metered; review the `--estimate-only` output before fetching data.

## Available Control Result

The Binance BTC control run was executed from the combined preset and
reproduces the previously rejected independent OOS result:

| Run | Activated trades | Net managed expectancy | Profit factor | Test expectancy | Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `BTCUSDT` `30m`, `BTCUSDT:ETHUSDT` SMT | 23 | `-0.185833R` | `0.616131` | `-0.264107R` | Fail |

Artifact:
`backtest_results/cme_crypto_turtle_oos_btc_control_30m/walk_forward_report.csv`.

## Current Decision

`DATABENTO_API_KEY` is not set in the current environment, so the CME OOS
download and results cannot yet be produced. Existing crypto candidates
remain rejected by prior OOS results; all live model filters remain disabled.
