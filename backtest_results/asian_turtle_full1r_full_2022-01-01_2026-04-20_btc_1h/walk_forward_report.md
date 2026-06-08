# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_full_2022-01-01_2026-04-20_btc_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-27 | 2026-04-11 | 58 | 58 | 0.317314 | 0.46881 | 2.452905 | 2.778063 | 0.775862 | 0.151496 | 0.0 | 0.151496 | 0 | False | min_managed_expectancy_r |
| train | 2022-03-27 | 2023-10-13 | 19 | 19 | 0.347927 | 0.492853 | 2.417764 | 2.657618 | 0.789474 | 0.144926 | 0.0 | 0.144926 | 0 | True |  |
| validation | 2023-11-08 | 2024-09-15 | 19 | 19 | 0.124728 | 0.270043 | 1.410752 | 2.778063 | 0.684211 | 0.145315 | 0.0 | 0.145315 | 0 | False | min_managed_expectancy_r |
| test | 2024-10-02 | 2026-04-11 | 20 | 20 | 0.471187 | 0.634797 | 5.216536 | 1.102915 | 0.85 | 0.16361 | 0.0 | 0.16361 | 0 | True |  |
