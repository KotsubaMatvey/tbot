# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_optional_smt_strong_quality\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 691 | 100 | True | 60.492041 | -0.1486 | 0.590468 | 1.280214 | -0.1486 | -3.109495 | 0.706199 | 107.433563 | 8 | -102.682918 | 0.545047 | 0.000238 | 0.545285 |
| filtered_all | ALL | model_rules | 0 | 392 | 299 | 100 | True | 70.234114 | 0.115987 | 0.677337 | 1.208547 | 0.115987 | 1.804706 | 1.322423 | 11.333963 | 6 | 34.680031 | 0.359343 | 0.000508 | 0.359852 |
| by_has_smt_confirmation | False | model_rules | 0 | 0 | 263 | 100 | True | 71.48289 | 0.146863 | 0.679036 | 1.187115 | 0.146863 | 2.193933 | 1.433826 | 10.566678 | 6 | 38.625083 | 0.357463 | 0.000578 | 0.358041 |
| by_has_smt_confirmation | True | model_rules | 0 | 0 | 36 | 100 | False | 61.111111 | -0.109585 | 0.662816 | 1.323358 | -0.109585 | -0.529752 | 0.787065 | 8.367663 | 3 | -3.945052 | 0.373081 | 0.0 | 0.373081 |
| by_score_bucket | high | model_rules | 0 | 0 | 162 | 100 | True | 63.580247 | -0.041794 | 0.619854 | 1.196874 | -0.041794 | -0.460602 | 0.90412 | 14.001074 | 9 | -6.770612 | 0.445331 | 0.000697 | 0.446028 |
| by_score_bucket | medium | model_rules | 0 | 0 | 137 | 100 | True | 78.10219 | 0.302559 | 0.732671 | 1.231503 | 0.302559 | 3.543108 | 2.121952 | 4.056237 | 3 | 41.450643 | 0.257665 | 0.000286 | 0.257951 |
| by_turtle_quality | strong | model_rules | 0 | 0 | 299 | 100 | True | 70.234114 | 0.115987 | 0.677337 | 1.208547 | 0.115987 | 1.804706 | 1.322423 | 11.333963 | 6 | 34.680031 | 0.359343 | 0.000508 | 0.359852 |
| by_session_label | custom | model_rules | 0 | 0 | 55 | 100 | False | 72.727273 | 0.172061 | 0.686685 | 1.20027 | 0.172061 | 1.170242 | 1.525623 | 4.912664 | 2 | 9.463338 | 0.335432 | 0.0 | 0.335432 |
| by_session_label | london_open | model_rules | 0 | 0 | 92 | 100 | False | 68.478261 | 0.124408 | 0.652545 | 1.022922 | 0.124408 | 1.140156 | 1.385831 | 7.16723 | 5 | 11.445573 | 0.431526 | 0.001557 | 0.433083 |
| by_session_label | ny_open | model_rules | 0 | 0 | 152 | 100 | True | 70.394737 | 0.090599 | 0.688439 | 1.33093 | 0.090599 | 0.974336 | 1.229933 | 9.883991 | 3 | 13.77112 | 0.324306 | 5.8e-05 | 0.324364 |
| by_direction | long | model_rules | 0 | 0 | 140 | 100 | True | 68.571429 | 0.052793 | 0.660015 | 1.272057 | 0.052793 | 0.543866 | 1.132051 | 5.506362 | 3 | 7.390968 | 0.360174 | 0.001314 | 0.361489 |
| by_direction | short | model_rules | 0 | 0 | 159 | 100 | True | 71.698113 | 0.171629 | 0.691923 | 1.146448 | 0.171629 | 2.031033 | 1.528959 | 7.659566 | 6 | 27.289063 | 0.358612 | -0.000201 | 0.358411 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 138 | 100 | True | 71.014493 | 0.118314 | 0.661581 | 1.212688 | 0.118314 | 1.264701 | 1.336595 | 11.333963 | 6 | 16.327399 | 0.406062 | 0.000256 | 0.406318 |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 161 | 100 | True | 69.565217 | 0.113992 | 0.691123 | 1.205166 | 0.113992 | 1.309559 | 1.310782 | 7.098558 | 4 | 18.352632 | 0.319299 | 0.000725 | 0.320024 |
