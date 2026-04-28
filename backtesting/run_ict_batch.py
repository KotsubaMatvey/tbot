from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from backtesting import grid_filter_analysis, run_ict_models, score_threshold_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run repeatable ICT backtest batches from a JSON preset.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args(argv)

    config_path = Path(args.config)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    thresholds = [str(item) for item in config.get("thresholds", [0, 50, 70])]
    for run in config.get("runs", []):
        run_args = build_run_args(config, run)
        result = run_ict_models.main(run_args)
        if result != 0:
            return result
        out_dir = Path(run["out_dir"])
        report_args = ["--events", str(out_dir / "events.csv"), "--thresholds", *thresholds]
        if config.get("model_filters"):
            report_args.extend(["--model-filters", str(config_path)])
        result = score_threshold_report.main(report_args)
        if result != 0:
            return result
        if config.get("grid_filters", True):
            grid_args = ["--events", str(out_dir / "events.csv"), "--min-count", str(config.get("grid_min_count", 10))]
            result = grid_filter_analysis.main(grid_args)
            if result != 0:
                return result
    return 0


def build_run_args(config: dict[str, Any], run: dict[str, Any]) -> list[str]:
    args = [
        "--data-dir",
        str(run.get("data_dir") or config["data_dir"]),
        "--symbols",
        *[str(item) for item in run.get("symbols", config["symbols"])],
        "--timeframes",
        *[str(item) for item in run["timeframes"]],
        "--models",
        *[str(item) for item in run.get("models", config["models"])],
        "--context-mode",
        str(run.get("context_mode", config.get("context_mode", "off"))),
        "--out-dir",
        str(run["out_dir"]),
    ]
    if config.get("smt_pairs"):
        args.extend(["--smt-pairs", *[str(item) for item in config["smt_pairs"]]])
    for name in ("forward_bars", "warmup_bars"):
        value = run.get(name, config.get(name))
        if value is not None:
            args.extend([f"--{name.replace('_', '-')}", str(value)])
    for name in ("pre_model_allow_neutral_htf", "pre_model_allow_equilibrium", "pre_model_require_smt", "pre_model_require_killzone"):
        if run.get(name, config.get(name)):
            args.append(f"--{name.replace('_', '-')}")
    pre_model_filter = run.get("pre_model_filter", config.get("pre_model_filter"))
    if pre_model_filter is False:
        args.append("--no-pre-model-filter")
    windows = run.get("pre_model_killzone_windows", config.get("pre_model_killzone_windows"))
    if windows:
        args.extend(["--pre-model-killzone-windows", str(windows)])
    return args


if __name__ == "__main__":
    raise SystemExit(main())
