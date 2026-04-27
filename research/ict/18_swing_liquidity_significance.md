# Swing and Liquidity Significance

## Swing Tiers

`STH/STL`:

- 3-candle fractal.

`ITH/ITL`:

- short-term swing surrounded by lower short-term highs or higher short-term lows.

`LTH/LTL`:

- intermediate swing surrounded by lower intermediate highs or higher intermediate lows.

## Usage

Sweep detection:

- can use STH/STL and equal highs/lows.

MSS / CHOCH:

- should prefer ITH/ITL.

Objective:

- should prefer HTF swings, equal highs/lows, and old liquidity.

HTF dealing range:

- should prefer LTH/LTL or significant HTF swing pair.

## Body vs Wick

Liquidity level uses wick high / low.

Reaction body level:

- swing high body level = `max(open, close)`;
- swing low body level = `min(open, close)`.

## Equal Highs / Lows

Do not use fixed pips for crypto.

Use:

```python
tolerance = max(price * EQ_TOLERANCE_BPS / 10000, atr * EQ_ATR_MULT)
```

Defaults:

- `EQ_TOLERANCE_BPS = 5`
- `EQ_ATR_MULT = 0.10`
- `MIN_EQ_TOUCHES = 2`

## Liquidity Quality

`strongest`:

- HTF swing;
- Daily high / low;
- Weekly high / low.

`strong`:

- EQH / EQL;
- old liquidity.

`medium`:

- obvious isolated swing with displacement.

`weak`:

- fresh intraday swing;
- random short-term swing.

Ignore:

- inside bars;
- tiny body swings;
- minor swings in chop;
- already swept liquidity;
- consolidation noise.

## Fields

- `significance`
- `liquidity_level`
- `body_level`
- `is_equal_level`
- `equal_group_id`
- `age_bars`
- `swept`
- `swept_at`
- `context_poi_type`
- `quality`
