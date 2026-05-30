# Global Algorithm Barrier Audit - 2026-05-29

Scope: all currently implemented ICT model families visible in live filters and
backtest outputs: `silver_bullet`, `turtle_soup`, `ict2022_mss_fvg`,
`ifvg_retest`, `breaker_block`, `reclaimed_ob`, `rejection_block`, and
`mitigation_block`.

External ICT source context used only as rule alignment guidance:

- Official channel reference requested by user: https://www.youtube.com/@InnerCircleTrader
- Public 2022 setup summaries consistently describe the sequence as sweep/POI,
  displacement/MSS, then FVG/OB entry, with premium/discount, SMT, and killzone
  as confluence filters rather than standalone profitability guarantees.
- Turtle Soup references describe false breakout/liquidity sweep followed by
  reversal confirmation or retrace into OB/FVG, not a blind sweep entry.

## Current Universal Blockers

1. Costed expectancy and profit factor do not survive validation phases.
   Several raw or short-window score reports show positive MFE or positive
   non-costed expectancy, but costed walk-forward gates fail on
   `min_managed_expectancy_r`, `min_profit_factor`, or phase sample size.

2. Strict ICT confluence often collapses sample size before it can prove edge.
   The best examples are strict `ict2022_mss_fvg` funding-aware reports with
   zero activated trades, and `reclaimed_ob`/`ifvg_retest` variants with a few
   attractive rows but fewer than a live-grade sample.

3. Tight stops turn normal execution cost into a large R drag.
   This is visible in Silver Bullet and older 30m Turtle/Silver reports where
   `avg_execution_cost_r` is large enough to flip borderline gross outcomes
   into negative net outcomes.

4. Target selection is still mismatched to reachable DOL.
   `target_rr_below_*`, weak `target_before_invalidation_rate`, and high MFE
   without target monetization recur across IFVG, mitigation, breaker, and
   reclaimed reports. The model often sees excursion, but the managed exit is
   not extracting it reliably.

5. Phase stability is the main live blocker.
   The best current Turtle candidate has a positive full-period result, but its
   validation phase still fails the minimum expectancy gate. That is not a live
   candidate; it is a research lead.

## Per-Model Findings

### silver_bullet

Recent costed BTC 15m validation is not tradeable:

- `silver_bullet_costed_2024-11-06_2026-04-20_btc_15m/walk_forward_report.csv`
- Overall: 17 activated trades, managed expectancy `-0.293280`, profit factor
  `0.536827`, max drawdown `8.293195R`.
- Failed gates: `min_managed_expectancy_r`, `min_phase_trades`,
  `min_profit_factor`, `min_total_trades`.
- Score report shows target-before-invalidation `0.176471`,
  hit-1R-before-invalidation `0.352941`, invalidation `0.588235`.

Interpretation: official-window alignment and HTF context are insufficient.
The model needs either a much better post-FVG rejection filter or wider logical
stops with a different exit policy; current tight FVG/session execution is
cost- and invalidation-sensitive.

### turtle_soup

Best current research lead:

- `asian_turtle_full1r_full_2022-01-01_2026-04-20_btc_1h/`
- Overall: 58 activated trades, managed expectancy `0.317314`, profit factor
  `2.452905`.
- But validation: 19 activated trades, managed expectancy `0.124728`, profit
  factor `1.410752`, failed `min_managed_expectancy_r`.
- OOS/control splits are directionally improved, but not stable enough for live.

Interpretation: the 1R/full-target exit improves the earlier Turtle failure,
but the edge still looks phase-dependent. Next useful work is not looser
activation; it is separating "sweep and reject" from "sweep and drift" with
hang-at-level, rejection candle, and time-to-reclaim features.

### ict2022_mss_fvg

Strict funding-aware crypto validation remains untradeable by sample:

- `ict2022_crypto_funding_late_2024-11-06_2026-04-20_1h/walk_forward_report.csv`
- `ict2022_crypto_funding_oos_2022-01-01_2024-11-05_1h/walk_forward_report.csv`
- Overall rows show `count=0`, `activated_trades=0`, failed
  `min_total_trades`.

Interpretation: the current strict sequence is source-aligned but too sparse
on available crypto history. Relaxed diagnostics should stay research-only
until a predeclared costed OOS/control pass exists.

### ifvg_retest

The broad IFVG raw/quality reports show large MFE but poor managed conversion:

- `ifvg_retest_quality_edge_ce/score_threshold_report.csv`
- 1377 activated trades at threshold 0, expectancy `-0.111387`,
  invalidation `0.700145`.
