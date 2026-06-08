# Trade P&L Report

- events: `backtest_results\ict2022_first_retested_fvg_research_2024_01_btc_30m_no_killzone\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_model | ict2022_mss_fvg | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_symbol | BTCUSDT | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_timeframe | 30m | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_direction | long | none | 0 | 0 | 8 | 30 | False | 75.0 | 0.138868 | 0.570521 | 1.156092 | 0.138868 | 1.480472 | 2.173221 | 1.110941 | 0.091006 | 0.004719 | 0.095725 |
| by_direction | short | none | 0 | 0 | 3 | 30 | False | 66.666667 | -0.139104 | 0.298947 | 1.015206 | -0.139104 | 0.588939 | 1.015206 | -0.417312 | 0.082877 | -0.000566 | 0.082311 |
| by_htf_bias | none | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
| by_htf_draw_direction | none | none | 0 | 0 | 11 | 30 | False | 72.727273 | 0.063057 | 0.502627 | 1.10913 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.088789 | 0.003277 | 0.092066 |
