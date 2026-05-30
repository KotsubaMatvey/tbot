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

## CME Index Futures Research

Crypto history remains sourced from Binance Futures. For CME Micro E-mini
research, install the optional official Databento client and set its API key:

```powershell
python -m pip install databento
$env:DATABENTO_API_KEY = "db-..."
python -m backtesting.download_databento_history --estimate-only --symbols MNQ MES --timeframes 30m --start 2022-01-01 --end 2024-11-06
python -m backtesting.download_databento_history --out-dir data/history_cme_oos_2022-01-01_2024-11-06 --symbols MNQ MES --timeframes 30m --start 2022-01-01 --end 2024-11-06
python -m backtesting.run_ict_batch --config configs/backtests/cme_crypto_turtle_oos_research.json
```

`download_databento_history` requests volume-based front continuous contracts
(`MNQ.v.0`, `MES.v.0`) from CME `GLBX.MDP3` and writes the same OHLCV CSV
shape consumed by existing Binance backtests. CME runs use fixed point costs;
keep Binance runs on basis-point costs and do not combine their cost
assumptions. All index runs are research-only until costed out-of-sample gates
pass. Run `--estimate-only` and review Databento's USD estimate before any
historical download.

## Free Hyperliquid Research Feed

Hyperliquid exposes public recent OHLCV for core crypto perps and HIP-3 index
perps. The `xyz` deployment currently exposes `XYZ100` and `SP500`; these are
tradeable perpetuals on Hyperliquid, not CME `MNQ`/`MES` contracts.

```powershell
python -m backtesting.download_hyperliquid_history --out-dir data/history_hyperliquid_recent_2026-02-10_2026-05-25 --coins BTC ETH xyz:XYZ100 xyz:SP500 --timeframes 30m --start 2026-02-10 --end 2026-05-25T23:59:59Z --include-funding
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_recent_turtle_research.json
python -m backtesting.download_hyperliquid_history --out-dir data/history_hyperliquid_recent_2026-02-10_2026-05-25 --coins BTC ETH xyz:XYZ100 xyz:SP500 --timeframes 15m --start 2026-03-20 --end 2026-05-25T23:59:59Z --include-funding
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_recent_silver_bullet_research.json
python -m backtesting.run_ict_batch --config configs/backtests/hyperliquid_official_silver_bullet_research.json
```

The public `candleSnapshot` endpoint retains only the most recent candles
(officially capped at 5000). Use this feed for recent research and forward
collection only; it is not a multi-year OOS substitute. Hyperliquid profiles
load hourly `fundingHistory` rows and include funding in net results using
entry price as the notional-price proxy. Strategies remain disabled for live
trading until long enough costed validation gates pass.
