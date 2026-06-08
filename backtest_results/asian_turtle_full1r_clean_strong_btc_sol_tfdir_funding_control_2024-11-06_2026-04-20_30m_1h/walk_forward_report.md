# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_sol_tfdir_funding_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-03-04 | 2026-03-30 | 8 | 8 | 0.120533 | 0.296031 | 1.430393 | 2.206281 | 0.625 | 0.17554 | -4.2e-05 | 0.175498 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-03-04 | 2025-05-14 | 3 | 3 | 0.55809 | 0.673171 | 50.031277 | 0.034147 | 0.666667 | 0.114876 | 0.000205 | 0.115081 | 0 | False | min_phase_trades |
| validation | 2025-05-26 | 2025-09-12 | 3 | 3 | 0.028011 | 0.333333 | 1.072187 | 1.164092 | 0.666667 | 0.305323 | 0.0 | 0.305323 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2025-10-22 | 2026-03-30 | 2 | 2 | -0.397019 | -0.325633 | 0.238106 | 1.042189 | 0.5 | 0.071863 | -0.000477 | 0.071386 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
