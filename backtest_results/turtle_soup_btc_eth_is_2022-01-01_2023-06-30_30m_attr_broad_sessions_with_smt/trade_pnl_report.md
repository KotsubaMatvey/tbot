# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_broad_sessions_with_smt\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
| by_model | turtle_soup | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
| by_symbol | BTCUSDT | none | 0 | 0 | 30 | 100 | False | 80.0 | 0.324316 | 0.572756 | 0.669443 | 0.324316 | 2.511018 | 3.422285 | 1.468707 | 1 | 9.729493 | 0.54235 | 0.0 | 0.54235 |
| by_symbol | ETHUSDT | none | 0 | 0 | 31 | 100 | False | 77.419355 | 0.311169 | 0.576685 | 0.599173 | 0.311169 | 2.34608 | 3.299896 | 1.421822 | 2 | 9.646242 | 0.455647 | 0.0 | 0.455647 |
| by_timeframe | 30m | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
| by_direction | long | none | 0 | 0 | 29 | 100 | False | 89.655172 | 0.400554 | 0.565644 | 1.030232 | 0.400554 | 3.209983 | 4.758395 | 1.468707 | 1 | 11.616055 | 0.436876 | 0.0 | 0.436876 |
| by_direction | short | none | 0 | 0 | 32 | 100 | False | 68.75 | 0.24249 | 0.585448 | 0.512017 | 0.24249 | 1.847598 | 2.515512 | 1.343135 | 2 | 7.75968 | 0.553943 | 0.0 | 0.553943 |
| by_htf_bias | none | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
| by_htf_draw_direction | none | none | 0 | 0 | 61 | 100 | False | 78.688525 | 0.317635 | 0.574721 | 0.631605 | 0.317635 | 3.431275 | 3.359767 | 1.468707 | 2 | 19.375735 | 0.498288 | 0.0 | 0.498288 |
