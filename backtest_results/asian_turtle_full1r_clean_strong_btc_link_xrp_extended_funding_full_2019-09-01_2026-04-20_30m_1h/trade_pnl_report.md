# Trade P&L Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_full_2019-09-01_2026-04-20_30m_1h\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 215 | 100 | True | 71.162791 | 0.223097 | 0.724896 | 1.015212 | 0.223097 | 1.762051 | 5.356296 | 47.965891 | 0.15733 | 0.000907 | 0.158236 |
| filtered_all | ALL | model_rules | 0 | 131 | 84 | 100 | False | 76.190476 | 0.331925 | 0.72593 | 0.928892 | 0.331925 | 2.500805 | 4.997172 | 27.881713 | 0.144332 | -0.00132 | 0.143012 |
| by_model | turtle_soup | model_rules | 0 | 0 | 84 | 100 | False | 76.190476 | 0.331925 | 0.72593 | 0.928892 | 0.331925 | 2.500805 | 4.997172 | 27.881713 | 0.144332 | -0.00132 | 0.143012 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 42 | 100 | False | 78.571429 | 0.396601 | 0.69553 | 0.699474 | 0.396601 | 3.645995 | 2.272719 | 16.657232 | 0.168073 | -0.000964 | 0.16711 |
| by_symbol | LINKUSDT | model_rules | 0 | 0 | 23 | 100 | False | 69.565217 | 0.221986 | 0.805336 | 1.111386 | 0.221986 | 1.656282 | 4.997172 | 5.10568 | 0.121396 | -0.002698 | 0.118699 |
| by_symbol | XRPUSDT | model_rules | 0 | 0 | 19 | 100 | False | 78.947368 | 0.322042 | 0.708112 | 1.125718 | 0.322042 | 2.358866 | 2.196659 | 6.118801 | 0.119616 | -0.000441 | 0.119176 |
| by_timeframe | 1h | model_rules | 0 | 0 | 58 | 100 | False | 74.137931 | 0.291403 | 0.712512 | 0.915778 | 0.291403 | 2.230382 | 4.997172 | 16.901346 | 0.117774 | -2.9e-05 | 0.117745 |
| by_timeframe | 30m | model_rules | 0 | 0 | 26 | 100 | False | 80.769231 | 0.422322 | 0.753407 | 0.968234 | 0.422322 | 3.268123 | 2.540677 | 10.980367 | 0.203577 | -0.004201 | 0.199376 |
| by_direction | long | model_rules | 0 | 0 | 34 | 100 | False | 73.529412 | 0.295389 | 0.758715 | 0.99163 | 0.295389 | 2.125331 | 2.73935 | 10.04321 | 0.11024 | 0.004151 | 0.114391 |
| by_direction | short | model_rules | 0 | 0 | 50 | 100 | False | 78.0 | 0.35677 | 0.704915 | 0.877561 | 0.35677 | 2.847943 | 2.60184 | 17.838503 | 0.167515 | -0.00504 | 0.162474 |
| by_htf_bias | none | model_rules | 0 | 0 | 84 | 100 | False | 76.190476 | 0.331925 | 0.72593 | 0.928892 | 0.331925 | 2.500805 | 4.997172 | 27.881713 | 0.144332 | -0.00132 | 0.143012 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 84 | 100 | False | 76.190476 | 0.331925 | 0.72593 | 0.928892 | 0.331925 | 2.500805 | 4.997172 | 27.881713 | 0.144332 | -0.00132 | 0.143012 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 84 | 100 | False | 76.190476 | 0.331925 | 0.72593 | 0.928892 | 0.331925 | 2.500805 | 4.997172 | 27.881713 | 0.144332 | -0.00132 | 0.143012 |
