# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_oos_2022-01-01_2024-11-05_btc_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-27 | 2024-10-02 | 30 | 30 | 0.014625 | 0.161928 | 1.031894 | 4.74746 | 0.566667 | 0.147303 | 0 | False | min_managed_expectancy_r;min_profit_factor |
| train | 2022-03-27 | 2023-04-12 | 10 | 10 | -0.036073 | 0.108697 | 0.93684 | 4.08667 | 0.5 | 0.14477 | 0 | False | min_managed_expectancy_r;min_profit_factor |
| validation | 2023-07-11 | 2024-02-23 | 10 | 10 | 0.280316 | 0.427087 | 2.087722 | 1.140955 | 0.7 | 0.146771 | 0 | False | min_managed_expectancy_r |
| test | 2024-03-12 | 2024-10-02 | 10 | 10 | -0.200369 | -0.05 | 0.633557 | 4.226754 | 0.5 | 0.150369 | 0 | False | min_managed_expectancy_r;min_profit_factor |
