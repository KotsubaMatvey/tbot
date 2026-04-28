# ICT Decision Score May-October 2025

Dataset: `data/history_2025-05-01_2025-10-31`

Preset:

```bash
python -m backtesting.run_ict_batch --config configs/backtests/ict_may_oct_2025.json
```

This is an event study, not a full execution simulation. It excludes fees, slippage, position sizing, partial exits, and break-even logic.

## Per-Model Filter Summary

Threshold: `decision_score >= 50`.

| Scope | Base Events | Base Expectancy | Filtered Events | Filtered Expectancy | Filtered Out |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1H BTC/ETH/SOL | 956 | +0.262R | 528 | +0.376R | 428 |
| 4H BTC/ETH/SOL | 276 | +0.259R | 148 | +0.470R | 128 |
| 30M BTC | 836 | +0.283R | 410 | +0.533R | 426 |

## 1H Filtered Model Ranking

Threshold: `decision_score >= 50`, symbols: BTCUSDT, ETHUSDT, SOLUSDT.

| Model | Events | Expectancy | Target hit | Invalidation | Avg RR |
| --- | ---: | ---: | ---: | ---: | ---: |
| `breaker_block` | 22 | +2.145R | 27.3% | 13.6% | 16.77 |
| `ifvg_retest` | 36 | +1.183R | 16.7% | 83.3% | 10.09 |
| `rejection_block` | 41 | +0.706R | 43.9% | 56.1% | 3.41 |
| `turtle_soup` | 396 | +0.278R | 8.1% | 79.5% | 9.03 |
| `reclaimed_ob` | 3 | +0.000R | 33.3% | 66.7% | 69.68 |
| `silver_bullet` | 8 | -0.018R | 12.5% | 50.0% | 2.00 |
| `mitigation_block` | 22 | -0.325R | 13.6% | 81.8% | 2.19 |

## Notes

- The first per-model filters improved expectancy on all tested scopes.
- `breaker_block`, `ifvg_retest`, and `rejection_block` are the strongest 1H candidates after filtering.
- `turtle_soup` still produces the most signals, but its edge mostly comes from large RR tails.
- `mitigation_block` remains weak after filtering.
- `ict2022_mss_fvg` has too few filtered signals for judgment.
- `silver_bullet` remains under-sampled and weak in this implementation.
