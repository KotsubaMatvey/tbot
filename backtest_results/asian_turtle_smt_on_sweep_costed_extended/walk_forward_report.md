# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_smt_on_sweep_costed_extended\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2024-12-10 | 2025-11-29 | 7 | 7 | 0.540621 | 0.752029 | 3.406826 | 1.288383 | 0.714286 | 0.211408 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2024-12-10 | 2025-04-23 | 2 | 2 | 0.510664 | 0.632102 | 4.596773 | 0.283957 | 0.5 | 0.121437 | 0 | False | min_phase_trades |
| validation | 2025-05-16 | 2025-05-26 | 2 | 2 | 1.299236 | 1.5 | inf | 0.0 | 1.0 | 0.200764 | 0 | False | min_phase_trades |
| test | 2025-06-14 | 2025-11-29 | 3 | 3 | 0.054849 | 0.333333 | 1.127717 | 1.288383 | 0.666667 | 0.278484 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
