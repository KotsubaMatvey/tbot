from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from strategies.ict_models.model_filters import passes_model_filter

REPORT_FIELDS = [
    "scope",
    "group",
    "filter_name",
    "threshold",
    "filtered_out",
    "trade_count",
    "min_trades",
    "sample_valid",
    "win_rate_pct",
    "avg_realized_rr",
    "avg_win_r",
    "avg_loss_r",
    "expectancy_r",
    "profit_factor",
    "max_drawdown_r",
    "total_pnl_r",
    "avg_execution_cost_r",
    "avg_funding_cost_r",
    "avg_total_cost_r",
]

GROUP_FIELDS = {
    "model": "model",
    "symbol": "symbol",
    "timeframe": "timeframe",
    "direction": "direction",
    "htf_bias": "htf_bias",
    "htf_context_alignment": "htf_context_alignment",
    "htf_draw_direction": "htf_draw_direction",
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize realized trade P&L from ICT event rows.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--model-filters", default=None)
    parser.add_argument("--min-trades", type=int, default=100)
    parser.add_argument("--group-by", nargs="+", default=["model", "symbol", "timeframe", "direction"])
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    rows = _read_csv(events_path)
    model_filters = _read_model_filters(Path(args.model_filters)) if args.model_filters else {}
    report = summarize_trade_pnl(
        rows,
        threshold=args.threshold,
        model_filters=model_filters,
        min_trades=args.min_trades,
        group_by=args.group_by,
    )
    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "trade_pnl_report.csv", report, REPORT_FIELDS)
    _write_markdown(out_dir / "trade_pnl_report.md", report, events_path)
    print(f"Trade P&L report complete: rows={len(report)} out_dir={out_dir}")
    return 0


def summarize_trade_pnl(
    events: list[dict[str, Any]],
    *,
    threshold: float = 0.0,
    model_filters: dict[str, dict[str, Any]] | None = None,
    min_trades: int = 100,
    group_by: list[str] | None = None,
) -> list[dict[str, Any]]:
    selected = _select_events(events, threshold=threshold, model_filters={})
    filtered = _select_events(events, threshold=threshold, model_filters=model_filters or {})
    rows = [
        _summary_row(selected, scope="all", group="ALL", threshold=threshold, filter_name="none", min_trades=min_trades),
    ]
    if model_filters:
        rows.append(
            _summary_row(
                filtered,
                scope="filtered_all",
                group="ALL",
                threshold=threshold,
                filter_name="model_rules",
                min_trades=min_trades,
                filtered_out=len(selected) - len(filtered),
            )
        )
    for field in group_by or []:
        source = filtered if model_filters else selected
        rows.extend(_group_rows(source, field, threshold=threshold, filter_name="model_rules" if model_filters else "none", min_trades=min_trades))
    return rows


def _group_rows(events: list[dict[str, Any]], field: str, *, threshold: float, filter_name: str, min_trades: int) -> list[dict[str, Any]]:
    event_field = GROUP_FIELDS.get(field, field)
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[str(event.get(event_field) or "none")].append(event)
    rows = []
    for value, group in sorted(buckets.items()):
        rows.append(
            _summary_row(
                group,
                scope=f"by_{field}",
                group=value,
                threshold=threshold,
                filter_name=filter_name,
                min_trades=min_trades,
            )
        )
    return rows


def _summary_row(
    events: list[dict[str, Any]],
    *,
    scope: str,
    group: str,
    threshold: float,
    filter_name: str,
    min_trades: int,
    filtered_out: int = 0,
) -> dict[str, Any]:
    trades = [event for event in events if _bool(event.get("activated_trade"))]
    outcomes = [_managed_outcome(event) for event in trades]
    outcomes = [value for value in outcomes if value is not None]
    wins = [value for value in outcomes if value > 0]
    losses = [abs(value) for value in outcomes if value < 0]
    win_rate = len(wins) / len(outcomes) if outcomes else None
    avg_win = sum(wins) / len(wins) if wins else None
    avg_loss = sum(losses) / len(losses) if losses else None
    expectancy = _expectancy(win_rate, avg_win, avg_loss)
    return {
        "scope": scope,
        "group": group,
        "filter_name": filter_name,
        "threshold": _format_number(threshold),
        "filtered_out": filtered_out,
        "trade_count": len(outcomes),
        "min_trades": min_trades,
        "sample_valid": len(outcomes) >= min_trades,
        "win_rate_pct": _round(win_rate * 100) if win_rate is not None else None,
        "avg_realized_rr": _avg(outcomes),
        "avg_win_r": _round(avg_win),
        "avg_loss_r": _round(avg_loss),
        "expectancy_r": _round(expectancy),
        "profit_factor": _profit_factor(wins, losses),
        "max_drawdown_r": _max_drawdown(outcomes),
        "total_pnl_r": _round(sum(outcomes)) if outcomes else None,
        "avg_execution_cost_r": _avg_field(trades, "execution_cost_r"),
        "avg_funding_cost_r": _avg_field(trades, "funding_cost_r"),
        "avg_total_cost_r": _avg_field(trades, "total_cost_r"),
    }


def _select_events(events: list[dict[str, Any]], *, threshold: float, model_filters: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    selected = []
    for event in events:
        score = _float_or_none(event.get("decision_score"))
        if threshold > 0 and (score is None or score < threshold):
            continue
        rules = model_filters.get(str(event.get("model") or ""), {})
        if model_filters and not passes_model_filter(event, rules):
            continue
        selected.append(event)
    return selected


def _expectancy(win_rate: float | None, avg_win: float | None, avg_loss: float | None) -> float | None:
    if win_rate is None:
        return None
    win_component = win_rate * (avg_win or 0.0)
    loss_component = (1 - win_rate) * (avg_loss or 0.0)
    return win_component - loss_component


def _managed_outcome(event: dict[str, Any]) -> float | None:
    value = _float_or_none(event.get("net_managed_outcome_r"))
    if value is not None:
        return value
    return _float_or_none(event.get("managed_outcome_r"))


def _profit_factor(wins: list[float], losses: list[float]) -> float | str | None:
    if not wins and not losses:
        return None
    if not losses:
        return "inf" if wins else None
    return _round(sum(wins) / sum(losses))


def _max_drawdown(outcomes: list[float]) -> float | None:
    equity = 0.0
    peak = 0.0
    drawdown = 0.0
    for outcome in outcomes:
        equity += outcome
        peak = max(peak, equity)
        drawdown = max(drawdown, peak - equity)
    return _round(drawdown) if outcomes else None


def _avg(values: list[float]) -> float | None:
    return _round(sum(values) / len(values)) if values else None


def _avg_field(events: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in events]
    return _avg([value for value in values if value is not None])


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    if str(value).lower() == "inf":
        return float("inf")
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
        "# Trade P&L Report",
        "",
        f"- events: `{events_path}`",
        "- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.",
        "- `sample_valid` is false when activated trade count is below `min_trades`.",
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
