# Trade P&L Report

- events: `backtest_results\ict2022_first_retested_fvg_smoke_2024_01_01_03_btc_30m\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 2 | 1 | True | 50.0 | 0.236272 | 1.48775 | 1.015206 | 0.236272 | 1.465466 | 1.015206 | 0.472544 | 0.031938 | 0.014858 | 0.046796 |
| by_model | ict2022_mss_fvg | none | 0 | 0 | 2 | 1 | True | 50.0 | 0.236272 | 1.48775 | 1.015206 | 0.236272 | 1.465466 | 1.015206 | 0.472544 | 0.031938 | 0.014858 | 0.046796 |
| by_symbol | BTCUSDT | none | 0 | 0 | 2 | 1 | True | 50.0 | 0.236272 | 1.48775 | 1.015206 | 0.236272 | 1.465466 | 1.015206 | 0.472544 | 0.031938 | 0.014858 | 0.046796 |
| by_timeframe | 30m | none | 0 | 0 | 2 | 1 | True | 50.0 | 0.236272 | 1.48775 | 1.015206 | 0.236272 | 1.465466 | 1.015206 | 0.472544 | 0.031938 | 0.014858 | 0.046796 |
| by_direction | long | none | 0 | 0 | 1 | 1 | True | 100.0 | 1.48775 | 1.48775 |  | 1.48775 | inf | 0.0 | 1.48775 | 0.046972 | 0.031414 | 0.078386 |
| by_direction | short | none | 0 | 0 | 1 | 1 | True | 0.0 | -1.015206 |  | 1.015206 | -1.015206 | 0.0 | 1.015206 | -1.015206 | 0.016903 | -0.001697 | 0.015206 |
