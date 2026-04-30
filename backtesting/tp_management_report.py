from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median
from typing import Any


FIELDS = [
    "run",
    "model",
    "tp1_r",
    "partial_close_fraction",
    "count",
    "activated_trades",
    "tp1_hit_rate",
    "target_hit_rate",
    "invalidation_rate",
    "avg_target_rr",
    "avg_mfe_r",
    "median_mfe_r",
    "managed_expectancy",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare partial TP/BE management variants over ICT events.csv files.")
    parser.add_argument("--events", nargs="+", required=True)
    parser.add_argument("--tp1-r", nargs="+", type=float, default=[1.0, 2.0])
    parser.add_argument("--partials", nargs="+", type=float, default=[0.3, 0.5, 0.7])
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    rows: list[dict[str, Any]] = []
    for raw_path in args.events:
        path = Path(raw_path)
        events = _read_csv(path)
        run_name = path.parent.name
        rows.extend(_summarize_run(run_name, events, args.tp1_r, args.partials))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(out, rows, FIELDS)
    _write_markdown(out.with_suffix(".md"), rows, args.events)
    print(f"TP management report complete: rows={len(rows)} out={out}")
    return 0


def _summarize_run(run_name: str, events: list[dict[str, Any]], tp1_rs: list[float], partials: list[float]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[str(event.get("model") or "unknown")].append(event)

    for model, group in sorted(buckets.items()):
        for tp1_r in tp1_rs:
            for partial in partials:
                outcomes = [_managed_outcome(event, tp1_r, partial) for event in group]
                outcomes = [item for item in outcomes if item is not None]
                mfes = [_float_or_none(event.get("mfe_r")) for event in group]
                mfes = [item for item in mfes if item is not None]
                rows.append(
                    {
                        "run": run_name,
                        "model": model,
                        "tp1_r": tp1_r,
                        "partial_close_fraction": partial,
                        "count": len(group),
                        "activated_trades": sum(1 for event in group if _bool(event.get("activated_trade"))),
                        "tp1_hit_rate": _tp1_rate(group, tp1_r),
                        "target_hit_rate": _rate(group, "target_before_invalidation"),
                        "invalidation_rate": _rate(group, "invalidated"),
                        "avg_target_rr": _avg(group, "target_distance_r"),
                        "avg_mfe_r": round(sum(mfes) / len(mfes), 6) if mfes else None,
                        "median_mfe_r": round(float(median(mfes)), 6) if mfes else None,
                        "managed_expectancy": round(sum(outcomes) / len(outcomes), 6) if outcomes else None,
                    }
                )
    rows.sort(key=lambda row: (row["run"], -float(row["managed_expectancy"] or -999), row["model"]))
    return rows


def _managed_outcome(event: dict[str, Any], tp1_r: float, partial: float) -> float | None:
    if _bool(event.get("invalidated_before_entry")) or _bool(event.get("target_reached_before_entry")):
        return None
    target_rr = _float_or_none(event.get("target_distance_r"))
    mfe = _float_or_none(event.get("mfe_r"))
    tp1_hit = _tp1_hit(event, tp1_r)
    if _bool(event.get("target_before_invalidation")) and target_rr is not None:
        return partial * tp1_r + (1.0 - partial) * target_rr if tp1_hit else target_rr
    if tp1_hit:
        return partial * tp1_r
    if _bool(event.get("invalidated")):
        return -1.0
    return mfe


def _tp1_rate(group: list[dict[str, Any]], tp1_r: float) -> float | None:
    return round(sum(1 for event in group if _tp1_hit(event, tp1_r)) / len(group), 6) if group else None


def _tp1_hit(event: dict[str, Any], tp1_r: float) -> bool:
    if tp1_r <= 1.0:
        return _bool(event.get("hit_1r_before_invalidation"))
    if tp1_r <= 2.0:
        return _bool(event.get("hit_2r_before_invalidation"))
    mfe = _float_or_none(event.get("mfe_r"))
    return bool(mfe is not None and mfe >= tp1_r and not _bool(event.get("invalidated")))


def _rate(group: list[dict[str, Any]], field: str) -> float | None:
    return round(sum(1 for event in group if _bool(event.get(field))) / len(group), 6) if group else None


def _avg(group: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in group]
    values = [item for item in values if item is not None]
    return round(sum(values) / len(values), 6) if values else None


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


def _read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], events: list[str]) -> None:
    lines = [
        "# TP Management Report",
        "",
        "Fast post-process report over existing `events.csv` files.",
        "",
        "Events:",
        *[f"- `{item}`" for item in events],
        "",
        "## Top Variants",
        _markdown_table(rows[:40]),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(FIELDS) + " |", "| " + " | ".join("---" for _ in FIELDS) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field) or "") for field in FIELDS) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
