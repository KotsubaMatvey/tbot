from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


RUN_FIELDS = [
    "run",
    "model",
    "count",
    "activated_trades",
    "managed_expectancy",
    "gross_managed_expectancy",
    "profit_factor",
    "avg_execution_cost_r",
    "avg_total_cost_r",
    "avg_mfe_r",
    "avg_rr",
    "target_before_invalidation_rate",
    "hit_1r_before_invalidation_rate",
    "hit_2r_before_invalidation_rate",
    "invalidation_rate",
    "walk_forward_passed",
    "walk_forward_failed_gates",
    "top_no_trade_reasons",
    "barriers",
    "source_dir",
]

MODEL_FIELDS = [
    "model",
    "runs",
    "passed_runs",
    "best_run",
    "best_expectancy",
    "best_profit_factor",
    "median_expectancy",
    "total_activated_trades",
    "top_barriers",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Aggregate ICT backtest outputs into a cross-model profitability barrier audit.")
    parser.add_argument("--results-dir", default="backtest_results")
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args(argv)

    run_rows = audit_result_tree(Path(args.results_dir))
    model_rows = summarize_by_model(run_rows)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "algorithm_barrier_audit.csv", run_rows, RUN_FIELDS)
    _write_csv(out_dir / "algorithm_barrier_by_model.csv", model_rows, MODEL_FIELDS)
    _write_markdown(out_dir / "algorithm_barrier_audit.md", run_rows, model_rows, Path(args.results_dir))
    print(f"Algorithm barrier audit complete: runs={len(run_rows)} models={len(model_rows)} out_dir={out_dir}")
    return 0


