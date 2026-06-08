# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 27 | 100 | False | 66.666667 | 0.074403 | 0.696987 | 1.170765 | 0.074403 | 0.341904 | 1.190652 | 3.200204 | 3 | 2.00888 | 0.198468 | 0.001148 | 0.199616 |
| filtered_all | ALL | model_rules | 0 | 15 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
| by_model | turtle_soup | model_rules | 0 | 0 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 8 | 100 | False | 50.0 | -0.128605 | 0.819637 | 1.076846 | -0.128605 | -0.315786 | 0.761146 | 2.975433 | 2 | -1.028837 | 0.26124 | 0.004144 | 0.265384 |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 4 | 100 | False | 100.0 | 0.757047 | 0.757047 |  | 0.757047 | 5.885292 | inf | 0.0 | 0 | 3.028188 | 0.117411 | 0.0 | 0.117411 |
| by_timeframe | 30m | model_rules | 0 | 0 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
| by_direction | long | model_rules | 0 | 0 | 4 | 100 | False | 50.0 | -0.258583 | 0.89179 | 1.408956 | -0.258583 | -0.555159 | 0.632944 | 1.928691 | 1 | -1.034332 | 0.244932 | 0.013651 | 0.258583 |
| by_direction | short | model_rules | 0 | 0 | 8 | 100 | False | 75.0 | 0.37921 | 0.753859 | 0.744736 | 0.37921 | 1.241943 | 3.036751 | 1.469358 | 1 | 3.033683 | 0.197479 | -0.002681 | 0.194797 |
| by_htf_bias | none | model_rules | 0 | 0 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 12 | 100 | False | 66.666667 | 0.166613 | 0.788342 | 1.076846 | 0.166613 | 0.543952 | 1.464168 | 2.975433 | 2 | 1.999351 | 0.213297 | 0.002763 | 0.216059 |
