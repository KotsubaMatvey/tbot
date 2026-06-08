# ICT2022 MSS+FVG Frequency Diagnostic

Diagnostic only. Counts rule-stage opportunities before event-study evaluation.

## Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- symbols: BTCUSDT
- timeframes: 30m
- start_date: 2024-01-01
- end_date: 2024-01-31
- scan_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_max_fvg_retest_bars: 20
- ict2022_require_killzone: False
- ict2022_require_same_session: False
- ict2022_require_strong_displacement: False
- ict2022_retest_must_occur_within_session: False

## Funnel
| symbol | timeframe | side | scan_side_bars | latest_sweep | sweep_session_gate | structure_after_sweep_any | structure_body_close | structure_valid_displacement | structure_strong_displacement | structure_config_displacement | sweep_age_gate | structure_session_gate | same_session_sweep_mss | active_fvg_after_mss | retest_any | retest_within_limit | retest_session_gate | target_open_until_retest | candidate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTCUSDT | 30m | long | 620 | 620 | 620 | 341 | 341 | 81 | 60 | 81 | 73 | 73 | 73 | 70 | 9 | 9 | 9 | 0 | 0 |
| BTCUSDT | 30m | short | 620 | 620 | 620 | 336 | 336 | 38 | 32 | 38 | 25 | 25 | 25 | 25 | 0 | 0 | 0 | 0 | 0 |
