# ICT Walk-Forward Quality Report

- events: `backtest_results\ict2022_first_retested_fvg_session_fallback_oos_2022-01-01_2024-11-05_btc_eth_30m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-02-27 | 2024-10-23 | 22 | 22 | -0.718236 | -0.666324 | 0.166366 | 15.801195 | 0.181818 | 0.048952 | 0.00296 | 0.051912 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2022-02-27 | 2022-10-25 | 8 | 8 | -0.736334 | -0.6875 | 0.197623 | 5.890675 | 0.125 | 0.047006 | 0.001828 | 0.048834 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2022-12-13 | 2023-10-30 | 6 | 6 | -1.069277 | -1.0 | 0.0 | 6.415661 | 0.0 | 0.067853 | 0.001424 | 0.069277 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2023-12-07 | 2024-10-23 | 8 | 8 | -0.436857 | -0.39489 | 0.327576 | 3.515899 | 0.375 | 0.036722 | 0.005245 | 0.041967 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
