# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_2025_btc_30m_nyopen_costed_minstop80\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-01-03 | 2025-12-30 | 98 | 98 | -0.188475 | -0.072377 | 0.672644 | 23.045365 | 0.469388 | 0.116099 | 3 | False | max_drawdown_r;max_trades_per_session;min_managed_expectancy_r;min_profit_factor |
| train | 2025-01-03 | 2025-04-27 | 32 | 32 | -0.057609 | 0.049475 | 0.885244 | 5.793263 | 0.5 | 0.107083 | 2 | False | min_managed_expectancy_r;min_profit_factor |
| validation | 2025-05-02 | 2025-08-30 | 33 | 33 | -0.374156 | -0.251567 | 0.450388 | 13.847133 | 0.393939 | 0.122589 | 0 | False | min_managed_expectancy_r;min_profit_factor;max_drawdown_r |
| test | 2025-09-02 | 2025-12-30 | 33 | 33 | -0.129696 | -0.011345 | 0.760815 | 6.654969 | 0.515152 | 0.118351 | 1 | False | min_managed_expectancy_r;min_profit_factor |
