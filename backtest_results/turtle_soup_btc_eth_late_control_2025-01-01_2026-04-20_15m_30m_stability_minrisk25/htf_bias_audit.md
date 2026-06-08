# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_late_control_2025-01-01_2026-04-20_15m_30m_stability_minrisk25\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | model_rules | 181 | 100.0 | 100 | True | 80.662983 | 0.362758 | 0.362758 | 2.525398 | 2.695426 | 65.659284 | 0.0 | 0.0 | 0.0 | neutral |
| htf_context_alignment | neutral | 0 | model_rules | 181 | 100.0 | 100 | True | 80.662983 | 0.362758 | 0.362758 | 2.525398 | 2.695426 | 65.659284 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias_relation | neutral_or_missing | 0 | model_rules | 181 | 100.0 | 100 | True | 80.662983 | 0.362758 | 0.362758 | 2.525398 | 2.695426 | 65.659284 | 0.0 | 0.0 | 0.0 | neutral |
| htf_draw_relation | neutral_or_missing | 0 | model_rules | 181 | 100.0 | 100 | True | 80.662983 | 0.362758 | 0.362758 | 2.525398 | 2.695426 | 65.659284 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias | none | 0 | model_rules | 181 | 100.0 | 100 | True | 80.662983 | 0.362758 | 0.362758 | 2.525398 | 2.695426 | 65.659284 | 0.0 | 0.0 | 0.0 | neutral |
