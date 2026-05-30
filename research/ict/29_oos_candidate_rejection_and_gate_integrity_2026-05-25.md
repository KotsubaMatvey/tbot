# OOS Candidate Rejection and Gate Integrity - 2026-05-25

## Success Criterion

A strategy may remain a research candidate only if it survives costed
out-of-sample evaluation. It may not be enabled live unless walk-forward
quality gates pass on activated trades:

- net managed expectancy at least `+0.3R`;
- profit factor at least `1.3`;
- at least `30` total and `10` per phase activated trades;
- maximum drawdown at most `8R`;
- no more than one activated trade per session.

## Correctness Fixes

Two gate-integrity defects were addressed before making any activation
decision:

1. Backtest SMT confirmation is now usable only by the configured primary
   symbol of a pair. A divergence calculated for `BTCUSDT:ETHUSDT` no longer
   confirms an `ETHUSDT` detector run. This matches the existing SMT event
   timestamp and direction semantics and the live scanner implementation.
2. `walk_forward_report` now creates phases, enforces sample-size gates, and
   counts session overtrading from `activated_trade=true` events only.
   Unfilled setups can no longer satisfy trade-count gates or create false
   overtrade failures.

## Turtle Soup SMT-on-Sweep

The prior BTC `30m` Asian-range candidate looked positive on the selected
2024-11 through 2026-04 interval. Independent Binance Futures BTC/ETH history
was downloaded for `2022-01-01` through `2024-11-05`; coverage passed at
`100%` for both `30m` series.

Unchanged costed `30m fixed_r` OOS result:

| Period | Activated trades | Net expectancy | Profit factor | Test phase |
| --- | ---: | ---: | ---: | ---: |
| 2022-01-01 through 2024-11-05 | 23 | `-0.185833R` | `0.616131` | `-0.264107R` |

The apparent `1h` improvement was also tested only after it appeared positive
on the selected interval:

| Variant | OOS trades | Net expectancy | Profit factor | Test phase |
| --- | ---: | ---: | ---: | ---: |
| `1h fixed_r` | 30 | `+0.014625R` | `1.031894` | `-0.200369R` |
| `1h dol_hierarchy` | 30 | `+0.061161R` | `1.175881` | `-0.214142R` |

`dol_hierarchy` is conceptually closer to the intended opposing-liquidity
target, but it still fails the stated gates. Daily HTF alignment was also
tested as a concept-driven gate; it left only two OOS trades and zero trades
on the selected interval, so it is not a viable current profile.

Decision: reject the Asian SMT-on-sweep Turtle Soup branch as a live candidate.
Keep it disabled.

## Rejection Block Follow-up

`rejection_block` on ETHUSDT `1h` was the least negative previously costed
non-Turtle artifact. It was reproduced with strict HTF context, existing
`dol_hierarchy` targeting, `TP1=1R`, partial close `0.3`, commission `4 bps`
per side, and slippage `1 bps` per side on the extended
`2024-11-06` through `2026-04-20` dataset.

After the activated-trades gate correction:

| Period | Activated trades | Net expectancy | Profit factor | Test phase |
| --- | ---: | ---: | ---: | ---: |
| 2024-11-06 through 2026-04-20 | 39 | `-0.087709R` | `0.816027` | `-0.076955R` |

Decision: keep `rejection_block` research-only and disabled.

## Live Decision

No model meets the profitability and OOS quality gates from this cycle. All
live strategy switches remain disabled. The useful deliverable from this
iteration is stricter validation integrity and removal of two false candidate
paths from further promotion work.
