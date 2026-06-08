# Turtle Soup Stability Candidate - min_risk_bps 25

Date: `2026-06-05`

## Diagnosis

The locked `min_risk_bps=35` Turtle Soup profile was already profitable after
costs, but it was not stable enough for intraday promotion:

- OOS `2023-07-01..2024-12-31` had only `92` deduped trades, so it failed
  `min_total_trades`.
- Late-control `2025-01-01..2026-04-20` had only `82` deduped trades and
  failed sample/phase gates.
- Bucket diagnostics showed weaker late-control performance in ETH `15m`,
  long trades, and London `02:00-05:00`; however, cutting those buckets reduced
  sample further.
- The main fixable issue was not negative edge, but excessive sample reduction
  from `min_risk_bps=35`.

## Strategy Change

Keep the same model and structure, change only the post-model risk filter:

- `min_risk_bps`: `35` -> `25`

Everything else stays unchanged:

- BTC/ETH only
- `15m+30m`
- Asian range Turtle Soup
- retest entry
- `dol_hierarchy` target
- kill zones `02:00-05:00`, `07:00-10:00`, `13:00-16:00`
- `strong` quality only
- `require_no_smt=true`
- first session dedupe
- funding-aware costs

This is a stability/sample repair, not a new model.

## Official Replay Results

Config:
`configs/backtests/turtle_soup_btc_eth_stability_minrisk25_2022_2026_15m_30m.json`

| Run | Period | Deduped trades | Winrate | Expectancy R | PF | Max DD R | Max losses | Sharpe | Gate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| IS | 2022-01-01..2023-06-30 | 232 | 75.86% | 0.277730 | 1.932881 | 5.800007 | 3 | 4.015885 | pass |
| OOS | 2023-07-01..2024-12-31 | 151 | 76.82% | 0.278062 | 1.947083 | 6.164166 | 3 | 3.243742 | pass |
| Late-control | 2025-01-01..2026-04-20 | 129 | 78.29% | 0.307165 | 2.142191 | 4.302191 | 3 | 3.716040 | pass |
| External | 2023-07-01..2026-04-20 | 280 | 77.50% | 0.291470 | 2.032734 | 6.164166 | 3 | 3.461770 | pass |
| Full | 2022-01-01..2026-04-20 | 512 | 76.76% | 0.285244 | 1.986164 | 6.164166 | 3 | 3.663145 | pass |

Full-sample yearly breakdown:

| Year | Trades | Expectancy R | PF | Total R |
| --- | ---: | ---: | ---: | ---: |
| 2022 | 165 | 0.240857 | 1.747789 | 39.741450 |
| 2023 | 114 | 0.289546 | 2.020210 | 33.008207 |
| 2024 | 104 | 0.323760 | 2.206719 | 33.671046 |
| 2025 | 97 | 0.289489 | 2.026850 | 28.080464 |
| 2026 partial | 32 | 0.360744 | 2.571599 | 11.543801 |

## Decision

Use the `min_risk_bps=25` candidate for paper/shadow validation.

New paper/shadow profile:
`configs/paper_model_filters_turtle_soup_stability_minrisk25_2026.json`

Live remains disabled. Historical replay is not enough for live deployment
because the next unknown is scanner-forward behavior: actual alert timing,
fill rate, slippage, missed retests, and net realized outcome.

## Forward Gates

Require before any live pilot:

- at least `100` forward paper signals;
- fill rate `>=70%`;
- average slippage `<=2` bps;
- average net outcome `>0R`;
- no unexplained drift between backtest signal frequency and scanner signal
  frequency.
