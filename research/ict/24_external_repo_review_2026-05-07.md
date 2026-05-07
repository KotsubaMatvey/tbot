# External ICT Repo Review - 2026-05-07

## Scope

Reviewed user-supplied GitHub repositories for ideas worth testing in this codebase.
Assumption: use these repos as research references only. Do not copy live-trading code into production without separate tests, license checks, and code review.

## High-Value References

### smart-money-concepts

Source: https://github.com/joshyattridge/smart-money-concepts

Useful because it provides compact pandas implementations for core SMC primitives:

- FVG with optional consecutive-gap joining and `MitigatedIndex`.
- Swing highs/lows with consecutive swing cleanup.
- BOS/CHOCH with close-break option.
- OB metadata including volume and percentage strength.
- Liquidity pools with swept index tracking.
- Previous high/low, sessions, and retracements.

Recommended use:

- Cross-check our primitive definitions against this library on fixed fixtures.
- Add missing metadata where it helps research: FVG mitigation index, liquidity swept index, OB strength/volume-style quality.
- Keep it as a reference/fixture generator, not a wholesale dependency unless we explicitly decide to adopt pandas-vectorized primitives.

### Asian Turtle Soup Trading Bot

Source: https://github.com/martin254/Asian-Turtle-Soup-Trading-Bot

Useful as a state-machine template for an Asian range Turtle Soup/Judas setup:

- Build Asian range.
- Require breach/sweep of Asian high or low.
- Require rejection back inside range within a timeout.
- Enter only during the target session.
- Align with HTF trend and an order-block style filter.
- Use structure/ATR stop and fixed RR.

Recommended use:

- Test a separate `asian_turtle_soup` variant instead of loosening the current Silver Bullet model.
- Define exact crypto session times before implementation, because BTC trades 24/7 and futures-style sessions do not map cleanly.

### Day-trading OTE entry

Source: https://github.com/ronald9954/Day-trading-OTE-entry-

Useful because the notebook turns ICT 2022 OTE into explicit data conditions on ES 5m:

- Session filter: Tuesday-Friday, AM `08:30-12:00`, PM `14:00-15:45`.
- Candidate scan checkpoints around `11:30` and `15:30`.
- Liquidity grab, BOS, imbalance, and displacement conditions before entry.
- Limit entry derived from stop and target: approximately one third of the distance from stop to target.
- Entry validity window around 45 minutes.
- Result model: no fill = 0R, stop = -1R, target = about 2.1R, otherwise EOD close outcome.

Recommended use:

- Add max-entry-wait and max-hold/EOD-style expiry to our simulator.
- Test OTE entry after sweep + BOS + displacement + FVG/imbalance as a separate model or ICT2022 variant.
- Do not copy the notebook directly; it is exploratory, hard-coded, and uses reversed-price data for shorts.

## Medium-Value References

### OPKYEI ICT-Trading

Sources:

- https://github.com/OPKYEI/ICT-Trading/blob/main/STRATEGY.md
- https://github.com/OPKYEI/ICT-Trading/blob/main/TRADING_LOGIC.md

Useful mainly for execution discipline and feature taxonomy:

- If a model predicts a fixed horizon, trade validity should use the same bar horizon.
- Avoid duplicate same-direction entries inside the active window.
- Late/restarted live entries need price validation: buy only if current price is not worse than original entry, sell only if current price is not worse than original entry.
- Feature candidates: session, day-of-week, liquidity distance, PD-array proximity, ATR/regime, market structure.

Recommended use:

- Add paper/live state constraints later.
- Export richer feature columns before any ML experiment.

### ozo

Sources:

- https://github.com/zakariab0/ozo/blob/master/judaswing.py
- https://github.com/zakariab0/ozo/blob/master/buy_structure.py
- https://github.com/zakariab0/ozo/blob/master/sell_structure.py

Useful as a procedural Judas Swing idea:

- Wait for London/NY session.
- Detect previous-session high/low sweep.
- After sweep, wait for structure break.
- Stop from recent candle extreme.
- Optional second entry near half the stop distance.

Recommended use:

- Test second-entry-at-half-risk only as a research option.
- Treat pair selection after sweep as an SMT-like idea, but not as a direct implementation.

### ict-ea

Source: https://github.com/darula-hpp/ict-ea

Useful only as filter hypotheses:

- Weekly open bias.
- Short MA vs long MA trend filter.
- Recent daily body/range exhaustion filter.
- Previous H1 candle body/range as a loose order-block proxy.

Recommended use:

- Consider weekly-open and exhaustion filters as grid dimensions.
- Do not port the EA logic directly; the ICT definitions and risk handling are loose.

## Low-Value / Avoid

### quotex-signal-bot

Sources:

- https://github.com/khokan4466/quotex-signal-bot/blob/main/smc_analyzer.py
- https://github.com/khokan4466/quotex-signal-bot/blob/main/quotex_signal_generator.py

Not useful for our engine:

- SMC layer is shallow: simple swings, trend, BOS, and sentiment score.
- Signal generator mixes generic TA, random OTC price adjustment, and broad accuracy claims.
- Possible async misuse around `get_smc_signal`.

Recommended use:

- Do not import logic from this repo.

## Suggested Backlog

1. Primitive audit: compare our FVG, swing, BOS/CHOCH, OB, and liquidity outputs against `smart-money-concepts` on small fixtures.
2. Metadata pass: add FVG mitigation index, liquidity swept index, and OB quality metrics where they improve reporting or filters.
3. New research model: implement Asian range Turtle Soup/Judas state machine with strict session, sweep, rejection, MSS/FVG, and HTF-bias gates.
4. OTE execution test: add entry-wait expiry and hold expiry, then test sweep + BOS + displacement + imbalance + OTE limit entry.
5. Filter experiments only after baseline works: weekly open bias, exhaustion filter, second entry near half risk.

