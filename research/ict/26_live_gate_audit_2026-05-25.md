# Live Model Gate Audit - 2026-05-25

## Goal And Assumption

The bot must not issue live strategy signals until the corresponding model has
positive costed out-of-sample evidence and passes the configured walk-forward
gates. This does not guarantee future profit; it prevents deployment of models
that have already failed or have not produced a sufficient validation sample.

Quality gates from `configs/ict_quality_gates.json`:

- minimum total trades: `30`
- minimum trades per phase: `10`
- minimum net managed expectancy: `0.3R`
- minimum profit factor: `1.3`
- maximum drawdown: `8R`
- maximum trades per session: `1`

Execution-cost assumption:

- commission: `4 bps` per side
- slippage/spread estimate: `1 bps` per side

## Pre-Change Live Audit

`silver_bullet` was already disabled in the preceding audit after its costed
BTC 15m walk-forward validation failed.

The remaining live-enabled strategies were evaluated by applying their live
filters to saved costed validation artifacts before disabling them:

| Model | Validation artifact | Live-filter result | Evidence |
| --- | --- | --- | --- |
| `ifvg_retest` | `probe_costed_2025_4h_ifvg_reclaimed/events.csv` | `1` activated BTC trade | net managed expectancy `-1.164073R` |
| `reclaimed_ob` | `probe_costed_2025_4h_ifvg_reclaimed/events.csv` | `1` activated BTC trade | net managed expectancy `-0.001597R` |
| `breaker_block` | `probe_costed_2025_btc_1h_core_models/events.csv` | `0` activated trades after live filters | insufficient validation sample |
| `breaker_block` | `breaker_research_may_oct_2025_30m_btc/events.csv` | `0` events after live filters | insufficient validation sample |

The combined `4h` active-live candidate report selected `3` events, activated
`2`, and produced net managed expectancy `-0.582835R` with profit factor `0.0`.
Its walk-forward report failed all required profitability/sample gates.

The `1h` active-live candidate report selected one non-activated event and also
failed the gates. The available `30m` breaker artifact selected no events.

An additional strict BTC `4h` run on the extended
`2024-11-06` through `2026-04-20` dataset produced no candidate events, so it
does not provide contrary evidence for live approval.

## Decision

Disable `ifvg_retest`, `breaker_block`, and `reclaimed_ob` in live scanning,
along with the already-disabled `silver_bullet`, `ict2022_mss_fvg`, and
`turtle_soup`.

All detectors remain available for backtest and research. A strategy may be
re-enabled only after its revised, documented rules pass costed walk-forward
validation on an adequate out-of-sample dataset.
