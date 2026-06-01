from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from backtesting import Candle
from backtesting.data import HistoricalDataError, load_history_for
from backtesting.run_ict_models import _date_scan_bounds, _scan_session_window_matches
from market_primitives import detect_fvg, detect_liquidity_raids, detect_structure_breaks, detect_sweeps
from strategies.ict_models.common import buffered_stop, closed_candles, nearest_liquidity_target
from strategies.ict_models.ict2022_mss_fvg import (
    _bars_between,
    _first_retest_index,
    _matching_window,
    _target_reached_before_retest,
    _window_list,
)
from strategies.types import PrimitiveSnapshot


STAGES = [
    "scan_side_bars",
    "latest_sweep",
    "sweep_session_gate",
    "structure_after_sweep_any",
    "structure_body_close",
    "structure_valid_displacement",
    "structure_strong_displacement",
    "structure_config_displacement",
    "sweep_age_gate",
    "structure_session_gate",
    "same_session_sweep_mss",
    "active_fvg_after_mss",
    "retest_any",
    "retest_within_limit",
    "retest_session_gate",
    "target_open_until_retest",
    "candidate",
    "retested_eligible_fvg_any",
    "retested_eligible_fvg_within_limit",
    "retested_eligible_fvg_session_gate",
    "target_open_until_retest_any_fvg",
    "candidate_any_fvg",
]

FVG_PATH_STAGES = [
    "retest_any",
    "retest_within_limit",
    "retest_session_gate",
    "target_open_until_retest",
    "candidate",
]


@dataclass(slots=True)
class ICT2022DiagnosticConfig:
    session_windows: list[str]
    max_fvg_retest_bars: int = 20
    max_sweep_age_bars: int = 20
    require_displacement: bool = True
    require_strong_displacement: bool = True
    require_body_close: bool = True
    require_killzone: bool = True
    require_same_session: bool = True
    retest_must_occur_within_session: bool = False
    entry_mode: str = "edge"
    stop_buffer_bps: float = 2.0


class ICT2022DiagnosticAccumulator:
    def __init__(
        self,
        symbol: str,
        timeframe: str,
        candles: list[Candle],
        *,
        start_index: int = 0,
        detector_window: int = 200,
        snapshot_candle_window: int = 1500,
        max_primitives_per_field: int = 1500,
    ) -> None:
        self.symbol = symbol
        self.timeframe = timeframe
        self.candles = candles
        self.next_index = max(0, start_index)
        self.detector_window = detector_window
        self.snapshot_candle_window = snapshot_candle_window
        self.max_primitives_per_field = max_primitives_per_field
        self.sweeps: dict[tuple[Any, ...], Any] = {}
        self.raids: dict[tuple[Any, ...], Any] = {}
        self.structure_breaks: dict[tuple[Any, ...], Any] = {}
        self.fvgs: dict[tuple[Any, ...], Any] = {}

    def snapshot_until(self, timestamp: int) -> PrimitiveSnapshot:
        while self.next_index < len(self.candles):
            candle = self.candles[self.next_index]
            if int(candle["time"]) > timestamp:
                break
            visible_start = max(0, self.next_index + 1 - self.detector_window)
            visible = self.candles[visible_start : self.next_index + 1]
            self._merge("sweeps", detect_sweeps(visible, self.symbol, self.timeframe))
            self._merge("raids", detect_liquidity_raids(visible, self.symbol, self.timeframe))
            self._merge("structure_breaks", detect_structure_breaks(visible, self.symbol, self.timeframe))
            self._merge("fvgs", detect_fvg(visible, self.symbol, self.timeframe))
            self.next_index += 1

        snapshot_start = max(0, self.next_index - self.snapshot_candle_window)
        return PrimitiveSnapshot(
            symbol=self.symbol,
            timeframe=self.timeframe,
            candles=self.candles[snapshot_start : self.next_index],
            sweeps=_sorted_values(self.sweeps),
            raids=_sorted_values(self.raids),
            structure_breaks=_sorted_values(self.structure_breaks),
            fvgs=_sorted_values(self.fvgs),
        )

    def _merge(self, field_name: str, values: list[Any]) -> None:
        bucket = getattr(self, field_name)
        for item in values:
            bucket[_primitive_key(field_name, item)] = item
        _prune(bucket, self.max_primitives_per_field)


