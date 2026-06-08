# ICT Phase Attribution Report

- events: `backtest_results\ifvg_retest_15m_wide_stop_costed_late_2024-11-06_2026-04-20_btc_eth\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | False | none | 5 | 30 | False | 40.0 | -0.558968 | 0.199113 | 3.164835 | -2.794842 | 70.0 | 3.136879 | 66.824125 | 0.158968 | 0.0 | 0.158968 |
| train | ALL | ALL | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| train | by_symbol | ETHUSDT | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| train | by_direction | long | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| train | by_displacement_grade | valid | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| train | by_dol_target_type | clean_equal_highs | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| train | by_dol_source | local_eqh | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.324847 | inf | 0.0 | 0.324847 | 73.0 | 3.222408 | 57.092784 | 0.175153 | 0.0 | 0.175153 |
| validation | ALL | ALL | model_rules | 0 | False | none | 2 | 30 | False | 0.0 | -1.146801 | 0.0 | 2.293602 | -2.293602 | 68.0 | 3.451317 | 74.554733 | 0.146801 | 0.0 | 0.146801 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.103672 | 0.0 | 1.103672 | -1.103672 | 73.0 | 4.122439 | 96.458424 | 0.103672 | 0.0 | 0.103672 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.18993 | 0.0 | 1.18993 | -1.18993 | 63.0 | 2.780196 | 52.651042 | 0.18993 | 0.0 | 0.18993 |
| validation | by_direction | long | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.18993 | 0.0 | 1.18993 | -1.18993 | 63.0 | 2.780196 | 52.651042 | 0.18993 | 0.0 | 0.18993 |
| validation | by_direction | short | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.103672 | 0.0 | 1.103672 | -1.103672 | 73.0 | 4.122439 | 96.458424 | 0.103672 | 0.0 | 0.103672 |
| validation | by_displacement_grade | valid | model_rules | 0 | False | none | 2 | 30 | False | 0.0 | -1.146801 | 0.0 | 2.293602 | -2.293602 | 68.0 | 3.451317 | 74.554733 | 0.146801 | 0.0 | 0.146801 |
| validation | by_dol_target_type | clean_equal_lows | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.103672 | 0.0 | 1.103672 | -1.103672 | 73.0 | 4.122439 | 96.458424 | 0.103672 | 0.0 | 0.103672 |
| validation | by_dol_target_type | external_swing_high | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.18993 | 0.0 | 1.18993 | -1.18993 | 63.0 | 2.780196 | 52.651042 | 0.18993 | 0.0 | 0.18993 |
| validation | by_dol_source | local_eql | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.103672 | 0.0 | 1.103672 | -1.103672 | 73.0 | 4.122439 | 96.458424 | 0.103672 | 0.0 | 0.103672 |
| validation | by_dol_source | local_swing | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.18993 | 0.0 | 1.18993 | -1.18993 | 63.0 | 2.780196 | 52.651042 | 0.18993 | 0.0 | 0.18993 |
| test | ALL | ALL | model_rules | 0 | False | none | 2 | 30 | False | 50.0 | -0.413044 | 0.309338 | 1.19608 | -0.826087 | 70.5 | 2.779675 | 63.959187 | 0.163044 | 0.0 | 0.163044 |
| test | by_symbol | ETHUSDT | model_rules | 0 | False | none | 2 | 30 | False | 50.0 | -0.413044 | 0.309338 | 1.19608 | -0.826087 | 70.5 | 2.779675 | 63.959187 | 0.163044 | 0.0 | 0.163044 |
| test | by_direction | short | model_rules | 0 | False | none | 2 | 30 | False | 50.0 | -0.413044 | 0.309338 | 1.19608 | -0.826087 | 70.5 | 2.779675 | 63.959187 | 0.163044 | 0.0 | 0.163044 |
| test | by_displacement_grade | strong | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.369993 | inf | 0.0 | 0.369993 | 78.0 | 3.363188 | 76.918869 | 0.130007 | 0.0 | 0.130007 |
| test | by_displacement_grade | valid | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.19608 | 0.0 | 1.19608 | -1.19608 | 63.0 | 2.196163 | 50.999505 | 0.19608 | 0.0 | 0.19608 |
| test | by_dol_target_type | clean_equal_lows | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.369993 | inf | 0.0 | 0.369993 | 78.0 | 3.363188 | 76.918869 | 0.130007 | 0.0 | 0.130007 |
| test | by_dol_target_type | external_swing_low | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.19608 | 0.0 | 1.19608 | -1.19608 | 63.0 | 2.196163 | 50.999505 | 0.19608 | 0.0 | 0.19608 |
| test | by_dol_source | local_eql | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.369993 | inf | 0.0 | 0.369993 | 78.0 | 3.363188 | 76.918869 | 0.130007 | 0.0 | 0.130007 |
| test | by_dol_source | local_swing | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.19608 | 0.0 | 1.19608 | -1.19608 | 63.0 | 2.196163 | 50.999505 | 0.19608 | 0.0 | 0.19608 |
