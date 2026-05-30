# Exit Policy and Cost Audit - 2026-05-29

## Scope

Investigated why validated ICT model candidates still fail costed OOS gates after
entry-side diagnostics. Added a post-process audit over existing `events.csv`
files and replayed the only materially improved exit-policy candidate.

Primary artifact:

- `backtesting/exit_policy_audit.py`
- `backtest_results/exit_policy_audit_2026-05-29/exit_policy_audit.csv`
- `backtest_results/exit_policy_audit_2026-05-29_turtle_full1r/exit_policy_audit.csv`

Source handling: the official ICT YouTube channel URL was checked, but no
machine-readable transcript or rule text was available through the browsing
tool. No entry-rule changes in this note rely on unverifiable external
transcript text.

## Findings

### Silver Bullet

Silver Bullet is not mainly an exit-policy problem.

| Run | Trades | Current net | Best simple policy | Avg cost R | Invalidation |
| --- | ---: | ---: | ---: | ---: | ---: |
| BTC `15m` official window | 60 | `-0.482389R` | `1R`, `-0.465682R` | `0.357970R` | `71.67%` |
| SP500 `15m` official window | 81 | `-1.586453R` | `1R`, `-1.534273R` | `1.516175R` | `72.84%` |

The SP500 run is structurally blocked by tight-stop cost drag. The average
execution cost is larger than 1R, so even directionally correct setups are
penalized too heavily to validate.

### Turtle Soup SMT-on-sweep

The DOL-target BTC `1h` OOS candidate is the only line where exit policy
materially improves the result.

Existing DOL OOS report:

- `30` trades
- current net expectancy: `+0.061161R`
- profit factor: `1.175881`
- audit-estimated full `1R` expectancy: `+0.111819R`
- audit-estimated full `1R` profit factor: `1.321559`

Replay checks:

| Variant | Trades | Net expectancy | Profit factor | Train | Validation | Test | Passed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| first signal only, full `1R` | 25 | `+0.214801R` | `1.775204` | `+0.249957R` | `+0.341060R` | `+0.071322R` | no |
| all signals, full `1R` | 32 | `+0.318196R` | `2.469883` | `+0.272918R` | `+0.499050R` | `+0.178503R` | no |

Full `1R` is a real improvement, but it is not stable enough. The all-signals
variant clears overall expectancy/PF but fails phase expectancy in train and
test. This is a research candidate only, not a live candidate.

### Rejection Block

Rejection Block has good MFE but poor final monetization.

- `39` activated trades
- current net expectancy: `-0.087709R`
- full `1R` audit expectancy: `+0.008696R`
- full `1R` audit PF: `1.018351`
- invalidation rate: `82.05%`

This suggests a weak entry/confirmation quality problem, not just a target
distance problem.

### IFVG / Reclaimed OB

The 4h IFVG/Reclaimed probe has too little evidence.

- `4` activated trades total
- current net expectancy: `-0.705348R`
- full `2R` audit expectancy: `+0.144653R`
- sample is far below validation gates

The high MFE values are interesting, but this cannot be promoted without a
larger replay/control set.

## Root Cause Update

Current dominant blockers:

1. Cost drag in R, especially when stops are very tight.
2. Exit policy mismatch: some models generate MFE but current runner targets
   fail to monetize it.
3. Entry quality remains weak: Silver Bullet and Rejection Block have high
   invalidation rates even under simpler exits.
4. Walk-forward phase instability: the improved Turtle full-1R variant still
   fails phase-level expectancy.

## Algorithm Direction

Do not add more entry variants blindly. Next useful work is:

1. Treat `turtle_soup` + `dol_hierarchy` + full `1R` as a research-only exit
   candidate.
2. Run the same full `1R` policy on the late/control windows before changing
   any live config.
3. Add cost-aware filters only after verifying they do not collapse sample size.
4. Keep all live model switches disabled until a candidate passes costed OOS and
   control gates.

Verification:

- `python -m unittest tests.test_new_ict_models` passed, `100` tests.
- New full `1R` Turtle OOS walk-forward reports both failed.
