# Model Stops, Invalidation, and Targets

Source: user-provided NotebookLM synthesis of ICT materials for crypto implementation.

## Shared Definitions

- Stop loss is the physical exit level, usually placed beyond a wick or structural extreme.
- Invalidation is the candle-close condition that kills the setup logic.
- Mean Threshold is 50% of an Order Block, Breaker, or Mitigation Block body.
- Consequent Encroachment is 50% of an FVG or liquidity void.
- Every setup needs a draw on liquidity: internal liquidity first, external liquidity as the main objective.

## Model Rules

| Model | Stop | Invalidation | Cancel | First Target | Main Target |
| --- | --- | --- | --- | --- | --- |
| `turtle_soup` | Sweep wick extreme | Body close beyond swept level | Opposite liquidity reached before entry | Internal FVG/liquidity | Opposite external BSL/SSL |
| `ict2022_mss_fvg` | Sweep swing extreme | Body close beyond FVG CE | Target reached before FVG retrace | LTF swing | HTF draw on liquidity |
| `ifvg_retest` | Nearest swing or IFVG CE | Body close back inside gap beyond CE | New strong opposite FVG | Nearest liquidity | HTF draw on liquidity |
| `silver_bullet` | Nearest local swing | Body full-fill of FVG in hour | Window ends with no fill | 2R | Session/Daily liquidity |
| `breaker_block` | Breaker MT or far boundary | Body close beyond breaker MT | Target reached without retest | Nearest liquidity | Opposite pool or HTF POI |
| `rejection_block` | Swing wick extreme | Body close beyond rejection body level | Deeper new sweep before entry | Internal FVG | Opposite rejection body/liquidity |
| `mitigation_block` | Mitigation candle extreme | Body close beyond block MT | Failure swing extreme updated pre-entry | Nearest liquidity | HTF draw on liquidity |
| `reclaimed_ob` | OB MT or original OB extreme | Body close beyond OB MT on retest | HTF objective reached | New swing | Next liquidity objective |

## Crypto Adaptation

- SMT is BTC/ETH or ETH/SOL instead of DXY relationships.
- Body-close invalidation should be checked on the entry timeframe to avoid 1m noise.
- Killzones remain New York time: London `02:00-05:00`, NY `07:00-11:00`, Silver Bullet `10:00-11:00`.
- Backtests must use only closed candles. FVG/MSS candles are not valid until closed.
