# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_attr_broad_sessions_with_smt\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | none | 61 | 100.0 | 100 | False | 78.688525 | 0.317635 | 0.317635 | 3.359767 | 1.468707 | 19.375735 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_context_alignment | neutral | 0 | none | 61 | 100.0 | 100 | False | 78.688525 | 0.317635 | 0.317635 | 3.359767 | 1.468707 | 19.375735 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias_relation | neutral_or_missing | 0 | none | 61 | 100.0 | 100 | False | 78.688525 | 0.317635 | 0.317635 | 3.359767 | 1.468707 | 19.375735 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_draw_relation | neutral_or_missing | 0 | none | 61 | 100.0 | 100 | False | 78.688525 | 0.317635 | 0.317635 | 3.359767 | 1.468707 | 19.375735 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias | none | 0 | none | 61 | 100.0 | 100 | False | 78.688525 | 0.317635 | 0.317635 | 3.359767 | 1.468707 | 19.375735 | 0.0 | 0.0 | 0.0 | insufficient_sample |
