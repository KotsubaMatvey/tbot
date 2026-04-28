# ICT Decision Score May-June 2025

Dataset: `data/history_2025-05-01_2025-06-30`

Preset:

```bash
python -m backtesting.run_ict_batch --config configs/backtests/ict_may_jun_2025.json
```

The report is an event study, not a full execution simulation. It excludes fees, slippage, portfolio sizing, partial exits, and break-even logic.

## Aligned Context Summary

Threshold: `decision_score >= 50`.

| Scope | Events | Expectancy | Target hit | 1R hit | 2R hit | Invalidation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1H BTC/ETH/SOL | 350 | +0.358R | 27.4% | 37.7% | 26.3% | 60.0% |
| 4H BTC/ETH/SOL | 96 | +0.263R | 27.1% | 40.6% | 28.1% | 60.4% |
| 30M BTC | 268 | +0.194R | 33.2% | 43.7% | 24.3% | 57.8% |

## 1H Model Ranking

Threshold: `decision_score >= 50`, symbols: BTCUSDT, ETHUSDT, SOLUSDT.

| Model | Events | Expectancy | Target hit | Invalidation | Avg RR |
| --- | ---: | ---: | ---: | ---: | ---: |
| `turtle_soup` | 133 | +0.787R | 12.0% | 74.4% | 9.53 |
| `rejection_block` | 70 | +0.746R | 55.7% | 38.6% | 2.41 |
| `breaker_block` | 31 | +0.522R | 22.6% | 19.4% | 4.35 |
| `reclaimed_ob` | 7 | +0.390R | 57.1% | 28.6% | 30.37 |
| `ict2022_mss_fvg` | 1 | +1.676R | 0.0% | 0.0% | 6.96 |
| `ifvg_retest` | 28 | -0.139R | 21.4% | 71.4% | 5.22 |
| `mitigation_block` | 78 | -0.567R | 30.8% | 69.2% | 1.14 |
| `silver_bullet` | 2 | -1.000R | 0.0% | 100.0% | 2.00 |

## Notes

- `decision_score >= 70` is not universally better than `>= 50`; thresholds need per-model/per-timeframe calibration.
- `turtle_soup`, `rejection_block`, and `breaker_block` are the best 1H candidates.
- `ifvg_retest` and `breaker_block` look better on 4H, but the sample is small.
- `mitigation_block` needs tighter filters before it should be considered active.
- `silver_bullet` and `ict2022_mss_fvg` need more data before judging them.
