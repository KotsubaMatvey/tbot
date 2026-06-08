# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_split_session_tfdir_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-08 | 2026-03-30 | 36 | 36 | 0.385174 | 0.559066 | 3.20317 | 2.821551 | 0.777778 | 0.173892 | 0.0 | 0.173892 | 0 | False | min_managed_expectancy_r |
| train | 2022-04-08 | 2023-04-30 | 11 | 11 | 0.452875 | 0.655826 | 4.322696 | 1.469358 | 0.818182 | 0.202951 | 0.0 | 0.202951 | 0 | True |  |
| validation | 2023-05-28 | 2024-04-07 | 12 | 12 | 0.17031 | 0.330195 | 1.556825 | 1.424525 | 0.666667 | 0.159885 | 0.0 | 0.159885 | 0 | False | min_managed_expectancy_r |
| test | 2024-04-23 | 2026-03-30 | 13 | 13 | 0.526223 | 0.688457 | 7.085174 | 1.090045 | 0.846154 | 0.162234 | 0.0 | 0.162234 | 0 | True |  |
