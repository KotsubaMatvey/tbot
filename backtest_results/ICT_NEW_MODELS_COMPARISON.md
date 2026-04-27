# ICT New Models Comparison

Event-study report for the migration from archived Entry Model 1/2/3 to the new ICT model registry.
This is not a profitability report and does not include execution assumptions beyond the configured forward-bar outcome scan.

## 1. Migration Summary

- Old Entry Model 1/2/3 code is archived in `strategies/legacy/`.
- Old models are disabled by default and are not part of the active ICT registry defaults.
- Legacy models can only be resolved through legacy names with `include_legacy=True`.
- New active registry lives in `strategies/ict_models/registry.py`.
- Default active models are `turtle_soup`, `silver_bullet`, and `ifvg_retest`.
- The old `backtesting.run_entry_models` runner is legacy-only and requires `--include-legacy` to run archived model1/model2/model3.
- New event-study runner is `backtesting.run_ict_models`.

## 2. New Model List

Active ICT models:

- `turtle_soup`: liquidity sweep and close-back model.
- `silver_bullet`: NY 10:00-11:00 FVG/retrace model.
- `ifvg_retest`: pure IFVG first retest model with edge entry default.
- `ict2022_mss_fvg`: simplified sweep, MSS, displacement, FVG model.
- `breaker_block`: conservative failed OB retest model.
- `reclaimed_ob`: conservative validated OB retest model.

Research-only:

- `rejection_block`: disabled by default, returns no setups in the current conservative skeleton.

Archived legacy:

- `legacy_model1`
- `legacy_model2`
- `legacy_model3`

## 3. Backtest Configs

Smoke:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT --timeframes 5m 15m --models turtle_soup silver_bullet ifvg_retest --same-bar-policy conservative --context-mode off --forward-bars 20 --out-dir backtest_results/smoke_new_ict_models
```

Main off-context:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 30m 1h 4h --models turtle_soup silver_bullet ifvg_retest ict2022_mss_fvg breaker_block reclaimed_ob --same-bar-policy conservative --context-mode off --forward-bars 20 --out-dir backtest_results/new_ict_models_off
```

Aligned-context:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 30m 1h 4h --models turtle_soup silver_bullet ifvg_retest ict2022_mss_fvg breaker_block reclaimed_ob --same-bar-policy conservative --context-mode aligned_only --forward-bars 20 --out-dir backtest_results/new_ict_models_aligned
```

Focused IFVG:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 5m 15m 30m 1h --models ifvg_retest --entry-mode edge --stop-mode ce --target-mode fixed_r --same-bar-policy conservative --forward-bars 20 --out-dir backtest_results/ifvg_retest_edge_ce
```

