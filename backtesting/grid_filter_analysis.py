from __future__ import annotations

import argparse
import csv
from itertools import product
from pathlib import Path
from typing import Any

from backtesting.score_threshold_report import _expectancy, _float_or_none, _rate
from strategies.ict_models.model_filters import passes_model_filter

GRID_FIELDS = [
    "rank",
    "filter_name",
    "count",
    "filtered_out",
    "expectancy",
    "gross_managed_expectancy",
    "managed_expectancy",
    "profit_factor",
    "target_before_invalidation_rate",
    "hit_2r_before_invalidation_rate",
    "invalidation_rate",
    "avg_decision_score",
    "avg_rr",
    "min_decision_score",
    "min_target_distance_r",
    "require_smt",
    "require_session_window",
    "allowed_displacement_grades",
    "allowed_htf_locations",
    "exclude_no_trade_reasons",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Grid-search post/backtest ICT filters over events.csv.")
    parser.add_argument("--events", required=True)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--min-count", type=int, default=10)
    args = parser.parse_args(argv)

    events_path = Path(args.events)
    events = _read_csv(events_path)
    rows = summarize_grid(events, min_count=args.min_count)
    out_dir = Path(args.out_dir) if args.out_dir else events_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "filter_grid_report.csv", rows, GRID_FIELDS)
    _write_markdown(out_dir / "filter_grid_report.md", rows, events_path, args.min_count)
    print(f"Filter grid report complete: rows={len(rows)} out_dir={out_dir}")
    return 0


def summarize_grid(events: list[dict[str, Any]], *, min_count: int = 10) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    grids = {
        "min_decision_score": [0, 50, 70],
        "min_target_distance_r": [0, 2, 3],
        "require_smt": [False, True],
        "require_session_window": [False, True],
        "allowed_displacement_grades": [[], ["valid", "strong"], ["strong"]],
        "allowed_htf_locations": [[], ["discount", "premium"]],
        "exclude_no_trade_reasons": [[], ["equilibrium", "poor_pd_location", "target_rr_below_2"]],
    }
    keys = list(grids)
    for values in product(*(grids[key] for key in keys)):
        rules = dict(zip(keys, values))
        accepted = [event for event in events if _passes_grid(event, rules)]
        if len(accepted) < min_count:
            continue
        rows.append(_grid_row(accepted, len(events) - len(accepted), rules))
    rows.sort(key=lambda row: (_float_or_none(row.get("managed_expectancy")) is None, -(_float_or_none(row.get("managed_expectancy")) or -999), -int(row["count"])))
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def _passes_grid(event: dict[str, Any], rules: dict[str, Any]) -> bool:
    threshold = _float_or_none(rules.get("min_decision_score")) or 0
    score = _float_or_none(event.get("decision_score"))
    if threshold > 0 and (score is None or score < threshold):
        return False
    model_rules = {key: value for key, value in rules.items() if key != "min_decision_score" and not _empty_filter(value)}
    return passes_model_filter(event, model_rules)


def _grid_row(group: list[dict[str, Any]], filtered_out: int, rules: dict[str, Any]) -> dict[str, Any]:
    return {
        "rank": None,
        "filter_name": _filter_name(rules),
        "count": len(group),
        "filtered_out": filtered_out,
        "expectancy": _expectancy(group),
        "gross_managed_expectancy": _avg(group, "gross_managed_outcome_r"),
        "managed_expectancy": _avg_managed_outcome(group),
        "profit_factor": _profit_factor(group),
        "target_before_invalidation_rate": _rate(group, "target_before_invalidation"),
        "hit_2r_before_invalidation_rate": _rate(group, "hit_2r_before_invalidation"),
        "invalidation_rate": _rate(group, "invalidated"),
        "avg_decision_score": _avg(group, "decision_score"),
        "avg_rr": _avg(group, "target_distance_r"),
        **{key: _format_value(value) for key, value in rules.items()},
    }


def _filter_name(rules: dict[str, Any]) -> str:
    parts = []
    for key, value in rules.items():
        if _empty_filter(value):
            continue
        parts.append(f"{key}={_format_value(value)}")
    return "none" if not parts else ";".join(parts)


def _avg(group: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(item.get(field)) for item in group]
    values = [item for item in values if item is not None]
    return round(sum(values) / len(values), 6) if values else None


def _avg_managed_outcome(group: list[dict[str, Any]]) -> float | None:
    values = [_managed_outcome(item) for item in group]
    values = [item for item in values if item is not None]
    return round(sum(values) / len(values), 6) if values else None


def _profit_factor(group: list[dict[str, Any]]) -> float | None:
    outcomes = [_managed_outcome(item) for item in group]
    wins = [item for item in outcomes if item is not None and item > 0]
    losses = [abs(item) for item in outcomes if item is not None and item < 0]
    if not wins or not losses:
        return None
    return round(sum(wins) / sum(losses), 6)


def _managed_outcome(item: dict[str, Any]) -> float | None:
    value = _float_or_none(item.get("net_managed_outcome_r"))
    if value is not None:
        return value
    return _float_or_none(item.get("managed_outcome_r"))


def _empty_filter(value: Any) -> bool:
    if isinstance(value, list):
        return not value
    return value in {None, 0, False, ""}


def _format_value(value: Any) -> str:
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], events_path: Path, min_count: int) -> None:
    lines = [
        "# ICT Filter Grid Report",
        "",
        f"- events: `{events_path}`",
        f"- min_count: {min_count}",
        "",
        "## Top Filters",
        _markdown_table(rows[:30]),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(GRID_FIELDS) + " |", "| " + " | ".join("---" for _ in GRID_FIELDS) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field) or "") for field in GRID_FIELDS) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
