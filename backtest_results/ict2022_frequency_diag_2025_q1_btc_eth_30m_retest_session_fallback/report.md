# ICT2022 MSS+FVG Frequency Diagnostic

Diagnostic only. Counts rule-stage opportunities before event-study evaluation.
`retest_*` and `candidate` use the current first-eligible-FVG policy.
`*_any_fvg` fields are research attribution across eligible subsequent FVGs; they do not change detector behavior.

## Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- start_date: 2025-01-01
- end_date: 2025-03-31
- scan_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_session_windows: 02:00-05:00,07:00-10:00,13:30-16:00
- ict2022_max_fvg_retest_bars: 3
- ict2022_require_killzone: True
- ict2022_require_same_session: True
- ict2022_require_strong_displacement: True
- ict2022_retest_must_occur_within_session: False

## Funnel
| symbol | timeframe | side | scan_side_bars | latest_sweep | sweep_session_gate | structure_after_sweep_any | structure_body_close | structure_valid_displacement | structure_strong_displacement | structure_config_displacement | sweep_age_gate | structure_session_gate | same_session_sweep_mss | active_fvg_after_mss | retest_any | retest_within_limit | retest_session_gate | target_open_until_retest | candidate | retested_eligible_fvg_any | retested_eligible_fvg_within_limit | retested_eligible_fvg_session_gate | target_open_until_retest_any_fvg | candidate_any_fvg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTCUSDT | 30m | long | 1798 | 1798 | 853 | 381 | 381 | 41 | 29 | 29 | 29 | 21 | 21 | 21 | 0 | 0 | 0 | 0 | 0 | 13 | 8 | 8 | 8 | 8 |
| BTCUSDT | 30m | short | 1798 | 1798 | 949 | 388 | 388 | 75 | 69 | 69 | 69 | 30 | 24 | 24 | 0 | 0 | 0 | 0 | 0 | 18 | 18 | 18 | 17 | 17 |
| ETHUSDT | 30m | long | 1798 | 1798 | 938 | 383 | 383 | 51 | 40 | 40 | 28 | 16 | 16 | 16 | 0 | 0 | 0 | 0 | 0 | 11 | 2 | 2 | 2 | 2 |
| ETHUSDT | 30m | short | 1798 | 1798 | 900 | 346 | 346 | 41 | 27 | 27 | 27 | 21 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 5 | 5 | 5 | 3 | 3 |
