from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from backtesting.walk_forward_report import (
    _auto_phases,
    _bool,
    _csv_list,
    _dedupe_session_trades,
    _events_in_range,
    _float_or_none,
    _managed_outcome,
    _max_drawdown,
    _parse_phases,
    _profit_factor,
    _select_events,
)

REPORT_FIELDS = [
    "phase",
    "scope",
    "group",
    "filter_name",
    "threshold",
    "dedupe_session",
    "dedupe_selection",
    "trade_count",
    "min_trades",
    "sample_valid",
    "win_rate_pct",
    "expectancy_r",
    "profit_factor",
    "max_drawdown_r",
    "total_pnl_r",
    "avg_decision_score",
    "avg_target_distance_r",
    "avg_risk_bps",
    "avg_execution_cost_r",
    "avg_funding_cost_r",
    "avg_total_cost_r",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Attribute realized ICT P&L by walk-forward phase and event fields.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--model-filters", default=None)
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--min-trades", type=int, default=30)
    parser.add_argument("--group-by", nargs="+", default=["symbol", "direction", "session_label", "score_bucket"])
    parser.add_argument("--dedupe-session", action="store_true")
    parser.add_argument("--dedupe-session-selection", choices=["timeframe_first", "first", "highest_score"], default="timeframe_first")
    parser.add_argument("--dedupe-session-timeframe-priority", default="")
    parser.add_argument("--phase", action="append", default=[])
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    events = _read_csv(events_path)
    model_filters = _read_model_filters(Path(args.model_filters)) if args.model_filters else {}
    rows = summarize_phase_attribution(
        events,
        threshold=args.threshold,
        model_filters=model_filters,
        min_trades=args.min_trades,
        group_by=args.group_by,
        dedupe_session=args.dedupe_session,
        dedupe_session_selection=args.dedupe_session_selection,
        dedupe_session_timeframe_priority=_csv_list(args.dedupe_session_timeframe_priority),
        phases=_parse_phases(args.phase) if args.phase else None,
    )

    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "phase_attribution_report.csv", rows, REPORT_FIELDS)
    _write_markdown(out_dir / "phase_attribution_report.md", rows, events_path)
    print(f"Phase attribution report complete: rows={len(rows)} out_dir={out_dir}")
    return 0


def summarize_phase_attribution(
    events: list[dict[str, Any]],
    *,
    threshold: float = 0.0,
    model_filters: dict[str, dict[str, Any]] | None = None,
    min_trades: int = 30,
    group_by: list[str] | None = None,
    dedupe_session: bool = False,
    dedupe_session_selection: str = "timeframe_first",
    dedupe_session_timeframe_priority: list[str] | None = None,
    phases: list[tuple[str, str, str]] | None = None,
) -> list[dict[str, Any]]:
    selected = _select_events(events, threshold=threshold, model_filters=model_filters or {})
    trades = [event for event in selected if _bool(event.get("activated_trade"))]
    if dedupe_session:
        trades = _dedupe_session_trades(trades, dedupe_session_timeframe_priority or [], dedupe_session_selection)
    phase_bounds = phases or _auto_phases(trades)
    filter_name = "model_rules" if model_filters else "none"
    rows = [
        _summary_row(
            "overall",
            "ALL",
            trades,
            filter_name=filter_name,
            threshold=threshold,
            min_trades=min_trades,
            dedupe_session=dedupe_session,
            dedupe_selection=dedupe_session_selection,
        )
    ]
    for phase, start, end in phase_bounds:
        phase_trades = _events_in_range(trades, start, end)
        rows.append(
            _summary_row(
                phase,
                "ALL",
                phase_trades,
                filter_name=filter_name,
                threshold=threshold,
                min_trades=min_trades,
                dedupe_session=dedupe_session,
                dedupe_selection=dedupe_session_selection,
            )
        )
        for field in group_by or []:
            rows.extend(
                _group_rows(
                    phase,
                    phase_trades,
                    field,
                    filter_name=filter_name,
                    threshold=threshold,
                    min_trades=min_trades,
                    dedupe_session=dedupe_session,
                    dedupe_selection=dedupe_session_selection,
                )
            )
    return rows


def _group_rows(
    phase: str,
    events: list[dict[str, Any]],
    field: str,
    *,
    filter_name: str,
    threshold: float,
    min_trades: int,
    dedupe_session: bool,
    dedupe_selection: str,
) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[str(event.get(field) or "none")].append(event)
    rows = []
    for value, group in sorted(buckets.items()):
        rows.append(
            _summary_row(
                phase,
                f"by_{field}",
                group,
                filter_name=filter_name,
                threshold=threshold,
                min_trades=min_trades,
                dedupe_session=dedupe_session,
                dedupe_selection=dedupe_selection,
                group=value,
            )
        )
    return rows


def _summary_row(
    phase: str,
    scope: str,
    events: list[dict[str, Any]],
    *,
    filter_name: str,
    threshold: float,
    min_trades: int,
    dedupe_session: bool,
    dedupe_selection: str,
    group: str = "ALL",
) -> dict[str, Any]:
    outcomes = [_managed_outcome(event) for event in events]
    outcomes = [value for value in outcomes if value is not None]
    wins = [value for value in outcomes if value > 0]
    losses = [abs(value) for value in outcomes if value < 0]
    win_rate = len(wins) / len(outcomes) if outcomes else None
    return {
        "phase": phase,
        "scope": scope,
        "group": group,
        "filter_name": filter_name,
        "threshold": _format_number(threshold),
        "dedupe_session": dedupe_session,
        "dedupe_selection": dedupe_selection if dedupe_session else "none",
        "trade_count": len(outcomes),
        "min_trades": min_trades,
        "sample_valid": len(outcomes) >= min_trades,
        "win_rate_pct": _round(win_rate * 100) if win_rate is not None else None,
        "expectancy_r": _avg_values(outcomes),
        "profit_factor": _profit_factor(outcomes),
        "max_drawdown_r": _max_drawdown(outcomes),
        "total_pnl_r": _round(sum(outcomes)) if outcomes else None,
        "avg_decision_score": _avg_field(events, "decision_score"),
        "avg_target_distance_r": _avg_field(events, "target_distance_r"),
        "avg_risk_bps": _avg_field(events, "risk_bps"),
        "avg_execution_cost_r": _avg_field(events, "execution_cost_r"),
        "avg_funding_cost_r": _avg_field(events, "funding_cost_r"),
        "avg_total_cost_r": _avg_field(events, "total_cost_r"),
    }


def _avg_values(values: list[float]) -> float | None:
    return _round(sum(values) / len(values)) if values else None


def _avg_field(events: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in events]
    return _avg_values([value for value in values if value is not None])


def _format_number(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else str(value)


def _round(value: float | None) -> float | None:
    return round(value, 6) if value is not None else None


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
        "# ICT Phase Attribution Report",
        "",
        f"- events: `{events_path}`",
        "- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.",
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
