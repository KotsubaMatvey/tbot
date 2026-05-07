# Session Handoff - 2026-05-06

Use this file as the first read in the next session. It captures the current state after the ICT model-improvement work and the quality-gate infrastructure pass.

## User Goal

Build ICT-based models until at least one intraday setup can be traded inside a session, ICT-style. The current practical target is not a guaranteed profit claim, but an evidence-backed model that passes strict walk-forward quality gates after realistic execution costs.

## Core ICT Rules In Force

- Main intraday focus: Silver Bullet in NY time.
- Silver Bullet windows: `10:00-11:00` and `14:00-15:00`.
- HTF draw on liquidity is required.
- Bias alignment is required.
- Premium/discount alignment is required.
- HTF context alignment must be `aligned`.
- Live expansion to ETH/SOL is blocked until separate validation is positive.
- ICT2022 retest may occur after the sweep/MSS session, but only if target was not reached before retest/entry.
- Turtle Soup and ICT2022 remain research/disabled until they produce positive expectancy under the same gates.

## Current Live Candidate

Only one live-like intraday candidate currently survives:

- Model: `silver_bullet`
- Symbol: `BTCUSDT`
- Timeframe: `15m`
- Windows: `10:00-11:00`, `14:00-15:00` NY
- Filters: HTF draw, bias alignment, premium/discount alignment, `htf_context_alignment=aligned`, target >= 2R, session window required.

Live config:

- `configs/live_model_filters_2025.json`
- Enabled models are restricted to `allowed_symbols: ["BTCUSDT"]`.
- `ict2022_mss_fvg` and `turtle_soup` are disabled.

## Important Code Changes

- `strategies/ict_models/ict2022_mss_fvg.py`
  - Supports configurable session windows including London, NY Open, NY PM.
  - Allows retest outside the sweep/MSS session when configured.
  - Skips setup if target was reached before FVG retest/entry.
  - Adds metadata: `target_reached_before_entry_policy=skip_before_retest`.

- `configs/live_model_filters_2025.json`
  - Silver Bullet enabled only for `BTCUSDT` on `15m`.
  - IFVG, Breaker, Reclaimed OB enabled only for `BTCUSDT`, mostly higher timeframe.
  - ICT2022 and Turtle Soup disabled but prepared.

- `backtesting/run_ict_models.py`
  - Adds execution costs:
    - `--commission-bps`
    - `--slippage-bps`
    - `commission_bps`
    - `slippage_bps`
    - `round_trip_cost_bps`
    - `execution_cost_r`
    - `gross_managed_outcome_r`
    - `net_managed_outcome_r`
  - Adds date-window scanning:
    - `--start-date`
    - `--end-date`

- `backtesting/score_threshold_report.py`
  - Uses net managed outcome when available.
  - Reports gross managed expectancy, net managed expectancy, average execution cost, and profit factor.

- `backtesting/grid_filter_analysis.py`
  - Uses net managed outcome when available.
  - Reports gross managed expectancy and profit factor.

- `backtesting/walk_forward_report.py`
  - New quality gate report.
  - Gates: min total trades, min phase trades, min managed expectancy, min profit factor, max drawdown, max trades per session.

- `backtesting/data_coverage_report.py`
  - New data coverage audit for symbol/timeframe history files.

- `backtesting/forward_log_report.py`
  - New paper/live log analyzer.
  - Checks fill rate, average slippage, and net outcome.

- `configs/ict_quality_gates.json`
  - Central quality criteria:
    - commission: `4.0 bps` per side
    - slippage: `1.0 bps` per side
    - min total trades: `30`
    - min phase trades: `10`
    - min managed expectancy: `0.3R`
    - min profit factor: `1.3`
    - max drawdown: `8R`
    - max trades per session: `1`
    - desired data range: `2024-01-01` to `2026-04-30`

## Latest Verification

Unit tests:

```powershell
python -m unittest discover
```

Result:

- `91` tests passed.

Costed BTC Silver Bullet smoke:

```powershell
python -m backtesting.run_ict_models --data-dir data/history_2025-05-01_2025-06-30 --symbols BTCUSDT --timeframes 15m --models silver_bullet --context-mode strict --forward-bars 32 --warmup-bars 100 --scan-session-windows 10:00-11:00,14:00-15:00 --scan-session-lag-bars 1 --silver-bullet-windows 10:00-11:00,14:00-15:00 --silver-bullet-max-retest-bars 1 --silver-bullet-min-retest-depth 0.15 --silver-bullet-retest-must-occur-within-window --commission-bps 4 --slippage-bps 1 --out-dir backtest_results/silver_bullet_live_like_costed_may_jun_2025_btc_15m
```

Result:

- `events=1`
- gross managed outcome: `+1.5R`
- execution cost: `0.14704R`
- net managed outcome: `+1.35296R`

