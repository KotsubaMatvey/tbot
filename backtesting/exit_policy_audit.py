from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median
from typing import Any


FIELDS = [
    "run",
    "scope",
    "model",
    "bucket",
    "count",
    "activated_trades",
    "current_expectancy",
    "current_profit_factor",
    "gross_expectancy",
    "one_r_expectancy",
    "one_r_profit_factor",
    "two_r_expectancy",
    "two_r_profit_factor",
    "best_policy",
    "best_expectancy",
    "target_hit_rate",
    "hit_1r_rate",
    "hit_2r_rate",
    "invalidation_rate",
    "avg_target_rr",
    "avg_mfe_r",
    "median_mfe_r",
    "avg_execution_cost_r",
    "avg_funding_cost_r",
    "avg_total_cost_r",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit ICT event rows for exit-policy and R-cost failure modes.")
    parser.add_argument("--events", nargs="+", required=True, help="One or more events.csv files from backtesting.run_ict_models.")
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args(argv)

    rows: list[dict[str, Any]] = []
    for raw_path in args.events:
        path = Path(raw_path)
        rows.extend(summarize_exit_policies(_read_csv(path), run_name=path.parent.name))

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "exit_policy_audit.csv", rows, FIELDS)
    _write_markdown(out_dir / "exit_policy_audit.md", rows, args.events)
    print(f"Exit policy audit complete: rows={len(rows)} out_dir={out_dir}")
    return 0


def summarize_exit_policies(events: list[dict[str, Any]], *, run_name: str = "events") -> list[dict[str, Any]]:
    rows = [_summary_row(run_name, "run", "all", "", events)]
    rows.extend(_bucket_rows(run_name, "model", events, lambda event: str(event.get("model") or "unknown")))
    rows.extend(_bucket_rows(run_name, "risk_bps", events, lambda event: _risk_bps_bucket(_float_or_none(event.get("risk_bps")))))
    rows.extend(_bucket_rows(run_name, "total_cost_r", events, lambda event: _cost_r_bucket(_event_cost(event))))
    rows.extend(_bucket_rows(run_name, "dol_target_type", events, lambda event: str(event.get("dol_target_type") or "none")))
    rows.extend(_bucket_rows(run_name, "turtle_quality", events, lambda event: str(event.get("turtle_quality") or "none")))
    rows.extend(_bucket_rows(run_name, "ny_hour", events, _ny_hour_bucket))
    return rows


def _bucket_rows(
    run_name: str,
    scope: str,
    events: list[dict[str, Any]],
    key_fn: Any,
) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        buckets[key_fn(event)].append(event)
    return [_summary_row(run_name, scope, bucket if scope == "model" else "all", "" if scope == "model" else bucket, group) for bucket, group in sorted(buckets.items())]


def _summary_row(run_name: str, scope: str, model: str, bucket: str, events: list[dict[str, Any]]) -> dict[str, Any]:
    activated = [event for event in events if _bool(event.get("activated_trade"))]
    current = _policy_outcomes(activated, "current")
    one_r = _policy_outcomes(activated, "one_r")
    two_r = _policy_outcomes(activated, "two_r")
    gross = [_float_or_none(event.get("gross_managed_outcome_r") or event.get("managed_outcome_r")) for event in activated]
    gross = [value for value in gross if value is not None]
    best_policy, best_expectancy = _best_policy(
        {
            "current": _avg_values(current),
            "one_r": _avg_values(one_r),
            "two_r": _avg_values(two_r),
        }
    )
    mfes = [_float_or_none(event.get("mfe_r")) for event in activated]
    mfes = [value for value in mfes if value is not None]
    return {
        "run": run_name,
        "scope": scope,
        "model": model,
        "bucket": bucket,
        "count": len(events),
        "activated_trades": len(activated),
        "current_expectancy": _avg_values(current),
        "current_profit_factor": _profit_factor(current),
        "gross_expectancy": _avg_values(gross),
        "one_r_expectancy": _avg_values(one_r),
        "one_r_profit_factor": _profit_factor(one_r),
        "two_r_expectancy": _avg_values(two_r),
        "two_r_profit_factor": _profit_factor(two_r),
        "best_policy": best_policy,
        "best_expectancy": best_expectancy,
        "target_hit_rate": _rate(activated, "target_before_invalidation"),
        "hit_1r_rate": _rate(activated, "hit_1r_before_invalidation"),
        "hit_2r_rate": _rate(activated, "hit_2r_before_invalidation"),
        "invalidation_rate": _rate(activated, "invalidated"),
        "avg_target_rr": _avg(activated, "target_distance_r"),
        "avg_mfe_r": round(sum(mfes) / len(mfes), 6) if mfes else None,
        "median_mfe_r": round(float(median(mfes)), 6) if mfes else None,
        "avg_execution_cost_r": _avg(activated, "execution_cost_r"),
        "avg_funding_cost_r": _avg(activated, "funding_cost_r"),
        "avg_total_cost_r": _avg(activated, "total_cost_r"),
    }


