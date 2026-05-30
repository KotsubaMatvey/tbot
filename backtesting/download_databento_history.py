from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import pandas as pd

from timeframes import SUPPORTED_TIMEFRAMES

DATABENTO_DATASET = "GLBX.MDP3"
TIMEFRAME_SOURCE = {
    "1m": ("ohlcv-1m", None),
    "3m": ("ohlcv-1m", "3min"),
    "5m": ("ohlcv-1m", "5min"),
    "15m": ("ohlcv-1m", "15min"),
    "30m": ("ohlcv-1m", "30min"),
    "1h": ("ohlcv-1h", None),
    "4h": ("ohlcv-1h", "4h"),
    "1d": ("ohlcv-1d", None),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Download CME futures OHLCV history from Databento into backtest CSV files.")
    parser.add_argument("--out-dir", default="data/history")
    parser.add_argument("--symbols", nargs="+", required=True, help="CME product roots, e.g. MNQ MES 6E.")
    parser.add_argument("--timeframes", nargs="+", required=True, choices=SUPPORTED_TIMEFRAMES)
    parser.add_argument("--start", required=True, help="UTC start datetime/date accepted by Databento.")
    parser.add_argument("--end", required=True, help="UTC exclusive end datetime/date accepted by Databento.")
    parser.add_argument("--dataset", default=DATABENTO_DATASET)
    parser.add_argument("--roll-rule", choices=["v", "n", "c"], default="v", help="Continuous contract roll rule; v is volume based.")
    parser.add_argument("--contract-rank", type=int, default=0, help="Continuous contract rank; 0 is the front contract.")
    parser.add_argument("--estimate-only", action="store_true", help="Print Databento request cost estimates without downloading time series.")
    args = parser.parse_args(argv)

    if args.contract_rank < 0:
        parser.error("--contract-rank must be non-negative")

    try:
        import databento as db
    except ImportError:
        print("Error: Databento downloader requires the optional package: python -m pip install databento")
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    client = db.Historical()
    requested_schemas = sorted({TIMEFRAME_SOURCE[timeframe][0] for timeframe in args.timeframes})
    if args.estimate_only:
        total_cost = 0.0
        for symbol in args.symbols:
            continuous_symbol = f"{symbol.upper()}.{args.roll_rule}.{args.contract_rank}"
            for schema in requested_schemas:
                cost = float(
                    client.metadata.get_cost(
                        dataset=args.dataset,
                        schema=schema,
                        symbols=continuous_symbol,
                        stype_in="continuous",
                        start=args.start,
                        end=args.end,
                    )
                )
                total_cost += cost
                print(f"Estimated cost USD {cost:.6f}: {continuous_symbol} {schema}")
        print(f"Estimated total cost USD {total_cost:.6f}")
        return 0

    for symbol in args.symbols:
        local_symbol = symbol.upper()
        continuous_symbol = f"{local_symbol}.{args.roll_rule}.{args.contract_rank}"
        frames = {
            schema: fetch_frame(client, args.dataset, continuous_symbol, schema, args.start, args.end)
            for schema in requested_schemas
        }
        for timeframe in args.timeframes:
            schema, resample_rule = TIMEFRAME_SOURCE[timeframe]
            candles = frame_to_candles(frames[schema], resample_rule)
            if not candles:
                print(f"SKIP {local_symbol} {timeframe}: no candles returned")
                continue
            path = out_dir / f"{local_symbol}_{timeframe}.csv"
            write_csv(path, candles)
            print(f"Wrote {len(candles)} candles from {continuous_symbol}: {path}")
    return 0


def fetch_frame(client: Any, dataset: str, symbol: str, schema: str, start: str, end: str) -> pd.DataFrame:
    data = client.timeseries.get_range(
        dataset=dataset,
        schema=schema,
        symbols=symbol,
        stype_in="continuous",
        start=start,
        end=end,
    )
    return data.to_df()


def frame_to_candles(frame: pd.DataFrame, resample_rule: str | None) -> list[dict[str, float | int]]:
    if frame.empty:
        return []
    bars = _ohlcv_frame(frame)
    if resample_rule is not None:
        bars = (
            bars.resample(resample_rule, origin="epoch", closed="left", label="left")
            .agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"})
            .dropna(subset=["open", "high", "low", "close"])
        )
    return [
        {
            "time": int(timestamp.value // 1_000_000),
            "open": float(row.open),
            "high": float(row.high),
            "low": float(row.low),
            "close": float(row.close),
            "volume": float(row.volume),
        }
        for timestamp, row in bars.iterrows()
    ]


def _ohlcv_frame(frame: pd.DataFrame) -> pd.DataFrame:
    missing = [column for column in ("open", "high", "low", "close", "volume") if column not in frame.columns]
    if missing:
        raise ValueError(f"Databento OHLCV frame missing columns: {', '.join(missing)}")
    bars = frame.loc[:, ["open", "high", "low", "close", "volume"]].copy()
    timestamps = frame["ts_event"] if "ts_event" in frame.columns else frame.index
    bars.index = pd.to_datetime(timestamps, utc=True)
    return bars[~bars.index.duplicated(keep="last")].sort_index()


def write_csv(path: Path, candles: list[dict[str, float | int]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["time", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        writer.writerows(candles)


if __name__ == "__main__":
    raise SystemExit(main())
