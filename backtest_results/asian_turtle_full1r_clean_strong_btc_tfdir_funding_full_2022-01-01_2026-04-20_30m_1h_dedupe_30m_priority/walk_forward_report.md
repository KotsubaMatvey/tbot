# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_tfdir_funding_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-08 | 2026-03-30 | 28 | 28 | 0.44259 | 0.625149 | 4.081342 | 2.59007 | 0.785714 | 0.18359 | -0.001031 | 0.182559 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_total_trades |
| train | 2022-04-08 | 2023-08-20 | 9 | 9 | 0.242532 | 0.431971 | 1.836258 | 2.59007 | 0.666667 | 0.193517 | -0.004077 | 0.189439 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| validation | 2023-10-13 | 2024-06-01 | 9 | 9 | 0.340277 | 0.537866 | 3.223289 | 1.09839 | 0.777778 | 0.196716 | 0.000873 | 0.197589 | 0 | False | min_phase_trades |
| test | 2024-06-14 | 2026-03-30 | 10 | 10 | 0.714723 | 0.877564 | 210.307816 | 0.034147 | 0.9 | 0.162844 | -4e-06 | 0.16284 | 0 | True |  |