- Model rules currently filter the full quality report down to zero rows.
- Several strict 4h rows are positive, but samples are small and target pressure
  remains frequent.

Interpretation: IFVG has excursion but poor survival and poor monetization.
The next useful filter is not simply higher score; it should test CE depth,
age/touches, and target-nearest-DOL before target-R.

### breaker_block

Breaker outputs are mixed and mostly not costed/live-grade:

- Off/aligned score rows can look positive, especially 30m/1h/4h short windows.
- Costed core probe:
  `probe_costed_2025_btc_1h_core_models/summary_by_model.csv` has 3 activated
  trades, managed expectancy `-0.815167`, target-before-invalidation `0`.
- Repeated no-trade/failure reasons include `insufficient_displacement`,
  `poor_pd_location`, and target-R pressure.

Interpretation: breaker needs a stricter real displacement definition and a
minimum post-break acceptance/retest quality. Current positives are too short
or non-costed to promote.

### reclaimed_ob

Reclaimed OB is the most deceptive family: many reports show high MFE and some
short-window positives, but sample stability is weak.

- Costed 4h IFVG/Reclaimed probe: 3 activated trades, managed expectancy
  `-0.552439`.
- Costed core probe: 2 activated trades, managed expectancy `-1.086898`.
- Some historical 1h/4h aligned score rows are positive, but counts are often
  3-14 and many live-filter rows collapse to zero.

Interpretation: this should be treated as a candidate feature source, not a
live standalone strategy. Useful next work is extracting "reclaim quality" as a
context score for IFVG/Breaker rather than enabling it directly.

### rejection_block

Rejection Block currently has MFE but poor realized outcome:

- `rejection_block_costed_extended_eth_1h_strict_baseline/summary_by_model.csv`
- 39 activated trades, avg MFE `2.400858R`, managed expectancy `-0.087709`,
  profit factor below the live gate in walk-forward.
- `probe_costed_2025_btc_1h_rejection_block/summary_by_model.csv` has 18
  activated trades, managed expectancy `-0.464745`.

Interpretation: the wick/body idea is directionally useful but enters too early
or targets too optimistically. Test delayed entry after close-back confirmation
and 1R/partial exits before adding more filters.

### mitigation_block

Mitigation Block is broadly negative in the current reports:

- 1h aligned May-Oct: 190 trades, expectancy `-0.320837`, many
  `target_rr_below_2` and `poor_pd_location` flags.
- 30m/1h/4h variants repeat the same pattern: high no-trade pressure, low
  target-hit conversion, and no stable costed validation.

Interpretation: do not improve this as a standalone model first. It may be
useful only as a POI/context label after other entries prove edge.

## Code Added

Added `backtesting/algorithm_barrier_audit.py`.

Purpose:

- scan `backtest_results/**/summary_by_model.csv`;
- join optional `walk_forward_report.csv` and
  `summary_by_no_trade_reasons.csv`;
- classify recurring profitability blockers into machine-readable barrier tags;
- output run-level and model-level CSV/Markdown reports.

Also added a focused unit test in `tests/test_new_ict_models.py` covering
cost drag, invalidation, target-R pressure, and model summary aggregation.

Added a research-only Turtle Soup refinement:

- `turtle_soup_asian_reject_prior_failed_sweep`
- `asian_failed_sweep_count_before_reclaim`

This lets Asian-range Turtle tests reject a reclaim if price already swept the
same range boundary and closed outside it before the eventual reclaim. The
intent is to test the observed blocker "sweep and drift" without changing any
existing preset by default.

## Verification Status

Static checks:

- The audit script was inspected after patching numeric parsing and sort keys.
- The test fixture validates expected barrier tags by construction.

Runtime checks:

- A targeted `python -m unittest` run could not be executed in this environment:
  the escalated attempt was rejected by the approval layer due a usage limit,
  and the sandboxed Python attempt failed during Windows sandbox setup refresh.
- Previous full suite from the prior iteration passed before this new audit
  file/test were added: `python -m unittest tests.test_new_ict_models`.

## Decision

No model should be live-enabled from this analysis.

The next algorithmic iteration should focus on:

1. Turtle 1h: add explicit rejection/reclaim quality after sweep, then rerun
   the same OOS/control split.
2. IFVG/Breaker: replace raw score gating with target-nearest-DOL and survival
   filters; do not chase high MFE alone.
3. Reclaimed/Mitigation: demote from standalone candidates to context features
   until they pass costed validation as independent entries.
4. Silver Bullet: only continue if execution-cost R drag is reduced by wider
   logical stops or a materially different entry/exit policy.
