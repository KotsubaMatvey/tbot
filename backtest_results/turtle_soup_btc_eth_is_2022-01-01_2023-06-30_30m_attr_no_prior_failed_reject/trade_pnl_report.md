# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_no_prior_failed_reject\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
| by_model | turtle_soup | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
| by_symbol | BTCUSDT | none | 0 | 0 | 23 | 100 | False | 86.956522 | 0.448799 | 0.596663 | 0.53696 | 0.448799 | 3.521673 | 7.407918 | 1.468707 | 1 | 10.322381 | 0.461863 | 0.002381 | 0.464244 |
| by_symbol | ETHUSDT | none | 0 | 0 | 14 | 100 | False | 92.857143 | 0.537197 | 0.676536 | 1.274207 | 0.537197 | 3.244857 | 6.902305 | 1.274207 | 1 | 7.520758 | 0.319946 | 0.0 | 0.319946 |
| by_timeframe | 30m | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
| by_direction | long | none | 0 | 0 | 13 | 100 | False | 92.307692 | 0.383369 | 0.537709 | 1.468707 | 0.383369 | 1.991864 | 4.393326 | 1.468707 | 1 | 4.983802 | 0.456272 | 0.006512 | 0.462784 |
| by_direction | short | none | 0 | 0 | 24 | 100 | False | 87.5 | 0.535806 | 0.679796 | 0.472126 | 0.535806 | 4.707221 | 10.079023 | 1.274207 | 1 | 12.859337 | 0.382107 | -0.001246 | 0.380861 |
| by_htf_bias | none | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
| by_htf_draw_direction | none | none | 0 | 0 | 37 | 100 | False | 89.189189 | 0.482247 | 0.628128 | 0.721272 | 0.482247 | 4.694656 | 7.184613 | 1.468707 | 1 | 17.843139 | 0.408165 | 0.00148 | 0.409645 |
