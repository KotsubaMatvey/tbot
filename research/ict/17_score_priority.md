# Score Priority

## Layers

Separate:

1. hard filters;
2. score modifiers;
3. future filters.

## Hard Filters in Strict Mode

- HTF alignment.
- Objective exists and is unreached.
- Correct location or active HTF POI.
- Valid model sequence.
- Valid risk.
- Valid displacement for Model 1 and Model 2.
- LTF reaction for Model 3.

## Score Modifiers

- `displacement_grade`
- FVG / IFVG quality
- sweep quality
- objective quality
- equal highs / equal lows
- distance to target
- RR to objective
- risk quality
- freshness
- retest timing

## Future Filters

Do not use these as active hard filters yet:

- Killzones
- SMT divergence
- DXY / macro context
- nested fractal logic

## Metadata

Each setup should expose:

- `htf_alignment`
- `objective_unreached`
- `objective_quality`
- `poi_quality`
- `displacement_grade`
- `fvg_quality`
- `ifvg_quality`
- `sweep_quality`
- `risk_quality`
- `rr_to_objective`
- `score_components`

Score components should be human-readable with `gates`, `quality`, and `risk` sections.

If high bucket is not statistically better than medium, report score as not calibrated.
