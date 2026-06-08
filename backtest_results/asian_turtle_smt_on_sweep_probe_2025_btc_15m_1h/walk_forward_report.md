# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_probe_2025_btc_15m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-03-16 | 2025-12-13 | 12 | 12 | 0.182091 | 0.574308 | 1.445244 | 3.396789 | 0.666667 | 0.392216 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-03-16 | 2025-05-16 | 4 | 4 | 0.800593 | 1.0 | inf | 0.0 | 1.0 | 0.199407 | 0 | False | min_phase_trades |
| validation | 2025-05-26 | 2025-06-14 | 4 | 4 | 0.342079 | 0.875 | 1.905658 | 1.510853 | 0.75 | 0.532921 | 0 | False | min_phase_trades |
| test | 2025-09-03 | 2025-12-13 | 4 | 4 | -0.596398 | -0.152077 | 0.297693 | 3.396789 | 0.25 | 0.44432 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
