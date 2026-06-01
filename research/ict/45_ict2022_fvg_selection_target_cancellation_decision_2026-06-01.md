# ICT2022 FVG Selection And Target Cancellation Decision - 2026-06-01

## Goal

Close the pending attribution decision from the Binance funding-aware
`ict2022_mss_fvg` handoff before any relaxed OOS/control validation is run.

This note decides two rules only:

- whether selecting the first active FVG after MSS is source-mandated;
- whether cancelling a setup when the draw/target is reached before FVG retest
  should remain.

It does not enable live trading and does not promote a relaxed variant.

## Evidence Boundary

Use the existing project source map in
`research/ict/33_official_ict_rule_map_and_silver_bullet_alignment_2026-05-25.md`.
That map links the 2022 model to a high-level sequence:

1. liquidity sweep / stop run;
2. MSS or displacement;
3. subsequent FVG or imbalance retest for execution;
4. draw on liquidity as the trade objective.

The available evidence supports the event order, but it does not prove that
the first active FVG after MSS is the only valid execution FVG. Exact FVG
refinements were explicitly deferred in that source map because direct
official captions were not available in the prior run.

## Current Implementation

`strategies/ict_models/ict2022_mss_fvg.py` currently does this:

- finds the latest sweep/raid in the trade direction;
- finds the first qualifying structure break after that sweep;
- selects the first non-invalidated FVG after the structure timestamp;
- requires a bounded retest of that selected FVG;
- skips the setup if the selected target was already reached before retest.

The bounded diagnostic in
`research/ict/36_ict2022_frequency_diagnostic_2026-05-29.md` showed that this
sequence is too sparse on BTCUSDT `30m`: strict runs often reach active FVGs
but not retests, and a no-killzone probe reached long retests that were all
removed by target-open-until-retest.

## Decision

### FVG selection

Treat `first active FVG after MSS` as an internal conservative research
restriction, not as a confirmed source-mandated rule.

Reason:

- the retrieved 2022 model evidence supports using a subsequent FVG/imbalance
  after sweep and MSS;
- it does not explicitly require the first available FVG only;
- the current zero-frequency diagnostics identify this first-FVG bottleneck as
  a construction problem, not a profitability result.

Do not change the live preset from this decision alone. The next valid research
step is bounded attribution that compares first-FVG behavior against an
explicit `first retested eligible FVG after MSS` research variant.

### Target reached before retest

Keep the cancellation rule.

Reason:

- the model is built around an open draw on liquidity;
- if that draw/target is reached before the retracement entry, the planned
  trade objective has already been delivered;
- entering afterward would require a new target and therefore a different
  predeclared model, not a relaxation of this one.

This rule can be audited, but it should not be disabled for live validation.

## Next Action

Add a bounded diagnostic or research-only preset that reports:

- first active FVG after MSS;
- first retested eligible FVG after MSS;
- target-open-until-retest for each FVG selection policy;
- candidate count before costed event-study evaluation.

Only if that attribution produces enough candidates should a predeclared
costed OOS and late-control run be executed. Live switches remain disabled.
