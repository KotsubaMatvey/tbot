# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_reclaim_oos_2022-01-01_2024-11-05_btc_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-24 | 2024-10-02 | 31 | 31 | 0.218642 | 0.368387 | 1.732759 | 3.237999 | 0.709677 | 0.149745 | 0.0 | 0.149745 | 0 | False | min_managed_expectancy_r;min_profit_factor |
| train | 2022-04-24 | 2023-02-28 | 10 | 10 | 0.320864 | 0.470155 | 2.368461 | 1.475246 | 0.8 | 0.149291 | 0.0 | 0.149291 | 0 | True |  |
| validation | 2023-04-12 | 2024-02-23 | 10 | 10 | 0.3243 | 0.477087 | 2.258393 | 1.140955 | 0.7 | 0.152787 | 0.0 | 0.152787 | 0 | True |  |
| test | 2024-03-12 | 2024-10-02 | 11 | 11 | 0.029661 | 0.177054 | 1.075385 | 3.237999 | 0.636364 | 0.147393 | 0.0 | 0.147393 | 0 | False | min_managed_expectancy_r;min_profit_factor |
