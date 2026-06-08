# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_early_2019-09-01_2021-12-31\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2020-01-22 | 2021-12-16 | 22 | 22 | 0.117699 | 0.232245 | 1.340414 | 5.619444 | 0.636364 | 0.112936 | 0.00161 | 0.114546 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2020-01-22 | 2020-08-30 | 7 | 7 | 0.483608 | 0.600925 | 4496.691899 | 0.000753 | 0.857143 | 0.111152 | 0.006165 | 0.117317 | 0 | False | min_phase_trades |
| validation | 2020-09-25 | 2021-06-30 | 9 | 9 | -0.207025 | -0.121899 | 0.65063 | 5.333097 | 0.444444 | 0.09053 | -0.005404 | 0.085126 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2021-06-30 | 2021-12-16 | 9 | 9 | -0.240193 | -0.111111 | 0.607086 | 3.51543 | 0.444444 | 0.124537 | 0.004544 | 0.129082 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