Focused Silver Bullet:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m --models silver_bullet --same-bar-policy conservative --forward-bars 20 --out-dir backtest_results/silver_bullet_ny_10
```

## 4. Overall Comparison

Main off-context, conservative same-bar policy:

| Model | Events | Avg MFE R | Median MFE R | Target Before Invalidation | Invalidation Rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| `breaker_block` | 4032 | 10.05 | 5.18 | 44.44% | 55.31% |
| `ifvg_retest` | 2172 | 18.09 | 7.13 | 35.82% | 63.58% |
| `reclaimed_ob` | 234 | 11.09 | 4.75 | 63.68% | 36.32% |
| `silver_bullet` | 167 | 3.10 | 1.06 | 23.95% | 52.10% |
| `turtle_soup` | 15874 | 5.12 | 2.86 | 16.01% | 72.25% |

Aligned-context, conservative same-bar policy:

| Model | Events | Avg MFE R | Median MFE R | Target Before Invalidation | Invalidation Rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| `breaker_block` | 379 | 7.01 | 3.38 | 41.42% | 58.31% |
| `ict2022_mss_fvg` | 72 | 2.22 | 1.08 | 63.89% | 23.61% |
| `ifvg_retest` | 351 | 14.36 | 6.66 | 37.04% | 61.82% |
| `reclaimed_ob` | 27 | 4.27 | 2.40 | 70.37% | 29.63% |
| `silver_bullet` | 50 | 2.86 | 0.77 | 30.00% | 36.00% |
| `turtle_soup` | 2200 | 4.75 | 2.64 | 15.14% | 74.27% |

## 5. Simple Model Ranking

By target-before-invalidation in the main off-context run:

1. `reclaimed_ob`: 63.68%, but only 234 events.
2. `breaker_block`: 44.44%, 4032 events.
3. `ifvg_retest`: 35.82%, 2172 events.
4. `silver_bullet`: 23.95%, 167 events.
5. `turtle_soup`: 16.01%, 15874 events.

By median MFE R in the main off-context run:

1. `ifvg_retest`: 7.13 R.
2. `breaker_block`: 5.18 R.
3. `reclaimed_ob`: 4.75 R.
4. `turtle_soup`: 2.86 R.
5. `silver_bullet`: 1.06 R.

## 6. Time / Session Analysis

- `silver_bullet` is the only model with a session window in the current implementation: `10:00-11:00` New York.
- Main off-context `silver_bullet`: 167 events, 23.95% target-before-invalidation, 52.10% invalidation.
- Focused 1m/5m `silver_bullet`: 70 events, 20.00% target-before-invalidation, 47.14% invalidation.
- Other models are currently session-agnostic and record `session_window=none`.

## 7. Entry Mode Analysis

Main off-context defaults:

- `turtle_soup`: `close` entry.
- `silver_bullet`: `edge` entry.
- `ifvg_retest`: `edge` entry.
- `breaker_block`: `edge` entry.
- `reclaimed_ob`: `body_edge` entry.

Focused IFVG `edge` + `ce` stop + fixed-R target:

- 1384 events.
- Avg MFE R: 19.49.
- Median MFE R: 10.46.
- Target-before-invalidation: 38.01%.
- Invalidation: 61.85%.

## 8. Stop Mode Analysis

Main off-context defaults:

- `turtle_soup`: `sweep_extreme`.
- `silver_bullet`: `swing_or_fvg`.
- `ifvg_retest`: `ce`.
- `breaker_block`: `mean_threshold`.
- `reclaimed_ob`: `mean_threshold`.

No stop-mode optimization was run. The first pass validates serialization and conservative event-study behavior only.

## 9. Same-Bar Conservative Impact

- All completed runs used `same_bar_policy=conservative`.
- `same_bar_ambiguous_count` was 0 in these runs because the conservative policy resolves same-bar target/stop collisions as invalidation-first.
- The runner also supports `neutral` and `optimistic` policies for future sensitivity checks.

## 10. Models Recommended To Keep

- Keep `ifvg_retest` as a default active model. It produced broad sample size and high MFE distribution, but still needs risk/invalidation refinement.
- Keep `turtle_soup` as a default active model for coverage and liquidity-sweep discovery, but it needs quality filters because invalidation is high.
- Keep `silver_bullet` as a default active model because it is intentionally narrow and session-specific, but current event count is small.
- Keep `breaker_block` in active research/backtest rotation because the initial sample is large enough and target-before-invalidation is competitive.

## 11. Models Recommended For Research Only

- `reclaimed_ob` should remain in research rotation until sample size increases.
- `ict2022_mss_fvg` should remain in research rotation because it only produced events under aligned context in this pass.
- `rejection_block` remains research-only and disabled by default.

## 12. Legacy Comparison

Legacy Entry Model 1/2/3 were not run in this migration pass. They are archived and available for a future explicit comparison via legacy names and `--include-legacy`.

## Problems Found

- `turtle_soup` is noisy in the first simple implementation: high event count and high invalidation rate.
- `silver_bullet` needs more sample size before ranking it against broader models.
- `ict2022_mss_fvg` is too restrictive off-context in the current implementation and produced no off-context row.
- `reclaimed_ob` looks promising on target-before-invalidation, but the sample is too small to treat as stable.

## Recommended Next Actions

1. Run neutral and optimistic same-bar sensitivity checks for the same output matrix.
2. Add quality summaries for sweep age, IFVG retest depth, breaker freshness, and OB retest count.
3. Compare archived legacy models only through `--include-legacy` after validating the new registry baseline.
4. Refine Turtle Soup with swing significance and equal-liquidity quality before treating it as a ranked signal.
