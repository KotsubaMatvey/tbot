# ICT2022 MSS+FVG Frequency Diagnostic

Diagnostic only. Counts rule-stage opportunities before event-study evaluation.

## Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- symbols: BTCUSDT
- timeframes: 30m
- start_date: 2025-01-01
- end_date: 2025-01-31
- scan_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_max_fvg_retest_bars: 3
- ict2022_require_killzone: True
- ict2022_require_same_session: True
- ict2022_require_strong_displacement: True
- ict2022_retest_must_occur_within_session: True

## Funnel
| symbol | timeframe | side | scan_side_bars | latest_sweep | sweep_session_gate | structure_after_sweep_any | structure_body_close | structure_valid_displacement | structure_strong_displacement | structure_config_displacement | sweep_age_gate | structure_session_gate | same_session_sweep_mss | active_fvg_after_mss | retest_any | retest_within_limit | retest_session_gate | target_open_until_retest | candidate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTCUSDT | 30m | long | 620 | 620 | 318 | 162 | 162 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | 0 |
| BTCUSDT | 30m | short | 620 | 620 | 309 | 95 | 95 | 12 | 12 | 12 | 12 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
