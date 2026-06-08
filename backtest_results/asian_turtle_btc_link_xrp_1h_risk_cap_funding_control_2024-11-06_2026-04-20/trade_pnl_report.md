# Trade P&L Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_control_2024-11-06_2026-04-20\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 33 | 100 | False | 84.848485 | 0.543136 | 0.764163 | 0.694613 | 0.543136 | 6.16071 | 1.26004 | 17.923487 | 0.150158 | -0.002154 | 0.148003 |
| filtered_all | ALL | model_rules | 0 | 3 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
| by_model | turtle_soup | model_rules | 0 | 0 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 11 | 100 | False | 90.909091 | 0.641891 | 0.709495 | 0.034147 | 0.641891 | 207.776701 | 0.034147 | 7.060804 | 0.21202 | -0.002252 | 0.209768 |
| by_symbol | LINKUSDT | model_rules | 0 | 0 | 10 | 100 | False | 90.0 | 0.67689 | 0.868181 | 1.044737 | 0.67689 | 7.479043 | 1.044737 | 6.768896 | 0.123083 | 2.8e-05 | 0.12311 |
| by_symbol | XRPUSDT | model_rules | 0 | 0 | 9 | 100 | False | 77.777778 | 0.419263 | 0.87378 | 1.171544 | 0.419263 | 2.610426 | 1.26004 | 3.773371 | 0.140919 | -0.004627 | 0.136292 |
| by_timeframe | 1h | model_rules | 0 | 0 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
| by_direction | long | model_rules | 0 | 0 | 15 | 100 | False | 93.333333 | 0.69944 | 0.839403 | 1.26004 | 0.69944 | 9.3264 | 1.26004 | 10.491597 | 0.169088 | -0.001861 | 0.167227 |
| by_direction | short | model_rules | 0 | 0 | 15 | 100 | False | 80.0 | 0.474098 | 0.772784 | 0.720644 | 0.474098 | 4.289407 | 1.083048 | 7.111474 | 0.152999 | -0.002548 | 0.150452 |
| by_htf_bias | none | model_rules | 0 | 0 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 30 | 100 | False | 86.666667 | 0.586769 | 0.808655 | 0.855493 | 0.586769 | 6.144131 | 1.26004 | 17.603071 | 0.161044 | -0.002205 | 0.158839 |
