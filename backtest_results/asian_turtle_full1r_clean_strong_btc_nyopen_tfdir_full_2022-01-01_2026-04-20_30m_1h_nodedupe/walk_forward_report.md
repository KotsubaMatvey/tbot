# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_nyopen_tfdir_full_2022-01-01_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-05-23 | 2026-03-30 | 31 | 31 | 0.360492 | 0.550748 | 2.881708 | 1.68545 | 0.83871 | 0.190256 | 0.0 | 0.190256 | 7 | False | max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2022-05-23 | 2023-05-28 | 10 | 10 | 0.035707 | 0.246307 | 1.095861 | 1.68545 | 0.7 | 0.210601 | 0.0 | 0.210601 | 2 | False | min_managed_expectancy_r;min_profit_factor |
| validation | 2023-06-15 | 2024-03-12 | 10 | 10 | 0.484184 | 0.643581 | 5.307664 | 1.124006 | 0.9 | 0.159397 | 0.0 | 0.159397 | 3 | True |  |
| test | 2024-04-23 | 2026-03-30 | 11 | 11 | 0.543304 | 0.743119 | 6.482658 | 1.090045 | 0.909091 | 0.199815 | 0.0 | 0.199815 | 2 | True |  |
