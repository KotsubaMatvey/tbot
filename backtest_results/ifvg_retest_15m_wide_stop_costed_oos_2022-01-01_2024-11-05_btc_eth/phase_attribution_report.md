# ICT Phase Attribution Report

- events: `backtest_results\ifvg_retest_15m_wide_stop_costed_oos_2022-01-01_2024-11-05_btc_eth\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | False | none | 4 | 30 | False | 75.0 | -0.002255 | 0.991643 | 1.07947 | -0.009021 | 69.25 | 2.562878 | 84.673764 | 0.127255 | 0.0 | 0.127255 |
| train | ALL | ALL | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| train | by_symbol | ETHUSDT | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| train | by_direction | short | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| train | by_displacement_grade | strong | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| train | by_dol_target_type | external_swing_low | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| train | by_dol_source | local_swing | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.342504 | inf | 0.0 | 0.342504 | 68.0 | 2.698505 | 63.493603 | 0.157496 | 0.0 | 0.157496 |
| validation | ALL | ALL | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| validation | by_direction | short | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| validation | by_displacement_grade | valid | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| validation | by_dol_target_type | external_swing_low | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| validation | by_dol_source | local_swing | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.380992 | inf | 0.0 | 0.380992 | 63.0 | 2.040118 | 84.027631 | 0.119008 | 0.0 | 0.119008 |
| test | ALL | ALL | model_rules | 0 | False | none | 2 | 30 | False | 50.0 | -0.366258 | 0.321411 | 1.07947 | -0.732517 | 73.0 | 2.756445 | 95.586911 | 0.116258 | 0.0 | 0.116258 |
| test | by_symbol | BTCUSDT | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.346953 | inf | 0.0 | 0.346953 | 78.0 | 3.333167 | 65.33948 | 0.153047 | 0.0 | 0.153047 |
| test | by_symbol | ETHUSDT | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.07947 | 0.0 | 1.07947 | -1.07947 | 68.0 | 2.179722 | 125.834343 | 0.07947 | 0.0 | 0.07947 |
| test | by_direction | long | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.07947 | 0.0 | 1.07947 | -1.07947 | 68.0 | 2.179722 | 125.834343 | 0.07947 | 0.0 | 0.07947 |
| test | by_direction | short | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.346953 | inf | 0.0 | 0.346953 | 78.0 | 3.333167 | 65.33948 | 0.153047 | 0.0 | 0.153047 |
| test | by_displacement_grade | strong | model_rules | 0 | False | none | 2 | 30 | False | 50.0 | -0.366258 | 0.321411 | 1.07947 | -0.732517 | 73.0 | 2.756445 | 95.586911 | 0.116258 | 0.0 | 0.116258 |
| test | by_dol_target_type | clean_equal_highs | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.07947 | 0.0 | 1.07947 | -1.07947 | 68.0 | 2.179722 | 125.834343 | 0.07947 | 0.0 | 0.07947 |
| test | by_dol_target_type | clean_equal_lows | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.346953 | inf | 0.0 | 0.346953 | 78.0 | 3.333167 | 65.33948 | 0.153047 | 0.0 | 0.153047 |
| test | by_dol_source | local_eqh | model_rules | 0 | False | none | 1 | 30 | False | 0.0 | -1.07947 | 0.0 | 1.07947 | -1.07947 | 68.0 | 2.179722 | 125.834343 | 0.07947 | 0.0 | 0.07947 |
| test | by_dol_source | local_eql | model_rules | 0 | False | none | 1 | 30 | False | 100.0 | 0.346953 | inf | 0.0 | 0.346953 | 78.0 | 3.333167 | 65.33948 | 0.153047 | 0.0 | 0.153047 |
