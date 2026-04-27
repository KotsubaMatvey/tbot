# Displacement Rules

## Valid Displacement

Valid displacement requires all of:

- body close beyond structure;
- FVG created in the displacement leg;
- meaningful body-to-range;
- range expansion.

Do not use a 2.0 ATR default hard rule. Keep ATR variants for future tests.

## Grades

`weak`:

- close beyond level but no FVG;
- or `body_ratio < 0.50`;
- or `range_expansion < 1.2`;
- or overlapping grind.

`valid`:

- close beyond structure;
- created FVG;
- `body_ratio >= 0.50`;
- `range_expansion >= 1.2`.

`strong`:

- close beyond structure;
- created FVG;
- `body_ratio >= 0.70`;
- `range_expansion >= 1.5`;
- preferably after sweep;
- fast price delivery.

## Fields

Displacement profile should expose:

- `has_displacement`
- `displacement_grade`
- `body_ratio`
- `range_expansion`
- `close_beyond_structure`
- `created_fvg_after_break`
- `bars_count`
- `impulse_direction`

Model usage:

- Model 1 requires valid displacement; strong boosts score.
- Model 2 IFVG breach requires valid displacement; strong boosts score.
- Model 3 LTF pickup requires valid displacement; strong boosts score.
