# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_recent_sp500_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 58 | 58 | -1.26128 | 0.072371 | 0.075659 | 73.549031 | 0.206897 | 1.333651 | 6 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-24 | 20 | 20 | -1.192348 | -0.03764 | 0.037432 | 23.84696 | 0.05 | 1.154708 | 1 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2026-04-24 | 2026-05-08 | 20 | 20 | -1.69864 | -0.085721 | 0.026527 | 33.972805 | 0.2 | 1.612919 | 1 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2026-05-12 | 2026-05-24 | 20 | 20 | -0.89593 | 0.383237 | 0.187485 | 18.48149 | 0.35 | 1.279167 | 4 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
