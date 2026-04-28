# ICT Telegram Trading Bot

Python Telegram bot for Binance Futures market analysis.

## Architecture

```text
bot.py

handlers/
  __init__.py
  callbacks.py
  charts.py
  common.py
  core.py
  sessions.py

market_primitives/
  common.py
  liquidity.py
  structure.py
  fvg.py
  ifvg.py
  order_blocks.py
  levels.py
  volume.py
  pd.py
  smt.py

strategies/
  types.py
  scoring.py
  formatter.py
  ict_models/
    registry.py
    turtle_soup.py
    silver_bullet.py
    ifvg_retest.py
    ict2022_mss_fvg.py
    breaker_block.py
    reclaimed_ob.py
    rejection_block.py
    mitigation_block.py
  legacy/
    entry_model_1_legacy.py
    entry_model_2_legacy.py
    entry_model_3_legacy.py

scanner/
  __init__.py
  engine.py
  snapshots.py
  cache.py
  dedup.py
  confluence.py
  scoring.py

presentation/
  types.py
  alert_builders.py
  chart_payloads.py
  formatters.py
```

## Features

- typed market primitives: swings, sweeps, BOS/CHOCH, FVG/IFVG, OB/breakers, EQH/EQL, PD, SMT, volume
- typed ICT setups: Turtle Soup, Silver Bullet, IFVG Retest, ICT2022 MSS+FVG, Breaker Block, Reclaimed OB, Rejection Block, Mitigation Block
- live strategy alerts use all current ICT models with per-model filters from `LIVE_MODEL_FILTER_CONFIG`
- strategy alerts include basic lifecycle status: limit pending, entry filled, cancelled, TP hit, SL hit
- archived legacy baselines: Entry Model 1, Entry Model 2, Entry Model 3 under `strategies/legacy/`
- Telegram alerts with optional chart overlays
- onboarding with primitive/model/direction preferences
- SQLite persistence for subscriptions and user settings
- classic channel alerts kept separately from ICT setup engine

## Setup

1. Create `.env` with your bot and payment credentials.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the bot:

```bash
python bot.py
```

## Required Environment

- `TELEGRAM_BOT_TOKEN`
- `CRYPTOBOT_TOKEN`
- `OWNER_IDS`
- `CHANNEL_ID`

## Verification

- `python -m compileall .`
- `python offline_smoke_test.py`
- `python offline_backtest.py`

## ICT Backtest Batch

The current research baseline uses the May-October 2025 dataset:

```bash
python -m backtesting.run_ict_batch --config configs/backtests/ict_may_oct_2025.json
```
