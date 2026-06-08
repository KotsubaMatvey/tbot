# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-08 | 2026-03-30 | 28 | 28 | 0.441559 | 0.625149 | 4.045525 | 2.604982 | 0.785714 | 0.18359 | 0.0 | 0.18359 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_total_trades |
| train | 2022-04-08 | 2023-08-20 | 9 | 9 | 0.238455 | 0.431971 | 1.814488 | 2.604982 | 0.666667 | 0.193517 | 0.0 | 0.193517 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| validation | 2023-10-13 | 2024-06-01 | 9 | 9 | 0.34115 | 0.537866 | 3.207989 | 1.090045 | 0.777778 | 0.196716 | 0.0 | 0.196716 | 0 | False | min_phase_trades |
| test | 2024-06-14 | 2026-03-30 | 10 | 10 | 0.71472 | 0.877564 | 210.306733 | 0.034147 | 0.9 | 0.162844 | 0.0 | 0.162844 | 0 | True |  |
