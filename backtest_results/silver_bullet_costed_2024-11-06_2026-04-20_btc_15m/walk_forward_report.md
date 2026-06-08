# ICT Walk-Forward Quality Report

- events: `backtest_results\silver_bullet_costed_2024-11-06_2026-04-20_btc_15m\events.csv`
- threshold: `70.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-01-10 | 2026-04-07 | 17 | 17 | -0.29328 | -0.094615 | 0.536827 | 8.293195 | 0.470588 | 0.198665 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-01-10 | 2025-04-28 | 5 | 5 | -0.097099 | 0.086234 | 0.803222 | 2.467216 | 0.6 | 0.183332 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2025-04-30 | 2025-08-14 | 6 | 6 | -0.161437 | -0.006605 | 0.715385 | 3.403256 | 0.5 | 0.154832 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| test | 2025-09-06 | 2026-04-07 | 6 | 6 | -0.588608 | -0.333333 | 0.278357 | 4.893903 | 0.333333 | 0.255275 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
