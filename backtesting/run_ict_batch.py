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
    if "smt_pairs" in config:
        args.extend(["--smt-pairs", *[str(item) for item in config.get("smt_pairs") or []]])
    for name in ("forward_bars", "warmup_bars"):
        value = run.get(name, config.get(name))
        if value is not None:
            args.extend([f"--{name.replace('_', '-')}", str(value)])
    for name in ("tp1_r", "partial_close_fraction"):
        value = run.get(name, config.get(name))
        if value is not None:
            args.extend([f"--{name.replace('_', '-')}", str(value)])
    move_to_be = run.get("move_to_be_after_tp1", config.get("move_to_be_after_tp1"))
    if move_to_be is not None:
        args.append("--move-to-be-after-tp1" if move_to_be else "--no-move-to-be-after-tp1")
    for name in (
        "entry_mode",
        "stop_mode",
        "target_mode",
        "turtle_soup_min_wick_fraction",
        "turtle_soup_min_wick_atr_ratio",
        "turtle_soup_min_close_back_fraction",
        "turtle_soup_min_level_age_bars",
        "turtle_soup_max_confirmation_bars",
        "min_ifvg_retest_bars",
        "max_ifvg_retest_bars",
        "ifvg_entry_mode",
        "ifvg_stop_mode",
        "ifvg_max_source_touches_before_inversion",
        "ifvg_max_source_age_bars",
        "ict2022_max_fvg_retest_bars",
        "breaker_max_trigger_to_retest_bars",
        "breaker_max_retest_count",
        "silver_bullet_windows",
        "silver_bullet_max_retest_bars",
    ):
        value = run.get(name, config.get(name))
        if value is not None:
            args.extend([f"--{name.replace('_', '-')}", str(value)])
    allowed_significances = run.get("turtle_soup_allowed_swing_significances", config.get("turtle_soup_allowed_swing_significances"))
    if allowed_significances:
        args.extend(["--turtle-soup-allowed-swing-significances", *[str(item) for item in allowed_significances]])
    for name in ("pre_model_allow_neutral_htf", "pre_model_allow_equilibrium", "pre_model_require_smt", "pre_model_require_killzone"):
        if run.get(name, config.get(name)):
            args.append(f"--{name.replace('_', '-')}")
    for name in ("turtle_soup_require_killzone", "turtle_soup_require_smt", "turtle_soup_require_mss_confirmation", "breaker_require_displacement"):
        if run.get(name, config.get(name)):
            args.append(f"--{name.replace('_', '-')}")
    confirmation_fvg = run.get("turtle_soup_require_confirmation_fvg", config.get("turtle_soup_require_confirmation_fvg"))
    if confirmation_fvg is not None:
        args.append("--turtle-soup-require-confirmation-fvg" if confirmation_fvg else "--no-turtle-soup-require-confirmation-fvg")
    silver_retest_in_window = run.get("silver_bullet_retest_must_occur_within_window", config.get("silver_bullet_retest_must_occur_within_window"))
    if silver_retest_in_window is not None:
        args.append("--silver-bullet-retest-must-occur-within-window" if silver_retest_in_window else "--no-silver-bullet-retest-must-occur-within-window")
    silver_ce_invalidation = run.get("silver_bullet_use_ce_invalidation", config.get("silver_bullet_use_ce_invalidation"))
    if silver_ce_invalidation is not None:
        args.append("--silver-bullet-use-ce-invalidation" if silver_ce_invalidation else "--no-silver-bullet-use-ce-invalidation")
    pre_model_filter = run.get("pre_model_filter", config.get("pre_model_filter"))
    if pre_model_filter is False:
        args.append("--no-pre-model-filter")
    require_htf_poi = run.get("pre_model_require_htf_poi", config.get("pre_model_require_htf_poi"))
    if require_htf_poi is False:
        args.append("--no-pre-model-require-htf-poi")
    windows = run.get("pre_model_killzone_windows", config.get("pre_model_killzone_windows"))
    if windows:
        args.extend(["--pre-model-killzone-windows", str(windows)])
    return args


if __name__ == "__main__":
    raise SystemExit(main())
