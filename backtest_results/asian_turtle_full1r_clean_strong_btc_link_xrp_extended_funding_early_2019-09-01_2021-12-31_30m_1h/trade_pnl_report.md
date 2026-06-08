# Trade P&L Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_early_2019-09-01_2021-12-31_30m_1h\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 33 | 100 | False | 60.606061 | 0.071396 | 0.773259 | 1.008393 | 0.071396 | 1.179728 | 4.79423 | 2.356077 | 0.110577 | 0.003159 | 0.113737 |
| filtered_all | ALL | model_rules | 0 | 16 | 17 | 100 | False | 52.941176 | -0.0641 | 0.724473 | 0.951243 | -0.0641 | 0.856807 | 5.634028 | -1.089693 | 0.101984 | -0.00074 | 0.101245 |
| by_model | turtle_soup | model_rules | 0 | 0 | 17 | 100 | False | 52.941176 | -0.0641 | 0.724473 | 0.951243 | -0.0641 | 0.856807 | 5.634028 | -1.089693 | 0.101984 | -0.00074 | 0.101245 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 8 | 100 | False | 62.5 | 0.07596 | 0.576231 | 0.757824 | 0.07596 | 1.267292 | 2.272719 | 0.607682 | 0.129705 | -0.001731 | 0.127973 |
| by_symbol | LINKUSDT | model_rules | 0 | 0 | 3 | 100 | False | 33.333333 | -0.388217 | 0.928991 | 1.04682 | -0.388217 | 0.44372 | 2.093641 | -1.16465 | 0.06285 | -0.007967 | 0.054883 |
| by_symbol | XRPUSDT | model_rules | 0 | 0 | 6 | 100 | False | 50.0 | -0.088787 | 0.903369 | 1.080944 | -0.088787 | 0.835722 | 2.196659 | -0.532725 | 0.084591 | 0.004196 | 0.088788 |
| by_timeframe | 1h | model_rules | 0 | 0 | 13 | 100 | False | 53.846154 | -0.041112 | 0.696976 | 0.902214 | -0.041112 | 0.90127 | 3.437369 | -0.534453 | 0.090655 | -0.000968 | 0.089686 |
| by_timeframe | 30m | model_rules | 0 | 0 | 4 | 100 | False | 50.0 | -0.13881 | 0.820709 | 1.098329 | -0.13881 | 0.747234 | 2.196659 | -0.55524 | 0.138806 | 4e-06 | 0.13881 |
| by_direction | long | model_rules | 0 | 0 | 10 | 100 | False | 60.0 | 0.085758 | 0.685834 | 0.814357 | 0.085758 | 1.263268 | 1.282264 | 0.857576 | 0.082012 | 0.005086 | 0.087098 |
| by_direction | short | model_rules | 0 | 0 | 7 | 100 | False | 42.857143 | -0.278181 | 0.801749 | 1.088129 | -0.278181 | 0.552611 | 4.352517 | -1.947269 | 0.130517 | -0.009062 | 0.121454 |
| by_htf_bias | none | model_rules | 0 | 0 | 17 | 100 | False | 52.941176 | -0.0641 | 0.724473 | 0.951243 | -0.0641 | 0.856807 | 5.634028 | -1.089693 | 0.101984 | -0.00074 | 0.101245 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 17 | 100 | False | 52.941176 | -0.0641 | 0.724473 | 0.951243 | -0.0641 | 0.856807 | 5.634028 | -1.089693 | 0.101984 | -0.00074 | 0.101245 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 17 | 100 | False | 52.941176 | -0.0641 | 0.724473 | 0.951243 | -0.0641 | 0.856807 | 5.634028 | -1.089693 | 0.101984 | -0.00074 | 0.101245 |
