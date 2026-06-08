# Trade P&L Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_tfdir_funding_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
| by_model | turtle_soup | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
| by_symbol | BTCUSDT | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
| by_timeframe | 1h | none | 0 | 0 | 42 | 1 | True | 76.190476 | 0.3276 | 0.719229 | 0.92561 | 0.3276 | 2.486502 | 3.239181 | 13.759213 | 0.166055 | 0.001303 | 0.167358 |
| by_timeframe | 30m | none | 0 | 0 | 42 | 1 | True | 71.428571 | 0.16653 | 0.637085 | 1.009857 | 0.16653 | 1.577166 | 3.200204 | 6.994269 | 0.22057 | 0.000588 | 0.221158 |
| by_direction | long | none | 0 | 0 | 32 | 1 | True | 71.875 | 0.135193 | 0.675563 | 1.245752 | 0.135193 | 1.385861 | 4.973357 | 4.326182 | 0.188411 | 0.008827 | 0.197238 |
| by_direction | short | none | 0 | 0 | 52 | 1 | True | 75.0 | 0.31591 | 0.681793 | 0.78174 | 0.31591 | 2.616443 | 2.121386 | 16.4273 | 0.196329 | -0.003905 | 0.192424 |
| by_htf_bias | none | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
| by_htf_draw_direction | none | none | 0 | 0 | 84 | 1 | True | 73.809524 | 0.247065 | 0.679482 | 0.971563 | 0.247065 | 1.970951 | 3.239181 | 20.753482 | 0.193313 | 0.000945 | 0.194258 |
