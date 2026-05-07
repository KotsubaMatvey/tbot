# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_debug_2025_btc_30m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-01-10 | 2025-12-17 | 23 | 23 | 0.078035 | 0.165108 | 1.195652 | 2.948196 | 0.565217 | 0.087072 | 1 | False | max_trades_per_session;min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-01-10 | 2025-03-10 | 7 | 7 | 0.331302 | 0.428571 | 2.059958 | 2.187929 | 0.714286 | 0.09727 | 0 | False | min_phase_trades |
| validation | 2025-03-11 | 2025-05-29 | 8 | 8 | -0.125348 | -0.052101 | 0.730188 | 2.948196 | 0.375 | 0.073247 | 1 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2025-06-05 | 2025-12-17 | 8 | 8 | 0.059811 | 0.151786 | 1.146373 | 2.150563 | 0.625 | 0.091975 | 0 | False | min_phase_trades |
