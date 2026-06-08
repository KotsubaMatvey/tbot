# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_official_xyz100_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 68 | 68 | -1.478487 | -0.058894 | 0.066541 | 100.537134 | 0.191176 | 1.415364 | 0.004229 | 1.419593 | 6 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-21 | 23 | 23 | -1.719257 | -0.218375 | 0.050201 | 39.542908 | 0.173913 | 1.491905 | 0.008976 | 1.500882 | 0 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2026-04-22 | 2026-05-12 | 21 | 21 | -1.142718 | -0.024384 | 0.085252 | 25.441036 | 0.190476 | 1.113819 | 0.004515 | 1.118334 | 2 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2026-05-13 | 2026-05-24 | 24 | 24 | -1.541548 | 0.063745 | 0.071297 | 37.732576 | 0.208333 | 1.605863 | -0.00057 | 1.605293 | 4 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