Score report:

```powershell
python -m backtesting.score_threshold_report --events backtest_results\silver_bullet_live_like_costed_may_jun_2025_btc_15m\events.csv --thresholds 0 70 --model-filters configs\live_model_filters_2025.json
```

Result:

- filtered Silver Bullet count: `1`
- net managed expectancy: `+1.35296R`

Walk-forward gate:

```powershell
python -m backtesting.walk_forward_report --events backtest_results\silver_bullet_live_like_costed_may_jun_2025_btc_15m\events.csv --threshold 70 --model-filters configs\live_model_filters_2025.json --min-total-trades 30 --min-phase-trades 10 --min-managed-expectancy-r 0.3 --min-profit-factor 1.3 --max-drawdown-r 8 --max-trades-per-session 1
```

Result:

- `passed=False`
- failed gates: `min_total_trades;min_phase_trades`

This is expected and correct. The model has a positive costed smoke result but does not yet have enough sample size for final approval.

Data coverage audit for May-Jun 2025:

```powershell
python -m backtesting.data_coverage_report --data-dir data/history_2025-05-01_2025-06-30 --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 1h 4h 1d --required-start 2025-05-01 --required-end 2025-06-30 --min-coverage-pct 95 --max-gap-bars 3 --out-dir backtest_results/data_coverage_may_jun_2025
```

Result:

- `passed=True`
- 18/18 symbol-timeframe files passed.

## Backtest Artifacts To Reuse

- `backtest_results/silver_bullet_live_like_costed_may_jun_2025_btc_15m/`
- `backtest_results/data_coverage_may_jun_2025/`
- `backtest_results/silver_bullet_notebooklm_am_pm_htf_poi_quality_gates_may_jun_2025_multi_15m/`
- `backtest_results/ict2022_notebooklm_retest_later_no_poi_smoke_may_jun_2025_btc_15m/`

## Known Findings

- BTC Silver Bullet has a valid positive smoke result after costs, but sample size is too small.
- ETH/SOL Silver Bullet May-Jun multi-symbol expansion was negative after live-like filters before the BTC-only restriction.
- ICT2022 remains very rare. BTC 15m May-Jun with late retest allowed still produced `events=0`.
- Turtle Soup remains disabled/research because previous session tests did not show positive expectancy.
- Long BTC May-Oct run timed out before producing a result. Use `--start-date/--end-date` chunks next time.

## What Is Needed From User Later

Not blocking for code work, but needed for final approval:

- Historical data for 2024-2026, ideally BTC/ETH/SOL on `1m`, `5m`, `15m`, `1h`, `4h`, `1d`.
- Paper/live logs CSV with at least:
  - `model`
  - `symbol`
  - `status`
  - `slippage_bps`
  - `net_outcome_r`

## Next Session Plan

1. Run data coverage audit for the largest available data folder:

```powershell
python -m backtesting.data_coverage_report --data-dir data/history_2025-01-01_2025-12-31 --symbols BTCUSDT ETHUSDT SOLUSDT --timeframes 1m 5m 15m 1h 4h 1d --required-start 2025-01-01 --required-end 2025-12-31 --min-coverage-pct 95 --max-gap-bars 3 --out-dir backtest_results/data_coverage_2025
```

2. Run BTC Silver Bullet in date chunks to avoid timeout:

```powershell
python -m backtesting.run_ict_models --data-dir data/history_2025-01-01_2025-12-31 --symbols BTCUSDT --timeframes 15m --models silver_bullet --context-mode strict --forward-bars 32 --warmup-bars 100 --start-date 2025-01-01 --end-date 2025-03-31 --scan-session-windows 10:00-11:00,14:00-15:00 --scan-session-lag-bars 1 --silver-bullet-windows 10:00-11:00,14:00-15:00 --silver-bullet-max-retest-bars 1 --silver-bullet-min-retest-depth 0.15 --silver-bullet-retest-must-occur-within-window --commission-bps 4 --slippage-bps 1 --out-dir backtest_results/silver_bullet_costed_2025_q1_btc_15m
```

Repeat for Q2/Q3/Q4, then combine or compare reports.

3. Run score and walk-forward report on each chunk and on a merged events file if a merge helper is added.

4. If BTC passes gates, only then test ETH/SOL as separate symbols. Do not add ETH/SOL to live config before separate positive walk-forward validation.

5. If sample remains too small, improve scanner speed/caching before changing strategy rules.

## Guardrails

- Do not claim the model is profitable until walk-forward gates pass after costs.
- Do not enable ICT2022/Turtle Soup live until their own walk-forward reports pass.
- Do not loosen HTF draw/bias/premium-discount gates just to increase event count.
- Prefer more data and faster backtest over adding speculative strategy complexity.
