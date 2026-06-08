# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nyopen_tfdir_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-05-23 | 2024-09-15 | 21 | 21 | 0.342047 | 0.530328 | 2.498465 | 2.579515 | 0.809524 | 0.188281 | 0.0 | 0.188281 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_total_trades |
| train | 2022-05-23 | 2023-04-30 | 7 | 7 | 0.371148 | 0.588551 | 2.768142 | 1.469358 | 0.857143 | 0.217403 | 0.0 | 0.217403 | 0 | False | min_phase_trades |
| validation | 2023-05-28 | 2023-12-06 | 7 | 7 | 0.269648 | 0.428571 | 1.844852 | 1.124006 | 0.714286 | 0.158923 | 0.0 | 0.158923 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| test | 2024-03-12 | 2024-09-15 | 7 | 7 | 0.385346 | 0.573863 | 3.474597 | 1.090045 | 0.857143 | 0.188517 | 0.0 | 0.188517 | 0 | False | min_phase_trades |
