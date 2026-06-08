# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_btc_link_xrp_1h_risk_cap_funding_oos_2022-01-01_2024-11-05\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-01-02 | 2024-10-02 | 54 | 54 | 0.22108 | 0.379724 | 1.746254 | 3.239181 | 0.722222 | 0.15658 | 0.002064 | 0.158644 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_total_trades |
| train | 2022-01-02 | 2023-03-11 | 19 | 19 | 0.359962 | 0.510608 | 2.507071 | 2.212709 | 0.789474 | 0.147919 | 0.002727 | 0.150646 | 0 | False | min_phase_trades |
| validation | 2023-03-11 | 2023-12-06 | 18 | 18 | 0.216551 | 0.360506 | 1.807465 | 2.326055 | 0.722222 | 0.139884 | 0.004071 | 0.143955 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| test | 2024-01-24 | 2024-10-02 | 19 | 19 | 0.155093 | 0.33234 | 1.444313 | 3.239181 | 0.684211 | 0.177703 | -0.000456 | 0.177247 | 0 | False | min_phase_trades;min_managed_expectancy_r |
