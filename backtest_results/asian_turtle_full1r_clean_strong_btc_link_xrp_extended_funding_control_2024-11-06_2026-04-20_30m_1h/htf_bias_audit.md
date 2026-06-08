# HTF Bias Audit

- events: `backtest_results\asian_turtle_full1r_clean_strong_btc_link_xrp_extended_funding_control_2024-11-06_2026-04-20_30m_1h\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | model_rules | 19 | 100.0 | 100 | False | 89.473684 | 0.618686 | 0.618686 | 10.082949 | 1.26004 | 11.755035 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_context_alignment | neutral | 0 | model_rules | 19 | 100.0 | 100 | False | 89.473684 | 0.618686 | 0.618686 | 10.082949 | 1.26004 | 11.755035 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias_relation | neutral_or_missing | 0 | model_rules | 19 | 100.0 | 100 | False | 89.473684 | 0.618686 | 0.618686 | 10.082949 | 1.26004 | 11.755035 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_draw_relation | neutral_or_missing | 0 | model_rules | 19 | 100.0 | 100 | False | 89.473684 | 0.618686 | 0.618686 | 10.082949 | 1.26004 | 11.755035 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias | none | 0 | model_rules | 19 | 100.0 | 100 | False | 89.473684 | 0.618686 | 0.618686 | 10.082949 | 1.26004 | 11.755035 | 0.0 | 0.0 | 0.0 | insufficient_sample |
