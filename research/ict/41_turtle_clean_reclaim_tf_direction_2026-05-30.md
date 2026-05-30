# Turtle Soup clean reclaim and timeframe-direction audit

Date: 2026-05-30

Status: research only. Live remains disabled.

## ICT premise checked

- Treat Turtle Soup as liquidity sweep plus decisive rejection/reclaim, not as
  any sweep that closes back inside a range.
- Use SMT and killzone as confluence, but do not assume they create edge by
  themselves.
- Keep one trade per symbol/session as a risk rule. Multi-timeframe duplicates
  must be resolved before a live promotion.

## Code changes

- Added model filter gates:
  - `max_asian_failed_sweep_count_before_reclaim`
  - `allowed_turtle_qualities`
  - `allowed_timeframe_directions`
- Added `summary_by_asian_failed_sweep_count` and `summary_by_symbol`.
- Added walk-forward `--dedupe-session` with deterministic timeframe priority.
- Added research configs:
  - `asian_turtle_full1r_clean_reclaim_research.json`
  - `asian_turtle_full1r_clean_strong_multi_research.json`
  - `asian_turtle_full1r_clean_strong_btc_30m_1h_research.json`
  - `asian_turtle_full1r_clean_strong_btc_tf_direction_research.json`

## Results

### BTC 1h clean reclaim

Path prefix: `asian_turtle_full1r_clean_reclaim_*_btc_1h`

- Full selected: 42 trades, managed expectancy `0.328903R`, PF `2.487931`.
- Full validation phase failed: `-0.010712R`, PF `0.974006`.
- Control looked strong but thin: 11 trades, `0.639639R`, PF `207.05122`.

Conclusion: clean reclaim helps, but BTC 1h is still phase-dependent and too
thin for live.

### BTC+ETH clean strong

Path prefix: `asian_turtle_full1r_clean_strong_multi_*_btc_eth_1h`

- Filtered full: 36 trades, `0.234643R`, PF `1.824662`.
- Filtered OOS: 27 trades, `0.330119R`, PF `2.277242`, but train phase failed.
- Filtered control: 8 trades, `0.076358R`, PF `1.279217`.
- Symbol diagnostic: ETH long was negative in full and OOS/control. ETH did
  not solve sample-size; it diluted the edge.

Conclusion: do not add ETH to this candidate.

### BTC 30m+1h clean strong

Path prefix: `asian_turtle_full1r_clean_strong_btc_*_30m_1h`

- Filtered full: 41 trades, `0.397213R`, PF `3.383915`, but failed
  `max_trades_per_session` and phase stability.
- OOS: 34 trades, `0.350895R`, PF `2.755155`, but validation phase only
  `0.219421R` and session overtrade count was 7.
- Timeframe/direction diagnostic:
  - 1h long and 1h short were both positive.
  - 30m short was positive.
  - 30m long was weak/negative OOS and should be excluded from this candidate.

Conclusion: 30m can add useful frequency only on the short side.

### BTC tf-direction candidate

Config: `asian_turtle_full1r_clean_strong_btc_tf_direction_research.json`

Rules:

- `BTCUSDT` only.
- `turtle_quality=strong`.
- `max_asian_failed_sweep_count_before_reclaim=0`.
- Allowed timeframe/direction pairs:
  - `1h:long`
  - `1h:short`
  - `30m:short`

Without session dedupe:

- Full: 34 trades, `0.471263R`, PF `4.946916`.
- All train/validation/test phases passed expectancy and PF gates.
- Failed only `max_trades_per_session`.

With session dedupe:

- Full: 28 trades, `0.424625R`, PF `3.928732`.
- OOS: 23 trades, `0.400267R`, PF `3.286979`.
- Control: 5 trades, `0.536671R`, PF `79.582511`.
- Failed sample-size gates. Full train also fell to `0.242436R` with 1h-first
  priority.

Conclusion: this is the strongest lead, but still not live-ready. The edge is
now blocked by independent-session sample size after realistic dedupe, not by
raw expectancy.

## Current blockers

1. `max_trades_per_session` blocks the non-deduped variant.
2. Session dedupe makes the sample too thin for the current gates.
3. Control period remains too small to validate robustness.
4. ETH and 30m long should stay excluded unless a separate source-aligned rule
   fixes their negative contribution.

## Follow-up probes on 2026-05-30

### Data expansion

- Attempted to download public Binance SOLUSDT `30m`/`1h` OOS data with
  `backtesting.download_history`.
- The request failed at DNS resolution for `fapi.binance.com`; no SOL OOS
  validation was produced.

### Source-aligned NY open window

Config:
`asian_turtle_full1r_clean_strong_btc_nyopen_tf_direction_research.json`

