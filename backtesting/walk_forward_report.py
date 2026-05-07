from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from strategies.ict_models.model_filters import passes_model_filter

SUMMARY_FIELDS = [
    "phase",
    "start_date",
    "end_date",
    "count",
    "activated_trades",
    "managed_expectancy",
    "gross_managed_expectancy",
    "profit_factor",
    "max_drawdown_r",
    "win_rate",
    "avg_execution_cost_r",
    "session_overtrade_count",
    "passed",
    "failed_gates",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Walk-forward quality gates for ICT event backtests.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--model-filters", default=None)
    parser.add_argument("--threshold", type=float, default=70.0)
    parser.add_argument("--min-total-trades", type=int, default=30)
    parser.add_argument("--min-phase-trades", type=int, default=10)
    parser.add_argument("--min-managed-expectancy-r", type=float, default=0.3)
    parser.add_argument("--min-profit-factor", type=float, default=1.3)
    parser.add_argument("--max-drawdown-r", type=float, default=8.0)
    parser.add_argument("--max-trades-per-session", type=int, default=1)
    parser.add_argument(
        "--phase",
        action="append",
        default=[],
        help="Optional NAME:YYYY-MM-DD:YYYY-MM-DD phase. Repeat for train/validation/test.",
    )
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    rows = _read_csv(events_path)
    model_filters = _read_model_filters(Path(args.model_filters)) if args.model_filters else {}
    selected = _select_events(rows, threshold=args.threshold, model_filters=model_filters)
    phases = _parse_phases(args.phase) if args.phase else _auto_phases(selected)
    summaries = summarize_walk_forward(
        selected,
        phases=phases,
        min_total_trades=args.min_total_trades,
        min_phase_trades=args.min_phase_trades,
        min_managed_expectancy_r=args.min_managed_expectancy_r,
        min_profit_factor=args.min_profit_factor,
        max_drawdown_r=args.max_drawdown_r,
        max_trades_per_session=args.max_trades_per_session,
    )

    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "walk_forward_report.csv", summaries, SUMMARY_FIELDS)
    _write_json(out_dir / "quality_gate_result.json", summaries)
    _write_markdown(out_dir / "walk_forward_report.md", summaries, events_path, args.threshold)
    passed = bool(summaries and summaries[0].get("passed"))
    print(f"Walk-forward report complete: passed={passed} rows={len(summaries)} out_dir={out_dir}")
    return 0


def summarize_walk_forward(
    events: list[dict[str, Any]],
    *,
    phases: list[tuple[str, str, str]] | None = None,
    min_total_trades: int = 30,
    min_phase_trades: int = 10,
    min_managed_expectancy_r: float = 0.3,
    min_profit_factor: float = 1.3,
    max_drawdown_r: float = 8.0,
    max_trades_per_session: int = 1,
) -> list[dict[str, Any]]:
    phases = phases or _auto_phases(events)
    phase_rows = [_summary_for_phase(name, _events_in_range(events, start, end), start, end, max_trades_per_session) for name, start, end in phases]
    overall = _summary_for_phase("overall", events, _min_date(events), _max_date(events), max_trades_per_session)
    failures = []
    if int(overall["count"] or 0) < min_total_trades:
        failures.append("min_total_trades")
    for row in phase_rows:
        failures.extend(_gate_failures(row, min_phase_trades, min_managed_expectancy_r, min_profit_factor, max_drawdown_r))
    if int(overall["session_overtrade_count"] or 0) > 0:
        failures.append("max_trades_per_session")
    overall["passed"] = not failures
    overall["failed_gates"] = ";".join(sorted(set(failures)))
    for row in phase_rows:
        row_failures = _gate_failures(row, min_phase_trades, min_managed_expectancy_r, min_profit_factor, max_drawdown_r)
        row["passed"] = not row_failures
        row["failed_gates"] = ";".join(row_failures)
    return [overall, *phase_rows]


def _summary_for_phase(
    phase: str,
    events: list[dict[str, Any]],
    start_date: str | None,
    end_date: str | None,
    max_trades_per_session: int,
) -> dict[str, Any]:
    outcomes = [_managed_outcome(event) for event in events]
    outcomes = [value for value in outcomes if value is not None]
    return {
        "phase": phase,
        "start_date": start_date,
        "end_date": end_date,
        "count": len(events),
        "activated_trades": sum(1 for event in events if _bool(event.get("activated_trade"))),
        "managed_expectancy": _avg_values(outcomes),
        "gross_managed_expectancy": _avg_field(events, "gross_managed_outcome_r"),
        "profit_factor": _profit_factor(outcomes),
        "max_drawdown_r": _max_drawdown(outcomes),
        "win_rate": _win_rate(outcomes),
        "avg_execution_cost_r": _avg_field(events, "execution_cost_r"),
        "session_overtrade_count": _session_overtrade_count(events, max_trades_per_session),
        "passed": False,
        "failed_gates": "",
    }