def diagnose_side(snapshot: PrimitiveSnapshot, side: str, config: ICT2022DiagnosticConfig) -> dict[str, int]:
    direction = "bullish" if side == "long" else "bearish"
    row = {stage: 0 for stage in STAGES}
    row["scan_side_bars"] = 1

    sweeps = sorted(
        [item for item in snapshot.sweeps + snapshot.raids if item.direction == direction],
        key=lambda item: item.timestamp,
        reverse=True,
    )
    if not sweeps:
        return row
    sweep = sweeps[0]
    row["latest_sweep"] = 1

    sweep_window = _matching_window(sweep.timestamp, config.session_windows)
    if config.require_killzone and sweep_window is None:
        return row
    row["sweep_session_gate"] = 1

    structures = sorted(
        [item for item in snapshot.structure_breaks if item.direction == direction and item.timestamp > sweep.timestamp],
        key=lambda item: item.timestamp,
    )
    if not structures:
        return row
    row["structure_after_sweep_any"] = 1

    body_structures = [item for item in structures if item.close_beyond_structure or not config.require_body_close]
    if not body_structures:
        return row
    row["structure_body_close"] = 1

    valid_structures = [
        item
        for item in body_structures
        if item.displacement_grade in {"valid", "strong"} or not config.require_displacement
    ]
    if not valid_structures:
        return row
    row["structure_valid_displacement"] = 1
    if any(item.displacement_grade == "strong" for item in valid_structures):
        row["structure_strong_displacement"] = 1

    config_structures = [
        item
        for item in valid_structures
        if item.displacement_grade == "strong" or not config.require_strong_displacement
    ]
    if not config_structures:
        return row
    structure = config_structures[0]
    row["structure_config_displacement"] = 1

    sweep_age = _bars_between(snapshot.candles, sweep.timestamp, structure.timestamp)
    if sweep_age is not None and sweep_age > config.max_sweep_age_bars:
        return row
    row["sweep_age_gate"] = 1

    structure_window = _matching_window(structure.timestamp, config.session_windows)
    if config.require_killzone and structure_window is None:
        return row
    row["structure_session_gate"] = 1

    if config.require_killzone and config.require_same_session and sweep_window != structure_window:
        return row
    row["same_session_sweep_mss"] = 1

    fvgs = [
        item
        for item in snapshot.fvgs
        if item.direction == direction and item.created_at >= structure.timestamp and not item.invalidated
    ]
    if not fvgs:
        return row
    row["active_fvg_after_mss"] = 1

    first_fvg = _evaluate_fvg_path(
        snapshot,
        fvgs[0],
        side,
        config,
        sweep,
        structure_window=structure_window,
        sweep_window=sweep_window,
    )
    for stage in FVG_PATH_STAGES:
        row[stage] = first_fvg[stage]

    any_fvg = _evaluate_any_fvg_path(
        snapshot,
        fvgs,
        side,
        config,
        sweep,
        structure_window=structure_window,
        sweep_window=sweep_window,
    )
    row["retested_eligible_fvg_any"] = any_fvg["retest_any"]
    row["retested_eligible_fvg_within_limit"] = any_fvg["retest_within_limit"]
    row["retested_eligible_fvg_session_gate"] = any_fvg["retest_session_gate"]
    row["target_open_until_retest_any_fvg"] = any_fvg["target_open_until_retest"]
    row["candidate_any_fvg"] = any_fvg["candidate"]
    return row


def _evaluate_any_fvg_path(
    snapshot: PrimitiveSnapshot,
    fvgs: list[Any],
    side: str,
    config: ICT2022DiagnosticConfig,
    sweep: Any,
    *,
    structure_window: str | None,
    sweep_window: str | None,
) -> dict[str, int]:
    aggregate = {stage: 0 for stage in FVG_PATH_STAGES}
    for fvg in fvgs:
        path = _evaluate_fvg_path(
            snapshot,
            fvg,
            side,
            config,
            sweep,
            structure_window=structure_window,
            sweep_window=sweep_window,
        )
        for stage in FVG_PATH_STAGES:
            aggregate[stage] = max(aggregate[stage], path[stage])
        if aggregate["candidate"]:
            break
    return aggregate


