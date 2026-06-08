# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_recent_xyz100_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 44 | 44 | -1.416135 | 0.091727 | 0.111207 | 62.309952 | 0.272727 | 1.507862 | 8 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-14 | 14 | 14 | -1.621771 | 0.0 | 0.092768 | 24.353611 | 0.214286 | 1.621771 | 2 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2026-04-16 | 2026-05-13 | 16 | 16 | -0.839244 | 0.353482 | 0.202978 | 15.425745 | 0.375 | 1.192726 | 3 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2026-05-13 | 2026-05-24 | 16 | 16 | -1.642661 | 0.023768 | 0.096319 | 27.028929 | 0.25 | 1.666429 | 4 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
