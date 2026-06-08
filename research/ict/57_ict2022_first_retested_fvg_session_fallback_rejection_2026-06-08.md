# ICT2022 First-Retested FVG Session Fallback Rejection - 2026-06-08

## Goal

Test whether `ict2022_mss_fvg` can recover enough sample without removing the
core session model:

- sweep and MSS must remain in the same configured ICT session;
- displacement must remain `strong`;
- the first eligible FVG that retests within `3` bars may be selected;
- the retest may occur after the session window;
- target-reached-before-retest cancellation remains enabled.

This was research-only. Live and paper profiles were not enabled.

## Frequency Gate

The bounded funnel used BTCUSDT and ETHUSDT `30m`.

| Period | Candidate scan rows |
| --- | ---: |
| OOS `2022-01-01..2024-11-05` | 232 |
| Late control `2024-11-06..2026-04-20` | 173 |

The session fallback fixed the prior zero-frequency construction failure, so a
costed event study was justified.

## Replay Optimization

Single-model ICT2022 replay previously calculated every accumulated primitive,
including IFVG, order blocks, volume, PD zones, and other fields unused by this
detector.

`ReplaySnapshotCache` now accepts an optional primitive-field set. A
single-model ICT2022 run accumulates only:

- sweeps;
- liquidity raids;
- structure breaks;
- FVGs.

The Q1 2025 BTC/ETH `30m` equivalence check produced the same `11` events and
matching key trade fields before and after the optimization. Runtime fell from
about `145` seconds to `66` seconds.

## Costed Results

Config:

`configs/backtests/crypto_ict2022_first_retested_fvg_session_fallback_validation.json`

Costs include `4` bps commission, `1` bps slippage, and Binance funding.

### Raw events

| Period | Trades | Win rate | Expectancy | PF | Max DD |
| --- | ---: | ---: | ---: | ---: | ---: |
| OOS | 59 | 33.90% | -0.467808R | 0.230369 | 28.220504R |
| Late control | 47 | 38.30% | -0.425013R | 0.277305 | 20.096803R |

### Model rules

Model rules require `strong` displacement and target distance of at least
`2R`.

| Period | Trades | Win rate | Expectancy | PF | Max DD |
| --- | ---: | ---: | ---: | ---: | ---: |
| OOS | 23 | 21.74% | -0.640915R | 0.222297 | 15.150984R |
| Late control | 12 | 16.67% | -0.729520R | 0.165284 | 10.214399R |

Gross managed expectancy was also negative:

- OOS: `-0.666324R`;
- late control: `-0.682631R`.

Costs are not the primary cause of failure.

## Decision

Reject this ICT2022 first-retested-FVG session-fallback variant.

- It solved candidate frequency but exposed strongly negative realized edge.
- The `RR>=2` model rule reduced sample and worsened expectancy.
- OOS and independent late control agree on the direction of failure.
- Do not relax killzone, same-session, displacement, or target-cancellation
  rules further to rescue this branch.
- Keep `ict2022_mss_fvg` disabled for live and paper use.

If FVG research continues, evaluate the separate `ifvg_retest` model as a new
predeclared branch rather than tuning this rejected ICT2022 construction.
