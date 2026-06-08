# Trade P&L Report

- events: `backtest_results\ifvg_retest_15m_costed_late_2024-11-06_2026-04-20_btc_eth\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 110 | 100 | True | 25.454545 | -1.402973 | 1.217813 | 2.297876 | -1.402973 | -6.342437 | 0.180967 | 154.327029 | 11 | -154.327029 | 1.438262 | 0.001097 | 1.439359 |
| filtered_all | ALL | model_rules | 0 | 165 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_direction | long | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_direction | short | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_displacement_grade | strong | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_displacement_grade | valid | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | clean_equal_highs | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | clean_equal_lows | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | external_swing_high | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | external_swing_low | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_source | local_eqh | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_source | local_eql | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_source | local_swing | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
