# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_tfdir_funding_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-03-04 | 2026-03-30 | 6 | 6 | 0.57888 | 0.728041 | 102.715524 | 0.034147 | 0.833333 | 0.149059 | 0.000102 | 0.149161 | 0 | False | min_phase_trades;min_total_trades |
| train | 2025-03-04 | 2025-03-16 | 2 | 2 | 0.459076 | 0.509757 | 27.888248 | 0.034147 | 0.5 | 0.050373 | 0.000307 | 0.050681 | 0 | False | min_phase_trades |
| validation | 2025-05-14 | 2025-05-26 | 2 | 2 | 0.758219 | 1.0 | inf | 0.0 | 1.0 | 0.241781 | 0.0 | 0.241781 | 0 | False | min_phase_trades |
| test | 2026-03-30 | 2026-03-30 | 2 | 2 | 0.519344 | 0.674367 | inf | 0.0 | 1.0 | 0.155023 | 0.0 | 0.155023 | 0 | False | min_phase_trades |
