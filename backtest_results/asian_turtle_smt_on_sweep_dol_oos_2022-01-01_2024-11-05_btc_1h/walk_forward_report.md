# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_dol_oos_2022-01-01_2024-11-05_btc_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-27 | 2024-10-02 | 30 | 30 | 0.061161 | 0.208464 | 1.175881 | 4.833136 | 0.666667 | 0.147303 | 0 | False | min_managed_expectancy_r;min_profit_factor |
| train | 2022-03-27 | 2023-04-12 | 10 | 10 | 0.117397 | 0.262167 | 1.332846 | 3.527076 | 0.7 | 0.14477 | 0 | False | min_managed_expectancy_r |
| validation | 2023-07-11 | 2024-02-23 | 10 | 10 | 0.280228 | 0.426998 | 2.087377 | 1.140955 | 0.7 | 0.146771 | 0 | False | min_managed_expectancy_r |
| test | 2024-03-12 | 2024-10-02 | 10 | 10 | -0.214142 | -0.063773 | 0.505222 | 4.003897 | 0.6 | 0.150369 | 0 | False | min_managed_expectancy_r;min_profit_factor |
