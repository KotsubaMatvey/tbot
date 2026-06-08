# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_control_2024-11-06_2026-04-20\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2024-12-10 | 2026-04-11 | 30 | 30 | 0.586769 | 0.745608 | 6.144131 | 1.26004 | 0.866667 | 0.161044 | -0.002205 | 0.158839 | 0 | False | min_phase_trades;min_total_trades |
| train | 2024-12-10 | 2025-05-12 | 10 | 10 | 0.596661 | 0.701951 | 6.530355 | 1.044737 | 0.8 | 0.105382 | -9.2e-05 | 0.10529 | 0 | False | min_phase_trades |
| validation | 2025-05-14 | 2025-11-15 | 10 | 10 | 0.860617 | 1.0 | inf | 0.0 | 1.0 | 0.143299 | -0.003915 | 0.139383 | 0 | False | min_phase_trades |
| test | 2025-11-23 | 2026-04-11 | 10 | 10 | 0.303029 | 0.534873 | 2.29329 | 1.26004 | 0.8 | 0.23445 | -0.002606 | 0.231844 | 0 | False | min_phase_trades |
