# ICT Walk-Forward Quality Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_broad_sessions_no_smt_no_prior\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-01-03 | 2023-06-30 | 1880 | 1880 | -0.13121 | 0.410317 | 0.738977 | 250.681565 | 0.617553 | 0.541279 | 0.000248 | 0.541527 | 463 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2022-01-03 | 2022-07-07 | 626 | 626 | 0.018422 | 0.45125 | 1.043403 | 31.321238 | 0.682109 | 0.43284 | -1.2e-05 | 0.432827 | 156 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| validation | 2022-07-08 | 2023-01-07 | 631 | 631 | -0.158557 | 0.386991 | 0.695489 | 113.979141 | 0.59588 | 0.544391 | 0.001158 | 0.545548 | 155 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2023-01-07 | 2023-06-30 | 628 | 628 | -0.260307 | 0.394461 | 0.541061 | 165.306934 | 0.571656 | 0.655175 | -0.000407 | 0.654768 | 154 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
