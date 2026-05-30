# Funding Turtle Session Selection and Barrier Audit

Date: 2026-05-30

Status: research only. Live remains disabled.

## ICT source context

Reference material checked for rule alignment:

- Official channel requested by user: https://www.youtube.com/@InnerCircleTrader
- Public 2022 model notes describe the sequence as liquidity sweep or POI,
  displacement/MSS, then FVG/PD-array entry during kill zones.
- Public Silver Bullet references describe it as a time-window model around
  liquidity and FVG, not as a generic all-day FVG strategy.

Implementation implication:

- Liquidity and time are gates, not profitability guarantees.
- A candidate must still pass costed OOS/control validation after session risk
  controls.
- Relaxing a filter only to satisfy sample size is not valid unless the relaxed
  branch keeps phase expectancy and profit factor.

## Tooling fixes

Updated `backtesting/algorithm_barrier_audit.py`:

- includes walk-forward-only directories that have `walk_forward_report.csv`
  but no `summary_by_model.csv`;
- preserves zero and false values in Markdown tables instead of rendering them
  as blanks.

Updated `backtesting/walk_forward_report.py` and
`backtesting/run_ict_batch.py`:

- added deterministic session dedupe selection:
  - `timeframe_first`
  - `first`
  - `highest_score`
- kept the existing timeframe-priority behavior as the default.

Unit coverage added in `tests/test_new_ict_models.py` for walk-forward-only
audit rows and highest-score session dedupe.

## Global barrier audit

Command:

```powershell
python -m backtesting.algorithm_barrier_audit --results-dir backtest_results --out-dir backtest_results\algorithm_barrier_audit_2026-05-30
```

Result:

- `360` run rows across `11` model labels.
- Only one walk-forward row passes: full-period funding-aware Turtle with
  `max_trades_per_session=2`, no session dedupe.
- No model family has an OOS/control live-grade pass.

Current model-level blockers:

- `turtle_soup`: strongest lead, but blocked by phase/sample stability after
  realistic one-trade-per-session risk control.
- `silver_bullet`: high invalidation, weak target hit rate, and cost drag.
- `ict2022_mss_fvg`: strict source-aligned crypto preset is too sparse; earlier
  funding-aware strict reports produced zero activated trades.
- `ifvg_retest` and `reclaimed_ob`: high MFE appears in score reports, but
  managed conversion and costed validation are not proven.
- `breaker_block`, `rejection_block`, `mitigation_block`: no costed
  walk-forward pass; repeated target pressure, poor fill/activation, or weak
  follow-through.

## Funding-aware Turtle session selection audit

Base candidate:

- Config:
  `configs/backtests/asian_turtle_full1r_clean_strong_btc_tf_direction_funding_research.json`
- Rules:
  - BTCUSDT only
  - `turtle_quality=strong`
  - `max_asian_failed_sweep_count_before_reclaim=0`
  - allowed directions: `1h:long`, `1h:short`, `30m:short`
  - funding-aware costs enabled

Policies tested:

- baseline: `timeframe_first` with priority `1h,30m`
- `first`
- `highest_score`
- `timeframe_first` with priority `30m,1h`

### OOS 2022-04-08 to 2024-10-02

Baseline:

- 23 trades, expectancy `0.400945R`, PF `3.312576`.
- Failed: `min_phase_trades`, `min_total_trades`.

First / highest-score / 30m-priority:

- 23 trades, expectancy `0.398582R`, PF `3.298948`.
- Failed: `min_phase_trades`, `min_total_trades`.

Conclusion: selection policy does not solve OOS sample size.

### Control 2025-03-04 to 2026-03-30

Baseline:

- 5 trades, expectancy `0.536548R`, PF `79.564501`.
- Failed sample gates.

First / highest-score / 30m-priority:

- 5 trades, expectancy `0.645026R`, PF `95.448385`.
- Failed sample gates.

Conclusion: control edge is positive but statistically too thin.

### Full 2022-04-08 to 2026-03-30

Baseline:

- 28 trades, expectancy `0.425160R`, PF `3.959993`.
- Failed: `min_managed_expectancy_r`, `min_phase_trades`,
  `min_total_trades`.

First / highest-score / 30m-priority:

- 28 trades, expectancy `0.442590R`, PF `4.081342`.
- Failed: `min_managed_expectancy_r`, `min_phase_trades`,
  `min_total_trades`.

Conclusion: deterministic one-trade-per-session selection slightly improves
full expectancy, but train has only 9 trades and remains below the expectancy
gate.

## Decision

Session-selection policy is not the root blocker. The remaining blocker is
independent OOS/control sample size under realistic one-trade-per-session risk.

The full-period `max_trades_per_session=2` variant is a research lead, not a
live candidate, because it does not prove robustness in OOS/control.

Do not enable live model filters.

## Next step

Continue with data/sample expansion before algorithm relaxation:

1. Add more independent BTC 30m/1h history or a new liquid symbol with the same
   funding-aware cost model.
2. Rerun the same strict Turtle candidate and the session-selection policies.
3. If sample remains too thin, treat this as a paper-forward candidate only,
   not live.
