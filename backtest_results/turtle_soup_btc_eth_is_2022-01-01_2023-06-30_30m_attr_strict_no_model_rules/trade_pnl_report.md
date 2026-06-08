# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_strict_no_model_rules\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
| by_model | turtle_soup | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
| by_symbol | BTCUSDT | none | 0 | 0 | 17 | 100 | False | 82.352941 | 0.393699 | 0.593125 | 0.53696 | 0.393699 | 2.375169 | 5.154797 | 1.468707 | 1 | 6.692876 | 0.485433 | 0.003222 | 0.488654 |
| by_symbol | ETHUSDT | none | 0 | 0 | 10 | 100 | False | 100.0 | 0.654791 | 0.654791 |  | 0.654791 | 9.885731 | inf | 0.0 | 0 | 6.547909 | 0.345209 | 0.0 | 0.345209 |
| by_timeframe | 30m | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
| by_direction | long | none | 0 | 0 | 10 | 100 | False | 90.0 | 0.354099 | 0.556633 | 1.468707 | 0.354099 | 1.613986 | 3.410957 | 1.468707 | 1 | 3.54099 | 0.437435 | 0.008466 | 0.445901 |
| by_direction | short | none | 0 | 0 | 17 | 100 | False | 88.235294 | 0.570576 | 0.656131 | 0.071086 | 0.570576 | 6.655566 | 69.225776 | 0.099277 | 1 | 9.699795 | 0.431182 | -0.001758 | 0.429424 |
| by_htf_bias | none | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
| by_htf_draw_direction | none | none | 0 | 0 | 27 | 100 | False | 88.888889 | 0.490399 | 0.618819 | 0.53696 | 0.490399 | 4.430751 | 9.219602 | 1.468707 | 1 | 13.240785 | 0.433498 | 0.002028 | 0.435526 |