def _gate_failures(
    row: dict[str, Any],
    min_phase_trades: int,
    min_managed_expectancy_r: float,
    min_profit_factor: float,
    max_drawdown_r: float,
) -> list[str]:
    failures = []
    if int(row["count"] or 0) < min_phase_trades:
        failures.append("min_phase_trades")
    expectancy = _float_or_none(row.get("managed_expectancy"))
    if expectancy is None or expectancy < min_managed_expectancy_r:
        failures.append("min_managed_expectancy_r")
    pf = _float_or_none(row.get("profit_factor"))
    if pf is None or pf < min_profit_factor:
        failures.append("min_profit_factor")
    dd = _float_or_none(row.get("max_drawdown_r"))
    if dd is not None and dd > max_drawdown_r:
        failures.append("max_drawdown_r")
    return failures


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


def _auto_phases(events: list[dict[str, Any]]) -> list[tuple[str, str, str]]:
    ordered = sorted((event for event in events if _event_date(event)), key=lambda event: (_event_date(event) or "", str(event.get("timestamp") or "")))
    if not ordered:
        return []
    dates = [_event_date(event) or "" for event in ordered]
    first = dates[0]
    last = dates[-1]
    if len(ordered) < 3:
        return [("test", first, last)]
    first_cut = max(1, len(ordered) // 3)
    second_cut = max(first_cut + 1, 2 * len(ordered) // 3)
    return [
        ("train", dates[0], dates[first_cut - 1]),
        ("validation", dates[first_cut], dates[second_cut - 1]),
        ("test", dates[second_cut], dates[-1]),
    ]


def _parse_phases(values: list[str]) -> list[tuple[str, str, str]]:
    phases = []
    for value in values:
        name, start, end = value.split(":", 2)
        phases.append((name, start, end))
    return phases


def _events_in_range(events: list[dict[str, Any]], start: str, end: str) -> list[dict[str, Any]]:
    return [event for event in events if (date := _event_date(event)) is not None and start <= date <= end]


def _event_date(event: dict[str, Any]) -> str | None:
    session_date = str(event.get("session_date") or "").strip()
    if session_date and session_date != "none":
        return session_date
    timestamp = _float_or_none(event.get("timestamp") or event.get("detected_at"))
    if timestamp is None:
        return None
    if timestamp < 10_000_000_000:
        timestamp *= 1000
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def _min_date(events: list[dict[str, Any]]) -> str | None:
    dates = [_event_date(event) for event in events if _event_date(event)]
    return min(dates) if dates else None


def _max_date(events: list[dict[str, Any]]) -> str | None:
    dates = [_event_date(event) for event in events if _event_date(event)]
    return max(dates) if dates else None


def _session_overtrade_count(events: list[dict[str, Any]], max_trades_per_session: int) -> int:
    if max_trades_per_session <= 0:
        return 0
    counts: Counter[tuple[str, str, str]] = Counter()
    for event in events:
        key = (
            str(event.get("symbol") or ""),
            _event_date(event) or "",
            str(event.get("session_window") or "none"),
        )
        counts[key] += 1
    return sum(1 for count in counts.values() if count > max_trades_per_session)


def _managed_outcome(event: dict[str, Any]) -> float | None:
    value = _float_or_none(event.get("net_managed_outcome_r"))
    if value is not None:
        return value
    return _float_or_none(event.get("managed_outcome_r"))


def _profit_factor(outcomes: list[float]) -> float | str | None:
    wins = [value for value in outcomes if value > 0]
    losses = [abs(value) for value in outcomes if value < 0]
    if not wins and not losses:
        return None
    if not losses:
        return "inf" if wins else None
    return round(sum(wins) / sum(losses), 6)


def _max_drawdown(outcomes: list[float]) -> float | None:
    equity = 0.0
    peak = 0.0
    drawdown = 0.0
    for outcome in outcomes:
        equity += outcome
        peak = max(peak, equity)
        drawdown = max(drawdown, peak - equity)
    return round(drawdown, 6) if outcomes else None


def _win_rate(outcomes: list[float]) -> float | None:
    return round(sum(1 for value in outcomes if value > 0) / len(outcomes), 6) if outcomes else None


def _avg_values(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def _avg_field(events: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in events]
    values = [value for value in values if value is not None]
    return _avg_values(values)


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    if value == "inf":
        return float("inf")
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


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


def _write_json(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(json.dumps({"passed": bool(rows and rows[0].get("passed")), "rows": rows}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def _write_markdown(path: Path, rows: list[dict[str, Any]], events_path: Path, threshold: float) -> None:
    lines = [
        "# ICT Walk-Forward Quality Report",
        "",
        f"- events: `{events_path}`",
        f"- threshold: `{threshold}`",
        f"- passed: `{bool(rows and rows[0].get('passed'))}`",
        "",
        "## Phases",
        _markdown_table(rows),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(SUMMARY_FIELDS) + " |", "| " + " | ".join("---" for _ in SUMMARY_FIELDS) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row.get(field)) for field in SUMMARY_FIELDS) + " |")
    return "\n".join(lines)


def _cell(value: Any) -> str:
    return "" if value is None else str(value)


if __name__ == "__main__":
    raise SystemExit(main())
