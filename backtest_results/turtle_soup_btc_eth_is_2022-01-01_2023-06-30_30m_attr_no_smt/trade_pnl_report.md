# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_no_smt\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
| by_model | turtle_soup | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
| by_symbol | BTCUSDT | none | 0 | 0 | 170 | 100 | True | 67.058824 | 0.033138 | 0.616247 | 1.153906 | 0.033138 | 0.386737 | 1.08718 | 16.248001 | 6 | 5.633455 | 0.459402 | 0.000955 | 0.460357 |
| by_symbol | ETHUSDT | none | 0 | 0 | 176 | 100 | True | 64.772727 | -0.02188 | 0.651007 | 1.259124 | -0.02188 | -0.239484 | 0.950671 | 23.62968 | 5 | -3.850872 | 0.432258 | 0.000349 | 0.432607 |
| by_timeframe | 30m | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
| by_direction | long | none | 0 | 0 | 170 | 100 | True | 64.117647 | -0.019511 | 0.628393 | 1.177239 | -0.019511 | -0.216363 | 0.953813 | 12.902894 | 4 | -3.316791 | 0.462427 | 0.002598 | 0.465025 |
| by_direction | short | none | 0 | 0 | 176 | 100 | True | 67.613636 | 0.028974 | 0.638422 | 1.243383 | 0.028974 | 0.331281 | 1.071951 | 16.331222 | 5 | 5.099374 | 0.429335 | -0.001237 | 0.428098 |
| by_htf_bias | none | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
| by_htf_draw_direction | none | none | 0 | 0 | 346 | 100 | True | 65.895954 | 0.005152 | 0.633627 | 1.20919 | 0.005152 | 0.082071 | 1.012493 | 23.62968 | 6 | 1.782583 | 0.445594 | 0.000647 | 0.446241 |
