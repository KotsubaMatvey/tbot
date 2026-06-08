# Trade P&L Report

- events: `backtest_results\ifvg_retest_15m_costed_oos_2022-01-01_2024-11-05_btc_eth\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 181 | 100 | True | 22.099448 | -1.310771 | 1.622677 | 2.142954 | -1.310771 | -4.937002 | 0.214813 | 237.907962 | 11 | -237.249465 | 1.543811 | 0.000197 | 1.544007 |
| filtered_all | ALL | model_rules | 0 | 234 | 4 | 100 | False | 100.0 | 0.755527 | 0.755527 |  | 0.755527 | 1.417637 | inf | 0.0 | 0 | 3.022109 | 0.135236 | 0.0 | 0.135236 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 2 | 100 | False | 100.0 | 1.16776 | 1.16776 |  | 1.16776 | 3.48454 | inf | 0.0 | 0 | 2.33552 | 0.113765 | 0.0 | 0.113765 |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 2 | 100 | False | 100.0 | 0.343295 | 0.343295 |  | 0.343295 | 2362.617253 | inf | 0.0 | 0 | 0.686589 | 0.156705 | 0.0 | 0.156705 |
| by_direction | long | model_rules | 0 | 0 | 3 | 100 | False | 100.0 | 0.877014 | 0.877014 |  | 0.877014 | 1.222409 | inf | 0.0 | 0 | 2.631041 | 0.144003 | 0.0 | 0.144003 |
| by_direction | short | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.391068 | 0.391068 |  | 0.391068 |  | inf | 0.0 | 0 | 0.391068 | 0.108932 | 0.0 | 0.108932 |
| by_displacement_grade | strong | model_rules | 0 | 0 | 4 | 100 | False | 100.0 | 0.755527 | 0.755527 |  | 0.755527 | 1.417637 | inf | 0.0 | 0 | 3.022109 | 0.135236 | 0.0 | 0.135236 |
| by_displacement_grade | valid | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | clean_equal_highs | model_rules | 0 | 0 | 3 | 100 | False | 100.0 | 0.877014 | 0.877014 |  | 0.877014 | 1.222409 | inf | 0.0 | 0 | 2.631041 | 0.144003 | 0.0 | 0.144003 |
| by_dol_target_type | clean_equal_lows | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | external_swing_high | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | external_swing_low | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.391068 | 0.391068 |  | 0.391068 |  | inf | 0.0 | 0 | 0.391068 | 0.108932 | 0.0 | 0.108932 |
| by_dol_source | local_eqh | model_rules | 0 | 0 | 3 | 100 | False | 100.0 | 0.877014 | 0.877014 |  | 0.877014 | 1.222409 | inf | 0.0 | 0 | 2.631041 | 0.144003 | 0.0 | 0.144003 |
| by_dol_source | local_eql | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_source | local_swing | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.391068 | 0.391068 |  | 0.391068 |  | inf | 0.0 | 0 | 0.391068 | 0.108932 | 0.0 | 0.108932 |
