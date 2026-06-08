# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_sol_tfdir_funding_oos_2022-01-01_2024-11-05_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2022-04-08 | 2024-10-02 | 36 | 36 | 0.279309 | 0.427844 | 2.194693 | 1.740139 | 0.75 | 0.149392 | -0.000857 | 0.148535 | 0 | False | min_managed_expectancy_r |
| train | 2022-04-08 | 2023-04-30 | 11 | 11 | 0.172237 | 0.330532 | 1.506703 | 1.469358 | 0.636364 | 0.158221 | 7.4e-05 | 0.158295 | 0 | False | min_managed_expectancy_r |
| validation | 2023-06-03 | 2024-03-12 | 13 | 13 | 0.297301 | 0.426951 | 2.532318 | 1.122482 | 0.769231 | 0.129636 | 1.4e-05 | 0.12965 | 0 | False | min_managed_expectancy_r |
| test | 2024-03-12 | 2024-10-02 | 13 | 13 | 0.341824 | 0.492896 | 3.061919 | 1.09839 | 0.846154 | 0.153521 | -0.00245 | 0.151072 | 0 | True |  |
