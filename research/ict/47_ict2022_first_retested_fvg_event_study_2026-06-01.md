# ICT2022 First-Retested FVG Event Study - 2026-06-01

## Goal

Continue the ICT2022 repair pass after any-FVG attribution showed that
`first_after_mss` can collapse sample under relaxed research settings.

This pass makes the event-study runner able to test a predeclared
`first_retested_after_mss` variant. It remains research-only and does not
change live configuration.

## Problems Found And Fixed

### Event-study did not match diagnostic snapshots

`backtesting/ict2022_diagnostic_report.py` used accumulated primitive
snapshots. `backtesting/run_ict_models.py` only built accumulated context when
`context_mode` was not `off`. For `context_mode=off`, ICT2022 fell back to a
fresh visible-window snapshot, so the event-study runner returned zero events
while the diagnostic reported candidates.

Fix:

- `run_ict_models.py` now builds a `StrategyContext` with accumulated primary
  primitives when a model needs accumulated primary, even if HTF context is
  off.

### Bounded replay started at the beginning of multi-year history

After accumulated primary was enabled for `context_mode=off`, even a
three-day replay initially timed out because the accumulator began processing
from the start of the 2022-2026 file.

Fix:

- `backtesting/accumulator.py` accepts a start index for replay accumulation.
- `backtesting/run_ict_models.py` adds `--seed-bars`, default `1500`, and
  starts accumulated primary at `start_idx - seed_bars`.
- `backtesting/run_ict_batch.py` forwards `seed_bars` from batch configs.

## Research Variant

Added explicit ICT2022 config/CLI support:

- `ict2022_fvg_selection = first_after_mss` keeps existing default behavior.
- `ict2022_fvg_selection = first_retested_after_mss` is a research-only mode
  that scans eligible subsequent FVGs after MSS and selects the first one that
  passes retest/session/target-open checks.

Added bounded preset:

`configs/backtests/crypto_ict2022_first_retested_fvg_research.json`

This preset intentionally disables killzone and same-session gates. It is
measuring the construction bottleneck, not a live-ready setup.

## Verification

Passed:

```powershell
python -m unittest
python -m compileall .
python offline_smoke_test.py
python offline_backtest.py
git diff --check
```

`git diff --check` produced only Windows CRLF warnings.

Runtime checks:

```powershell
python -m backtesting.run_ict_models --data-dir data/history_crypto_2022-01-01_2026-04-20 --funding-data-dir data/history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT --timeframes 30m --models ict2022_mss_fvg --context-mode off --out-dir backtest_results\ict2022_first_retested_fvg_smoke_2024_01_01_03_btc_30m --start-date 2024-01-01 --end-date 2024-01-03 --warmup-bars 150 --seed-bars 1500 --forward-bars 32 --commission-bps 4 --slippage-bps 1 --entry-mode edge --ict2022-fvg-selection first_retested_after_mss --ict2022-max-fvg-retest-bars 20 --no-ict2022-require-killzone --no-ict2022-require-same-session --no-ict2022-require-strong-displacement --no-ict2022-retest-must-occur-within-session --scan-session-windows 02:00-05:00,07:00-10:00,13:30-16:00 --scan-session-lag-bars 0 --no-pre-model-filter --no-pre-model-require-htf-poi
```

Result: completed in about 22 seconds with `2` events.

```powershell
python -m backtesting.run_ict_batch --config configs/backtests/crypto_ict2022_first_retested_fvg_research.json
```

Result: completed in about 81.5 seconds.

## Bounded Trade-Level Results

| Run | Trades | Sample valid | Win rate | Avg realized RR | Expectancy | Profit factor | Max DD |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Jan 2024 BTCUSDT 30m no-killzone | 11 | false | 72.727273% | 0.063057R | 0.063057R | 1.20846 | 2.173221R |
| Jan 2025 BTCUSDT 30m no-killzone | 4 | false | 50.0% | 0.20695R | 0.20695R | 1.400552 | 1.034291R |

## Decision

The code path now works and is reproducible, but the research variant is not a
live candidate:

- both bounded samples are far below the `30`-trade research minimum, and far
  below the user's preferred `100`-trade meaningful sample;
- the run only produces trades after disabling strict session constraints;
- positive expectancy in 4-11 trades is not evidence of durable edge.

Next useful work is either performance-optimized full OOS/control evaluation
of this research variant or a stricter source-aligned session model that can
recover enough sample without disabling the core time filter.
