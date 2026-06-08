# ICT Walk-Forward Quality Report

- events: `backtest_results\silver_bullet_costed_2025_q3_btc_15m\events.csv`
- threshold: `70.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-07-21 | 2025-09-15 | 5 | 5 | -0.955571 | -0.7 | 0.000829 | 4.777854 | 0.2 | 0.255571 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-07-21 | 2025-07-21 | 1 | 1 | -1.155361 | -1.0 | 0.0 | 1.155361 | 0.0 | 0.155361 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2025-07-22 | 2025-08-14 | 2 | 2 | -1.123947 | -1.0 | 0.0 | 2.247895 | 0.0 | 0.123947 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2025-09-06 | 2025-09-15 | 2 | 2 | -0.687299 | -0.25 | 0.002875 | 1.378562 | 0.5 | 0.437299 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
