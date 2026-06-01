# ICT2022 Any-FVG Attribution - 2026-06-01

## Goal

Follow up the FVG-selection decision in
`45_ict2022_fvg_selection_target_cancellation_decision_2026-06-01.md` with a
bounded diagnostic that compares the current first-eligible-FVG policy against
a research-only "any retested eligible FVG after MSS" attribution path.

This does not change `ict2022_mss_fvg` detector behavior and does not enable
live trading.

## Code Change

Extended `backtesting/ict2022_diagnostic_report.py` with research attribution
fields:

- `retested_eligible_fvg_any`
- `retested_eligible_fvg_within_limit`
- `retested_eligible_fvg_session_gate`
- `target_open_until_retest_any_fvg`
- `candidate_any_fvg`

Existing fields `retest_any`, `retest_within_limit`,
`target_open_until_retest`, and `candidate` still report the current
first-eligible-FVG behavior.

Added unit coverage in `tests/test_new_ict_models.py` for the case where the
first FVG after MSS never retests but a later eligible FVG does.

## Verification

Passed:

```powershell
python -m unittest tests.test_new_ict_models.NewICTModelTests.test_ict2022_diagnostic_identifies_retest_timing_gate tests.test_new_ict_models.NewICTModelTests.test_ict2022_diagnostic_separates_first_fvg_from_any_retested_fvg
```

Result: `Ran 2 tests ... OK`.

## Bounded Results

### Strict January 2025

Command:

```powershell
python -m backtesting.ict2022_diagnostic_report --data-dir data/history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT --timeframes 30m --start-date 2025-01-01 --end-date 2025-01-31 --ict2022-max-fvg-retest-bars 3 --out-dir backtest_results\ict2022_frequency_diag_2025_01_btc_30m_strict_any_fvg_audit
```

Output:
`backtest_results/ict2022_frequency_diag_2025_01_btc_30m_strict_any_fvg_audit`

| Side | First-FVG candidate | Any-FVG within limit | Any-FVG candidate | Interpretation |
| --- | ---: | ---: | ---: | --- |
| long | 0 | 7 | 0 | Later FVGs retest, but strict retest-session gate still removes them. |
| short | 0 | 0 | 0 | Same-session sweep/MSS remains the earlier blocker. |

### No-killzone January 2024

Command:

```powershell
python -m backtesting.ict2022_diagnostic_report --data-dir data/history_crypto_2022-01-01_2026-04-20 --symbols BTCUSDT --timeframes 30m --start-date 2024-01-01 --end-date 2024-01-31 --ict2022-max-fvg-retest-bars 20 --no-ict2022-require-killzone --no-ict2022-require-same-session --no-ict2022-require-strong-displacement --no-ict2022-retest-must-occur-within-session --out-dir backtest_results\ict2022_frequency_diag_2024_01_btc_30m_no_killzone_any_fvg_audit
```

Output:
`backtest_results/ict2022_frequency_diag_2024_01_btc_30m_no_killzone_any_fvg_audit`

| Side | First-FVG candidate | Any-FVG candidate | Interpretation |
| --- | ---: | ---: | --- |
| long | 0 | 41 | First-FVG selection is a material sample bottleneck once session gates are relaxed. |
| short | 0 | 17 | Same conclusion on the short side under this relaxed diagnostic. |

## Decision

The attribution confirms that first-FVG selection can be a construction
bottleneck, but it does not justify live relaxation:

- under strict January 2025 rules, any-FVG still produces zero candidates
  because session coupling removes the retests;
- under no-killzone January 2024 rules, any-FVG creates candidates only after
  several source-alignment/session constraints are disabled.

Next valid research step is a predeclared research-only detector variant or
diagnostic event study for `first retested eligible FVG after MSS`, still with
costed OOS/control validation before any live consideration.
