# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-03-04 | 2026-03-30 | 7 | 7 | 0.622188 | 0.766893 | 128.546139 | 0.034147 | 0.857143 | 0.144704 | 0.0 | 0.144704 | 1 | False | max_trades_per_session;min_phase_trades;min_total_trades |
| train | 2025-03-04 | 2025-03-16 | 2 | 2 | 0.459384 | 0.509757 | 27.906258 | 0.034147 | 0.5 | 0.050373 | 0.0 | 0.050373 | 0 | False | min_phase_trades |
| validation | 2025-05-14 | 2025-05-26 | 2 | 2 | 0.758219 | 1.0 | inf | 0.0 | 1.0 | 0.241781 | 0.0 | 0.241781 | 0 | False | min_phase_trades |
| test | 2025-08-25 | 2026-03-30 | 3 | 3 | 0.640037 | 0.782911 | inf | 0.0 | 1.0 | 0.142874 | 0.0 | 0.142874 | 1 | False | min_phase_trades |
