# ICT Walk-Forward Quality Report

- events: `backtest_results\probe_costed_2025_eth_1h_rejection_block\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-01-19 | 2025-12-30 | 21 | 21 | -0.01767 | 0.124159 | 0.965444 | 4.67084 | 0.47619 | 0.14183 | 5 | False | max_trades_per_session;min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-01-18 | 2025-06-13 | 7 | 7 | -0.633946 | -0.54851 | 0.098464 | 4.437625 | 0.285714 | 0.085436 | 2 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2025-06-26 | 2025-10-18 | 6 | 6 | 0.542212 | 0.680532 | 3.937215 | 1.107605 | 0.833333 | 0.138319 | 1 | False | min_phase_trades |
| test | 2025-10-21 | 2025-12-31 | 8 | 8 | 0.101659 | 0.295466 | 1.172719 | 3.486489 | 0.375 | 0.193807 | 2 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
