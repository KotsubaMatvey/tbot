# NotebookLM Answers: ICT Models 4/6/12 Integration

Source: user-provided NotebookLM synthesis from ICT materials.

## Core Workflow

1. Macro validation: use Monthly/Weekly direction, DXY validation when relevant, and interest-rate triad failure swings for FX-style macro confirmation.
2. Draw on liquidity: define an unreached HTF objective, usually old Daily highs/lows, equal highs/lows, HTF FVGs, or liquidity void fills.
3. Trade plan: wait for price to trade into the correct Premium/Discount side on Daily/4H.
4. Execution: enter on 15m/5m using Turtle Soup, Rejection Block, Reclaimed OB, IFVG Retest, Silver Bullet, or ICT2022 MSS+FVG depending on context.

Crypto implementation note: DXY/interest-rate triad is useful macro validation, but BTC/ETH/SOL intraday execution should not hard-block all trades on unavailable DXY/triad data unless that data is explicitly integrated and tested.

## Model Priority

| Model | Priority | Expected Frequency | Live Status |
| --- | --- | --- | --- |
| Silver Bullet | 1 | High, fixed NY windows | Primary live |
| IFVG Retest / Model 2 | 2 | High in LRLR/trending conditions | Primary live |
| ICT2022 MSS + FVG | 3 | Moderate reversal/expansion model | Primary live |
| Turtle Soup | 4 | Moderate at HTF liquidity pools | Primary live if SMT-confirmed |
| Breaker Block | 5 | Moderate after sweep + displacement | Live |
| Reclaimed OB | 6 | Lower-frequency continuation | Research/continuation |
| Rejection Block | 7 | Context-specific wick/body model | Research unless hard displacement filter exists |
| Mitigation Block | 8 | Lowest frequency, failure-swing variant | Research |

## HTF Context Gate

Mandatory:

- Clear unreached draw on liquidity.
- Direction aligned with Daily/4H institutional order flow.
- Longs only in HTF discount; shorts only in HTF premium.
- Reject HTF equilibrium.
- Reject if HTF objective is already tapped.

Useful but not always mandatory:

- Entry forms inside or near HTF POI: OB, FVG, Breaker.
- LRLR: path to objective has no major opposing PD arrays.

Implementation implication: current strict gate should probably require bias, P/D side, and unreached objective, but `inside_htf_poi` may need to be a score/filter rather than a universal hard block.

## Turtle Soup

Required sequence:

1. Price sweeps a major liquidity pool: PDH/PDL, EQH/EQL, or major intermediate swing.
2. Rejection happens quickly.
3. Candle closes back inside the previous range.

Crypto confirmation:

- SMT is required for live crypto Turtle Soup.
- Long example: BTC makes lower low while ETH/SOL makes higher low.

Entry:

- Limit at old high/low level, or market on close back inside range.

Stop and invalidation:

- Physical stop beyond sweep wick extreme.
- Logical invalidation if candle closes beyond sweep extreme.

Targets:

- TP1: internal range liquidity / FVG.
- Final: opposing external liquidity pool.

Reject:

- Price hangs/consolidates at the swept level for more than 3 candles.
- Sweep behaves like continuation BOS rather than immediate rejection.

## Breaker, Reclaimed OB, Mitigation Block

Breaker Block:

- OB performed a liquidity raid.
- Aggressive displacement breaks through the OB.
- Entry on block edge or Mean Threshold.
- Stop beyond Mean Threshold or far boundary depending risk mode.
- Target opposing liquidity or HTF POI.

Reclaimed OB:

- OB was already tested/respected once.
- Price breaks structure away from the OB again.
- Entry at original OB open/body after new structure break.
- Stop beyond original OB body/defensive extreme.
- Target next HTF DOL.

Mitigation Block:

- OB/failure-swing variant without liquidity raid.
- MSS/BOS breaks failure swing.
- Entry on last down/up candle in failure swing.
- Stop beyond block body extreme.
- Target liquidity void equilibrium or next PD array.

## ICT2022 MSS + FVG

Required sequence:

1. HTF POI tapped.
2. LTF liquidity sweep.
3. LTF MSS with displacement.
4. FVG created by that displacement leg.
5. Price retraces into the FVG.

Displacement:

- Full-bodied candle preferred.
- Body-to-range should be greater than 70%.

Entry:

- CE entry preferred for large gaps.
- Edge entry can be used for high-momentum LRLR.

Stop and invalidation:

- Physical stop at sweep extreme.
- Logical invalidation on close beyond FVG CE.

Validity:

- Valid until first target is reached or current killzone expires.
- Reject if DOL was already reached before retrace.
- Reject MSS without FVG.

## IFVG Retest

Qualification:

- IFVG requires body close through an existing FVG boundary.
- Wick breach alone is not inversion.
- Source FVG should have no more than 12 touches before inversion.
- Source FVG should be no older than 50-100 execution-timeframe candles.

Entry:

- Limit at IFVG edge.

Stop:

- Aggressive: beyond IFVG CE.
- Conservative: opposite boundary or nearest structural swing.

Invalidation:

- Body close back inside the gap beyond CE after entry.
- Cancel if main DOL is reached before entry retrace.

## Silver Bullet

NY windows:

- Primary: 10:00-11:00 and 14:00-15:00 NY.
- Secondary: 03:00-04:00 NY.

Rules:

- FVG must form inside the window, or be the first FVG price trades into during the window.
- Retest/entry must happen inside the same window.
- If window closes before retest, discard.
- Target minimum 2R or nearest session liquidity pool.
- SMT is optional score confirmation, not a hard block.

## Rejection Block

Definition:

- Bearish RB: swing high with wick rejection; use highest candle body level.
- Bullish RB: swing low with wick rejection; use lowest candle body level.

Freshness:

- Fresh until candle closes beyond wick extreme.
- If a deeper sweep/new extreme forms before entry, cancel and rebuild from new bodies.

Execution:

- Limit at body level.
- Logical invalidation: body close beyond wick extreme.
- Research-only unless paired with hard displacement filter greater than 2.0x ATR.

## Deterministic OHLC Backtest Rules

- Target before limit entry: cancel order, do not count as activated trade.
- Logical invalidation before entry: cancel order.
- Same-bar stop and target: flag ambiguity; conservative policy counts loss.
- At 1R: close 50%.
- After 1R: move stop to breakeven plus spread/buffer.
- Logical invalidation after fill: exit remaining position on candle close beyond CE/MT/relevant logical level.
- Final target: exit runner at HTF DOL touch.
