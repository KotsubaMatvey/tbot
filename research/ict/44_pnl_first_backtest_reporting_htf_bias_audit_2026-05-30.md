# P&L-first backtest reporting and HTF bias audit

## Change

Backtest diagnostics now separate pattern discovery from trade-quality validation.

- `score_threshold_report` remains useful for pattern and score diagnostics.
- `trade_pnl_report` is the primary trade-stat report: win rate, realized average RR, expectancy, profit factor, max drawdown in R, total P&L in R, costs, and `sample_valid`.
- `htf_bias_audit` checks whether HTF context improves realized P&L versus the full baseline or only reduces the sample.

## Metrics

`trade_pnl_report` uses activated trades only. It prefers `net_managed_outcome_r` when available and falls back to `managed_outcome_r`.

Expectancy is computed from realized trade outcomes:

`winrate * avg_win_r - (1 - winrate) * avg_loss_r`

`avg_realized_rr` is the mean realized trade outcome in R, not the planned target RR. `sample_valid` is false below the configured minimum sample size, default `100` trades.

## HTF audit interpretation

`htf_bias_audit` compares each bucket against the full realized P&L baseline:

- `improves_edge`: expectancy improves and win rate does not deteriorate.
- `worse_than_baseline`: expectancy is below the baseline.
- `cuts_sample_only`: sample is reduced without a positive expectancy improvement.
- `insufficient_sample`: bucket has fewer trades than `min_trades`.

This directly tests the current concern: HTF bias must prove that it improves direction/edge, not merely that it filters out trades.

## Live stance

This is reporting and validation infrastructure only. It does not enable live trading. Live remains disabled until a costed OOS/control candidate passes the trade-level gates with a meaningful sample.
