# Trade P&L Report

- events: `backtest_results\ict2022_first_retested_fvg_research_2025_01_btc_30m_no_killzone\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.
- `sample_valid` is false when activated trade count is below `min_trades`.

| scope | group | filter_name | threshold | filtered_out | trade_count | min_trades | sample_valid | win_rate_pct | avg_realized_rr | avg_win_r | avg_loss_r | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_model | ict2022_mss_fvg | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_symbol | BTCUSDT | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_timeframe | 30m | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_direction | long | none | 0 | 0 | 2 | 30 | False | 0.0 | -1.033322 |  | 1.033322 | -1.033322 | 0.0 | 2.066644 | -2.066644 | 0.033322 | 0.0 | 0.033322 |
| by_direction | short | none | 0 | 0 | 2 | 30 | False | 100.0 | 1.447221 | 1.447221 |  | 1.447221 | inf | 0.0 | 2.894443 | 0.058919 | -0.006141 | 0.052779 |
| by_htf_bias | none | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_htf_context_alignment | neutral | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
| by_htf_draw_direction | none | none | 0 | 0 | 4 | 30 | False | 50.0 | 0.20695 | 1.447221 | 1.033322 | 0.20695 | 1.400552 | 1.034291 | 0.827799 | 0.046121 | -0.00307 | 0.04305 |
