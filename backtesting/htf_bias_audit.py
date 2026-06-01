from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

from backtesting.trade_pnl_report import summarize_trade_pnl

REPORT_FIELDS = [
    "section",
    "bucket",
    "threshold",
    "filter_name",
    "trade_count",
    "retention_pct",
    "min_trades",
    "sample_valid",
    "win_rate_pct",
    "avg_realized_rr",
    "expectancy_r",
    "profit_factor",
    "max_drawdown_r",
    "total_pnl_r",
    "expectancy_delta_vs_all",
    "win_rate_delta_vs_all",
    "avg_realized_rr_delta_vs_all",
    "verdict",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit whether HTF bias improves realized trade P&L or only cuts sample size.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--model-filters", default=None)
    parser.add_argument("--min-trades", type=int, default=100)
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    rows = _read_csv(events_path)
    model_filters = _read_model_filters(Path(args.model_filters)) if args.model_filters else {}
    report = summarize_htf_bias(
        rows,
        threshold=args.threshold,
        model_filters=model_filters,
        min_trades=args.min_trades,
    )
    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "htf_bias_audit.csv", report, REPORT_FIELDS)
    _write_markdown(out_dir / "htf_bias_audit.md", report, events_path)
    print(f"HTF bias audit complete: rows={len(report)} out_dir={out_dir}")
    return 0


def summarize_htf_bias(
    events: list[dict[str, Any]],
    *,
    threshold: float = 0.0,
    model_filters: dict[str, dict[str, Any]] | None = None,
    min_trades: int = 100,
) -> list[dict[str, Any]]:
    baseline = _pnl_row(events, threshold=threshold, model_filters=model_filters, min_trades=min_trades)
    rows = [_audit_row("baseline", "all", baseline, baseline, threshold=threshold, model_filters=model_filters, min_trades=min_trades)]
    rows.extend(
        _bucket_rows(
            events,
            section="htf_context_alignment",
            bucket_fn=lambda event: str(event.get("htf_context_alignment") or "none"),
            baseline=baseline,
            threshold=threshold,
            model_filters=model_filters,
            min_trades=min_trades,
        )
    )
    rows.extend(
        _bucket_rows(
            events,
            section="htf_bias_relation",
            bucket_fn=_htf_bias_relation,
            baseline=baseline,
            threshold=threshold,
            model_filters=model_filters,
            min_trades=min_trades,
        )
    )
    rows.extend(
        _bucket_rows(
            events,
            section="htf_draw_relation",
            bucket_fn=_htf_draw_relation,
            baseline=baseline,
            threshold=threshold,
            model_filters=model_filters,
            min_trades=min_trades,
        )
    )
    rows.extend(
        _bucket_rows(
            events,
            section="htf_bias",
            bucket_fn=lambda event: str(event.get("htf_bias") or "none"),
            baseline=baseline,
            threshold=threshold,
            model_filters=model_filters,
            min_trades=min_trades,
        )
    )
    return rows


def _bucket_rows(
    events: list[dict[str, Any]],
    *,
    section: str,
    bucket_fn: Callable[[dict[str, Any]], str],
    baseline: dict[str, Any],
    threshold: float,
    model_filters: dict[str, dict[str, Any]] | None,
    min_trades: int,
) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[bucket_fn(event)].append(event)
    rows = []
    for bucket, bucket_events in sorted(buckets.items()):
        metrics = _pnl_row(bucket_events, threshold=threshold, model_filters=model_filters, min_trades=min_trades)
        rows.append(
            _audit_row(
                section,
                bucket,
                metrics,
                baseline,
                threshold=threshold,
                model_filters=model_filters,
                min_trades=min_trades,
            )
        )
    return rows


def _pnl_row(
    events: list[dict[str, Any]],
    *,
    threshold: float,
    model_filters: dict[str, dict[str, Any]] | None,
    min_trades: int,
) -> dict[str, Any]:
    rows = summarize_trade_pnl(
        events,
        threshold=threshold,
        model_filters=model_filters,
        min_trades=min_trades,
        group_by=[],
    )
    if model_filters:
        return next(row for row in rows if row["scope"] == "filtered_all")
    return next(row for row in rows if row["scope"] == "all")


