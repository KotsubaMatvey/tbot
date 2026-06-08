# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_full_2019-09-01_2026-04-20\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2020-01-22 | 2026-04-11 | 106 | 106 | 0.303121 | 0.452667 | 2.188874 | 6.478457 | 0.745283 | 0.148785 | 0.000761 | 0.149547 | 0 | False | min_managed_expectancy_r |
| train | 2020-01-22 | 2022-09-12 | 35 | 35 | 0.181461 | 0.308884 | 1.578835 | 6.478457 | 0.685714 | 0.124968 | 0.002455 | 0.127423 | 0 | False | min_managed_expectancy_r |
| validation | 2022-12-01 | 2024-06-21 | 35 | 35 | 0.280305 | 0.429927 | 2.044486 | 2.326055 | 0.742857 | 0.147916 | 0.001707 | 0.149622 | 0 | False | min_managed_expectancy_r |
| test | 2024-07-09 | 2026-04-11 | 36 | 36 | 0.443583 | 0.614566 | 3.397331 | 3.239181 | 0.805556 | 0.172787 | -0.001804 | 0.170983 | 0 | True |  |
