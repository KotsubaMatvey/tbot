# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_late_control_2025-01-01_2026-04-20_15m_30m_strong_no_smt_minrisk35_first\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | model_rules | 119 | 100.0 | 100 | True | 77.310924 | 0.347632 | 0.347632 | 2.277739 | 4.437094 | 41.368153 | 0.0 | 0.0 | 0.0 | neutral |
| htf_context_alignment | neutral | 0 | model_rules | 119 | 100.0 | 100 | True | 77.310924 | 0.347632 | 0.347632 | 2.277739 | 4.437094 | 41.368153 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias_relation | neutral_or_missing | 0 | model_rules | 119 | 100.0 | 100 | True | 77.310924 | 0.347632 | 0.347632 | 2.277739 | 4.437094 | 41.368153 | 0.0 | 0.0 | 0.0 | neutral |
| htf_draw_relation | neutral_or_missing | 0 | model_rules | 119 | 100.0 | 100 | True | 77.310924 | 0.347632 | 0.347632 | 2.277739 | 4.437094 | 41.368153 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias | none | 0 | model_rules | 119 | 100.0 | 100 | True | 77.310924 | 0.347632 | 0.347632 | 2.277739 | 4.437094 | 41.368153 | 0.0 | 0.0 | 0.0 | neutral |
