# ICT Walk-Forward Quality Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_broad_sessions_with_smt\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-01-12 | 2023-06-28 | 61 | 61 | 0.317635 | 0.815923 | 3.359767 | 1.468707 | 0.786885 | 0.498288 | 0.0 | 0.498288 | 1 | False | max_trades_per_session;min_phase_trades;min_total_trades |
| train | 2022-01-12 | 2022-08-02 | 20 | 20 | 0.386085 | 0.9 | 6.017432 | 1.091725 | 0.75 | 0.513915 | 0.0 | 0.513915 | 0 | False | min_phase_trades |
| validation | 2022-08-04 | 2023-02-03 | 20 | 20 | 0.322236 | 0.664273 | 2.642826 | 1.468707 | 0.85 | 0.342037 | 0.0 | 0.342037 | 1 | False | min_phase_trades |
| test | 2023-02-05 | 2023-06-28 | 21 | 21 | 0.248063 | 0.880279 | 2.895023 | 1.421822 | 0.761905 | 0.632216 | 0.0 | 0.632216 | 0 | False | min_phase_trades |
