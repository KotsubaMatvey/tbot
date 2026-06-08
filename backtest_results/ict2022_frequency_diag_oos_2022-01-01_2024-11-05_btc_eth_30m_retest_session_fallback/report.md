# ICT2022 MSS+FVG Frequency Diagnostic

Diagnostic only. Counts rule-stage opportunities before event-study evaluation.
`retest_*` and `candidate` use the current first-eligible-FVG policy.
`*_any_fvg` fields are research attribution across eligible subsequent FVGs; they do not change detector behavior.

## Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- start_date: 2022-01-01
- end_date: 2024-11-05
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
| BTCUSDT | 30m | long | 20734 | 20734 | 11029 | 5083 | 5083 | 698 | 526 | 526 | 479 | 291 | 215 | 211 | 5 | 3 | 3 | 3 | 3 | 132 | 114 | 114 | 94 | 94 |
| BTCUSDT | 30m | short | 20734 | 20734 | 11369 | 5025 | 5025 | 526 | 351 | 351 | 342 | 130 | 88 | 83 | 23 | 16 | 16 | 9 | 9 | 67 | 57 | 57 | 46 | 46 |
| ETHUSDT | 30m | long | 20734 | 20734 | 11043 | 4978 | 4978 | 614 | 391 | 391 | 317 | 222 | 132 | 132 | 7 | 0 | 0 | 0 | 0 | 75 | 74 | 74 | 66 | 66 |
| ETHUSDT | 30m | short | 20734 | 20734 | 11506 | 5288 | 5288 | 616 | 438 | 438 | 375 | 139 | 111 | 111 | 19 | 6 | 6 | 6 | 6 | 52 | 32 | 32 | 26 | 26 |
