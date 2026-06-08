# ICT Walk-Forward Quality Report

- events: `backtest_results\asian_turtle_full1r_clean_strong_crypto_expansion_funding_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2025-02-19 | 2026-04-16 | 46 | 46 | 0.217754 | 0.344627 | 1.668607 | 5.875415 | 0.695652 | 0.127725 | -0.000853 | 0.126873 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2025-02-19 | 2025-06-08 | 15 | 15 | 0.522582 | 0.642673 | 4.460718 | 2.230911 | 0.8 | 0.120374 | -0.000282 | 0.120092 | 0 | False | min_phase_trades |
| validation | 2025-06-27 | 2025-11-15 | 16 | 16 | 0.494757 | 0.601712 | 3.396062 | 1.164092 | 0.8125 | 0.107848 | -0.000893 | 0.106955 | 0 | False | min_phase_trades |
| test | 2025-11-17 | 2026-04-16 | 15 | 15 | -0.382542 | -0.227643 | 0.390376 | 5.860812 | 0.466667 | 0.156279 | -0.00138 | 0.154899 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
