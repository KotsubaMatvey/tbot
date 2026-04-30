from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median
from typing import Any

from strategies.ict_models.model_filters import passes_model_filter

REPORT_FIELDS = [
    "scope",
    "model",
    "threshold",
    "filter_name",
    "filtered_out",
    "count",
    "activated_trades",
    "invalidated_before_entry",
    "avg_decision_score",
    "avg_mfe_r",
    "median_mfe_r",
    "avg_rr",
    "expectancy",
    "managed_expectancy",
    "avg_managed_outcome_r",
    "target_before_invalidation_rate",
    "hit_1r_before_invalidation_rate",
    "hit_2r_before_invalidation_rate",
    "invalidation_rate",
    "same_bar_ambiguous_count",
    "no_trade_reason_count",
    "top_no_trade_reasons",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize ICT event rows by decision-score thresholds.")
    parser.add_argument("--events", required=True, help="Path to events.csv from backtesting.run_ict_models.")
    parser.add_argument("--out-dir", default=None, help="Output directory. Defaults to the events file directory.")
    parser.add_argument("--thresholds", nargs="+", type=float, default=[0.0, 50.0, 70.0])
    parser.add_argument("--model-filters", default=None, help="JSON file with a model_filters object.")
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    rows = _read_csv(events_path)
    model_filters = _read_model_filters(Path(args.model_filters)) if args.model_filters else {}
    report = summarize_thresholds(rows, args.thresholds, model_filters=model_filters)
    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "score_threshold_report.csv", report, REPORT_FIELDS)
    _write_markdown(out_dir / "score_threshold_report.md", report, events_path, args.thresholds)
    print(f"Score threshold report complete: rows={len(report)} out_dir={out_dir}")
    return 0


def summarize_thresholds(
    events: list[dict[str, Any]],
    thresholds: list[float],
    *,
    model_filters: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for threshold in thresholds:
        filtered = [
            event
            for event in events
            if threshold <= 0 or (_float_or_none(event.get("decision_score")) is not None and _float_or_none(event.get("decision_score")) >= threshold)
        ]
        rows.append(_summary_row(filtered, scope="all", model="ALL", threshold=threshold, filter_name="none"))
        by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for event in filtered:
            by_model[str(event.get("model") or "unknown")].append(event)
        for model in sorted(by_model):
            rows.append(_summary_row(by_model[model], scope="model", model=model, threshold=threshold, filter_name="none"))
        if model_filters:
            _add_filtered_rows(rows, filtered, threshold, model_filters)
    return rows


def _add_filtered_rows(
    rows: list[dict[str, Any]],
    events: list[dict[str, Any]],
    threshold: float,
    model_filters: dict[str, dict[str, Any]],
) -> None:
    by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        by_model[str(event.get("model") or "unknown")].append(event)

    filtered_all: list[dict[str, Any]] = []
    filtered_out = 0
    for model, group in sorted(by_model.items()):
        rules = model_filters.get(model, {})
        accepted = [event for event in group if passes_model_filter(event, rules)]
        filtered_all.extend(accepted)
        filtered_out += len(group) - len(accepted)
        rows.append(
            _summary_row(
                accepted,
                scope="filtered_model",
                model=model,
                threshold=threshold,
                filter_name="model_rules",
                filtered_out=len(group) - len(accepted),
            )
        )
    rows.append(
        _summary_row(
            filtered_all,
            scope="filtered_all",
            model="ALL",
            threshold=threshold,
            filter_name="model_rules",
            filtered_out=filtered_out,
        )
    )


def _summary_row(
    group: list[dict[str, Any]],
    *,
    scope: str,
    model: str,
    threshold: float,
    filter_name: str,
    filtered_out: int = 0,
) -> dict[str, Any]:
    mfes = [_float_or_none(event.get("mfe_r")) for event in group]
    mfes = [value for value in mfes if value is not None]
    reasons = _reason_counter(group)
    return {
        "scope": scope,
        "model": model,
        "threshold": _format_threshold(threshold),
        "filter_name": filter_name,
        "filtered_out": filtered_out,
        "count": len(group),
        "activated_trades": sum(1 for event in group if _bool(event.get("activated_trade"))),
        "invalidated_before_entry": sum(1 for event in group if _bool(event.get("invalidated_before_entry"))),
        "avg_decision_score": _avg(group, "decision_score"),
        "avg_mfe_r": round(sum(mfes) / len(mfes), 6) if mfes else None,
        "median_mfe_r": round(float(median(mfes)), 6) if mfes else None,
        "avg_rr": _avg(group, "target_distance_r"),
        "expectancy": _expectancy(group),
        "managed_expectancy": _avg(group, "managed_outcome_r"),
        "avg_managed_outcome_r": _avg(group, "managed_outcome_r"),
        "target_before_invalidation_rate": _rate(group, "target_before_invalidation"),
        "hit_1r_before_invalidation_rate": _rate(group, "hit_1r_before_invalidation"),
        "hit_2r_before_invalidation_rate": _rate(group, "hit_2r_before_invalidation"),
        "invalidation_rate": _rate(group, "invalidated"),
        "same_bar_ambiguous_count": sum(1 for event in group if _bool(event.get("same_bar_ambiguous"))),
        "no_trade_reason_count": sum(1 for event in group if event.get("no_trade_reasons")),
        "top_no_trade_reasons": ";".join(f"{reason}:{count}" for reason, count in reasons.most_common(5)),
    }


def _expectancy(group: list[dict[str, Any]]) -> float | None:
    outcomes: list[float] = []
    for event in group:
        if _bool(event.get("invalidated_before_entry")):
            continue
        rr = _float_or_none(event.get("target_distance_r"))
        mfe = _float_or_none(event.get("mfe_r"))
        if _bool(event.get("target_before_invalidation")) and rr is not None:
            outcomes.append(rr)
        elif _bool(event.get("invalidated")):
            outcomes.append(-1.0)
        elif mfe is not None:
            outcomes.append(mfe)
    return round(sum(outcomes) / len(outcomes), 6) if outcomes else None


def _reason_counter(group: list[dict[str, Any]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for event in group:
        for reason in str(event.get("no_trade_reasons") or "").split(";"):
            reason = reason.strip()
            if reason:
                counter[reason] += 1
    return counter


def _avg(group: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in group]
    values = [value for value in values if value is not None]
    return round(sum(values) / len(values), 6) if values else None


def _rate(group: list[dict[str, Any]], field: str) -> float | None:
    return round(sum(1 for event in group if _bool(event.get(field))) / len(group), 6) if group else None


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _format_threshold(value: float) -> str:
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


def _write_markdown(path: Path, rows: list[dict[str, Any]], events_path: Path, thresholds: list[float]) -> None:
    lines = [
        "# ICT Decision Score Threshold Report",
        "",
        f"- events: `{events_path}`",
        f"- thresholds: {', '.join(_format_threshold(item) for item in thresholds)}",
        "",
        "## All Models",
        _markdown_table([row for row in rows if row["scope"] in {"all", "filtered_all"}]),
        "",
        "## By Model",
        _markdown_table([row for row in rows if row["scope"] in {"model", "filtered_model"}]),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    headers = REPORT_FIELDS
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(header) or "") for header in headers) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
