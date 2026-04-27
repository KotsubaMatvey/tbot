# Risk and Invalidation Policy

## Principle

Stop-loss and structural invalidation are separate fields.

- `stop_loss`: technical risk level used for R calculations.
- `structural_invalidation`: level where the trade idea is invalid.
- `invalidation_source`: why the invalidation level was selected.
- `stop_hit_policy`: how backtest stop is hit, usually `wick` for exchange-style touch.
- `invalidation_confirmation`: how ICT idea failure is confirmed, usually `close`.

ICT invalidation is often confirmed by candle close. Real exchange stops execute on touch/wick. Backtests must support both.

## Buffer

Use bps or ATR-like buffer, not pips:

```python
buffer = max(price * STOP_BUFFER_BPS / 10000, optional_atr * 0.05)
```

Defaults:

- `STOP_BUFFER_BPS = 2`
- `DEFAULT_STOP_MODE = "structural"`
- `DEFAULT_MODEL3_STOP_MODE = "source_zone_extreme"`
- `INVALIDATION_CONFIRMATION = "close"`

## Stop Modes

Model 1:

- `aggressive`: beyond FVG boundary.
- `standard`: beyond FVG CE / midpoint.
- `structural`: beyond sweep extreme.
- Default: `structural`.

Model 2:

- `aggressive`: near IFVG edge.
- `standard`: IFVG CE / 50%.
- `structural`: opposite IFVG boundary / breach failure.
- Default research mode: `standard`.

Model 3:

- `ltf_mss`: behind local LTF MSS protected swing.
- `source_zone_extreme`: behind source FVG / OB extreme.
- `htf_ob_extreme`: behind HTF OB extreme.
- Default baseline: `source_zone_extreme`.

## Backtest Requirements

Backtest events must serialize:

- `stop_mode`
- `model3_stop_mode`
- `stop_loss`
- `structural_invalidation`
- `invalidation_source`
- `risk_bps`
- `risk_valid`
- `stop_buffer_bps`
- `invalidation_confirmation`
- `stop_hit_policy`
