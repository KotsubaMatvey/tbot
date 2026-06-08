# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_dol_full_2022-01-01_2026-04-20_btc_1h_tp1full_0900_1100\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-27 | 2026-04-11 | 49 | 49 | 0.352803 | 0.512502 | 2.722341 | 1.665064 | 0.816327 | 0.159699 | 0.0 | 0.159699 | 0 | False | min_managed_expectancy_r |
| train | 2022-03-27 | 2023-11-08 | 16 | 16 | 0.402579 | 0.552022 | 2.850766 | 1.475246 | 0.8125 | 0.149443 | 0.0 | 0.149443 | 0 | True |  |
| validation | 2023-11-30 | 2024-10-05 | 16 | 16 | 0.173705 | 0.334997 | 1.638034 | 1.665064 | 0.75 | 0.161292 | 0.0 | 0.161292 | 0 | False | min_managed_expectancy_r |
| test | 2024-11-14 | 2026-04-11 | 17 | 17 | 0.474518 | 0.642371 | 4.665399 | 1.102915 | 0.882353 | 0.167853 | 0.0 | 0.167853 | 0 | True |  |
