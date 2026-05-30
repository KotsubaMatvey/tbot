# Live SMT Context Plumbing - 2026-05-25

## Assumption and Boundary

The current research candidate is BTCUSDT Asian-range Turtle Soup on `30m`,
requiring same-sweep directional SMT against ETHUSDT. That rule is retained as
a project research hypothesis from the existing specification, not asserted as
a verbatim ICT rule.

Official public material checked:

- The Inner Circle Trader channel: https://www.youtube.com/@InnerCircleTrader
- Official Turtle Soup example visible on that channel:
  https://www.youtube.com/watch?v=PFUe6OKmKuk
- ICT X account supplied for monitoring: https://x.com/I_Am_The_ICT

The official pages accessible in this run identify a Turtle Soup example but
do not expose retrievable transcript text establishing a crypto BTC/ETH SMT
requirement. No live rule is promoted from unavailable source detail.

## Scanner Gap

Backtesting could provide `smt_divergences` to Turtle Soup. The live scanner
computed standalone SMT alerts after model detection, so no model detector
could receive paired-symbol SMT context. A same-sweep SMT-gated candidate
therefore could not be evaluated consistently in forward/live scanning.

## Change

- Build one scanner SMT map from already-fetched paired candles.
- Keep divergences oriented to the configured primary symbol only:
  `BTCUSDT` for `BTCUSDT:ETHUSDT`, `ETHUSDT` for `ETHUSDT:SOLUSDT`.
- Pass the mapped divergences and `has_smt_confirmation` into model detector
  configuration.
- Include `30m` in scanner SMT timeframes because it is the timeframe of the
  costed Turtle Soup research candidate.
- Reuse the same map for standalone SMT primitive alerts.

## Verification and Decision

- Unit coverage checks `30m` primary-symbol SMT mapping and detector context
  delivery.
- All models in `configs/live_model_filters_2025.json` remain disabled.
- Turtle Soup remains research-only: its previous costed same-sweep runs had
  positive aggregate net managed expectancy but failed walk-forward sample
  and out-of-sample gates. Forward observation can now be implemented without
  treating the model as live-approved.
