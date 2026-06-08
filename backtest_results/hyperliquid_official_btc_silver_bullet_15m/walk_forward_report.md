# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_official_btc_silver_bullet_15m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-04-04 | 2026-05-24 | 60 | 60 | -0.482389 | -0.124419 | 0.339243 | 34.527157 | 0.383333 | 0.357211 | 0.000759 | 0.35797 | 4 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2026-04-04 | 2026-04-18 | 23 | 23 | -0.560593 | -0.23913 | 0.280499 | 13.861176 | 0.304348 | 0.321194 | 0.000269 | 0.321462 | 2 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2026-04-19 | 2026-05-07 | 19 | 19 | -0.590879 | -0.217184 | 0.196671 | 11.696534 | 0.315789 | 0.373097 | 0.000599 | 0.373695 | 2 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2026-05-08 | 2026-05-24 | 18 | 18 | -0.267947 | 0.120075 | 0.59497 | 9.770694 | 0.555556 | 0.386465 | 0.001556 | 0.388022 | 0 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
