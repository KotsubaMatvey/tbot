# Turtle Soup SMT-On-Sweep Validation - 2026-05-25

## Hypothesis

For crypto Turtle Soup, the existing specification requires SMT confirmation
for a live candidate. It further states that confirmation applies at the
liquidity sweep. Therefore an Asian-range reclaim should not qualify merely
because a directional SMT divergence occurred several bars earlier.

This is a rules-correctness hypothesis, not a profitability claim.

## Defect Found

The Asian-range detector branch ignored `turtle_soup_require_smt`. A
before-change reproduction using the same BTC 30m Q1 2025 command with and
without `--turtle-soup-require-smt` generated identical `events.csv` hashes and
the same `20` events.

The existing non-Asian Turtle Soup SMT check also accepted any SMT direction
before building a directional setup.

## Changes

- Require directional SMT when `turtle_soup_require_smt=true`:
  - bullish SMT for a long setup;
  - bearish SMT for a short setup.
- Add optional `turtle_soup_require_smt_on_sweep=true`, requiring the selected
  directional SMT timestamp to equal the swept-liquidity candle timestamp.
- Apply these checks to standard, confirmed, and Asian-range Turtle Soup paths.
- Export `smt_timestamp` in event CSVs for auditability.
- Add repeatable costed preset:
  `configs/backtests/asian_turtle_smt_on_sweep_validation.json`.

The temporal gate is applied to the BTC research profile where BTC is the
primary symbol of `BTCUSDT:ETHUSDT`. It is not silently imposed on all
secondary-symbol research because the current SMT event schema stores the
primary swing timestamp.

## Costed Validation

Execution assumptions:

- commission: `4 bps` per side
- slippage/spread: `1 bps` per side
- target model: existing `fixed_r` Asian-range research profile
- no newly selected performance filters

Command:

```powershell
python -m backtesting.run_ict_batch --config configs\backtests\asian_turtle_smt_on_sweep_validation.json
```

Results:

| Dataset | Activated trades | Net managed expectancy | Profit factor | Walk-forward |
| --- | ---: | ---: | ---: | --- |
| BTC 30m, 2025 | 6 | `+0.413177R` | `2.576671` | failed |
| BTC 30m, 2024-11-06 through 2026-04-20 | 7 | `+0.540621R` | `3.406826` | failed |

Extended phase results:

| Phase | Trades | Net managed expectancy | Profit factor | Result |
| --- | ---: | ---: | ---: | --- |
| Train | 2 | `+0.510664R` | `4.596773` | fails sample size |
| Validation | 2 | `+1.299236R` | `inf` | fails sample size |
| Test | 3 | `+0.054849R` | `1.127717` | fails expectancy, PF, and sample size |

The variant is materially cleaner than the ungated Asian-range profile, but
seven trades cannot establish durable expectancy or justify live trading.

## Decision

Keep `turtle_soup` disabled in live scanning. Preserve SMT-on-sweep as the
current research candidate, expand truly out-of-sample coverage and/or
forward logging, and require it to pass the existing costed gates before any
activation.

The live scanner also needs paired-symbol SMT context before this model could
produce a correctly validated live signal.
