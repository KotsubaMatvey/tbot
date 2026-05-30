# ICT2022 Frequency Diagnostic - 2026-05-29

## Goal

Continue the Binance funding-aware `ict2022_mss_fvg` validation by adding a
bounded attribution report for the zero-frequency result. The diagnostic counts
rule-stage opportunities before `EntrySetup` creation, so empty event-study
reports no longer hide which rule removed the sample.

This is diagnostic evidence only. It does not change live filters and does not
promote any relaxed profile.

## Diagnostic Tool

Added `backtesting/ict2022_diagnostic_report.py`.

The report walks the source-aligned sequence:

1. latest sweep;
2. sweep session gate;
3. MSS after sweep;
4. displacement/body-close gates;
5. sweep-age and same-session gates;
6. active FVG after MSS;
7. FVG retest timing/session gates;
8. target-not-reached-before-retest gate;
9. candidate.

It intentionally reuses the project detectors and only bounds the replay by
`start_date`, `end_date`, and a pre-scan seed window.

## Verification

Targeted tests passed:

```powershell
python -m unittest tests.test_new_ict_models.NewICTModelTests.test_ict2022_diagnostic_identifies_retest_timing_gate tests.test_new_ict_models.NewICTModelTests.test_binance_funding_costs_use_settlement_mark_price tests.test_new_ict_models.NewICTModelTests.test_binance_funding_uses_official_history_response_shape tests.test_new_ict_models.NewICTModelTests.test_hyperliquid_funding_costs_apply_direction_and_partial_close
```

Result: `Ran 4 tests ... OK`.

## Bounded Diagnostic Results

Dataset: `data/history_crypto_2022-01-01_2026-04-20`.
All runs below use `BTCUSDT`, `30m`, and scan only the configured ICT windows
`02:00-05:00,07:00-10:00,13:30-16:00`.

| Run | Side | Key funnel result | Candidate |
| --- | --- | --- | ---: |
| `backtest_results/ict2022_frequency_diag_2025_01_btc_30m_strict` | long | `15` active FVGs after MSS, `0` retests | 0 |
| `backtest_results/ict2022_frequency_diag_2025_01_btc_30m_strict` | short | `6` structure-session passes, `0` same-session sweep/MSS passes | 0 |
| `backtest_results/ict2022_frequency_diag_2025_01_btc_30m_relaxed` | long | relaxing strong displacement and retest session still leaves `0` retests | 0 |
| `backtest_results/ict2022_frequency_diag_2025_01_btc_30m_no_same_session` | short | disabling same-session reaches `6` active FVGs, but `0` retests | 0 |
| `backtest_results/ict2022_frequency_diag_2024_01_btc_30m_strict` | long | `30` sweep-age passes, `0` structure-session passes | 0 |
| `backtest_results/ict2022_frequency_diag_2024_01_btc_30m_strict` | short | `4` sweep-age passes, `0` structure-session passes | 0 |
| `backtest_results/ict2022_frequency_diag_2024_01_btc_30m_no_killzone` | long | `70` active FVGs and `9` retests, but `0` pass target-open-until-retest | 0 |
| `backtest_results/ict2022_frequency_diag_2024_01_btc_30m_no_killzone` | short | `25` active FVGs, `0` retests | 0 |

## Interpretation

- HTF context is not the first blocker in these bounded probes: context-free
  diagnostics still produce zero candidates.
- Strong displacement is not the primary blocker: relaxing it increases
  intermediate counts but does not create candidates.
- Session gating is a major blocker in early-OOS January 2024 and for January
  2025 shorts.
- For January 2025 longs and relaxed January 2025 shorts, the current model
  reaches active FVGs but finds no FVG retest.
- When killzone/same-session constraints are disabled in January 2024, some
  long retests appear, but all are cancelled by the target-reached-before-retest
  policy.

## Decision

Keep `ict2022_mss_fvg` disabled. The strict Binance funding-aware profile
already had zero activated trades, and bounded attribution shows the missing
sample is structural to the current rule sequence rather than only an HTF or
strong-displacement issue.

Further research should not relax toward live use unless it first makes an
explicit source-backed decision about FVG selection and the
target-reached-before-retest cancellation rule, then reruns costed OOS and late
control validation.
