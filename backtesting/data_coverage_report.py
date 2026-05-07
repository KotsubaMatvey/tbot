from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from backtesting.data import find_history_file, load_candles
from strategies.setup_utils import timeframe_to_ms

COVERAGE_FIELDS = [
    "symbol",
    "timeframe",
    "path",
    "candles",
    "start",
    "end",
    "expected_candles",
    "coverage_pct",
    "max_gap_bars",
    "passes",
    "missing_reason",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit historical candle coverage before ICT backtests.")
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--symbols", nargs="+", required=True)
    parser.add_argument("--timeframes", nargs="+", required=True)
    parser.add_argument("--required-start", default=None, help="YYYY-MM-DD inclusive UTC date.")
    parser.add_argument("--required-end", default=None, help="YYYY-MM-DD inclusive UTC date.")
    parser.add_argument("--min-coverage-pct", type=float, default=95.0)
    parser.add_argument("--max-gap-bars", type=float, default=3.0)
    parser.add_argument("--out-dir", default=None)
    args = parser.parse_args(argv)

    rows = summarize_coverage(
        Path(args.data_dir),
        args.symbols,
        args.timeframes,
        required_start=args.required_start,
        required_end=args.required_end,
        min_coverage_pct=args.min_coverage_pct,
        max_gap_bars=args.max_gap_bars,
    )
    out_dir = Path(args.out_dir) if args.out_dir else Path(args.data_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "data_coverage_report.csv", rows, COVERAGE_FIELDS)
    _write_markdown(out_dir / "data_coverage_report.md", rows, args.data_dir)
    passed = all(row["passes"] for row in rows)
    print(f"Data coverage report complete: passed={passed} rows={len(rows)} out_dir={out_dir}")
    return 0


def summarize_coverage(
    data_dir: Path,
    symbols: list[str],
    timeframes: list[str],
    *,
    required_start: str | None = None,
    required_end: str | None = None,
    min_coverage_pct: float = 95.0,
    max_gap_bars: float = 3.0,
) -> list[dict[str, Any]]:
    rows = []
    for symbol in symbols:
        for timeframe in timeframes:
            rows.append(
                _coverage_row(
                    data_dir,
                    symbol,
                    timeframe,
                    required_start=required_start,
                    required_end=required_end,
                    min_coverage_pct=min_coverage_pct,
                    max_gap_bars=max_gap_bars,
                )
            )
    return rows


def _coverage_row(
    data_dir: Path,
    symbol: str,
    timeframe: str,
    *,
    required_start: str | None,
    required_end: str | None,
    min_coverage_pct: float,
    max_gap_bars: float,
) -> dict[str, Any]:
    path = find_history_file(data_dir, symbol, timeframe)
    if path is None:
        return _missing_row(symbol, timeframe, "file_missing")
    candles = load_candles(path)
    if not candles:
        return _missing_row(symbol, timeframe, "empty_file", path)
    tf_ms = timeframe_to_ms(timeframe)
    if tf_ms is None:
        return _missing_row(symbol, timeframe, "unsupported_timeframe", path)
    first = int(candles[0]["time"])
    last = int(candles[-1]["time"])
    audit_start = _date_to_ms(required_start) if required_start else first
    audit_end = _date_to_ms(required_end, end_of_day=True) if required_end else last
    candles_in_range = [candle for candle in candles if audit_start <= int(candle["time"]) <= audit_end]
    expected = max(0, int((audit_end - audit_start) // tf_ms) + 1)
    coverage_pct = (len(candles_in_range) / expected * 100.0) if expected else 0.0
    max_gap = _max_gap_bars(candles_in_range, tf_ms)
    missing = []
    if coverage_pct < min_coverage_pct:
        missing.append("coverage_below_min")
    if max_gap > max_gap_bars:
        missing.append("gap_above_max")
    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "path": str(path),
        "candles": len(candles_in_range),
        "start": _format_ms(first),
        "end": _format_ms(last),
        "expected_candles": expected,
        "coverage_pct": round(coverage_pct, 4),
        "max_gap_bars": round(max_gap, 4),
        "passes": not missing,
        "missing_reason": ";".join(missing),
    }


def _missing_row(symbol: str, timeframe: str, reason: str, path: Path | None = None) -> dict[str, Any]:
    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "path": str(path or ""),
        "candles": 0,
        "start": None,
        "end": None,
        "expected_candles": None,
        "coverage_pct": 0.0,
        "max_gap_bars": None,
        "passes": False,
        "missing_reason": reason,
    }


def _max_gap_bars(candles: list[dict[str, Any]], tf_ms: int) -> float:
    if len(candles) < 2:
        return 0.0
    gaps = [int(candles[idx]["time"]) - int(candles[idx - 1]["time"]) for idx in range(1, len(candles))]
    return max(gaps) / tf_ms if gaps else 0.0


def _date_to_ms(value: str, *, end_of_day: bool = False) -> int:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    if end_of_day and len(value) == 10:
        dt = dt.replace(hour=23, minute=59, second=59, microsecond=999000)
    return int(dt.timestamp() * 1000)


def _format_ms(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], data_dir: str) -> None:
    lines = [
        "# ICT Data Coverage Report",
        "",
        f"- data_dir: `{data_dir}`",
        f"- passed: `{all(row['passes'] for row in rows)}`",
        "",
        "## Coverage",
        _markdown_table(rows),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(COVERAGE_FIELDS) + " |", "| " + " | ".join("---" for _ in COVERAGE_FIELDS) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row.get(field)) for field in COVERAGE_FIELDS) + " |")
    return "\n".join(lines)


def _cell(value: Any) -> str:
    return "" if value is None else str(value)


if __name__ == "__main__":
    raise SystemExit(main())
