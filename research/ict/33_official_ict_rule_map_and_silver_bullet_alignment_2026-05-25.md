# Official ICT Rule Map And Silver Bullet Alignment - 2026-05-25

## Evidence Boundary

The official Inner Circle Trader YouTube channel is the primary source:
<https://www.youtube.com/@InnerCircleTrader>.

On `2026-05-25`, official playlist and video metadata were accessible, but
direct YouTube caption/player requests from this environment returned
`LOGIN_REQUIRED`. Rule text below is therefore split into:

- `verified transcript derivative`: text indexed from a transcript page that
  links to the official video; suitable for correcting a direct mismatch, but
  to be rechecked against direct official captions when available;
- `official catalog only`: an official video exists on the topic, but no exact
  deterministic rule is asserted from its title alone;
- `internal adaptation`: a project research constraint, not presented as an
  ICT rule.

This boundary prevents secondary notes from silently becoming live strategy
requirements.

## Official Curriculum Map

| Topic needed by bot | Official source | Evidence available in this run | Implementation status |
| --- | --- | --- | --- |
| Context, expansion/retracement/reversal/consolidation | Core Content Month 1, `Elements Of A Trade Setup`: <https://www.youtube.com/watch?v=0LhteuLVuDU> | Indexed transcript derivative | Represented by HTF context and PD-array primitives; no new change |
| Liquidity draw and 2022 entry sequence | 2022 Mentorship Episode 2: <https://www.youtube.com/watch?v=tmeCWULSTHc> and Episode 3: <https://www.youtube.com/watch?v=nQfHZ2DEJ8c> | Indexed transcripts available | `ict2022_mss_fvg` represents sweep -> MSS -> FVG -> retest; remains research-only |
| FVG | Core Content Month 04, `ICT Fair Value Gaps FVG`: <https://www.youtube.com/watch?v=FgacYSN9QEo> | Official catalog only in this run | FVG primitive exists; exact refinements deferred |
| Order block | Core Content Month 04, `Orderblocks`: <https://www.youtube.com/watch?v=PIYh0CxoY9c> | Indexed transcript derivative | Existing primitive retained after focused block audit |
| Breaker block | Core Content Month 04, `ICT Breaker Block`: <https://www.youtube.com/watch?v=UrS-mtGHtAA> | Indexed summary derivative | Existing detector has sweep/MSS/retest structure; retained after audit |
| Mitigation block | Core Content Month 04, `Mitigation Blocks`: <https://www.youtube.com/watch?v=FOUzW0QmsfI> | Indexed summary derivative | Existing failure/MSS/retest structure retained after audit |
| Rejection block | Core Content Month 04, `ICT Rejection Block`: <https://www.youtube.com/watch?v=oALYX0HCSYw> | Indexed transcript derivative | Existing wick/body execution retained after audit |
| Reclaimed order block | Core Content Month 04, `Reclaimed ICT Orderblock`: <https://www.youtube.com/watch?v=X5pQjfkAUCI> | Official catalog only in this run | Research-only; no deterministic change |
| Silver Bullet | 2023 Mentorship, `ICT Silver Bullet Time Based Trading Model`: <https://www.youtube.com/watch?v=tRq1hyGGtl4> | Indexed transcript derivative with timestamped script | Corrected in this cycle |
| NQ Turtle Soup examples | `June 24, 2024 NQ Turtle Soup Short`: <https://www.youtube.com/watch?v=PFUe6OKmKuk>; `NQ PM Session Turtle Soup Long Full Pull`: <https://www.youtube.com/watch?v=HM2M9a4OEFQ> | Official catalog only in this run | Existing crypto SMT-on-sweep variant remains an internal research adaptation |
| SMT | `ICT Forex - The ICT Smart Money Technique or SMT`: <https://www.youtube.com/watch?v=isXicdayBwA> | Official catalog only in this run | Paired-feed plumbing exists; exact model gating not broadened |

## Rules Supported By Retrieved Text

### Framework And 2022 Model

The indexed transcript of official 2022 Mentorship Episode 2 identifies:

- primary study instruments as Nasdaq E-mini futures, with S&P and Dow also
  relevant;
- a weekly directional expectation followed by Daily liquidity targets;
- draws on price as old highs/lows containing stops or imbalances;
- after a stop run, lower-timeframe MSS and an FVG/imbalance retest as the
  execution framework;
- practice/backtesting and paper trading, rather than immediate live trading.

The indexed transcript of Episode 3 further identifies intraday `MSS` after
liquidity is taken and using the subsequent FVG/OB area for execution.

Mapping: `ict2022_mss_fvg` has the right high-level event order. It produced
no signals in the recent Hyperliquid `15m` probe; that is not evidence for
relaxing its conditions.

