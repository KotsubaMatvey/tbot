# Trade P&L Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 124 | 100 | True | 70.16129 | 0.167312 | 0.699611 | 1.084312 | 0.167312 | 1.51712 | 3.661615 | 20.746631 | 0.167758 | 0.001557 | 0.169315 |
| filtered_all | ALL | model_rules | 0 | 76 | 48 | 100 | False | 79.166667 | 0.358674 | 0.707634 | 0.967371 | 0.358674 | 2.779708 | 4.05857 | 17.216371 | 0.159768 | -0.000936 | 0.158833 |
| by_model | turtle_soup | model_rules | 0 | 0 | 48 | 100 | False | 79.166667 | 0.358674 | 0.707634 | 0.967371 | 0.358674 | 2.779708 | 4.05857 | 17.216371 | 0.159768 | -0.000936 | 0.158833 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 28 | 100 | False | 82.142857 | 0.449152 | 0.72017 | 0.797529 | 0.449152 | 4.15381 | 1.469358 | 12.57627 | 0.18311 | -0.000973 | 0.182138 |
| by_symbol | LINKUSDT | model_rules | 0 | 0 | 16 | 100 | False | 68.75 | 0.17839 | 0.776391 | 1.137212 | 0.17839 | 1.501971 | 4.05857 | 2.854237 | 0.126387 | -0.002542 | 0.123845 |
| by_symbol | XRPUSDT | model_rules | 0 | 0 | 4 | 100 | False | 100.0 | 0.446466 | 0.446466 |  | 0.446466 | inf | 0.0 | 1.785864 | 0.129903 | 0.005749 | 0.135652 |
| by_timeframe | 1h | model_rules | 0 | 0 | 30 | 100 | False | 76.666667 | 0.29688 | 0.692852 | 1.004171 | 0.29688 | 2.26706 | 2.903531 | 8.906409 | 0.123705 | 0.001955 | 0.125659 |
| by_timeframe | 30m | model_rules | 0 | 0 | 18 | 100 | False | 83.333333 | 0.461665 | 0.730298 | 0.881504 | 0.461665 | 4.142344 | 1.469358 | 8.309962 | 0.219874 | -0.005753 | 0.214122 |
| by_direction | long | model_rules | 0 | 0 | 16 | 100 | False | 75.0 | 0.272718 | 0.730891 | 1.1018 | 0.272718 | 1.990082 | 1.822873 | 4.363488 | 0.107398 | 0.00763 | 0.115028 |
| by_direction | short | model_rules | 0 | 0 | 32 | 100 | False | 81.25 | 0.401653 | 0.6969 | 0.877751 | 0.401653 | 3.440496 | 2.377252 | 12.852883 | 0.185953 | -0.005219 | 0.180735 |
| by_htf_bias | none | model_rules | 0 | 0 | 48 | 100 | False | 79.166667 | 0.358674 | 0.707634 | 0.967371 | 0.358674 | 2.779708 | 4.05857 | 17.216371 | 0.159768 | -0.000936 | 0.158833 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 48 | 100 | False | 79.166667 | 0.358674 | 0.707634 | 0.967371 | 0.358674 | 2.779708 | 4.05857 | 17.216371 | 0.159768 | -0.000936 | 0.158833 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 48 | 100 | False | 79.166667 | 0.358674 | 0.707634 | 0.967371 | 0.358674 | 2.779708 | 4.05857 | 17.216371 | 0.159768 | -0.000936 | 0.158833 |
