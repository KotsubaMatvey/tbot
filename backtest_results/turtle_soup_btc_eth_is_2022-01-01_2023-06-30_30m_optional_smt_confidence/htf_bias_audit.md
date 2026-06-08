# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_optional_smt_confidence\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | none | 691 | 100.0 | 100 | True | 60.492041 | -0.1486 | -0.1486 | 0.706199 | 107.433563 | -102.682918 | 0.0 | 0.0 | 0.0 | neutral |
| htf_context_alignment | neutral | 0 | none | 691 | 100.0 | 100 | True | 60.492041 | -0.1486 | -0.1486 | 0.706199 | 107.433563 | -102.682918 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias_relation | neutral_or_missing | 0 | none | 691 | 100.0 | 100 | True | 60.492041 | -0.1486 | -0.1486 | 0.706199 | 107.433563 | -102.682918 | 0.0 | 0.0 | 0.0 | neutral |
| htf_draw_relation | neutral_or_missing | 0 | none | 691 | 100.0 | 100 | True | 60.492041 | -0.1486 | -0.1486 | 0.706199 | 107.433563 | -102.682918 | 0.0 | 0.0 | 0.0 | neutral |
| htf_bias | none | 0 | none | 691 | 100.0 | 100 | True | 60.492041 | -0.1486 | -0.1486 | 0.706199 | 107.433563 | -102.682918 | 0.0 | 0.0 | 0.0 | neutral |
