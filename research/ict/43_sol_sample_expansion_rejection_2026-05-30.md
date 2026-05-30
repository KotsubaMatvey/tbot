# SOL Sample Expansion Rejection

Date: 2026-05-30

Status: rejected research branch. Live remains disabled.

## Purpose

Previous funding-aware BTC-only Turtle candidate was positive but too thin
after one-trade-per-session risk control. This probe tested whether adding
SOLUSDT could increase independent sample size without relaxing the strict
source-aligned Turtle rules.

## Data added

Command:

```powershell
python -m backtesting.download_history --out-dir data/history_crypto_2022-01-01_2026-04-20 --symbols SOLUSDT --timeframes 30m 1h --start 2022-01-01 --end 2026-04-20 --timeout 240 --include-funding
```

Output:

- `SOLUSDT_30m.csv`: 75408 candles
- `SOLUSDT_1h.csv`: 37704 candles
- `SOLUSDT_funding.csv`: 4788 funding rows

## Config

Added:

- `configs/backtests/asian_turtle_full1r_clean_strong_btc_sol_tf_direction_funding_research.json`

Rules preserved from the BTC-only lead:

- `turtle_quality=strong`
- `max_asian_failed_sweep_count_before_reclaim=0`
- allowed directions: `1h:long`, `1h:short`, `30m:short`
- session: `08:30-12:00`
- SMT required on sweep
- funding-aware costs enabled

SMT pairs:

- `BTCUSDT:ETHUSDT`
- `SOLUSDT:ETHUSDT`

## Runtime note

The full BTC+SOL batch timed out after the OOS run. OOS was written
successfully; control was run separately with the same parameters. Full-period
BTC+SOL was not needed for the rejection because OOS/control already failed.

## OOS result

Path:

- `backtest_results/asian_turtle_full1r_clean_strong_btc_sol_tfdir_funding_oos_2022-01-01_2024-11-05_30m_1h`

Strict one-trade-per-session:

- 36 trades, expectancy `0.279309R`, PF `2.194693`.
- Failed: `min_managed_expectancy_r`.
- Train: 11 trades, `0.172237R`, PF `1.506703`.
- Validation: 13 trades, `0.297301R`, PF `2.532318`.
- Test: 13 trades, `0.341824R`, PF `3.061919`.

No dedupe, `max_trades_per_session=2` diagnostic:

- 41 trades, expectancy `0.327065R`, PF `2.593261`.
- Failed: `min_managed_expectancy_r`.
- Train: 13 trades, `0.278858R`, PF `1.969530`.

Symbol diagnostic before walk-forward dedupe:

- BTCUSDT: 64 trades, managed expectancy `0.151911R`.
- SOLUSDT: 33 trades, managed expectancy `0.069389R`,
  invalidation rate `0.666667`.

Interpretation: SOL increases count but dilutes the OOS edge. The OOS branch
fails because early phase expectancy is too low.

## Control result

Path:

- `backtest_results/asian_turtle_full1r_clean_strong_btc_sol_tfdir_funding_control_2024-11-06_2026-04-20_30m_1h`

Strict one-trade-per-session:

- 8 trades, expectancy `0.120533R`, PF `1.430393`.
- Failed: `min_managed_expectancy_r`, `min_phase_trades`,
  `min_profit_factor`, `min_total_trades`.
- Validation: 3 trades, `0.028011R`, PF `1.072187`.
- Test: 2 trades, `-0.397019R`, PF `0.238106`.

No dedupe, `max_trades_per_session=2` diagnostic:

- 9 trades, expectancy `0.194978R`, PF `1.783245`.
- Failed: `min_managed_expectancy_r`, `min_phase_trades`,
  `min_profit_factor`, `min_total_trades`.

Interpretation: control rejects the expansion. The added SOL sample does not
create robustness under the live gate.

## Decision

Reject BTC+SOL expansion for this Turtle candidate.

The current blocker remains unchanged: the BTC-only strict candidate has
positive expectancy but insufficient independent OOS/control sample under
realistic session risk, while SOL increases frequency at the cost of phase
stability.

Do not enable live filters.
