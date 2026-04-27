# IFVG Rules

## Primitive IFVG

Sweep is not required for primitive IFVG.

Long IFVG:

- source FVG is bearish;
- body close above source FVG high;
- wick-only breach is not inversion.

Short IFVG:

- source FVG is bullish;
- body close below source FVG low;
- wick-only breach is not inversion.

Breach must have valid displacement.

## Entry Model 2

Entry Model 2 is stricter than primitive IFVG:

- sweep is required;
- opposite FVG must exist before breach;
- breach timestamp must be after sweep timestamp;
- retest timestamp must be after breach;
- IFVG must not be stale;
- HTF alignment is required in strict mode.

## IFVG Grade

`weak`:

- wick-only breach;
- no displacement;
- against HTF bias;
- outside HTF POI;
- stale.

`valid`:

- body close beyond source FVG;
- valid displacement;
- aligned with HTF bias.

`strong`:

- body close beyond source FVG;
- strong displacement;
- preceding sweep close to breach;
- inside HTF POI;
- objective aligned and unreached.

Model 2 ignores weak IFVG, allows valid, and boosts strong.

## Fields

- `ifvg_grade`
- `source_fvg_direction`
- `source_fvg_time`
- `ifvg_ce_level`
- `ifvg_retest_depth`
- `ifvg_retest_touched_ce`
- `ifvg_retest_breached_ce_by_close`
- `ifvg_breach_time`
- `ifvg_retest_time`
- `ifvg_time_to_retest_bars`
- `preceding_sweep`
- `sweep_time`
- `sweep_level`
- `bars_sweep_to_breach`
- `breach_displacement_factor`
- `breach_displacement_grade`
- `has_htf_confluence`
- `rr_to_objective`
