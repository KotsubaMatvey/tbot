# HTF Bias Audit

- events: `backtest_results\ict2022_first_retested_fvg_research_2024_01_btc_30m_no_killzone\events.csv`
- verdict compares each HTF bucket against the full realized P&L baseline.

| section | bucket | threshold | filter_name | trade_count | retention_pct | min_trades | sample_valid | win_rate_pct | avg_realized_rr | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | expectancy_delta_vs_all | win_rate_delta_vs_all | avg_realized_rr_delta_vs_all | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | all | 0 | none | 11 | 100.0 | 30 | False | 72.727273 | 0.063057 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_context_alignment | neutral | 0 | none | 11 | 100.0 | 30 | False | 72.727273 | 0.063057 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias_relation | neutral_or_missing | 0 | none | 11 | 100.0 | 30 | False | 72.727273 | 0.063057 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_draw_relation | neutral_or_missing | 0 | none | 11 | 100.0 | 30 | False | 72.727273 | 0.063057 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.0 | 0.0 | 0.0 | insufficient_sample |
| htf_bias | none | 0 | none | 11 | 100.0 | 30 | False | 72.727273 | 0.063057 | 0.063057 | 1.20846 | 2.173221 | 0.693629 | 0.0 | 0.0 | 0.0 | insufficient_sample |
