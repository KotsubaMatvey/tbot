# Trade P&L Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_strong_no_smt_minrisk35_first\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | sharpe | profit_factor | max_drawdown_r | max_consecutive_losses | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 691 | 100 | True | 60.492041 | -0.1486 | 0.590468 | 1.280214 | -0.1486 | -3.109495 | 0.706199 | 107.433563 | 8 | -102.682918 | 0.545047 | 0.000238 | 0.545285 |
| filtered_all | ALL | model_rules | 0 | 548 | 143 | 100 | True | 77.622378 | 0.350612 | 0.795664 | 1.193162 | 0.350612 | 4.175081 | 2.313148 | 3.688448 | 3 | 50.13752 | 0.187745 | 0.0001 | 0.187845 |
| by_score_bucket | high | model_rules | 0 | 0 | 50 | 100 | False | 74.0 | 0.279876 | 0.800644 | 1.20231 | 0.279876 | 2.029221 | 1.895315 | 3.516586 | 3 | 13.993797 | 0.200621 | -0.000497 | 0.200124 |
| by_score_bucket | medium | model_rules | 0 | 0 | 93 | 100 | False | 79.569892 | 0.388642 | 0.793174 | 1.186902 | 0.388642 | 3.8643 | 2.602745 | 4.706021 | 2 | 36.143723 | 0.180823 | 0.000421 | 0.181244 |
| by_session_label | custom | model_rules | 0 | 0 | 27 | 100 | False | 85.185185 | 0.498964 | 0.797355 | 1.216785 | 0.498964 | 3.032222 | 3.767956 | 1.652727 | 1 | 13.47203 | 0.191248 | 0.0 | 0.191248 |
| by_session_label | london_open | model_rules | 0 | 0 | 33 | 100 | False | 81.818182 | 0.428268 | 0.790958 | 1.203839 | 0.428268 | 2.848362 | 2.956636 | 3.974252 | 2 | 14.132839 | 0.186389 | 0.000167 | 0.186556 |
| by_session_label | ny_open | model_rules | 0 | 0 | 83 | 100 | False | 73.493976 | 0.271478 | 0.797109 | 1.185954 | 0.271478 | 2.339382 | 1.863618 | 3.943041 | 3 | 22.532651 | 0.187145 | 0.000106 | 0.187251 |
| by_direction | long | model_rules | 0 | 0 | 65 | 100 | False | 78.461538 | 0.352212 | 0.773616 | 1.182904 | 0.352212 | 2.997912 | 2.382419 | 3.423439 | 3 | 22.893758 | 0.185528 | 0.000712 | 0.18624 |
| by_direction | short | model_rules | 0 | 0 | 78 | 100 | False | 76.923077 | 0.349279 | 0.814405 | 1.20114 | 0.349279 | 3.030489 | 2.260088 | 3.970324 | 2 | 27.243762 | 0.189593 | -0.00041 | 0.189183 |
| by_symbol | BTCUSDT | model_rules | 0 | 0 | 61 | 100 | False | 83.606557 | 0.446387 | 0.769438 | 1.20117 | 0.446387 | 3.956304 | 3.266925 | 2.319587 | 2 | 27.22963 | 0.200035 | 0.000579 | 0.200614 |
| by_symbol | ETHUSDT | model_rules | 0 | 0 | 82 | 100 | False | 73.170732 | 0.279365 | 0.817956 | 1.189521 | 0.279365 | 2.371978 | 1.875367 | 3.688448 | 3 | 22.90789 | 0.178603 | -0.000256 | 0.178347 |
| by_no_trade_reasons | none | model_rules | 0 | 0 | 50 | 100 | False | 74.0 | 0.279876 | 0.800644 | 1.20231 | 0.279876 | 2.029221 | 1.895315 | 3.516586 | 3 | 13.993797 | 0.200621 | -0.000497 | 0.200124 |
| by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | 0 | 66 | 100 | False | 81.818182 | 0.433315 | 0.793227 | 1.186289 | 0.433315 | 3.768092 | 3.008982 | 3.446392 | 2 | 28.598793 | 0.172143 | 0.000593 | 0.172736 |
| by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | 0 | 27 | 100 | False | 74.074074 | 0.279442 | 0.793031 | 1.187954 | 0.279442 | 1.412205 | 1.907314 | 2.993477 | 2 | 7.54493 | 0.20204 | 0.0 | 0.20204 |
