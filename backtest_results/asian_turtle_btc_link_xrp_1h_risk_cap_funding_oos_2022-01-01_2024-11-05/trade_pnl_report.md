# Trade P&L Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_oos_2022-01-01_2024-11-05\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 58 | 100 | False | 72.413793 | 0.20712 | 0.692703 | 1.067535 | 0.20712 | 1.703313 | 3.239181 | 12.01297 | 0.149302 | 0.002127 | 0.151429 |
| filtered_all | ALL | model_rules | 0 | 3 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
| by_model | turtle_soup | model_rules | 0 | 0 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 29 | 100 | False | 68.965517 | 0.192878 | 0.740771 | 1.024662 | 0.192878 | 1.606538 | 3.30567 | 5.593468 | 0.157066 | 0.002764 | 0.15983 |
| by_symbol | LINKUSDT | model_rules | 0 | 0 | 16 | 100 | False | 68.75 | 0.152411 | 0.734442 | 1.128057 | 0.152411 | 1.43235 | 2.602442 | 2.438577 | 0.105155 | -0.004607 | 0.100548 |
| by_symbol | XRPUSDT | model_rules | 0 | 0 | 10 | 100 | False | 80.0 | 0.282343 | 0.630218 | 1.109157 | 0.282343 | 2.272782 | 1.135451 | 2.82343 | 0.229717 | 0.010863 | 0.24058 |
| by_timeframe | 1h | model_rules | 0 | 0 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
| by_direction | long | model_rules | 0 | 0 | 28 | 100 | False | 75.0 | 0.267489 | 0.726511 | 1.109578 | 0.267489 | 1.964291 | 4.189373 | 7.489689 | 0.145643 | 0.010016 | 0.155659 |
| by_direction | short | model_rules | 0 | 0 | 27 | 100 | False | 66.666667 | 0.124659 | 0.704405 | 1.034834 | 0.124659 | 1.361388 | 2.121386 | 3.365786 | 0.165058 | -0.006125 | 0.158933 |
| by_htf_bias | none | model_rules | 0 | 0 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
| by_htf_context_alignment | neutral | model_rules | 0 | 0 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
| by_htf_draw_direction | none | model_rules | 0 | 0 | 55 | 100 | False | 70.909091 | 0.197372 | 0.716308 | 1.067535 | 0.197372 | 1.635546 | 4.159443 | 10.855475 | 0.155174 | 0.002092 | 0.157266 |
