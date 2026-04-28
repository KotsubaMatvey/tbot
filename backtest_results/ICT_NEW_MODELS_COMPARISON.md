# ICT New Models Quality Comparison

Event-study report after fixing setup timestamp alignment, explicit entry prices, 1R/2R hit metrics, Turtle Soup quality filters, and Silver Bullet retest-window constraints.
This is not a profitability report.

## 1. Migration / Current State

- Old Entry Model 1/2/3 remain archived in `strategies/legacy/`.
- New ICT registry remains active in `strategies/ict_models/registry.py`.
- Default active models remain `turtle_soup`, `silver_bullet`, and `ifvg_retest`.
- New runner remains `backtesting.run_ict_models`.

## 2. Alignment And Outcome Rules

- Event-study rows are aligned by `setup_timestamp`, which is the model confirmation timestamp.
- `entry_time` is stored separately when the actual entry/retest happens later.
- Forward event windows start after `setup_timestamp`.
- R-based outcomes start from `entry_time`.
- `hit_1r_before_invalidation` and `hit_2r_before_invalidation` are calculated from explicit `entry_price` and initial `stop_loss`.
- Same-bar default is conservative: if target and invalidation are touched in the same OHLC bar, invalidation is counted first.

## 3. Backtest Configs

Smoke:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT --timeframes 5m 15m --models turtle_soup silver_bullet ifvg_retest --same-bar-policy conservative --context-mode off --forward-bars 20 --out-dir backtest_results/smoke_new_ict_models_quality
```

Main off-context:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 30m 1h 4h --models turtle_soup silver_bullet ifvg_retest ict2022_mss_fvg breaker_block reclaimed_ob --same-bar-policy conservative --context-mode off --forward-bars 20 --out-dir backtest_results/new_ict_models_quality_off
```

Aligned-context:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 30m 1h 4h --models turtle_soup silver_bullet ifvg_retest ict2022_mss_fvg breaker_block reclaimed_ob --same-bar-policy conservative --context-mode aligned_only --forward-bars 20 --out-dir backtest_results/new_ict_models_quality_aligned
```

Focused IFVG:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 5m 15m 30m 1h --models ifvg_retest --entry-mode edge --stop-mode ce --target-mode fixed_r --same-bar-policy conservative --forward-bars 20 --out-dir backtest_results/ifvg_retest_quality_edge_ce
```

Focused Silver Bullet:

```bash
python -m backtesting.run_ict_models --data-dir data/history --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m --models silver_bullet --same-bar-policy conservative --forward-bars 20 --out-dir backtest_results/silver_bullet_quality_ny_10
```

## 4. Main Off-Context Comparison

| Model | Setups | Activated | Invalid Before Entry | Win Rate | Hit 1R Before Inv. | Hit 2R Before Inv. | Invalidation | Median MFE R | Expectancy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `breaker_block` | 933 | 741 | 167 | 56.81% | 56.27% | 46.41% | 21.76% | 8.18 | 0.82 |
| `ifvg_retest` | 2172 | 2160 | 0 | 28.31% | 37.80% | 28.31% | 69.61% | 7.22 | -0.11 |
| `reclaimed_ob` | 158 | 150 | 8 | 79.11% | 72.78% | 61.39% | 15.82% | 5.77 | 1.13 |
| `silver_bullet` | 91 | 91 | 0 | 12.09% | 34.07% | 12.09% | 53.85% | 0.88 | -0.00 |
| `turtle_soup` | 11267 | 11267 | 0 | 15.59% | 46.75% | 29.51% | 72.00% | 2.55 | 0.26 |

Total main off-context events: 14,621.

## 5. Aligned-Context Comparison

| Model | Setups | Activated | Invalid Before Entry | Win Rate | Hit 1R Before Inv. | Hit 2R Before Inv. | Invalidation | Median MFE R | Expectancy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `breaker_block` | 98 | 62 | 29 | 43.88% | 38.78% | 26.53% | 16.33% | 4.36 | 0.48 |
| `ict2022_mss_fvg` | 72 | 72 | 0 | 76.39% | 31.94% | 13.89% | 12.50% | 1.21 | 0.25 |
| `ifvg_retest` | 351 | 351 | 0 | 28.21% | 39.60% | 28.21% | 69.52% | 6.73 | -0.10 |
| `reclaimed_ob` | 20 | 19 | 1 | 75.00% | 70.00% | 40.00% | 20.00% | 3.56 | 0.64 |
| `silver_bullet` | 35 | 35 | 0 | 14.29% | 34.29% | 14.29% | 42.86% | 0.84 | 0.21 |
| `turtle_soup` | 1550 | 1550 | 0 | 14.39% | 46.39% | 28.06% | 74.00% | 2.34 | 0.20 |

Total aligned-context events: 2,126.

## 6. Focused Runs

IFVG edge + CE stop:

- Events: 1,384.
- Activated: 1,377.
- Win rate: 29.26%.
- Hit 1R before invalidation: 35.84%.
- Hit 2R before invalidation: 29.26%.
- Invalidation rate: 70.01%.
- Median MFE R: 10.35.

Silver Bullet NY 10:00-11:00:

- Events: 60.
- Activated: 60.
- Win rate: 10.00%.
- Hit 1R before invalidation: 23.33%.
- Hit 2R before invalidation: 10.00%.
- Invalidation rate: 48.33%.
- Median MFE R: 0.68.

## 7. Turtle Soup Quality Filter Impact

The new default quality filters reduced main off-context Turtle Soup events from the previous 15,874 to 11,267.

Remaining Turtle Soup quality buckets:

| Quality | Events | Win Rate | Hit 1R Before Inv. | Hit 2R Before Inv. | Invalidation | Median MFE R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| strong | 5,767 | 16.49% | 48.17% | 29.20% | 69.26% | 2.23 |
| valid | 5,500 | 14.65% | 45.25% | 29.84% | 74.87% | 2.97 |

## 8. Silver Bullet Retest Constraint Impact

Silver Bullet now requires:

- FVG creation inside the configured NY window.
- Retest within `silver_bullet_max_retest_bars`.
- Retest inside the same configured window by default.

The focused 1m/5m event count moved from the prior 70 to 60 after the retest-window constraint.

## 9. Ranking Notes

- `reclaimed_ob` has the best off-context win-rate and 2R-before-invalidation rate, but sample size is small.
- `breaker_block` remains the strongest larger-sample model in this pass.
- `ifvg_retest` still shows large MFE tails but high invalidation rate, so entry/stop policy needs more work.
- `turtle_soup` remains broad and noisy even after filters; quality filtering helped event count but not enough to call it clean.
- `silver_bullet` remains narrow; sample size is too small to rank confidently.

## 10. Problems Found

- The previous new ICT runner aligned forward outcome from the replay scan index, not always from `setup.timestamp`.
- IFVG/Silver/Breaker style setups used retest time as event timestamp, which biased event-study alignment later than model confirmation.
- The new runner did not expose `hit_1r_before_invalidation` or `hit_2r_before_invalidation`.
- Silver Bullet allowed late retests before the new retest-window gate.
- Chart labels used opaque backgrounds that could cover candles.

## 11. Recommended Next Actions

1. Add neutral and optimistic same-bar sensitivity runs.
2. Add a dedicated event-study export around `setup_timestamp` with pre-event and post-event normalized returns.
3. Split Breaker/Reclaimed OB activation logic into setup-created, entry-activated, and invalid-before-entry cohorts.
4. Continue tightening Turtle Soup with liquidity significance and optional killzone/SMT experiments, but keep them off by default.
