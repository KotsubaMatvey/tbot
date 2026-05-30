# ICT Source-Aligned Turtle Refinement - 2026-05-29

## Source Handling

Reviewed the official ICT YouTube channel entry point:

- `https://www.youtube.com/@InnerCircleTrader`

The browser tool did not expose machine-readable transcripts, so no new rule was
implemented from an unverifiable quote. The implementation direction was cross-
checked against the existing project ICT synthesis in
`research/ict/21_notebooklm_answers_spec.md`:

- Turtle Soup requires a liquidity sweep, quick rejection, close back inside the
  prior range, crypto SMT confirmation, stop beyond sweep wick, TP1/internal
  liquidity, and final opposing external liquidity.
- HTF/DOL context remains mandatory conceptually, but strict HTF gates have
  historically collapsed crypto sample size and must remain research-only until
  costed validation proves otherwise.

## Code Changes

Added DOL-quality filter primitives in `strategies/ict_models/model_filters.py`:

- `allowed_dol_target_types`
- `allowed_dol_sources`
- `allowed_target_models`
- `max_dol_priority`

These let reports and future live gates distinguish source-aligned liquidity
targets (`clean_equal_highs/lows`, `external_swing_high/low`) from weak fallback
targets without hard-coding model-specific logic.

Extended `backtesting/exit_policy_audit.py` with ICT attribute buckets:

- `dol_target_type`
- `turtle_quality`
- `ny_hour`

Added repeatable research preset:

- `configs/backtests/asian_turtle_full1r_research.json`

This preset tests the best current Turtle candidate:

- BTCUSDT `1h`
- Asian range sweep/reclaim
- directional SMT on the sweep candle
- `dol_hierarchy` target
- full close at `1R`
- commission `4 bps`, slippage `1 bps`
- OOS, control, and full 2022-2026 runs

## Validation Results

Command:

```powershell
python -m backtesting.run_ict_batch --config configs\backtests\asian_turtle_full1r_research.json
```

| Run | Trades | Net expectancy | PF | Walk-forward |
| --- | ---: | ---: | ---: | --- |
| OOS 2022-2024 | 40 | `+0.259288R` | `1.994182` | fail: train/test expectancy |
| Control 2024-2026 | 18 | `+0.446259R` | `4.594118` | fail: sample size |
| Full 2022-2026 | 58 | `+0.317314R` | `2.452905` | fail: validation expectancy |

Full run phases:

| Phase | Trades | Net expectancy | PF | Passed |
| --- | ---: | ---: | ---: | --- |
| train | 19 | `+0.347927R` | `2.417764` | yes |
| validation | 19 | `+0.124728R` | `1.410752` | no |
| test | 20 | `+0.471187R` | `5.216536` | yes |

## Diagnosis

The source-aligned full-1R Turtle profile is materially better than the prior
partial-exit profile, but still not robust enough:

1. The full 2022-2026 aggregate passes total sample, PF, drawdown, and overtrade
   constraints, but fails the validation phase expectancy gate.
2. The late control period is positive but too thin at `18` trades.
3. No simple ICT attribute bucket is stable enough across phases to justify a
   hard live filter today:
   - `turtle_quality=strong` helps OOS but is not stable in control.
   - `ny_hour` shifts by regime.
   - `dol_target_type` remains useful for reporting but not sufficient alone.

## Decision

Do not enable live trading.

Keep the new Turtle full-1R profile as the leading research candidate. The next
algorithmic work should target validation-phase weakness, not further optimize
the already-positive train/test periods.

Immediate next experiments:

1. Test a candle-level "hang at swept level" rejection metric for Turtle Soup:
   reject if price spends more than three candles around the swept level before
   acceptance/rejection is clear.
2. Test a lower-cost or wider-stop variant only if it does not reduce sample
   below validation gates.
3. Revisit HTF/DOL context with a soft scoring gate instead of a hard
   `context_mode=strict` gate.

Verification:

- `python -m unittest tests.test_new_ict_models.NewICTModelTests.test_live_model_filter_event_uses_setup_rr tests.test_new_ict_models.NewICTModelTests.test_exit_policy_audit_estimates_costed_1r_and_2r_policies` passed.