### Silver Bullet

The timestamped transcript derivative for the official 2023 Silver Bullet
video identifies:

- the model as time-based;
- three New York-local windows: `03:00-04:00`, `10:00-11:00`,
  `14:00-15:00`;
- a fair value gap formed inside the window and entry/repricing into that FVG
  inside the window;
- a minimum anticipated framework of `10` index points / `40` ticks or
  `15` Forex pips;
- draw-on-liquidity as part of the trade framework.

The previous detector contradicted the FVG timing requirement: it accepted an
FVG formed before the window if first retested inside the window. It also
omitted `03:00-04:00` from the model default.

## Implemented Correction

Changed:

- `strategies/ict_models/silver_bullet.py`
  - rejects any FVG whose creation timestamp is outside a configured Silver
    Bullet window;
  - default research windows now include London, AM and PM Silver Bullet.
- `strategies/ict_models/sessions.py`
  - adds `SILVER_BULLET_LONDON = "03:00-04:00"`.
- `tests/test_new_ict_models.py`
  - adds London-window acceptance coverage;
  - changes the prior-FVG test to require rejection.

This does not enable any live model. Existing live and constrained research
configs explicitly list only their tested windows and remain disabled or
research-only.

The absolute `10`-point index framework has not been forced onto
`xyz:XYZ100` or crypto: Hyperliquid HIP-3 markets are not CME index contracts,
and an instrument-specific unit/risk mapping must be established first.

## Source-Backed Hyperliquid Probe

Added:

- `configs/backtests/hyperliquid_official_silver_bullet_research.json`

It tests all three official Silver Bullet windows on the common `15m`
Hyperliquid sample from `2026-04-04` through `2026-05-24`. The `15m`
timeframe is a data-availability research proxy; it is not asserted to
duplicate ICT's finer index execution examples.

The report was rerun after hourly Hyperliquid funding support was added, as
documented in `34_hyperliquid_funding_cost_integrity_2026-05-25.md`.

| Market | Activated trades | Gross managed expectancy | Avg execution cost | Avg funding cost | Net managed expectancy | Profit factor | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `XYZ100` | 68 | `-0.058894R` | `1.415364R` | `0.004229R` | `-1.478487R` | `0.066541` | Fail |
| `SP500` | 81 | `-0.070278R` | `1.512049R` | `0.004126R` | `-1.586453R` | `0.047457` | Fail |
| `BTC` | 60 | `-0.124419R` | `0.357211R` | `0.000759R` | `-0.482389R` | `0.339243` | Fail |

No window is positive after cost in the report. For example, `BTC` net
managed expectancy is `-0.824799R`, `-0.378539R`, and `-0.288623R` for
London, AM and PM respectively.

## Focused Block Model Audit

The detailed text available for these Core Content videos in this run comes
from indexed transcript or summary derivatives linked to the official ICT
uploads. It is sufficient to reject unsupported changes, but not to add
unverified refinements.

| Model | Retrieved rule anchor | Current implementation audit | Decision |
| --- | --- | --- | --- |
| `rejection_block` | Wick extreme to open/close rejection range; execution from the body-side boundary with invalidation beyond the wick. | Uses the wick/body rejection level, stops beyond the wick, and cancels a stale retest after a new extreme. | No code change: aligned at the retrieved rule level. |
| `mitigation_block` | Failed swing followed by a structure shift, then retrace to the last opposing candle/block. | Detects failure and structure break, selects the opposing candle zone, and enters only on retest. | No code change: no confirmed mismatch. |
| `breaker_block` | Liquidity raid/failed order block, structure break, then retracement into the breaker. | Primitive requires sweep and break; strategy adds displacement quality and retest execution. | No code change: current restrictions remain research filters. |
| `reclaimed_ob` | An official Reclaimed ICT Orderblock lecture exists in Core Content Month 04. | No detailed retrievable transcript was sufficient to validate a deterministic adjustment in this cycle. | Keep research-only; no unsupported edit. |

## Live Decision

All live models remain disabled. The corrected Silver Bullet model is closer
to the retrieved ICT specification, but the costed recent Hyperliquid sample
rejects it for live use. Further code changes to Turtle Soup, blocks, SMT, or
ICT2022 require either directly accessible official content or a transcript
derivative with sufficient rule detail followed by independent costed
validation.

## Supporting Transcript Access

These are derivative access paths linked to the official videos, not
independent authorities:

- Silver Bullet timestamped script:
  <https://lilys.ai/en/notes/541724>
- 2022 Episode 2 transcript:
  <https://sozai.app/transcript/2022-ict-mentorship-episode-2/>
- 2022 Episode 3 transcript:
  <https://sozai.app/transcript/2022-ict-mentorship-episode-3/>
