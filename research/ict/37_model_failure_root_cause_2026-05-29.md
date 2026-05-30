# Model Failure Root Cause Map - 2026-05-29

## Scope

This note summarizes why the current ICT model family does not pass live gates.
It uses existing `walk_forward_report.csv`, `summary_by_model.csv`, and the
new bounded ICT2022 frequency diagnostics. Repository code and report files
remain authoritative.

Live promotion gates require enough activated trades, positive costed managed
expectancy, profit factor, controlled drawdown, and no session overtrading.
Across the current `backtest_results`, no walk-forward row passed all gates.

## Aggregate Gate Evidence

Read-only audit of `38` walk-forward reports (`124` rows):

| Failed gate | Rows |
| --- | ---: |
| `min_managed_expectancy_r` | 87 |
| `min_profit_factor` | 80 |
| `min_phase_trades` | 76 |
| `min_total_trades` | 28 |
| `max_drawdown_r` | 22 |
| `max_trades_per_session` | 12 |

Interpretation: the dominant problem is not only insufficient sample. Most
tested variants that trade enough still do not have a costed edge.

## Model-Level Findings

### Silver Bullet

Representative official-window Hyperliquid results:

| Market | Activated trades | Gross expectancy | Avg execution cost | Net expectancy | Profit factor |
| --- | ---: | ---: | ---: | ---: | ---: |
| `BTC` | 60 | `-0.124419R` | `0.306181R` | `-0.482389R` | `0.339243` |
| `SP500` | 81 | `-0.070278R` | `1.458047R` | `-1.586453R` | `0.047457` |

Algorithm problem:

- The detector accepts any FVG created inside the configured Silver Bullet
  window, then enters on a constrained retest.
- There is no required MSS/displacement context, SMT context, or liquidity-draw
  quality inside the detector itself.
- Stop distance comes from a very local swing or FVG boundary, so ordinary
  execution costs become large in R terms, especially on tight-index setups.

Result: the model finds activity, but the signal has low win rate and costs
turn weak gross outcomes into strongly negative net outcomes.

### Turtle Soup / Asian Range

Representative OOS crypto results:

| Variant | Activated trades | Gross expectancy | Avg execution cost | Net expectancy | Profit factor |
| --- | ---: | ---: | ---: | ---: | ---: |
| BTC `30m` Asian SMT-on-sweep OOS | 23 | `0.025472R` | `0.211305R` | `-0.185833R` | `0.616131` |
| BTC `1h` Asian SMT-on-sweep OOS | 30 | `0.161928R` | `0.147303R` | `0.014625R` | `1.031894` |
| BTC `1h` Asian SMT-on-sweep DOL OOS | 30 | `0.208464R` | `0.147303R` | `0.061161R` | `1.175881` |

Algorithm problem:

- The sweep/reclaim pattern has some MFE, but the final edge is too thin after
  realistic execution costs.
- DOL target selection improves hit rate in some rows, but many setups still
  have `target_rr_below_2` or `target_rr_below_3`, which means the target is
  too close for the risk gate or the trade is not worth its stop.
- The exact SMT-on-sweep requirement reduces frequency but does not create a
  robust enough edge in independent OOS.

Result: this branch is closer than the others, but it is still a rejected live
candidate because the OOS edge is small or negative after costs.

### ICT2022 MSS + FVG

Strict Binance funding-aware validation produced zero activated trades across
early-OOS and late-control `30m`/`1h` runs.

Bounded BTCUSDT `30m` diagnostics show the zero-frequency source:

| Probe | Key blocker |
| --- | --- |
| Strict January 2025 | Long side reaches `15` active FVGs after MSS, but `0` retests. |
| Strict January 2025 | Short side reaches `6` structure-session passes, then `0` same-session sweep/MSS passes. |
| Relaxed January 2025 | Removing strong displacement and retest-session gates still leaves `0` retests. |
| Strict January 2024 | Both sides fail at structure session gate after sweep-age pass. |
| No-killzone January 2024 | Long side reaches `9` retests, but all fail target-open-until-retest. |

Algorithm problem:

- The sequence is too brittle: latest sweep -> first qualifying MSS -> first
  active FVG -> fast retest.
- The selected FVG often never retests under the current replay view.
- Session coupling removes otherwise plausible structure events.
- The target-reached-before-retest cancellation rule can remove the remaining
  relaxed candidates before entry.

Result: this is not a profitability problem yet; it is a construction problem.
The algorithm does not produce a tradable sample under source-aligned filters.

### Rejection Block, IFVG Retest, Reclaimed OB

Representative costed rows:

| Model/run | Activated trades | Net expectancy | Profit factor / target issue |
| --- | ---: | ---: | --- |
| ETH `1h` rejection block strict baseline | 39 | `-0.087709R` | PF `0.816027` |
| BTC `4h` IFVG retest strict probe | 1 | `-1.164073R` | target-before-invalidation `0` |
| BTC `4h` reclaimed OB strict probe | 3 | `-0.552439R` | target-before-invalidation `0` |

Algorithm problem:

- These models often show high MFE, but final target hits are rare or absent.
- The DOL/HTF target can be too far from the entry, so the trade has excursion
  but does not monetize it before invalidation or horizon close.
- Strict HTF/POI filters leave too few activated trades for validation.

Result: the entry may capture movement, but the target and trade management
logic are not aligned with the realized path.

## Cross-Cutting Root Causes

1. **Cost sensitivity is too high.**
   Many setups have tight stops. Execution costs of `0.1R` to `1.4R` are enough
   to turn small gross edges into negative net outcomes.

2. **Pattern detection is not the same as edge detection.**
   FVG, sweep, rejection wick, or OB retest presence is not predictive enough
   unless paired with a proven draw, timing, and invalidation model.

3. **Targets and exits are weakly matched to the entry.**
   Some models target too close and fail RR gates. Others target far HTF
   objectives, show high MFE, but never hit the final target.

4. **Session and confirmation filters are brittle.**
   They reduce false positives, but often collapse the sample before OOS gates
   can even evaluate profitability.

5. **Selected-window performance does not survive OOS.**
   Several branches looked acceptable on selected 2025 windows but failed
   independent 2022-2024 or late-control validation.

## What To Diagnose Next

Do not add another relaxed live candidate yet. The next useful work is
algorithm-level attribution:

1. Add per-model funnel diagnostics similar to ICT2022 for Silver Bullet and
   Turtle Soup: raw primitive -> session gate -> HTF gate -> entry activation
   -> 1R/2R/final target -> invalidation.
2. Add an exit-policy audit that compares final-target outcome with best
   available managed exits: fixed 1R/2R, time stop, BE after 1R, partials, and
   horizon close.
3. Add a cost-sensitivity table by stop-size bucket. Any setup whose expected
   edge disappears at realistic costs should be discarded before deeper tuning.
4. Revisit target selection before entry selection. The current DOL target is
   often either too close for RR gates or too far to monetize.

## Working Decision

The current algorithms fail because they encode ICT-looking event sequences,
but they do not yet encode a validated trade lifecycle. Live switches should
remain off until a model passes costed OOS/control validation with enough
activated trades and a target/exit policy that survives realistic costs.
