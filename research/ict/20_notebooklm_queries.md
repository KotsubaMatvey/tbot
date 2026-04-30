# NotebookLM Queries For ICT Model Refinement

Context for every query:

We are implementing ICT-style intraday crypto futures setups for BTCUSDT, ETHUSDT, and SOLUSDT. The bot scans execution timeframes from 1m to 1h, uses HTF context from 1h/4h/1d, and backtests with closed candles only. Please answer as implementable rules, not general trading advice. For each rule, separate required conditions, optional filters, invalidation, entry trigger, stop placement, first target, final draw on liquidity, and examples of cases that should be rejected.

## 1. Model Priority And Expected Frequency

Which ICT entry models are intended to be used most often for intraday/day trading, and which are more rare or context-specific? Rank these models for crypto intraday implementation: Turtle Soup, Silver Bullet, ICT 2022 MSS + FVG, IFVG Retest, Breaker Block, Reclaimed Order Block, Rejection Block, Mitigation Block. For each model, describe the expected market condition, best session/time window if any, and whether it should be a primary live model or research-only model.

## 2. HTF Context Gate

What exact higher-timeframe context should exist before looking for a lower-timeframe ICT entry? Clarify whether the setup requires HTF bias, premium/discount location, being inside or approaching a POI, and an unreached draw on liquidity. Also clarify which conditions are mandatory versus useful filters. Please include how strict the gate should be for day trading so that valid setups are not filtered out too early.

## 3. Turtle Soup

For Turtle Soup, what is the exact sequence of events? Clarify the swept liquidity type, minimum swing significance, whether SMT is required or optional, whether MSS is required after the sweep, whether a confirmation FVG is required, the entry trigger, stop/invalidation, and target selection. Also describe how to reject weak Turtle Soup signals that are just continuation breakdowns or breakouts.

## 4. Breaker, Reclaimed OB, And Mitigation Block Differences

Define the practical difference between Breaker Block, Reclaimed Order Block, and Mitigation Block. For each one, specify how the original block is formed, what must invalidate or reclaim it, what retest qualifies as entry, where the stop should go, whether mean threshold matters, and what target should be used. Include examples that distinguish these three models from each other.

## 5. ICT 2022 MSS + FVG

For the ICT 2022 model using liquidity sweep, MSS, displacement, and FVG, what exact candles confirm the setup? Clarify whether the FVG must be created by the displacement leg, how deep price should retrace into the FVG, whether CE entry is preferred over edge entry, where stop/invalidation belongs, and how long the setup remains valid after MSS.

## 6. IFVG Retest

For IFVG Retest, define the exact IFVG qualification rules. Does inversion require body close through the FVG or is wick violation enough? How many source FVG touches are allowed before inversion? How old can the source FVG be? Should entry be at IFVG edge or CE? Should stop be CE, opposite boundary, or a structural swing? What invalidates the trade idea before and after entry?

## 7. Silver Bullet For Crypto

How should Silver Bullet be adapted to crypto futures? Confirm the exact New York windows, whether only 10:00-11:00 NY should be traded or also 03:00-04:00 and 14:00-15:00, whether the FVG must form and retrace inside the same window, what target is valid, and whether BTC/ETH SMT is required or only optional confirmation.

## 8. Rejection Block

Define Rejection Block precisely. What candle or swing creates it, what body level is used for entry, what makes the rejection block fresh or invalid, what should happen if a new extreme forms before entry, and where should logical invalidation be placed? Clarify whether this model should be live-tradable or research-only.

## 9. Backtest Outcome Rules

For ICT intraday model backtesting, what is the correct way to count outcomes when using limit entries? Clarify how to handle target reached before entry, invalidation before entry, same-bar target and stop ambiguity, partial TP at 1R, move to breakeven, logical invalidation by candle close, and final target hit. Please return rules suitable for deterministic OHLC backtesting.
