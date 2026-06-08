# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_official_sp500_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 81 | 81 | -1.586453 | -0.070278 | 0.047457 | 128.898765 | 0.17284 | 1.512049 | 0.004126 | 1.516175 | 9 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-24 | 26 | 26 | -1.712907 | -0.384205 | 0.020588 | 44.53559 | 0.038462 | 1.321484 | 0.007218 | 1.328702 | 1 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2026-04-25 | 2026-05-09 | 27 | 27 | -2.021662 | -0.174608 | 0.017451 | 54.584886 | 0.148148 | 1.845438 | 0.001616 | 1.847054 | 2 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2026-05-10 | 2026-05-24 | 28 | 28 | -1.049365 | 0.321829 | 0.132723 | 29.778289 | 0.321429 | 1.367519 | 0.003675 | 1.371194 | 6 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