- Window: `07:00-10:00`.
- Dedupe full: 24 trades, `0.380841R`, PF `2.906759`.
- OOS dedupe: 21 trades, `0.342047R`, PF `2.498465`.
- Control dedupe: 3 trades, `0.652395R`, but too thin.
- Raw full without dedupe had 31 trades, but train failed at `0.035707R`,
  PF `1.095861`, and overtraded 7 sessions.

Conclusion: `07:00-10:00` is rejected for this candidate. It does not solve
sample size and worsens early-phase stability.

### Split NY open / NY AM windows

Config:
`asian_turtle_full1r_clean_strong_btc_split_session_tf_direction_research.json`

- Windows: `07:00-10:00,10:00-12:00`.
- OOS dedupe: 31 trades, `0.360738R`, PF `2.786512`, no overtrade.
- OOS validation phase failed hard: `0.068055R`, PF `1.158895`.
- Control dedupe: 5 trades, `0.536671R`, still too thin.
- The full run timed out before writing the full-period directory; OOS/control
  are enough to reject the branch.

Conclusion: split sessions improve sample but break OOS phase stability. Reject.

### NY PM session-label bug and PM probe

Implementation bug fixed:

- `NY_PM_SESSION` is `13:30-16:00`.
- `_session_label()` previously returned `ny_pm` only for starts at `14:00` or
  later, causing `13:30-16:00` events to be labelled `custom` and filtered out.
- Fixed the boundary to `13:30` and added unit coverage.

Config: `asian_turtle_full1r_clean_strong_btc_nypm_research.json`

- After the label fix, PM events pass the `ny_pm` label filter.
- Filtered full: 11 trades, managed expectancy `-0.070953R`, PF `0.841095`.
- OOS: 8 trades, `-0.009188R`, PF `0.980054`.
- Control: 2 trades, `-0.294086R`, PF `0.46898`.

Conclusion: the label bug was real, but NY PM Turtle is rejected as a live
candidate.

### Funding-aware tf-direction validation

Config:
`asian_turtle_full1r_clean_strong_btc_tf_direction_funding_research.json`

Reason for this rerun:

- Earlier Turtle reports included commission/slippage but showed
  `avg_funding_cost_r=0.0`.
- For crypto perpetuals, live promotion requires funding-aware validation.

Result with the same strict rules and session dedupe:

- OOS: 23 trades, `0.400945R`, PF `3.312576`; failed only sample gates
  (`min_phase_trades`, `min_total_trades`).
- Control: 5 trades, `0.536548R`, PF `79.564501`; failed sample gates.
- Full: 28 trades, `0.425160R`, PF `3.959993`; failed sample gates and train
  expectancy (`0.244969R`).
- Funding impact was small: full `avg_funding_cost_r=-0.000535R`.

Result without dedupe but with `max_trades_per_session=2`:

- Full passed all walk-forward gates: 34 trades, `0.472046R`, PF `4.990648`.
- Train: 11 trades, `0.357752R`, PF `2.507660`.
- Validation: 11 trades, `0.364728R`, PF `3.912614`.
- Test: 12 trades, `0.675189R`, PF `238.276276`.
- OOS still failed strict sample gates: 28 trades total; train had 9 trades.
- Control stayed too thin: 6 trades.
- Duplicate session count inspection showed exactly six sessions with two
  selected signals and no session with more than two:
  `2023-02-28`, `2023-04-12`, `2023-10-13`, `2024-03-12`,
  `2024-09-15`, `2026-03-30`.

Interpretation:

- Funding is not the blocker for this Turtle candidate.
- A risk policy allowing at most two same-session signals makes full-period
  walk-forward pass, but OOS/control are still not strong enough for live.
- Do not promote. The remaining blocker is independent OOS/control sample size,
  not raw expectancy.

### Funding-aware rule grid

A local grid over `allowed_turtle_qualities` and `allowed_timeframe_directions`
on the funding-aware events showed:

- Adding `valid` trades can lift OOS count, but phase gates degrade.
- Including `30m:long` also lifts count, but lowers expectancy and introduces
  phase failures.
- The only OOS-count>=30 positive variants still failed at least one phase gate.

Conclusion: the current exclusions (`30m:long` and broad `valid`) are justified
by evidence; they should not be relaxed to satisfy sample-size gates.

## Next step

Do not relax the live gate. Next research should test a larger independent
BTC-only sample without violating session risk:

1. Add more historical BTC 1h/30m coverage if available.
2. Test deterministic session selection policies that do not use future PnL:
   first signal, 1h priority, 30m priority, and higher decision score.
3. Only consider live promotion if OOS/control pass costed walk-forward after
   session dedupe.