def audit_result_tree(results_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen_run_dirs: set[Path] = set()
    for summary_path in sorted(results_dir.rglob("summary_by_model.csv")):
        run_dir = summary_path.parent
        seen_run_dirs.add(run_dir)
        rows.extend(audit_run_dir(run_dir))
    for walk_forward_path in sorted(results_dir.rglob("walk_forward_report.csv")):
        run_dir = walk_forward_path.parent
        if run_dir in seen_run_dirs:
            continue
        rows.extend(audit_run_dir(run_dir))
    rows.sort(key=lambda row: (str(row["model"]), -_sort_float(row.get("managed_expectancy")), str(row["run"])))
    return rows


def audit_run_dir(run_dir: Path) -> list[dict[str, Any]]:
    summary_path = run_dir / "summary_by_model.csv"
    walk_forward = _walk_forward_overall(run_dir / "walk_forward_report.csv")
    no_trade = _no_trade_reasons(run_dir / "summary_by_no_trade_reasons.csv")
    if not summary_path.exists():
        if not walk_forward:
            return []
        return [_walk_forward_only_row(run_dir, walk_forward)]

    model_rows = _read_csv(summary_path)
    rows = []
    for row in model_rows:
        model = str(row.get("model") or "unknown")
        barriers = _barriers(row, walk_forward, no_trade.get(model, ""))
        rows.append(
            {
                "run": run_dir.name,
                "model": model,
                "count": row.get("count"),
                "activated_trades": row.get("activated_trades"),
                "managed_expectancy": row.get("managed_expectancy") or row.get("avg_managed_outcome_r"),
                "gross_managed_expectancy": row.get("gross_managed_expectancy"),
                "profit_factor": _walk_field(row, walk_forward, "profit_factor"),
                "avg_execution_cost_r": row.get("avg_execution_cost_r"),
                "avg_total_cost_r": row.get("avg_total_cost_r"),
                "avg_mfe_r": row.get("avg_mfe_r"),
                "avg_rr": row.get("avg_rr"),
                "target_before_invalidation_rate": row.get("target_before_invalidation_rate"),
                "hit_1r_before_invalidation_rate": row.get("hit_1r_before_invalidation_rate"),
                "hit_2r_before_invalidation_rate": row.get("hit_2r_before_invalidation_rate"),
                "invalidation_rate": row.get("invalidation_rate"),
                "walk_forward_passed": walk_forward.get("passed"),
                "walk_forward_failed_gates": walk_forward.get("failed_gates"),
                "top_no_trade_reasons": no_trade.get(model, ""),
                "barriers": ";".join(barriers),
                "source_dir": str(run_dir),
            }
        )
    return rows


def _walk_forward_only_row(run_dir: Path, walk_forward: dict[str, Any]) -> dict[str, Any]:
    model = _infer_model_from_run(run_dir.name)
    barriers = _barriers(walk_forward, walk_forward, "")
    return {
        "run": run_dir.name,
        "model": model,
        "count": walk_forward.get("count"),
        "activated_trades": walk_forward.get("activated_trades"),
        "managed_expectancy": walk_forward.get("managed_expectancy"),
        "gross_managed_expectancy": walk_forward.get("gross_managed_expectancy"),
        "profit_factor": walk_forward.get("profit_factor"),
        "avg_execution_cost_r": walk_forward.get("avg_execution_cost_r"),
        "avg_total_cost_r": walk_forward.get("avg_total_cost_r"),
        "avg_mfe_r": walk_forward.get("avg_mfe_r"),
        "avg_rr": walk_forward.get("avg_rr"),
        "target_before_invalidation_rate": walk_forward.get("target_before_invalidation_rate"),
        "hit_1r_before_invalidation_rate": walk_forward.get("hit_1r_before_invalidation_rate"),
        "hit_2r_before_invalidation_rate": walk_forward.get("hit_2r_before_invalidation_rate"),
        "invalidation_rate": walk_forward.get("invalidation_rate"),
        "walk_forward_passed": walk_forward.get("passed"),
        "walk_forward_failed_gates": walk_forward.get("failed_gates"),
        "top_no_trade_reasons": "",
        "barriers": ";".join(barriers),
        "source_dir": str(run_dir),
    }


def _infer_model_from_run(run_name: str) -> str:
    lowered = run_name.lower()
    patterns = [
        ("silver", "silver_bullet"),
        ("turtle", "turtle_soup"),
        ("ict2022", "ict2022_mss_fvg"),
        ("ifvg", "ifvg_retest"),
        ("breaker", "breaker_block"),
        ("reclaimed", "reclaimed_ob"),
        ("rejection", "rejection_block"),
        ("mitigation", "mitigation_block"),
    ]
    for pattern, model in patterns:
        if pattern in lowered:
            return model
    return "unknown"


def summarize_by_model(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[str(row.get("model") or "unknown")].append(row)
    summaries = []
    for model, group in sorted(buckets.items()):
        expectancies = [_float_or_none(row.get("managed_expectancy")) for row in group]
        expectancies = [value for value in expectancies if value is not None]
        best = max(group, key=lambda row: _sort_float(row.get("managed_expectancy")))
        barrier_counts: Counter[str] = Counter()
        for row in group:
            barrier_counts.update(reason for reason in str(row.get("barriers") or "").split(";") if reason)
        summaries.append(
            {
                "model": model,
                "runs": len(group),
                "passed_runs": sum(1 for row in group if _bool(row.get("walk_forward_passed"))),
                "best_run": best.get("run"),
                "best_expectancy": best.get("managed_expectancy"),
                "best_profit_factor": best.get("profit_factor"),
                "median_expectancy": _median(expectancies),
                "total_activated_trades": sum(_int_or_zero(row.get("activated_trades")) for row in group),
                "top_barriers": ";".join(item for item, _ in barrier_counts.most_common(8)),
            }
        )
    summaries.sort(key=lambda row: (-int(row["passed_runs"]), -_sort_float(row.get("best_expectancy")), str(row["model"])))
    return summaries


def _barriers(summary: dict[str, Any], walk_forward: dict[str, Any], no_trade: str) -> list[str]:
    barriers = []
    activated = _float_or_none(summary.get("activated_trades"))
    count = _float_or_none(summary.get("count"))
    expectancy = _float_or_none(summary.get("managed_expectancy") or summary.get("avg_managed_outcome_r"))
    gross = _float_or_none(summary.get("gross_managed_expectancy"))
    pf = _float_or_none(_walk_field(summary, walk_forward, "profit_factor"))
    avg_cost = _float_or_none(summary.get("avg_total_cost_r") or summary.get("avg_execution_cost_r"))
    avg_mfe = _float_or_none(summary.get("avg_mfe_r"))
    target_rate = _float_or_none(summary.get("target_before_invalidation_rate"))
    hit_1r = _float_or_none(summary.get("hit_1r_before_invalidation_rate"))
    invalidation = _float_or_none(summary.get("invalidation_rate"))

    if activated is None or activated == 0:
        barriers.append("zero_activated_trades")
    elif activated < 30:
        barriers.append("thin_sample")
    if count is not None and activated is not None and count > 0 and activated / count < 0.5:
        barriers.append("poor_fill_or_activation")
    if expectancy is None:
        barriers.append("missing_expectancy")
    elif expectancy <= 0:
        barriers.append("negative_expectancy")
    elif expectancy < 0.3:
        barriers.append("low_expectancy")
    if pf is None:
        barriers.append("missing_profit_factor")
    elif pf < 1.3:
        barriers.append("low_profit_factor")
    if avg_cost is not None and avg_cost >= 0.25:
        barriers.append("cost_drag")
    if gross is not None and expectancy is not None and gross - expectancy >= 0.15:
        barriers.append("net_cost_gap")
    if invalidation is not None and invalidation >= 0.55:
        barriers.append("high_invalidation")
    if target_rate is not None and target_rate < 0.25:
        barriers.append("low_target_hit_rate")
    if hit_1r is not None and hit_1r < 0.45:
        barriers.append("weak_1r_followthrough")
    if avg_mfe is not None and avg_mfe >= 2 and (target_rate is None or target_rate < 0.25):
        barriers.append("mfe_not_monetized")
    failed_gates = str(walk_forward.get("failed_gates") or "")
    if failed_gates:
        barriers.extend(f"wf_{item}" for item in failed_gates.split(";") if item)
    if "target_rr_below" in no_trade:
        barriers.append("target_rr_pressure")
    return sorted(set(barriers))


def _walk_forward_overall(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    for row in _read_csv(path):
        if str(row.get("phase") or "") == "overall":
            return row
    return {}


def _walk_field(summary: dict[str, Any], walk_forward: dict[str, Any], field: str) -> Any:
    value = walk_forward.get(field)
    if value not in {None, ""}:
        return value
    return summary.get(field)


def _no_trade_reasons(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    grouped: dict[str, list[tuple[int, str, str]]] = defaultdict(list)
    for row in _read_csv(path):
        model = str(row.get("model") or "unknown")
        reason = str(row.get("no_trade_reasons") or "none")
        count = _int_or_zero(row.get("count"))
        expectancy = str(row.get("managed_expectancy") or "")
        grouped[model].append((count, reason, expectancy))
    return {
        model: ";".join(f"{reason}:{count}:{expectancy}" for count, reason, expectancy in sorted(items, reverse=True)[:4])
        for model, items in grouped.items()
    }


def _median(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return round(ordered[mid], 6)
    return round((ordered[mid - 1] + ordered[mid]) / 2, 6)


def _read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], model_rows: list[dict[str, Any]], results_dir: Path) -> None:
    failed = [row for row in rows if row.get("barriers")]
    lines = [
        "# Algorithm Barrier Audit",
        "",
        f"Results dir: `{results_dir}`",
        "",
        "## By Model",
        _markdown_table(model_rows[:20], MODEL_FIELDS),
        "",
        "## Run Rows",
        _markdown_table(rows[:40], RUN_FIELDS),
        "",
        "## Highest Barrier Density",
        _markdown_table(sorted(failed, key=lambda row: (-len(str(row.get("barriers") or "").split(";")), str(row.get("run"))))[:40], RUN_FIELDS),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> str:
    if not rows:
        return "_No rows._"
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_markdown_value(row.get(field)) for field in fields) + " |")
    return "\n".join(lines)


def _markdown_value(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _float_or_none(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    if str(value).lower() == "inf":
        return 999.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _sort_float(value: Any, default: float = -999.0) -> float:
    parsed = _float_or_none(value)
    if parsed is None:
        return default
    return parsed


def _int_or_zero(value: Any) -> int:
    parsed = _float_or_none(value)
    if parsed is None:
        return 0
    return int(parsed)


if __name__ == "__main__":
    raise SystemExit(main())
