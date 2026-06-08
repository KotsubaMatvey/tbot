# Turtle Soup Foundation IS Pass

Date: 2026-06-02

Status: IS-only diagnostics. OOS remains untouched.

## Purpose

The goal was to stop adding models and rebuild the validation foundation around
one model: Turtle Soup. This pass only used in-sample data:

- IS: `2022-01-01` through `2023-06-30`
- Planned OOS: `2023-07-01` through `2024-12-31`

No OOS run was executed in this pass.

## Data

Existing local Binance USD-M data already covered BTCUSDT and ETHUSDT `30m`,
`1h`, `4h`, `1d` in `data/history_crypto_2022-01-01_2026-04-20`.

Missing data:

- BTCUSDT `15m`
- ETHUSDT `15m`

The attempted Binance download failed before any file was written:

- command: `python -m backtesting.download_history --out-dir data\history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT ETHUSDT --timeframes 15m --limit 1500 --start 2022-01-01 --end 2024-12-31 --timeout 180`
- error: DNS resolution failed for `fapi.binance.com` (`getaddrinfo failed`)

Therefore the completed runs are `30m` only.

## Infrastructure

`config.py` now uses `CANDLE_LIMIT = 500` instead of `200`.

This improves live scanner context depth for current and HTF candles. It does
not change the offline multi-year replay, which reads local history files and
already has long context available.

## Strict Asian Turtle IS

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023.json`

Rules:

- BTCUSDT and ETHUSDT
- `30m`
- Asian range Turtle Soup
- NY open `08:30-12:00`
- SMT required on sweep
- prior failed Asian sweep rejected
- funding-aware costs
- entry at close
- model rules enabled

Result:

- Generated events: `27`
- After model rules: `12` trades
- Walk-forward deduped count: `11`
- Walk-forward expectancy: `+0.100921R`
- Profit factor: `1.257727`
- Max drawdown: `2.975433R`
- Failed gates: `min_total_trades`, `min_phase_trades`,
  `min_managed_expectancy_r`, `min_profit_factor`

Verdict:

- Not statistically usable. The result is below the 100-trade floor.
- BTCUSDT was negative after model rules: `-0.128605R` over `8` trades.
- ETHUSDT was positive but only `4` trades.

## Retest Entry Diagnostic

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_retest_entry.json`

Only change from strict Asian Turtle IS:

- `entry_mode: retest`

Result:

- Generated events: `27`
- After model rules: `12` trades
- Walk-forward deduped count: `11`
- Walk-forward expectancy: `+0.415328R`
- Profit factor: `4.110634`
- Max drawdown: `1.468707R`
- Failed gates: `min_total_trades`, `min_phase_trades`

Verdict:

- Retest entry materially improves the strict Asian Turtle sample.
- It still has no statistical conclusion because only `11` deduped trades
  survive the IS period.

## Baseline Turtle Frequency Diagnostic

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_baseline_retest.json`

Rules:

- BTCUSDT and ETHUSDT
- `30m`
- baseline swing Turtle Soup, not Asian range
- no SMT/confluence
- killzones: `02:00-05:00`, `07:00-10:00`, `13:00-16:00`
- retest entry
- funding-aware costs

Result:

- Generated events: `12216`
- Trade P&L sample valid.
- Gross managed expectancy: `+0.333447R`
- Net managed expectancy: `-0.360221R`
- Profit factor: `0.441861`
- Average total cost: `0.693669R`
- Max drawdown: `4406.176832R`
- Session overtrade buckets: `2638`

Verdict:

- Frequency exists, but the baseline is untradeable.
- The gross signal is positive before costs, but execution cost in R is too
  large and turns it deeply negative.
- The raw baseline also overtrades sessions badly.

## Dedupe Control

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_baseline_retest_dedupe.json`

Only change from the baseline frequency diagnostic:

- `dedupe_session: true`
- first trade per symbol/session

Walk-forward result:

- Deduped trades: `2979`
- Net managed expectancy: `-0.311504R`
- Gross managed expectancy: `+0.35348R`
- Profit factor: `0.490425`
- Max drawdown: `934.144208R`
- Session overtrade count: `0`
- Failed gates: `min_managed_expectancy_r`, `min_profit_factor`,
  `max_drawdown_r`

Phase results:

- Train: `1012` trades, `-0.148545R`, PF `0.710937`
- Validation: `1010` trades, `-0.373746R`, PF `0.435128`
- Test: `969` trades, `-0.408808R`, PF `0.375048`

Verdict:

- Dedupe fixes overtrading but does not create a net edge.
- The baseline has enough sample, but costs overwhelm the gross signal in
  every IS phase.

## Algorithmic Findings

Entry:

- Current strict Asian Turtle presets used `entry_mode: close`.
- Retest entry improved expectancy and drawdown on IS but sample stayed invalid.

Stop:

- Turtle Soup stop placement is already behind the sweep wick:
  `stop_mode: sweep_extreme` / `asian_sweep_extreme`.
- The stop placement issue is not the primary bug in this pass.

Session filter:

- The strict Asian variant already had a killzone/session filter.
- The broad baseline was also tested with London, NY open, and NY PM windows.

HTF context:

- These IS runs used `context_mode: off`, so `htf_bias_audit` reports neutral
  context only.
- HTF edge-vs-sample attribution still requires a separate IS run with HTF
  context enabled and adequate HTF data.

Scoring/confluence:

- The baseline diagnostic removed SMT and model rules to avoid confluence
  leakage. It still failed after costs.

## Decision

Do not run OOS yet.

Current IS evidence rejects the broad baseline as net-negative after costs and
keeps the strict Asian retest variant as a frequency-blocked hypothesis, not a
candidate.

## Next Step

1. Restore Binance/network access and download BTCUSDT/ETHUSDT `15m` for
   `2022-01-01` through `2024-12-31`.
2. Re-run the strict Asian retest IS on `15m` and `30m`.
3. If sample remains below 100, do not tune OOS. Diagnose which strict filters
   kill frequency.
4. If sample reaches 100+ on IS, only then prepare the locked OOS run.
