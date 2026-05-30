# Official ICT Sources And Live Validation - 2026-05-25

## Official Source Baseline

- YouTube channel: `https://www.youtube.com/@InnerCircleTrader`
- YouTube channel ID: `UCtjxa77NqamhVC8atV85Rog`
- X profile: `https://x.com/I_Am_The_ICT`

Official YouTube playlists identified for strategy research:

- 2022 ICT Mentorship: `PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s` (41 videos)
- 2023 ICT Mentorship: `PLVgHx4Z63pabpjlduWBaEsn8VMtALhjGV` (105 videos)
- ICT 2024 Mentorship: `PLVgHx4Z63paaM41aubnHOmqfeNjSAoBCV` (51 videos)
- 2025 Lecture Series: `PLVgHx4Z63paYf6xk2a8KKuf2CYJ8SX0Wy` (83 videos)
- 2026 ICT Smart Money Concept Lecture: `PLVgHx4Z63paaja3GW0dYSr6y_V2Sttx4-` (55 videos)
- ICT Trade Executions: `PLVgHx4Z63paYhYt0DTyeBBxQomkeCEIq1` (56 videos)

Research use:

- Use the 2022 mentorship as the primary rule-definition source for the existing ICT 2022 model.
- Use Trade Executions to test whether proposed deterministic rules match actual demonstrated entries and exclusions.
- Use 2024-2026 lectures for candidate refinements only; do not change live rules from a video title or isolated example.
- Use X as a discovery/source-link channel, not as sufficient proof of a trading rule.

## Live Silver Bullet Audit

The existing live config enabled `silver_bullet` for `BTCUSDT` on `15m`, with strict HTF quality filters and New York windows `10:00-11:00` and `14:00-15:00`.

The saved costed backtest artifacts were merged for validation without changing strategy rules:

- 2025 quarterly artifacts: `13` events, net managed expectancy `-0.217593R`, profit factor `0.609781`.
- 2025 through 2026-04 partial artifacts: `17` events, net managed expectancy `-0.293280R`, profit factor `0.536827`.

Walk-forward gates failed for both samples:

- 2025 failures: `min_managed_expectancy_r`, `min_phase_trades`, `min_profit_factor`, `min_total_trades`.
- Extended failures: `min_managed_expectancy_r`, `min_phase_trades`, `min_profit_factor`, `min_total_trades`.

## Decision

`silver_bullet` remains implemented and available for research/backtests, but it is disabled in live scanning until a revised, source-backed variant passes costed walk-forward validation.

No additional model is enabled as a replacement from this audit.
