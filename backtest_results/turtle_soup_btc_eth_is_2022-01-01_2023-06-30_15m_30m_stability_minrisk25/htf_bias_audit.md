# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_15m_30m_stability_minrisk25\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | model_rules | 357 | 100.0 | 100 | True | 78.151261 | 0.325523 | 0.325523 | 2.202572 | 3.688448 | 116.211636 | 0.0 | 0.0 | 0.0 | neutral |
| htf_context_alignment | neutral | 0 | model_rules | 357 | 100.0 | 100 | True | 78.151261 | 0.325523 | 0.325523 | 2.202572 | 3.688448 | 116.211636 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias_relation | neutral_or_missing | 0 | model_rules | 357 | 100.0 | 100 | True | 78.151261 | 0.325523 | 0.325523 | 2.202572 | 3.688448 | 116.211636 | 0.0 | 0.0 | 0.0 | neutral |
| htf_draw_relation | neutral_or_missing | 0 | model_rules | 357 | 100.0 | 100 | True | 78.151261 | 0.325523 | 0.325523 | 2.202572 | 3.688448 | 116.211636 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias | none | 0 | model_rules | 357 | 100.0 | 100 | True | 78.151261 | 0.325523 | 0.325523 | 2.202572 | 3.688448 | 116.211636 | 0.0 | 0.0 | 0.0 | neutral |
