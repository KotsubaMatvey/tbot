# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_recent_btc_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 39 | 39 | -0.252086 | 0.056019 | 0.577496 | 10.847829 | 0.461538 | 0.308105 | 5 | False | max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-18 | 13 | 13 | -0.222471 | 0.038462 | 0.61639 | 3.275154 | 0.461538 | 0.260933 | 2 | False | min_managed_expectancy_r;min_profit_factor |
| validation | 2026-04-20 | 2026-05-08 | 13 | 13 | -0.428649 | -0.158464 | 0.304964 | 7.825878 | 0.307692 | 0.270186 | 2 | False | min_managed_expectancy_r;min_profit_factor |
| test | 2026-05-09 | 2026-05-24 | 13 | 13 | -0.105138 | 0.288058 | 0.822783 | 3.119528 | 0.615385 | 0.393195 | 1 | False | min_managed_expectancy_r;min_profit_factor |
