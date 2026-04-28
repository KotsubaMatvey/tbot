# Entry Model Taxonomy

## Project Taxonomy

The current project uses Sayx-style execution model names.

Preserve these names:

- Entry Model 1: Sweep -> BOS/MSS -> post-BOS FVG / imbalance.
- Entry Model 2: Sweep -> FVG Inversion / IFVG.
- Entry Model 3: Missed Entry -> Full Fill FVG / retracement -> LTF pickup.

## NotebookLM Naming Conflict

Some NotebookLM notes or ICT summaries may use different labels:

- Model 1 = OB retest.
- Model 2 = FVG entry.
- Model 3 = Turtle Soup + SMT.

Do not rename or replace the current project models with those labels.

If those concepts are useful, map them as supporting components or future strategies, not as replacements for the current Entry Model 1/2/3.

## Common Requirements

All models should carry:

- HTF metadata.
- Sweep or source-zone metadata where relevant.
- Structure and displacement metadata.
- FVG/IFVG/OB lifecycle metadata.
- Timestamp ordering metadata.
- Risk quality metadata.

## Common Rejection Rules

Reject or penalize:

- Opposite strict HTF bias.
- Neutral HTF in strict Model 3.
- Missing HTF context in strict mode.
- Missing required sweep for Model 1 and Model 2.
- Wrong timestamp ordering.
- Wick-only IFVG breach.
- Invalid or tiny risk.
- Ancient unbounded zones.

## NotebookLM Candidate Models

Use these as implementation candidates, not as profitability claims.

### ICT 2022 MSS + FVG

- HTF: prefer a tested HTF PD array and long in discount / short in premium.
- Trigger: liquidity sweep, body-close MSS, displacement leg that creates FVG.
- Entry: FVG edge or CE.
- Stop: sweep extreme.
- Target: nearest liquidity or HTF external liquidity when context provides it.
- Filters: London / NY killzone and SMT are candidate filters; SMT is not mandatory until a stable correlated feed exists.

### Breaker Block

- Trigger: failed order block after liquidity sweep and displaced structure break.
- Entry: breaker boundary or mean threshold.
- Stop / invalidation: mean threshold or block extreme depending on configured stop mode.
- Target: opposite liquidity pool.

### Rejection Block

- Confidence: medium.
- Trigger: candle sweeps a prior swing body level but does not exceed the wick extreme.
- Entry: highest body for bearish rejection, lowest body for bullish rejection.
- Stop: beyond the original wick extreme.
- Target: nearest internal liquidity.

### Mitigation Block

- Confidence: medium-low.
- Trigger: failure swing without a clean liquidity sweep, followed by MSS.
- Entry: retest of the opposite candle in the failed swing leg.
- Stop: beyond the mitigation candle extreme.
- Target: nearest liquidity or opposing void CE when available.

### Crypto SMT

- Primary pair: BTCUSDT vs ETHUSDT.
- Secondary confirmation: ETHUSDT vs SOLUSDT when available.
- Bullish SMT: primary makes a lower low while the comparison asset makes a higher low.
- Bearish SMT: primary makes a higher high while the comparison asset makes a lower high.
- Defaults: 3-candle swings (`left=1`, `right=1`), lookback 50 bars, max 10 bars between compared extrema, minimum divergence 5 bps, minimum close-return correlation 0.7.
- Use SMT as a recommended filter for reversal entries. Do not require it globally until cross-asset data is present in the runner/live scanner.

## Killzone Defaults

- ICT 2022 MSS + FVG: require sweep and MSS in London Open `02:00-05:00` or NY Open `07:00-10:00` New York time.
- Silver Bullet: require FVG retest/entry in `10:00-11:00` or `14:00-15:00` New York time.
- Turtle Soup: optional killzone filter; event is the sweep/raid.
- Breaker Block: optional `02:00-11:00` New York filter; event is MSS / breaker trigger.
- Rejection Block and Mitigation Block: optional London / NY Open filter; event is zone retest.
- Window start and end are inclusive for minute-level timestamps.
