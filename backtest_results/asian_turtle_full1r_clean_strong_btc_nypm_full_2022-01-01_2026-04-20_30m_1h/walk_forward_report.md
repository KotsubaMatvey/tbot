# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nypm_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-02-11 | 2026-02-23 | 10 | 10 | -0.066168 | 0.129848 | 0.861944 | 2.623071 | 0.6 | 0.196016 | 0.0 | 0.196016 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2022-02-11 | 2022-12-14 | 3 | 3 | 0.236689 | 0.333333 | 1.668538 | 1.06212 | 0.666667 | 0.096644 | 0.0 | 0.096644 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| validation | 2023-05-13 | 2024-06-19 | 4 | 4 | -0.416262 | -0.17538 | 0.365229 | 2.623071 | 0.5 | 0.240882 | 0.0 | 0.240882 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2024-06-19 | 2026-02-23 | 4 | 4 | 0.261791 | 0.5 | 1.945412 | 1.107627 | 0.75 | 0.238209 | 0.0 | 0.238209 | 0 | False | min_phase_trades;min_managed_expectancy_r |
