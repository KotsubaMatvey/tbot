from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import aiohttp

from timeframes import SUPPORTED_TIMEFRAMES

HYPERLIQUID_INFO_API = "https://api.hyperliquid.xyz/info"


async def main_async(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Download public Hyperliquid OHLCV candles into backtest CSV files.")
    parser.add_argument("--out-dir", default="data/history")
    parser.add_argument("--coins", nargs="+", required=True, help="API coins, e.g. BTC ETH xyz:XYZ100 xyz:SP500.")
    parser.add_argument("--timeframes", nargs="+", required=True, choices=SUPPORTED_TIMEFRAMES)
    parser.add_argument("--start", required=True, help="UTC start datetime/date.")
    parser.add_argument("--end", required=True, help="UTC end datetime/date.")
    parser.add_argument("--timeout", type=float, default=120.0, help="HTTP session timeout in seconds.")
    parser.add_argument("--include-funding", action="store_true", help="Also save hourly perp funding history for costed backtests.")
    args = parser.parse_args(argv)

    start_ms = parse_time_ms(args.start, is_end=False)
    end_ms = parse_time_ms(args.end, is_end=True)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=args.timeout)) as session:
        for coin in args.coins:
            local_symbol = output_symbol(coin)
            for timeframe in args.timeframes:
                candles = await fetch_candles(session, coin, timeframe, start_ms, end_ms)
                if not candles:
                    print(f"SKIP {coin} {timeframe}: no candles returned")
                    continue
                path = out_dir / f"{local_symbol}_{timeframe}.csv"
                write_csv(path, candles)
                print(f"Wrote {len(candles)} candles for {coin} as {local_symbol}: {path}")
            if args.include_funding:
                funding = await fetch_funding(session, coin, start_ms, end_ms)
                path = out_dir / f"{local_symbol}_funding.csv"
                write_funding_csv(path, funding)
                print(f"Wrote {len(funding)} hourly funding rows for {coin} as {local_symbol}: {path}")
    return 0


async def fetch_candles(
    session: aiohttp.ClientSession,
    coin: str,
    interval: str,
    start_ms: int,
    end_ms: int,
) -> list[dict[str, float | int]]:
    payload = {
        "type": "candleSnapshot",
        "req": {"coin": coin, "interval": interval, "startTime": start_ms, "endTime": end_ms},
    }
    async with session.post(HYPERLIQUID_INFO_API, json=payload) as response:
        data: Any = await response.json()
        if response.status != 200:
            raise RuntimeError(f"Hyperliquid error {response.status} for {coin} {interval}: {data}")
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected Hyperliquid payload for {coin} {interval}: {data}")
    deduped = {int(item["t"]): normalize_candle(item) for item in data}
    return [deduped[timestamp] for timestamp in sorted(deduped)]


async def fetch_funding(
    session: aiohttp.ClientSession,
    coin: str,
    start_ms: int,
    end_ms: int,
) -> list[dict[str, float | int]]:
    rows: dict[int, dict[str, float | int]] = {}
    cursor = start_ms
    while cursor <= end_ms:
        payload = {"type": "fundingHistory", "coin": coin, "startTime": cursor, "endTime": end_ms}
        async with session.post(HYPERLIQUID_INFO_API, json=payload) as response:
            data: Any = await response.json()
            if response.status != 200:
                raise RuntimeError(f"Hyperliquid error {response.status} for {coin} funding: {data}")
        if not isinstance(data, list):
            raise RuntimeError(f"Unexpected Hyperliquid funding payload for {coin}: {data}")
        if not data:
            break
        for item in data:
            normalized = normalize_funding(item)
            rows[int(normalized["time"])] = normalized
        next_cursor = int(data[-1]["time"]) + 1
        if next_cursor <= cursor:
            break
        cursor = next_cursor
    return [rows[timestamp] for timestamp in sorted(rows)]


def normalize_candle(item: dict[str, Any]) -> dict[str, float | int]:
    return {
        "time": int(item["t"]),
        "open": float(item["o"]),
        "high": float(item["h"]),
        "low": float(item["l"]),
        "close": float(item["c"]),
        "volume": float(item["v"]),
    }


def normalize_funding(item: dict[str, Any]) -> dict[str, float | int]:
    return {
        "time": int(item["time"]),
        "funding_rate": float(item["fundingRate"]),
        "premium": float(item["premium"]),
    }


def output_symbol(coin: str) -> str:
    symbol = coin.rsplit(":", 1)[-1].upper()
    if not symbol or not symbol.replace("_", "").replace("-", "").isalnum():
        raise ValueError(f"Unsupported output symbol for Hyperliquid coin: {coin}")
    return symbol


def write_csv(path: Path, candles: list[dict[str, float | int]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["time", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        writer.writerows(candles)


def write_funding_csv(path: Path, funding: list[dict[str, float | int]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["time", "funding_rate", "premium"])
        writer.writeheader()
        writer.writerows(funding)


def parse_time_ms(value: str, *, is_end: bool) -> int:
    text = value.strip()
    if len(text) == 10 and text[4] == "-" and text[7] == "-":
        text = f"{text}T23:59:59.999+00:00" if is_end else f"{text}T00:00:00+00:00"
    elif text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return int(parsed.timestamp() * 1000)


def main(argv: list[str] | None = None) -> int:
    return asyncio.run(main_async(argv))


if __name__ == "__main__":
    raise SystemExit(main())
