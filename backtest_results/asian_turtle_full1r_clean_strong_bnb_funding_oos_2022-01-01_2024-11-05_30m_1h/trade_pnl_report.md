# Trade P&L Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_bnb_funding_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 31 | 100 | False | 67.741935 | 0.045855 | 0.58468 | 1.085677 | 0.045855 | 1.130933 | 4.540638 | 1.421504 | 0.168156 | -0.005353 | 0.162803 |
| filtered_all | ALL | model_rules | 0 | 15 | 16 | 100 | False | 81.25 | 0.183697 | 0.480245 | 1.101341 | 0.183697 | 1.889569 | 2.525597 | 2.939156 | 0.166742 | 1.7e-05 | 0.166759 |
| by_model | turtle_soup | model_rules | 0 | 0 | 16 | 100 | False | 81.25 | 0.183697 | 0.480245 | 1.101341 | 0.183697 | 1.889569 | 2.525597 | 2.939156 | 0.166742 | 1.7e-05 | 0.166759 |
| by_symbol | BNBUSDT | model_rules | 0 | 0 | 16 | 100 | False | 81.25 | 0.183697 | 0.480245 | 1.101341 | 0.183697 | 1.889569 | 2.525597 | 2.939156 | 0.166742 | 1.7e-05 | 0.166759 |
| by_timeframe | 1h | model_rules | 0 | 0 | 10 | 100 | False | 90.0 | 0.296175 | 0.451422 | 1.10104 | 0.296175 | 3.68996 | 1.10104 | 2.961754 | 0.141157 | 2.7e-05 | 0.141184 |
| by_timeframe | 30m | model_rules | 0 | 0 | 6 | 100 | False | 66.666667 | -0.003766 | 0.545096 | 1.101491 | -0.003766 | 0.989742 | 2.202983 | -0.022598 | 0.209385 | 0.0 | 0.209385 |
| by_direction | long | model_rules | 0 | 0 | 6 | 100 | False | 100.0 | 0.377619 | 0.377619 |  | 0.377619 | inf | 0.0 | 2.265714 | 0.159464 | 4.5e-05 | 0.159509 |
| by_direction | short | model_rules | 0 | 0 | 10 | 100 | False | 70.0 | 0.067344 | 0.568209 | 1.101341 | 0.067344 | 1.203825 | 2.658953 | 0.673442 | 0.171109 | 0.0 | 0.171109 |
