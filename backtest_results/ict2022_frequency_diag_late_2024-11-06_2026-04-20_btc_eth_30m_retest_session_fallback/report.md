# ICT2022 MSS+FVG Frequency Diagnostic

Diagnostic only. Counts rule-stage opportunities before event-study evaluation.
`retest_*` and `candidate` use the current first-eligible-FVG policy.
`*_any_fvg` fields are research attribution across eligible subsequent FVGs; they do not change detector behavior.

## Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- start_date: 2024-11-06
- end_date: 2026-04-20
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
| BTCUSDT | 30m | long | 10616 | 10616 | 5199 | 2289 | 2289 | 322 | 218 | 218 | 205 | 96 | 75 | 75 | 22 | 7 | 7 | 6 | 6 | 61 | 50 | 50 | 43 | 43 |
| BTCUSDT | 30m | short | 10616 | 10616 | 5686 | 2516 | 2516 | 465 | 306 | 306 | 264 | 148 | 136 | 135 | 12 | 6 | 6 | 6 | 6 | 98 | 81 | 81 | 75 | 75 |
| ETHUSDT | 30m | long | 10616 | 10616 | 5196 | 2260 | 2260 | 315 | 195 | 195 | 167 | 129 | 86 | 86 | 18 | 0 | 0 | 0 | 0 | 67 | 46 | 46 | 33 | 33 |
| ETHUSDT | 30m | short | 10616 | 10616 | 5737 | 2538 | 2538 | 331 | 233 | 233 | 167 | 97 | 64 | 62 | 11 | 8 | 8 | 7 | 7 | 32 | 25 | 25 | 22 | 22 |
