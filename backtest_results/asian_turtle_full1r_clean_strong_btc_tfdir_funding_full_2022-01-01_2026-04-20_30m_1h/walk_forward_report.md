# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_tfdir_funding_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-08 | 2026-03-30 | 28 | 28 | 0.42516 | 0.600001 | 3.959993 | 2.59007 | 0.785714 | 0.175376 | -0.000535 | 0.174841 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_total_trades |
| train | 2022-04-08 | 2023-08-20 | 9 | 9 | 0.244969 | 0.431971 | 1.84466 | 2.59007 | 0.666667 | 0.189535 | -0.002532 | 0.187002 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| validation | 2023-10-13 | 2024-06-01 | 9 | 9 | 0.340814 | 0.53199 | 3.226797 | 1.09839 | 0.777778 | 0.190303 | 0.000873 | 0.191176 | 0 | False | min_phase_trades |
| test | 2024-06-14 | 2026-03-30 | 10 | 10 | 0.663243 | 0.812437 | 195.231675 | 0.034147 | 0.9 | 0.149198 | -4e-06 | 0.149194 | 0 | True |  |
