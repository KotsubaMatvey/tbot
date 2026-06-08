# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_multi_control_2024-11-06_2026-04-20_btc_eth_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-02-27 | 2026-03-30 | 8 | 8 | 0.076358 | 0.184083 | 1.279217 | 2.153619 | 0.5 | 0.107725 | 0.0 | 0.107725 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-02-27 | 2025-03-04 | 2 | 2 | -0.058608 | 0.0 | 0.890467 | 1.07013 | 0.5 | 0.058607 | 0.0 | 0.058607 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2025-03-16 | 2025-05-31 | 3 | 3 | 0.221734 | 0.374644 | 8.316666 | 0.056769 | 0.333333 | 0.15291 | 0.0 | 0.15291 | 0 | False | min_phase_trades;min_managed_expectancy_r |
| test | 2025-12-17 | 2026-03-30 | 3 | 3 | 0.020958 | 0.116245 | 1.061239 | 1.02672 | 0.666667 | 0.095286 | 0.0 | 0.095286 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
