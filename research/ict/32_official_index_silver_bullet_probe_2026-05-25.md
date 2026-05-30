# Official ICT Index Silver Bullet Probe - 2026-05-25

Historical note: this probe was executed before the source-alignment change
documented in `33_official_ict_rule_map_and_silver_bullet_alignment_2026-05-25.md`.
It includes the former detector behavior that could accept an FVG created
before the Silver Bullet window. Use note 33 and its official baseline preset
for current results.

## Scope

The official Inner Circle Trader YouTube channel catalog was inspected on
`2026-05-25`. Relevant official video titles include:

- `ICT 2026 Trading MNQ Futures & CFD US100 \ April 28, 2026`:
  <https://www.youtube.com/watch?v=jz0RbL1oVK8>
- `NQ PM Session Silver Bullet - August 26, 2024`:
  <https://www.youtube.com/watch?v=yzZhC2lc1Ko>
- `2023 ICT Mentorship - ICT Silver Bullet Time Based Trading Model`:
  <https://www.youtube.com/watch?v=tRq1hyGGtl4>
- `June 24, 2024 NQ Turtle Soup Short`:
  <https://www.youtube.com/watch?v=PFUe6OKmKuk>

Inference limited to the titles: NQ/MNQ and ES are appropriate instruments
for researching the already implemented Silver Bullet/Turtle Soup models.
Public caption requests for these videos returned no transcript in this
environment, so this cycle does not introduce a new rule claimed to come from
their spoken content.

`xyz:XYZ100` and `xyz:SP500` are free Hyperliquid HIP-3 perpetual research
markets, not CME `NQ`/`ES` contracts. They can test execution viability for a
recent index-like feed, but they cannot validate CME behavior.

## Change

Added `configs/backtests/hyperliquid_recent_silver_bullet_research.json` for
the existing strict Silver Bullet candidate:

- `15m` execution timeframe;
- New York windows `10:00-11:00` and `14:00-15:00`;
- FVG retest within the same window and within one bar;
- fixed-R target with 50 percent taken at `1R`, remainder moved to break even;
- `9 bps` commission and `2 bps` slippage per side for HIP-3 index perps;
- `4.5 bps` commission and `1 bps` slippage per side for the BTC comparator.

No strategy detector was loosened or enabled for live execution.

## Data Coverage

Downloaded `15m` bars through the public Hyperliquid endpoint for `BTC`,
`ETH`, `xyz:XYZ100`, and `xyz:SP500`. Coverage validation passed on the common
full-day interval `2026-04-04` through `2026-05-24` at `100%` coverage with a
maximum gap of one bar for each symbol.

## Costed Silver Bullet Result

The reproducible batch was run with:

```powershell
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_recent_silver_bullet_research.json
```

| Market | Activated trades | Gross managed expectancy | Avg execution cost | Net managed expectancy | Profit factor | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `XYZ100` | 44 | `+0.091727R` | `1.507862R` | `-1.416135R` | `0.111207` | Reject |
| `SP500` | 58 | `+0.072371R` | `1.333651R` | `-1.261280R` | `0.075659` | Reject |
| `BTC` | 39 | `+0.056019R` | `0.308105R` | `-0.252086R` | `0.577496` | Reject |

All three walk-forward reports failed. The index-perp rejection is decisive
under these assumptions: narrow Silver Bullet stops make HIP-3 fee/slippage
larger than the gross signal edge.

## Predeclared Gate Diagnostics

Two existing gate principles were evaluated without changing the detector:

| Diagnostic | `XYZ100` | `SP500` | `BTC` | Conclusion |
| --- | ---: | ---: | ---: | --- |
| Keep only events with cost at most `0.30R` | 1 trade, `-1.201686R` | 0 trades | 25 trades, `-0.125688R` | Not viable |
| Keep first event per session | 36 trades, `-1.350438R` | 52 trades, `-1.313426R` | 34 trades, `-0.235357R` | Not viable |

The cost cap is already supported by `model_filters.max_execution_cost_r`.
Adding it to a live candidate would not produce an admissible sample here.

## ICT2022 MSS/FVG Probe

An additional research-only probe used the existing `ict2022_mss_fvg`
detector on `15m` bars with New York AM/PM sessions and the same costs. It
produced zero events on `XYZ100`, `SP500`, and `BTC`. No condition was relaxed
because no newly sourced ICT rule justifies doing so.

## Decision

Do not promote Silver Bullet, Turtle Soup, or ICT2022 to live trading on the
Hyperliquid index markets. Live filters remain disabled. Before a
Hyperliquid candidate can be accepted, the backtest must also model perpetual
funding and pass the existing costed walk-forward gates on a materially longer
forward-collected sample or appropriately sourced long-history index data.