def _audit_row(
    section: str,
    bucket: str,
    metrics: dict[str, Any],
    baseline: dict[str, Any],
    *,
    threshold: float,
    model_filters: dict[str, dict[str, Any]] | None,
    min_trades: int,
) -> dict[str, Any]:
    baseline_count = int(baseline.get("trade_count") or 0)
    trade_count = int(metrics.get("trade_count") or 0)
    return {
        "section": section,
        "bucket": bucket,
        "threshold": _format_number(threshold),
        "filter_name": "model_rules" if model_filters else "none",
        "trade_count": trade_count,
        "retention_pct": _round((trade_count / baseline_count) * 100) if baseline_count else None,
        "min_trades": min_trades,
        "sample_valid": trade_count >= min_trades,
        "win_rate_pct": metrics.get("win_rate_pct"),
        "avg_realized_rr": metrics.get("avg_realized_rr"),
        "expectancy_r": metrics.get("expectancy_r"),
        "profit_factor": metrics.get("profit_factor"),
        "max_drawdown_r": metrics.get("max_drawdown_r"),
        "total_pnl_r": metrics.get("total_pnl_r"),
        "expectancy_delta_vs_all": _delta(metrics.get("expectancy_r"), baseline.get("expectancy_r")),
        "win_rate_delta_vs_all": _delta(metrics.get("win_rate_pct"), baseline.get("win_rate_pct")),
        "avg_realized_rr_delta_vs_all": _delta(metrics.get("avg_realized_rr"), baseline.get("avg_realized_rr")),
        "verdict": _verdict(metrics, baseline, min_trades=min_trades),
    }


def _htf_bias_relation(event: dict[str, Any]) -> str:
    direction = str(event.get("direction") or "").lower()
    bias = str(event.get("htf_bias") or "").lower()
    if (direction == "long" and bias == "bullish") or (direction == "short" and bias == "bearish"):
        return "with_bias"
    if (direction == "long" and bias == "bearish") or (direction == "short" and bias == "bullish"):
        return "against_bias"
    return "neutral_or_missing"


def _htf_draw_relation(event: dict[str, Any]) -> str:
    direction = str(event.get("direction") or "").lower()
    draw = str(event.get("htf_draw_direction") or "").lower()
    if (direction == "long" and draw == "up") or (direction == "short" and draw == "down"):
        return "with_draw"
    if (direction == "long" and draw == "down") or (direction == "short" and draw == "up"):
        return "against_draw"
    return "neutral_or_missing"


def _verdict(metrics: dict[str, Any], baseline: dict[str, Any], *, min_trades: int) -> str:
    baseline_count = int(baseline.get("trade_count") or 0)
    trade_count = int(metrics.get("trade_count") or 0)
    if baseline_count == 0:
        return "no_baseline_trades"
    if trade_count < min_trades:
        return "insufficient_sample"
    baseline_expectancy = _float_or_none(baseline.get("expectancy_r"))
    expectancy = _float_or_none(metrics.get("expectancy_r"))
    if baseline_expectancy is None or expectancy is None:
        return "no_realized_pnl"
    win_delta = _delta(metrics.get("win_rate_pct"), baseline.get("win_rate_pct")) or 0.0
    expectancy_delta = expectancy - baseline_expectancy
    if expectancy_delta > 0 and win_delta >= 0:
        return "improves_edge"
    if expectancy_delta < 0:
        return "worse_than_baseline"
    if trade_count < baseline_count:
        return "cuts_sample_only"
    return "neutral"


def _delta(value: Any, baseline: Any) -> float | None:
    current = _float_or_none(value)
    base = _float_or_none(baseline)
    if current is None or base is None:
        return None
    return _round(current - base)


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _round(value: float | None) -> float | None:
    return round(value, 6) if value is not None else None


def _format_number(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else str(value)


def _read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _read_model_filters(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("model_filters", payload)


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], events_path: Path) -> None:
    lines = [
        "# HTF Bias Audit",
        "",
        f"- events: `{events_path}`",
        "- verdict compares each HTF bucket against the full realized P&L baseline.",
        "",
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
