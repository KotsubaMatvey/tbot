# ICT Walk-Forward Quality Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-03-18 | 2023-04-30 | 11 | 11 | 0.100921 | 0.326551 | 1.257727 | 2.975433 | 0.636364 | 0.223398 | 0.002232 | 0.22563 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2022-03-18 | 2022-09-08 | 4 | 4 | 0.698151 | 0.874457 | inf | 0.0 | 1.0 | 0.176307 | 0.0 | 0.176307 | 0 | False | min_phase_trades |
| validation | 2022-09-17 | 2023-02-28 | 4 | 4 | 0.09456 | 0.273558 | 1.283975 | 1.331952 | 0.5 | 0.184361 | -0.005363 | 0.178997 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| test | 2023-04-12 | 2023-04-30 | 3 | 3 | -0.686905 | -0.333333 | 0.307423 | 2.975433 | 0.333333 | 0.338236 | 0.015336 | 0.353572 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
