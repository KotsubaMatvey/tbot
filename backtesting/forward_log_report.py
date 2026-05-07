from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

REPORT_FIELDS = [
    "scope",
    "model",
    "symbol",
    "signals",
    "filled",
    "fill_rate",
    "avg_slippage_bps",
    "avg_outcome_r",
    "avg_net_outcome_r",
    "win_rate",
    "missing_fill_count",
    "passed",
    "failed_gates",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize paper/live forward logs for ICT model validation.")
    parser.add_argument("--logs", required=True, help="CSV with model,symbol,status/outcome/slippage columns.")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--min-signals", type=int, default=20)
    parser.add_argument("--min-fill-rate", type=float, default=0.7)
    parser.add_argument("--max-avg-slippage-bps", type=float, default=2.0)
    parser.add_argument("--min-avg-net-outcome-r", type=float, default=0.0)
    args = parser.parse_args(argv)

    logs_path = Path(args.logs)
    rows = _read_csv(logs_path)
    report = summarize_forward_logs(
        rows,
        min_signals=args.min_signals,
        min_fill_rate=args.min_fill_rate,
        max_avg_slippage_bps=args.max_avg_slippage_bps,
        min_avg_net_outcome_r=args.min_avg_net_outcome_r,
    )
    out_dir = Path(args.out_dir) if args.out_dir else logs_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "forward_log_report.csv", report, REPORT_FIELDS)
    _write_markdown(out_dir / "forward_log_report.md", report, logs_path)
    print(f"Forward log report complete: rows={len(report)} out_dir={out_dir}")
    return 0


def summarize_forward_logs(
    rows: list[dict[str, Any]],
    *,
    min_signals: int = 20,
    min_fill_rate: float = 0.7,
    max_avg_slippage_bps: float = 2.0,
    min_avg_net_outcome_r: float = 0.0,
) -> list[dict[str, Any]]:
    report = [_summary_row("overall", "ALL", "ALL", rows, min_signals, min_fill_rate, max_avg_slippage_bps, min_avg_net_outcome_r)]
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(str(row.get("model") or "unknown"), str(row.get("symbol") or "unknown"))].append(row)
    for (model, symbol), group in sorted(groups.items()):
        report.append(_summary_row("model_symbol", model, symbol, group, min_signals, min_fill_rate, max_avg_slippage_bps, min_avg_net_outcome_r))
    return report


def _summary_row(
    scope: str,
    model: str,
    symbol: str,
    rows: list[dict[str, Any]],
    min_signals: int,
    min_fill_rate: float,
    max_avg_slippage_bps: float,
    min_avg_net_outcome_r: float,
) -> dict[str, Any]:
    filled = [row for row in rows if _is_filled(row)]
    outcomes = [_float_or_none(row.get("outcome_r")) for row in filled]
    outcomes = [value for value in outcomes if value is not None]
    net_outcomes = [_float_or_none(row.get("net_outcome_r")) for row in filled]
    net_outcomes = [value for value in net_outcomes if value is not None]
    slippage = [_float_or_none(row.get("slippage_bps")) for row in filled]
    slippage = [abs(value) for value in slippage if value is not None]
    fill_rate = len(filled) / len(rows) if rows else 0.0
    avg_net = _avg(net_outcomes) if net_outcomes else _avg(outcomes)
    avg_slippage = _avg(slippage)
    failures = []
    if len(rows) < min_signals:
        failures.append("min_signals")
    if fill_rate < min_fill_rate:
        failures.append("min_fill_rate")
    if avg_slippage is None or avg_slippage > max_avg_slippage_bps:
        failures.append("max_avg_slippage_bps")
    if avg_net is None or avg_net < min_avg_net_outcome_r:
        failures.append("min_avg_net_outcome_r")
    return {
        "scope": scope,
        "model": model,
        "symbol": symbol,
        "signals": len(rows),
        "filled": len(filled),
        "fill_rate": round(fill_rate, 6) if rows else 0.0,
        "avg_slippage_bps": avg_slippage,
        "avg_outcome_r": _avg(outcomes),
        "avg_net_outcome_r": avg_net,
        "win_rate": round(sum(1 for value in (net_outcomes or outcomes) if value > 0) / len(net_outcomes or outcomes), 6) if (net_outcomes or outcomes) else None,
        "missing_fill_count": len(rows) - len(filled),
        "passed": not failures,
        "failed_gates": ";".join(failures),
    }


def _is_filled(row: dict[str, Any]) -> bool:
    status = str(row.get("status") or row.get("fill_status") or "").strip().lower()
    if status in {"filled", "closed", "tp", "sl", "be"}:
        return True
    return _float_or_none(row.get("filled_price")) is not None or _float_or_none(row.get("fill_price")) is not None


def _avg(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], logs_path: Path) -> None:
    lines = [
        "# ICT Forward Log Report",
        "",
        f"- logs: `{logs_path}`",
        "",
        "## Summary",
        _markdown_table(rows),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(REPORT_FIELDS) + " |", "| " + " | ".join("---" for _ in REPORT_FIELDS) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row.get(field)) for field in REPORT_FIELDS) + " |")
    return "\n".join(lines)


def _cell(value: Any) -> str:
    return "" if value is None else str(value)


if __name__ == "__main__":
    raise SystemExit(main())
