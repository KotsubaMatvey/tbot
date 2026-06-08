# ICT Walk-Forward Quality Report

- events: `backtest_results\silver_bullet_costed_2025_btc_15m\events.csv`
- threshold: `70.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-01-10 | 2025-09-15 | 13 | 13 | -0.217593 | -0.008343 | 0.609781 | 4.777854 | 0.538462 | 0.20925 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-01-10 | 2025-03-08 | 4 | 4 | -0.4409 | -0.267208 | 0.285186 | 2.467216 | 0.5 | 0.173693 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2025-04-28 | 2025-06-02 | 4 | 4 | 0.928186 | 1.115093 | inf | 0.0 | 1.0 | 0.186907 | 0 | False | min_phase_trades |
| test | 2025-07-21 | 2025-09-15 | 5 | 5 | -0.955571 | -0.7 | 0.000829 | 4.777854 | 0.2 | 0.255571 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