def _evaluate_fvg_path(
    snapshot: PrimitiveSnapshot,
    fvg: Any,
    side: str,
    config: ICT2022DiagnosticConfig,
    sweep: Any,
    *,
    structure_window: str | None,
    sweep_window: str | None,
) -> dict[str, int]:
    row = {stage: 0 for stage in FVG_PATH_STAGES}
    any_retest_idx = _first_retest_index(
        snapshot.candles,
        fvg.created_at,
        fvg.gap_low,
        fvg.gap_high,
        max(len(snapshot.candles), config.max_fvg_retest_bars),
    )
    if any_retest_idx is None:
        return row
    row["retest_any"] = 1

    retest_idx = _first_retest_index(
        snapshot.candles,
        fvg.created_at,
        fvg.gap_low,
        fvg.gap_high,
        config.max_fvg_retest_bars,
    )
    if retest_idx is None:
        return row
    row["retest_within_limit"] = 1

    retest = snapshot.candles[retest_idx]
    retest_window = _matching_window(int(retest["time"]), config.session_windows)
    if config.retest_must_occur_within_session and retest_window != (structure_window or sweep_window):
        return row
    row["retest_session_gate"] = 1

    ce = (fvg.gap_low + fvg.gap_high) / 2
    entry = fvg.gap_high if side == "long" and config.entry_mode == "edge" else fvg.gap_low if side == "short" and config.entry_mode == "edge" else ce
    stop = buffered_stop(side, sweep.wick_extreme, entry, config.stop_buffer_bps)
    target = nearest_liquidity_target(closed_candles(snapshot.candles), side, entry, stop)
    if _target_reached_before_retest(snapshot.candles, fvg.created_at, int(retest["time"]), side, target):
        return row
    row["target_open_until_retest"] = 1
    row["candidate"] = 1
    return row


def run_diagnostic(args: argparse.Namespace) -> list[dict[str, int | str]]:
    config = ICT2022DiagnosticConfig(
        session_windows=_window_list(args.ict2022_session_windows),
        max_fvg_retest_bars=args.ict2022_max_fvg_retest_bars,
        max_sweep_age_bars=args.ict2022_max_sweep_age_bars,
        require_displacement=args.ict2022_require_displacement,
        require_strong_displacement=args.ict2022_require_strong_displacement,
        require_body_close=args.ict2022_require_body_close,
        require_killzone=args.ict2022_require_killzone,
        require_same_session=args.ict2022_require_same_session,
        retest_must_occur_within_session=args.ict2022_retest_must_occur_within_session,
        entry_mode=args.entry_mode,
        stop_buffer_bps=args.stop_buffer_bps,
    )
    scan_windows = _window_list(args.scan_session_windows)
    totals: dict[tuple[str, str, str], Counter[str]] = defaultdict(Counter)

    for symbol in args.symbols:
        for timeframe in args.timeframes:
            candles = load_history_for(args.data_dir, symbol, timeframe)
            start_idx, end_idx = _date_scan_bounds(candles, args.warmup_bars, args.start_date, args.end_date)
            seed_idx = max(0, start_idx - args.seed_bars)
            accumulator = ICT2022DiagnosticAccumulator(
                symbol,
                timeframe,
                candles,
                start_index=seed_idx,
                detector_window=args.detector_window,
                snapshot_candle_window=args.snapshot_candle_window,
            )
            for idx in range(start_idx, end_idx):
                if scan_windows and not _scan_session_window_matches(candles, idx, scan_windows, args.scan_session_lag_bars):
                    continue
                snapshot = accumulator.snapshot_until(int(candles[idx]["time"]))
                for side in ("long", "short"):
                    key = (symbol, timeframe, side)
                    totals[key].update(diagnose_side(snapshot, side, config))

    rows: list[dict[str, int | str]] = []
    for (symbol, timeframe, side), counts in sorted(totals.items()):
        row: dict[str, int | str] = {"symbol": symbol, "timeframe": timeframe, "side": side}
        row.update({stage: counts.get(stage, 0) for stage in STAGES})
        rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        rows = run_diagnostic(args)
    except HistoricalDataError as exc:
        print(f"Error: {exc}")
        return 2
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / "ict2022_funnel.csv", rows)
    _write_report(out_dir / "report.md", rows, vars(args))
    print(f"ICT2022 diagnostic complete: rows={len(rows)} out_dir={out_dir}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bounded ICT2022 MSS+FVG frequency diagnostic.")
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--symbols", nargs="+", required=True)
    parser.add_argument("--timeframes", nargs="+", required=True)
    parser.add_argument("--start-date", default=None)
    parser.add_argument("--end-date", default=None)
    parser.add_argument("--warmup-bars", type=int, default=150)
    parser.add_argument("--seed-bars", type=int, default=1500)
    parser.add_argument("--detector-window", type=int, default=200)
    parser.add_argument("--snapshot-candle-window", type=int, default=1500)
    parser.add_argument("--entry-mode", choices=["edge", "ce"], default="edge")
    parser.add_argument("--stop-buffer-bps", type=float, default=2.0)
    parser.add_argument("--ict2022-session-windows", default="02:00-05:00,07:00-10:00,13:30-16:00")
    parser.add_argument("--ict2022-max-fvg-retest-bars", type=int, default=3)
    parser.add_argument("--ict2022-max-sweep-age-bars", type=int, default=20)
    parser.add_argument("--ict2022-require-displacement", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--ict2022-require-strong-displacement", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--ict2022-require-body-close", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--ict2022-require-killzone", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--ict2022-require-same-session", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--ict2022-retest-must-occur-within-session", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--scan-session-windows", default="02:00-05:00,07:00-10:00,13:30-16:00")
    parser.add_argument("--scan-session-lag-bars", type=int, default=0)
    parser.add_argument("--out-dir", default="backtest_results/ict2022_diagnostic")
    return parser


