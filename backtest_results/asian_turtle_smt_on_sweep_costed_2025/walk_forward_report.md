# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_costed_2025\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-04-23 | 2025-11-29 | 6 | 6 | 0.413177 | 0.627367 | 2.576671 | 1.288383 | 0.666667 | 0.21419 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-04-23 | 2025-05-16 | 2 | 2 | 0.527097 | 0.632102 | 4.712516 | 0.283957 | 0.5 | 0.105004 | 0 | False | min_phase_trades |
| validation | 2025-05-26 | 2025-06-14 | 2 | 2 | -0.014031 | 0.25 | 0.978218 | 1.288383 | 0.5 | 0.264031 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2025-08-05 | 2025-11-29 | 2 | 2 | 0.726465 | 1.0 | inf | 0.0 | 1.0 | 0.273535 | 0 | False | min_phase_trades |