def _policy_outcomes(events: list[dict[str, Any]], policy: str) -> list[float]:
    outcomes: list[float] = []
    for event in events:
        value = _policy_outcome(event, policy)
        if value is not None:
            outcomes.append(value)
    return outcomes


def _policy_outcome(event: dict[str, Any], policy: str) -> float | None:
    if _bool(event.get("invalidated_before_entry")) or _bool(event.get("target_reached_before_entry")):
        return None
    if policy == "current":
        value = _float_or_none(event.get("net_managed_outcome_r"))
        if value is not None:
            return value
        return _float_or_none(event.get("managed_outcome_r"))
    cost = _event_cost(event) or 0.0
    if policy == "one_r":
        if _bool(event.get("hit_1r_before_invalidation")):
            return round(1.0 - cost, 6)
    if policy == "two_r":
        if _bool(event.get("hit_2r_before_invalidation")):
            return round(2.0 - cost, 6)
    if _bool(event.get("invalidated")):
        return round(-1.0 - cost, 6)
    return _policy_outcome(event, "current")


def _event_cost(event: dict[str, Any]) -> float | None:
    value = _float_or_none(event.get("total_cost_r"))
    if value is not None:
        return value
    return _float_or_none(event.get("execution_cost_r"))


def _best_policy(values: dict[str, float | None]) -> tuple[str | None, float | None]:
    ranked = [(policy, value) for policy, value in values.items() if value is not None]
    if not ranked:
        return None, None
    policy, value = max(ranked, key=lambda item: item[1])
    return policy, value


def _risk_bps_bucket(value: float | None) -> str:
    if value is None:
        return "unknown"
    if value < 25:
        return "<25"
    if value < 50:
        return "25-50"
    if value < 100:
        return "50-100"
    if value < 200:
        return "100-200"
    return ">=200"


def _cost_r_bucket(value: float | None) -> str:
    if value is None:
        return "unknown"
    if value < 0.05:
        return "<0.05"
    if value < 0.10:
        return "0.05-0.10"
    if value < 0.25:
        return "0.10-0.25"
    if value < 0.50:
        return "0.25-0.50"
    return ">=0.50"


def _ny_hour_bucket(event: dict[str, Any]) -> str:
    value = str(event.get("ny_time") or "")
    if len(value) >= 13:
        return value[11:13]
    return "unknown"


def _rate(group: list[dict[str, Any]], field: str) -> float | None:
    return round(sum(1 for event in group if _bool(event.get(field))) / len(group), 6) if group else None


def _avg(group: list[dict[str, Any]], field: str) -> float | None:
    values = [_float_or_none(event.get(field)) for event in group]
    values = [value for value in values if value is not None]
    return _avg_values(values)


def _avg_values(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def _profit_factor(outcomes: list[float]) -> float | str | None:
    wins = [value for value in outcomes if value > 0]
    losses = [abs(value) for value in outcomes if value < 0]
    if not wins and not losses:
        return None
    if not losses:
        return "inf" if wins else None
    return round(sum(wins) / sum(losses), 6)


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
        "# Exit Policy Audit",
        "",
        "Post-process audit over existing `events.csv` files. Alternative policies use existing hit flags, so they are diagnostic estimates, not a replacement for candle-level replays.",
        "",
        "Events:",
        *[f"- `{item}`" for item in events],
        "",
        "## Run And Model Rows",
        _markdown_table([row for row in rows if row["scope"] in {"run", "model"}]),
        "",
        "## Risk And Cost Buckets",
        _markdown_table([row for row in rows if row["scope"] in {"risk_bps", "total_cost_r"}]),
        "",
        "## ICT Attribute Buckets",
        _markdown_table([row for row in rows if row["scope"] in {"dol_target_type", "turtle_quality", "ny_hour"}]),
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
