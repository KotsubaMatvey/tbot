# Turtle Soup Optional SMT Strong-Quality IS

Date: 2026-06-04

Status: IS-only diagnostics. OOS remains untouched.

## Purpose

Test the practical version of optional SMT:

- Turtle Soup must stand on its own without SMT as a hard gate.
- SMT remains available as a confidence feature through `smt_score`.
- Session dedupe can prefer higher confidence, but only if the score is aligned
  with realized P&L.

IS window:

- `2022-01-01` through `2023-06-30`

## Config

Config:

- `configs/backtests/turtle_soup_btc_eth_is_2022_2023_optional_smt_strong_quality_30m.json`

Rules:

- model: `turtle_soup`
- symbols: BTCUSDT, ETHUSDT
- timeframe: `30m`
- range source: Asian range
- entry: retest
- sessions: `02:00-05:00,07:00-10:00,13:00-16:00`
- SMT pairs loaded, but no `turtle_soup_require_smt`
- model filter: `allowed_turtle_qualities=["strong"]`
- costs: commission `4.0` bps, slippage `1.0` bps, funding-aware
- session dedupe: `highest_score`

## Results

Raw filtered P&L:

| Scope | Trades | Net exp | PF | Max DD | Sharpe |
| --- | ---: | ---: | ---: | ---: | ---: |
| strong quality | 299 | `+0.115987R` | `1.322423` | `11.333963R` | `1.804706` |
| strong, no SMT | 263 | `+0.146863R` | `1.433826` | `10.566678R` | `2.193933` |
| strong, SMT | 36 | `-0.109585R` | `0.787065` | `8.367663R` | `-0.529752` |
| strong, medium score | 137 | `+0.302559R` | `2.121952` | `4.056237R` | `3.543108` |
| strong, high score | 162 | `-0.041794R` | `0.904120` | `14.001074R` | `-0.460602` |

Walk-forward with session dedupe:

| Phase | Trades | Net exp | Gross exp | PF | Max DD | Passed |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 263 | `+0.099492R` | `+0.465185R` | `1.268824` | `15.446388R` | false |
| train | 83 | `+0.254315R` | `+0.518072R` | `1.821940` | `3.221054R` | true |
| validation | 93 | `-0.089354R` | `+0.315327R` | `0.821193` | `11.903924R` | false |
| test | 89 | `+0.141954R` | `+0.562002R` | `1.470774` | `6.251154R` | true |

Failed gates:

- `min_managed_expectancy_r`
- `min_profit_factor`
- `max_drawdown_r`

Deduped SMT attribution:

- Selected after model filter: `299`
- Deduped trades: `263`
- Deduped no-SMT: `230`, `+0.130461R`
- Deduped SMT: `33`, `-0.116355R`

Session dedupe selection check:

| Selection | Trades | Net exp | PF | Max DD |
| --- | ---: | ---: | ---: | ---: |
| first | 263 | `+0.101206R` | `1.271144` | `13.182548R` |
| highest_score | 263 | `+0.099492R` | `1.268824` | `15.446388R` |
| timeframe_first | 263 | `+0.101206R` | `1.271144` | `13.182548R` |

## Interpretation

Optional SMT is the right architecture, but not yet the right selection signal.

The base strong-quality Turtle Soup subset has a real IS lead:

- `299` raw trades
- `+0.115987R` expectancy
- PF `1.322423`

But the lead is not stable enough:

- validation phase is negative;
- overall drawdown is above the `8R` gate;
- score calibration is wrong for this subset: medium-score trades outperform
  high-score trades.

SMT should not be a hard gate in this branch. It also should not receive blind
priority in session dedupe yet:

- no-SMT strong trades are profitable in this IS run;
- SMT strong trades are negative and below the `100` trade floor;
- `highest_score` dedupe is slightly worse than `first` and increases drawdown.

## Decision

Do not run OOS.

Continue improving the no-SMT strong-quality Turtle Soup base first. Keep SMT as
metadata/confidence for reporting, not as a required filter or decisive session
selection bonus until its P&L contribution is proven on a larger sample.

## Next Step

The next algorithmic diagnostic should explain why validation fails:

1. Split strong-quality trades by session, direction, symbol, score bucket, and
   target/no-trade reason across train/validation/test.
2. Avoid increasing `min_decision_score`; high-score trades currently underperform.
3. Test `first` session dedupe before `highest_score` in future strong-quality
   configs.
4. Restore Binance DNS/network and add BTCUSDT/ETHUSDT `15m` before any OOS.
