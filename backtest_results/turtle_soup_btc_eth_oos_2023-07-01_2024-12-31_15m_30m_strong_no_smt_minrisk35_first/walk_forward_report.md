# ICT Walk-Forward Quality Report

- events: `backtest_results\turtle_soup_btc_eth_oos_2023-07-01_2024-12-31_15m_30m_strong_no_smt_minrisk35_first\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2023-07-06 | 2024-12-31 | 92 | 92 | 0.389537 | 0.573499 | 2.572923 | 3.175337 | 0.793478 | 0.182752 | 0.00121 | 0.183962 | 0 | False | min_total_trades |
| train | 2023-07-06 | 2024-01-05 | 30 | 30 | 0.260057 | 0.452475 | 1.813771 | 3.175337 | 0.733333 | 0.188707 | 0.003711 | 0.192418 | 0 | True |  |
| validation | 2024-01-09 | 2024-07-09 | 32 | 32 | 0.511899 | 0.6875 | 3.704463 | 1.272268 | 0.84375 | 0.175601 | 0.0 | 0.175601 | 0 | True |  |
| test | 2024-07-09 | 2024-12-31 | 33 | 33 | 0.431856 | 0.611747 | 2.995988 | 2.37565 | 0.818182 | 0.179891 | 0.0 | 0.179891 | 0 | True |  |
