# ICT Walk-Forward Quality Report

- events: `backtest_results\hyperliquid_probe_btc_no_smt_30m\events.csv`
- threshold: `0.0`
- passed: `False`

## Phases
| phase | start_date | end_date | count | activated_trades | managed_expectancy | gross_managed_expectancy | profit_factor | max_drawdown_r | win_rate | avg_execution_cost_r | session_overtrade_count | passed | failed_gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | 2026-03-20 | 2026-05-23 | 13 | 13 | -0.251766 | 0.084492 | 0.562447 | 4.553063 | 0.538462 | 0.336258 | 0 | False | min_managed_expectancy_r;min_phase_trades;min_profit_factor;min_total_trades |
| train | 2026-03-20 | 2026-04-08 | 4 | 4 | -0.687981 | -0.375 | 0.325649 | 2.874114 | 0.25 | 0.31298 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
| validation | 2026-04-09 | 2026-04-30 | 4 | 4 | 0.360617 | 0.75 | inf | 0.0 | 1.0 | 0.389383 | 0 | False | min_phase_trades |
| test | 2026-05-03 | 2026-05-23 | 5 | 5 | -0.392701 | -0.080321 | 0.42238 | 3.121416 | 0.4 | 0.31238 | 0 | False | min_phase_trades;min_managed_expectancy_r;min_profit_factor |
