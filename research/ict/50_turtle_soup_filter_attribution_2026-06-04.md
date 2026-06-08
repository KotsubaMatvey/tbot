# Turtle Soup Filter Attribution

Date: 2026-06-04

Status: IS-only diagnostics. OOS remains untouched.

## Purpose

The previous Turtle Soup foundation pass found that strict Asian Turtle Soup
with retest entry improved quality but produced only `11` deduped IS trades.
This pass diagnoses which strict filters suppress frequency on BTCUSDT/ETHUSDT
`30m` in-sample data.

IS window:

- `2022-01-01` through `2023-06-30`

## Data blocker

BTCUSDT/ETHUSDT `15m` is still unavailable locally.

The retry command failed again before writing files:

- `python -m backtesting.download_history --out-dir data\history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT ETHUSDT --timeframes 15m --limit 1500 --start 2022-01-01 --end 2024-12-31 --timeout 180`
- error: DNS resolution failed for `fapi.binance.com` (`getaddrinfo failed`)

All runs below are `30m` only.

## Config

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_filter_attribution_30m.json`

Common rules:

- model: `turtle_soup`
- symbols: BTCUSDT, ETHUSDT
- timeframe: `30m`
- range source: Asian range
- entry: retest
- target: DOL hierarchy
- costs: commission `4.0` bps, slippage `1.0` bps, funding-aware
- no OOS runs

## Results

| Variant | Events | WF trades | Net exp | Gross exp | PF | Max DD | Main failed gates |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strict retest, no model rules | 27 | 27 | `+0.490399R` | `+0.925926R` | `9.219602` | `1.468707R` | sample, phase trades, one session overtrade |
| no prior failed reject | 37 | 37 | `+0.482247R` | `+0.891892R` | `7.184613` | `1.468707R` | sample, phase trades, one session overtrade |
| no SMT | 346 | 346 | `+0.005152R` | `+0.451393R` | `1.012493` | `23.62968R` | expectancy, PF, DD, session overtrade |
| broad sessions with SMT | 61 | 61 | `+0.317635R` | `+0.815923R` | `3.359767` | `1.468707R` | sample, phase trades, one session overtrade |
| broad sessions, no SMT, no prior reject | 1880 | 1880 | `-0.13121R` | `+0.410317R` | `0.738977` | `250.681565R` | expectancy, PF, DD, session overtrade |

## Interpretation

SMT is the dominant frequency limiter:

- Strict retest with SMT: `27` events.
- Removing prior-failed-sweep rejection only increases to `37` events.
- Removing SMT increases to `346` events in NY open.
- Removing SMT and broadening sessions increases to `1880` events.

But SMT is also the dominant quality filter:

- No-SMT NY open has enough sample but net expectancy is only `+0.005152R`
  and PF `1.012493`; after phase gates it is not viable.
- Broad sessions without SMT become net-negative: `-0.13121R`, PF `0.738977`.

Broader sessions with SMT are the best frequency/quality compromise in this
pass:

- `61` trades
- `+0.317635R` net expectancy
- PF `3.359767`
- Max DD `1.468707R`

This is still below the `100` trade floor, so it is not enough for OOS.

## Decision

Do not run OOS.

The strict Asian retest hypothesis is not rejected on quality, but it remains
sample-blocked. The most useful next research branch is not removing SMT; it is
expanding SMT-preserving frequency.

## Next Step

1. Restore Binance DNS/network and download BTCUSDT/ETHUSDT `15m`.
2. Re-run strict and broad-session SMT-preserving retest variants on
   `15m + 30m`.
3. If still below `100` trades, test carefully scoped symbol expansion while
   preserving SMT and retest entry.
4. Only create an OOS config after IS has `100+` trades and survives net
   costs/phase gates.
