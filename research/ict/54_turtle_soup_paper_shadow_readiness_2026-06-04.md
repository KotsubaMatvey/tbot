# Turtle Soup Paper Shadow Readiness

Date: 2026-06-04

Status: Locked candidate prepared for paper/shadow validation only.

## What Changed

Created a dedicated paper/shadow filter profile:

- `configs/paper_model_filters_turtle_soup_locked_2026.json`

The default live profile remains disabled:

- `configs/live_model_filters_2025.json`

The scanner can now read top-level `scanner_config` from the active filter
profile. This matters because the locked Turtle Soup candidate was validated
with:

- `context_mode=off`
- `pre_model_filter=false`

Without this, live/paper scanner alerts would be filtered by extra HTF
pre-model logic that was not part of the locked backtest.

Update on 2026-06-05:

- Added `forward_logging.py`.
- Wired `alerts.scanner_loop` to call `record_forward_shadow_alerts` immediately
  after `run_scanner`, before user subscription filters or Telegram sends.
- Added `target_hint` to `AlertPayload` so paper logs can evaluate target
  outcomes instead of only fill quality.
- Enabled `forward_log` in
  `configs/paper_model_filters_turtle_soup_locked_2026.json`.
- The default live profile still does not enable forward logging.

## Locked Paper Profile

Rules:

- model: `turtle_soup`
- symbols: BTCUSDT, ETHUSDT
- timeframes: `15m`, `30m`
- entry: retest
- target: `dol_hierarchy`
- range source: Asian range
- sessions: `02:00-05:00`, `07:00-10:00`, `13:00-16:00`
- Asian range window: `00:00-08:00` UTC
- quality: `strong`
- SMT: `require_no_smt=true`
- minimum risk: `35` bps
- all other selectable ICT models: disabled

This is intentionally a paper/shadow profile, not a live execution profile.

Forward log settings:

- enabled: `true`
- path: `logs/turtle_soup_forward_shadow.csv`
- horizon: `24` bars
- models: `turtle_soup`

The log path is under `logs/`, which is ignored by git.

## Evidence Snapshot

Source note:

- `research/ict/53_turtle_soup_15m_external_validation_2026-06-04.md`

Key results:

- IS `2022-01-01..2023-06-30`: `171` deduped trades,
  `+0.330721R` expectancy, PF `2.189534`, all phases passed.
- Locked OOS `2023-07-01..2024-12-31`: `92` deduped trades,
  `+0.389537R` expectancy, PF `2.572923`, all phases passed but total sample
  missed the `100` trade gate by `8` trades.
- Late-control `2025-01-01..2026-04-20`: `82` deduped trades,
  `+0.260068R` expectancy, PF `1.806924`, but failed standalone sample and
  phase gates.
- Full external `2023-07-01..2026-04-20`: `174` deduped trades,
  `+0.328523R` expectancy, PF `2.161562`, all phases passed.

## Promotion Gate

Do not enable live execution until a forward/paper log passes:

- minimum signals: `50` absolute minimum, `100` preferred
- fill rate: `>= 70%`
- average slippage: `<= 2` bps
- average net outcome: `> 0R`
- no unexplained alert drift versus the locked paper profile

Existing analyzer:

```powershell
python -m backtesting.forward_log_report --logs path\to\forward_logs.csv --out-dir backtest_results\turtle_soup_forward_shadow --min-signals 50 --min-fill-rate 0.7 --max-avg-slippage-bps 2 --min-avg-net-outcome-r 0
```

Expected forward log columns include:

- `model`
- `symbol`
- `status` or `fill_status`
- `slippage_bps`
- `outcome_r` or `net_outcome_r`
- `filled_price` or `fill_price`

The implemented logger writes one row per signal and updates that row as the
paper state progresses:

- `open` / `pending`: signal logged, retest entry not filled yet
- `filled`: retest entry touched
- `missed`: retest entry not touched inside the configured horizon
- `closed`: target, stop, or horizon close resolved the paper trade

Current limitations:

- Fill is simulated from OHLC candles, not exchange order acknowledgements.
- Simulated fill slippage is `0.0` bps until actual paper/broker fills are
  wired in.
- If target and stop are both touched in the same candle after fill, the logger
  is conservative and closes at the stop.
- Net outcome currently equals simulated R outcome; fee/slippage adjustment
  should be revisited once actual fill prices are logged.

## How To Run Shadow Scanner

Use the paper profile explicitly:

```powershell
$env:LIVE_MODEL_FILTER_CONFIG="configs/paper_model_filters_turtle_soup_locked_2026.json"
$env:SYMBOLS="BTCUSDT,ETHUSDT"
$env:TIMEFRAMES="15m,30m"
$env:STRATEGY_TIMEFRAMES="15m,30m"
```

This should be used only for paper/shadow signal collection. Default live
settings remain disabled.

## Next Work

The remaining blocker is not another strategy filter. It is execution quality:

1. Run the paper profile until the forward log reaches at least `50` signals.
2. Analyze `logs/turtle_soup_forward_shadow.csv` with
   `backtesting.forward_log_report`.
3. Compare forward outcomes against the backtest assumptions for retest fills.
4. Only after that, decide whether a tiny-risk live pilot is justified.
