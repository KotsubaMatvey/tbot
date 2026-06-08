# HTF Bias Audit

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_retest_entry\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | model_rules | 12 | 100.0 | 100 | False | 91.666667 | 0.451438 | 0.451438 | 4.688452 | 1.468707 | 5.417256 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_context_alignment | neutral | 0 | model_rules | 12 | 100.0 | 100 | False | 91.666667 | 0.451438 | 0.451438 | 4.688452 | 1.468707 | 5.417256 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias_relation | neutral_or_missing | 0 | model_rules | 12 | 100.0 | 100 | False | 91.666667 | 0.451438 | 0.451438 | 4.688452 | 1.468707 | 5.417256 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_draw_relation | neutral_or_missing | 0 | model_rules | 12 | 100.0 | 100 | False | 91.666667 | 0.451438 | 0.451438 | 4.688452 | 1.468707 | 5.417256 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias | none | 0 | model_rules | 12 | 100.0 | 100 | False | 91.666667 | 0.451438 | 0.451438 | 4.688452 | 1.468707 | 5.417256 | 0.0 | 0.0 | 0.0 | insufficient_sample |
