# Trade P&L Report

- events: `backtest_results\ifvg_retest_15m_wide_stop_costed_oos_2022-01-01_2024-11-05_btc_eth\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 193 | 100 | True | 45.07772 | -0.514703 | 0.961517 | 1.726318 | -0.514703 | -2.409011 | 0.45714 | 104.955085 | 8 | -99.337771 | 0.995501 | 7.8e-05 | 0.995579 |
| filtered_all | ALL | model_rules | 0 | 321 | 4 | 100 | False | 75.0 | -0.002255 | 0.356816 | 1.07947 | -0.002255 | -0.004138 | 0.991643 | 1.07947 | 1 | -0.009021 | 0.127255 | 0.0 | 0.127255 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.346953 | 0.346953 |  | 0.346953 |  | inf | 0.0 | 0 | 0.346953 | 0.153047 | 0.0 | 0.153047 |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 3 | 100 | False | 66.666667 | -0.118658 | 0.361748 | 1.07947 | -0.118658 | -0.162731 | 0.670233 | 1.07947 | 1 | -0.355974 | 0.118658 | 0.0 | 0.118658 |
| by_direction | long | model_rules | 0 | 0 | 1 | 100 | False | 0.0 | -1.07947 |  | 1.07947 | -1.07947 |  | 0.0 | 1.07947 | 1 | -1.07947 | 0.07947 | 0.0 | 0.07947 |
| by_direction | short | model_rules | 0 | 0 | 3 | 100 | False | 100.0 | 0.356816 | 0.356816 |  | 0.356816 | 19.602517 | inf | 0.0 | 0 | 1.070449 | 0.143184 | 0.0 | 0.143184 |
| by_displacement_grade | strong | model_rules | 0 | 0 | 3 | 100 | False | 66.666667 | -0.130004 | 0.344728 | 1.07947 | -0.130004 | -0.18047 | 0.6387 | 1.07947 | 1 | -0.390013 | 0.130004 | 0.0 | 0.130004 |
| by_displacement_grade | valid | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.380992 | 0.380992 |  | 0.380992 |  | inf | 0.0 | 0 | 0.380992 | 0.119008 | 0.0 | 0.119008 |
| by_dol_target_type | clean_equal_highs | model_rules | 0 | 0 | 1 | 100 | False | 0.0 | -1.07947 |  | 1.07947 | -1.07947 |  | 0.0 | 1.07947 | 1 | -1.07947 | 0.07947 | 0.0 | 0.07947 |
| by_dol_target_type | clean_equal_lows | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.346953 | 0.346953 |  | 0.346953 |  | inf | 0.0 | 0 | 0.346953 | 0.153047 | 0.0 | 0.153047 |
| by_dol_target_type | external_swing_high | model_rules | 0 | 0 | 0 | 100 | False |  |  |  |  |  |  |  |  | 0 |  |  |  |  |
| by_dol_target_type | external_swing_low | model_rules | 0 | 0 | 2 | 100 | False | 100.0 | 0.361748 | 0.361748 |  | 0.361748 | 41.209667 | inf | 0.0 | 0 | 0.723496 | 0.138252 | 0.0 | 0.138252 |
| by_dol_source | local_eqh | model_rules | 0 | 0 | 1 | 100 | False | 0.0 | -1.07947 |  | 1.07947 | -1.07947 |  | 0.0 | 1.07947 | 1 | -1.07947 | 0.07947 | 0.0 | 0.07947 |
| by_dol_source | local_eql | model_rules | 0 | 0 | 1 | 100 | False | 100.0 | 0.346953 | 0.346953 |  | 0.346953 |  | inf | 0.0 | 0 | 0.346953 | 0.153047 | 0.0 | 0.153047 |
| by_dol_source | local_swing | model_rules | 0 | 0 | 2 | 100 | False | 100.0 | 0.361748 | 0.361748 |  | 0.361748 | 41.209667 | inf | 0.0 | 0 | 0.723496 | 0.138252 | 0.0 | 0.138252 |
