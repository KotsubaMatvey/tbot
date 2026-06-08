# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_dol_oos_2022-01-01_2024-11-05_btc_1h_tp1full_allsignals\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-27 | 2024-10-05 | 32 | 32 | 0.318196 | 0.504452 | 2.469883 | 1.665064 | 0.78125 | 0.186256 | 0.0 | 0.186256 | 0 | False | min_managed_expectancy_r |
| train | 2022-03-27 | 2023-07-22 | 10 | 10 | 0.272918 | 0.511985 | 2.061417 | 1.497885 | 0.7 | 0.239068 | 0.0 | 0.239068 | 0 | False | min_managed_expectancy_r |
| validation | 2023-08-23 | 2024-05-05 | 11 | 11 | 0.49905 | 0.658566 | 5.81136 | 1.140955 | 0.909091 | 0.159517 | 0.0 | 0.159517 | 0 | True |  |
| test | 2024-05-08 | 2024-10-05 | 11 | 11 | 0.178503 | 0.343489 | 1.610733 | 1.665064 | 0.727273 | 0.164985 | 0.0 | 0.164985 | 0 | False | min_managed_expectancy_r |
