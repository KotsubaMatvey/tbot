from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
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
    "sharpe",
    "profit_factor",
    "max_drawdown_r",
    "max_consecutive_losses",
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


@dataclass(slots=True)
class BacktestReport:
    model_name: str
    symbol: str
    timeframe: str
    period: str
    n_trades: int
    winrate: float | None
    avg_rr: float | None
    expectancy: float | None
    sharpe: float | None
    max_dd_r: float | None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize realized trade P&L from ICT event rows.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--model-filters", default=None)
    parser.add_argument("--min-trades", type=int, default=100)
    parser.add_argument("--period", default=None, help="Optional backtest period label, e.g. 2022-01-01..2023-06-30.")
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
    backtest_reports = build_backtest_reports(rows, threshold=args.threshold, model_filters=model_filters, period=args.period)
    _write_backtest_report_json(out_dir / "backtest_report.json", backtest_reports)
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


def build_backtest_reports(
    events: list[dict[str, Any]],
    *,
    threshold: float = 0.0,
    model_filters: dict[str, dict[str, Any]] | None = None,
    period: str | None = None,
) -> list[BacktestReport]:
    selected = _select_events(events, threshold=threshold, model_filters=model_filters or {})
    buckets: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for event in selected:
        if not _bool(event.get("activated_trade")):
            continue
        key = (
            str(event.get("model") or "none"),
            str(event.get("symbol") or "none"),
            str(event.get("timeframe") or "none"),
        )
        buckets[key].append(event)
    reports = []
    for (model, symbol, timeframe), group in sorted(buckets.items()):
        reports.append(_backtest_report(group, model=model, symbol=symbol, timeframe=timeframe, period=period))
    return reports


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
        "sharpe": _annualized_sharpe(outcomes, trades, None),
        "profit_factor": _profit_factor(wins, losses),
        "max_drawdown_r": _max_drawdown(outcomes),
        "max_consecutive_losses": _max_consecutive_losses(outcomes),
        "total_pnl_r": _round(sum(outcomes)) if outcomes else None,
        "avg_execution_cost_r": _avg_field(trades, "execution_cost_r"),
        "avg_funding_cost_r": _avg_field(trades, "funding_cost_r"),
        "avg_total_cost_r": _avg_field(trades, "total_cost_r"),
    }


def _backtest_report(
    trades: list[dict[str, Any]],
    *,
    model: str,
    symbol: str,
    timeframe: str,
    period: str | None,
) -> BacktestReport:
    outcomes = [_managed_outcome(event) for event in trades]
    outcomes = [value for value in outcomes if value is not None]
    wins = [value for value in outcomes if value > 0]
    losses = [abs(value) for value in outcomes if value < 0]
    win_rate = len(wins) / len(outcomes) if outcomes else None
    avg_win = sum(wins) / len(wins) if wins else None
    avg_loss = sum(losses) / len(losses) if losses else None
    return BacktestReport(
        model_name=model,
        symbol=symbol,
        timeframe=timeframe,
        period=period or _period_for_events(trades),
        n_trades=len(outcomes),
        winrate=_round(win_rate * 100) if win_rate is not None else None,
        avg_rr=_avg(outcomes),
        expectancy=_round(_expectancy(win_rate, avg_win, avg_loss)),
        sharpe=_annualized_sharpe(outcomes, trades, period),
        max_dd_r=_max_drawdown(outcomes),
    )


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


def _max_consecutive_losses(outcomes: list[float]) -> int:
    current = 0
    maximum = 0
    for outcome in outcomes:
        if outcome < 0:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0
    return maximum


def _annualized_sharpe(outcomes: list[float], events: list[dict[str, Any]], period: str | None) -> float | None:
    if len(outcomes) < 2:
        return None
    mean = sum(outcomes) / len(outcomes)
    variance = sum((value - mean) ** 2 for value in outcomes) / (len(outcomes) - 1)
    stdev = math.sqrt(variance)
    if stdev == 0:
        return None
    bounds = _period_bounds(events, period)
    if bounds is None:
        return None
    start, end = bounds
    days = max((end - start).days + 1, 1)
    trades_per_year = len(outcomes) / (days / 365.25)
    return _round((mean / stdev) * math.sqrt(trades_per_year))


def _period_for_events(events: list[dict[str, Any]]) -> str:
    dates = [_event_date(event) for event in events]
    dates = [value for value in dates if value is not None]
    if not dates:
        return ""
    return f"{min(dates)}..{max(dates)}"


def _period_bounds(events: list[dict[str, Any]], period: str | None) -> tuple[datetime, datetime] | None:
    if period and ".." in period:
        start, end = period.split("..", 1)
        start_dt = _parse_date(start)
        end_dt = _parse_date(end)
        if start_dt is not None and end_dt is not None:
            return start_dt, end_dt
    dates = [_event_date(event) for event in events]
    dates = [value for value in dates if value is not None]
    if not dates:
        return None
    start_dt = _parse_date(min(dates))
    end_dt = _parse_date(max(dates))
    if start_dt is None or end_dt is None:
        return None
    return start_dt, end_dt


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


def _parse_date(value: str) -> datetime | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return None


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


def _write_backtest_report_json(path: Path, reports: list[BacktestReport]) -> None:
    payload = {"reports": [asdict(report) for report in reports]}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


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
