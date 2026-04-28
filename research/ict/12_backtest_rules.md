# Backtest Rules

## Purpose

Backtests are event studies for model quality and context quality.

They are not full execution simulations.

## Scope

Keep:

- Forward-bar event study.
- Hit 1R before invalidation.
- Hit 2R before invalidation.
- Invalidation rate.
- MFE / MAE style metrics if already present.
- Score distribution.

Do not add:

- Fees.
- Slippage.
- Break-even.
- Partial exits.
- Full position management.

## Required Modes

`--htf-mode strict`:

- Require HTF context and allowed direction.

`--htf-mode soft`:

- Allow weaker context but penalize score.

`--htf-mode off`:

- Legacy comparison behavior.

## Research Variants

Add when implementation reaches Step 6:

- `--require-displacement true|false`
- `--model3-fill-threshold 0.25|0.5|1.0`
- `--entry-mode near_edge|midpoint|full_fill`
- `--same-bar-policy conservative|neutral|optimistic`

If scope is constrained, prioritize:

- `--require-displacement`
- `--model3-fill-threshold`

## Event Columns

Common columns:

- `setup_timestamp`: model creation timestamp used for event-study alignment.
- `entry_time`: timestamp of fill/retest/activation when different from setup creation.
- `entry_price`: explicit model-computed entry price, not recomputed by the runner.
- `hit_1r_before_invalidation`
- `hit_2r_before_invalidation`
- `displacement_factor`
- `has_displacement`
- `swing_significance`
- `fvg_status`
- `fvg_fill_percent`
- `htf_bias`
- `htf_location`
- `htf_zone_type`
- `htf_objective_type`
- `htf_objective_level`

Model 2 columns:

- `source_fvg_direction`
- `breach_time`
- `breach_displacement_factor`
- `ifvg_mean_threshold`

Model 3 columns:

- `source_zone_type`
- `source_zone_time`
- `fill_percent`
- `fill_mode`
- `ltf_mss_time`

## Report Sections

Add summaries:

- `summary_by_htf_bias`
- `summary_by_htf_location`
- `summary_by_htf_zone`
- `summary_by_displacement`
- `summary_by_model3_fill_threshold`
- `summary_by_fvg_status`

## Interpretation Notes

HTF strict should reduce signal count versus legacy.

If strict mode does not reduce signals, gating is too weak.

If nearly every signal scores high, scoring is not calibrated.

If strict quality worsens badly, HTFContext may be too crude or objective/location rules may be misweighted.

## Lookahead Rule

All primitive snapshots, HTF context, LTF context, FVG lifecycle state, and objective state must be sliced to the current replay timestamp.

No future candles may influence current setup creation.

## New ICT Model Event Alignment

For `backtesting.run_ict_models`, event-study rows are aligned by `setup.timestamp`.

- `setup.timestamp` is the model confirmation time.
- `entry_time` is stored separately when a later retest/fill activates the setup.
- Forward event windows are sliced from `setup.timestamp`.
- R-based outcomes are measured from `entry_time`.
- If invalidation occurs before `entry_time`, `invalidated_before_entry=True` and the setup is not counted as an activated trade.
- Same-bar order is controlled by `same_bar_policy`: conservative = invalidation first, optimistic = target first, neutral = ambiguous.

## Turtle Soup Quality Filters

Turtle Soup keeps the one-candle sweep/close-back model but adds configurable quality filters:

- `turtle_soup_min_wick_fraction`: wick beyond liquidity as a fraction of candle range.
- `turtle_soup_min_wick_atr_ratio`: optional wick beyond liquidity versus recent average range.
- `turtle_soup_min_close_back_fraction`: close-back distance inside the swept level as a fraction of candle range.
- `turtle_soup_min_level_age_bars`: minimum age of swept swing liquidity.
- `turtle_soup_max_confirmation_bars`: defaults to one-candle confirmation.
- `turtle_soup_require_killzone`: optional NY killzone gate.
- `turtle_soup_require_smt`: optional SMT gate only if context provides SMT confirmation.

## Silver Bullet Retest Window

Silver Bullet uses New York time via `zoneinfo`.

- FVG creation must occur inside a configured Silver Bullet window.
- `silver_bullet_windows` accepts one or more NY windows such as `10:00-11:00`.
- `silver_bullet_retest_must_occur_within_window=True` requires the retest/entry inside the same configured window.
- `silver_bullet_max_retest_bars` limits how late the retest can occur after FVG creation.

## Chart Styling

Chart elements use stable colors:

- Bullish FVG: green; bearish FVG: red.
- IFVG: purple.
- Order Block: blue.
- Breaker Block: orange.
- Rejection Block: yellow/gold.
- Turtle Soup: cyan.
- Silver Bullet: magenta.
- Liquidity/structure markers use contrasting line colors.

Labels use transparent boxes with thin colored borders so candles remain visible underneath.