def _primitive_key(field_name: str, item: Any) -> tuple[Any, ...]:
    if field_name in {"sweeps", "raids"}:
        return (item.direction, item.timestamp, round(float(item.liquidity_level), 8), round(float(item.wick_extreme), 8))
    if field_name == "structure_breaks":
        return (item.break_type, item.direction, item.timestamp, round(float(item.broken_level), 8))
    if field_name == "fvgs":
        return (item.direction, item.created_at, round(float(item.gap_low), 8), round(float(item.gap_high), 8))
    return (repr(item),)


def _primitive_timestamp(item: Any) -> int:
    return int(getattr(item, "timestamp", None) or getattr(item, "created_at", None) or 0)


def _sorted_values(bucket: dict[tuple[Any, ...], Any]) -> list[Any]:
    return sorted(bucket.values(), key=_primitive_timestamp)


def _prune(bucket: dict[tuple[Any, ...], Any], max_items: int) -> None:
    if max_items <= 0 or len(bucket) <= max_items:
        return
    ordered = sorted(bucket, key=lambda key: _primitive_timestamp(bucket[key]))
    for key in ordered[: len(bucket) - max_items]:
        del bucket[key]


def _write_csv(path: Path, rows: list[dict[str, int | str]]) -> None:
    fields = ["symbol", "timeframe", "side", *STAGES]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_report(path: Path, rows: list[dict[str, int | str]], config: dict[str, Any]) -> None:
    lines = [
        "# ICT2022 MSS+FVG Frequency Diagnostic",
        "",
        "Diagnostic only. Counts rule-stage opportunities before event-study evaluation.",
        "`retest_*` and `candidate` use the current first-eligible-FVG policy.",
        "`*_any_fvg` fields are research attribution across eligible subsequent FVGs; they do not change detector behavior.",
        "",
        "## Config",
        f"- data_dir: {config.get('data_dir')}",
        f"- symbols: {', '.join(config.get('symbols') or [])}",
        f"- timeframes: {', '.join(config.get('timeframes') or [])}",
        f"- start_date: {config.get('start_date')}",
        f"- end_date: {config.get('end_date')}",
        f"- scan_session_windows: {config.get('scan_session_windows')}",
        f"- ict2022_session_windows: {config.get('ict2022_session_windows')}",
        f"- ict2022_max_fvg_retest_bars: {config.get('ict2022_max_fvg_retest_bars')}",
        f"- ict2022_require_killzone: {config.get('ict2022_require_killzone')}",
        f"- ict2022_require_same_session: {config.get('ict2022_require_same_session')}",
        f"- ict2022_require_strong_displacement: {config.get('ict2022_require_strong_displacement')}",
        f"- ict2022_retest_must_occur_within_session: {config.get('ict2022_retest_must_occur_within_session')}",
        "",
        "## Funnel",
        _markdown_table(rows),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _markdown_table(rows: list[dict[str, int | str]]) -> str:
    if not rows:
        return "_No rows._"
    headers = ["symbol", "timeframe", "side", *STAGES]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(header, "")) for header in headers) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
