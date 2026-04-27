# Bias, Draw, and Liquidity Objective

## Separation

HTF bias is structure / order flow.

Objective is draw on liquidity / target.

Location is premium, discount, equilibrium, or unknown.

POI is the zone where entry is allowed.

Objective above does not create bullish bias. Objective below does not create bearish bias.

Correct:

```python
if structure_bias == "bullish" and objective_above:
    long_context_quality += bonus
```

Incorrect:

```python
if objective_above:
    bias = "bullish"
```

## Strict Long

- `structure_bias == bullish`
- objective above exists;
- objective is unreached;
- location is discount or price is inside bullish HTF POI;
- POI is not invalidated.

## Strict Short

- `structure_bias == bearish`
- objective below exists;
- objective is unreached;
- location is premium or price is inside bearish HTF POI;
- POI is not invalidated.

## Alignment

`aligned`:

- HTF bias and signal direction agree.

`mixed`:

- partial conflict.

`opposed`:

- signal direction against HTF.

`neutral`:

- no clear structure.

In strict mode aligned is allowed. Mixed/opposed are blocked or heavily penalized. Neutral blocks Model 3.

## Fields

- `structure_bias`
- `draw_direction`
- `objective_reached`
- `objective_unreached`
- `location`
- `poi_direction`
- `context_alignment`
- `allows_long`
- `allows_short`
- `reason`
