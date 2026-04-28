"""Chart generation for primitive and strategy alerts."""
from __future__ import annotations

import asyncio
import io
import logging

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

from presentation.chart_payloads import visible_alerts_for_chart
from presentation.types import AlertPayload

logger = logging.getLogger(__name__)

_BACKGROUND = "#f0f0f0"
_GRID = "#cfcfcf"
_TEXT = "#3b3b3d"
_BULL = "#39ADA2"
_BEAR = "#2f2f31"
_BULL_VOLUME = "#afd6db"
_BEAR_VOLUME = "#c9cdce"
_BULL_VOLUME_EDGE = "#4b9fb0"
_BEAR_VOLUME_EDGE = "#8c99a3"
_PRICE_LABEL = "#e85a54"
_BULL_ZONE_FILL = "#39ADA2"
_BULL_ZONE_LINE = "#4b9fb0"
_BEAR_ZONE_FILL = "#b4b0b2"
_BEAR_ZONE_LINE = "#7b7679"
_INVALIDATION = "#8c99a3"
_ZONE_ALPHA = 0.16
_LABEL_ALPHA = 0.10

_ELEMENT_COLORS = {
    "FVG": {"bull": ("#00D084", "#1DE9A6"), "bear": ("#FF4D5E", "#FF7A86")},
    "IFVG": {"bull": ("#8E44FF", "#B084FF"), "bear": ("#6D28D9", "#A78BFA")},
    "OB": {"bull": ("#2F80ED", "#56CCF2"), "bear": ("#1F5FBF", "#7FB3FF")},
    "Breaker": {"bull": ("#FF8A00", "#FFB020"), "bear": ("#D66A00", "#FF9F43")},
    "BB": {"bull": ("#FF8A00", "#FFB020"), "bear": ("#D66A00", "#FF9F43")},
    "Rejection": {"bull": ("#FFD43B", "#FFE66D"), "bear": ("#DFAF00", "#FFD43B")},
    "RB": {"bull": ("#FFD43B", "#FFE66D"), "bear": ("#DFAF00", "#FFD43B")},
    "turtle_soup": {"bull": ("#00C2FF", "#66E3FF"), "bear": ("#0096C7", "#48CAE4")},
    "Turtle Soup": {"bull": ("#00C2FF", "#66E3FF"), "bear": ("#0096C7", "#48CAE4")},
    "silver_bullet": {"bull": ("#FF4FD8", "#FF8BE8"), "bear": ("#C026D3", "#E879F9")},
    "Silver Bullet": {"bull": ("#FF4FD8", "#FF8BE8"), "bear": ("#C026D3", "#E879F9")},
    "ifvg_retest": {"bull": ("#8E44FF", "#B084FF"), "bear": ("#6D28D9", "#A78BFA")},
    "breaker_block": {"bull": ("#FF8A00", "#FFB020"), "bear": ("#D66A00", "#FF9F43")},
    "reclaimed_ob": {"bull": ("#2F80ED", "#56CCF2"), "bear": ("#1F5FBF", "#7FB3FF")},
    "ict2022_mss_fvg": {"bull": ("#22C55E", "#86EFAC"), "bear": ("#EF4444", "#FCA5A5")},
}

_STYLE = mpf.make_mpf_style(
    base_mpf_style="default",
    marketcolors=mpf.make_marketcolors(
        up=_BULL,
        down=_BEAR,
        wick={"up": _BULL, "down": _BEAR},
        edge={"up": _BULL, "down": _BEAR},
        volume={"up": _BULL_VOLUME, "down": _BEAR_VOLUME},
        ohlc={"up": _BULL, "down": _BEAR},
    ),
    facecolor=_BACKGROUND,
    figcolor=_BACKGROUND,
    gridstyle="dotted",
    gridcolor=_GRID,
    rc={
        "font.family": "DejaVu Sans",
        "axes.edgecolor": _BACKGROUND,
        "axes.labelcolor": _TEXT,
        "axes.titlecolor": _TEXT,
        "xtick.color": _TEXT,
        "ytick.color": _TEXT,
        "figure.facecolor": _BACKGROUND,
        "axes.facecolor": _BACKGROUND,
        "grid.alpha": 0.9,
        "grid.linewidth": 0.5,
        "axes.grid": True,
    },
)

_CANDLE_COUNT = {"1m": 150, "3m": 140, "5m": 120, "15m": 96, "30m": 84, "1h": 72, "4h": 60, "1d": 45}


def _to_df(candles: list[dict], timeframe: str) -> pd.DataFrame:
    raw = candles[-_CANDLE_COUNT.get(timeframe, 60) :]
    frame = pd.DataFrame(raw)
    frame["time"] = pd.to_datetime(frame["time"], unit="ms", utc=True)
    frame = frame.set_index("time")
    frame.columns = [name.capitalize() for name in frame.columns]
    return frame[["Open", "High", "Low", "Close", "Volume"]].astype(float)


def _datetime_format(timeframe: str) -> str:
    if timeframe == "1d":
        return "%Y-%m-%d"
    if timeframe in {"30m", "1h", "4h"}:
        return "%m-%d %H:%M"
    return "%H:%M"


def _direction_is_bullish(alert: AlertPayload) -> bool:
    direction = (alert.trade_direction or alert.direction or "").lower()
    return direction.startswith("long") or direction.startswith("bull")


def _zone_colors(alert: AlertPayload) -> tuple[str, str, float]:
    key = "bull" if _direction_is_bullish(alert) else "bear"
    palette = _ELEMENT_COLORS.get(alert.pattern)
    if palette is None and alert.pattern.startswith("legacy_"):
        palette = _ELEMENT_COLORS.get("ict2022_mss_fvg")
    if palette is not None:
        fill, line = palette[key]
        return fill, line, _ZONE_ALPHA if alert.alert_kind == "strategy" else 0.12
    if _direction_is_bullish(alert):
        return _BULL_ZONE_FILL, _BULL_ZONE_LINE, 0.14 if alert.alert_kind == "strategy" else 0.10
    return _BEAR_ZONE_FILL, _BEAR_ZONE_LINE, 0.16 if alert.alert_kind == "strategy" else 0.11


def _draw_patterns(ax, frame: pd.DataFrame, patterns: list[AlertPayload], n: int) -> None:
    for pattern in patterns:
        if pattern.alert_kind == "strategy":
            _draw_setup(ax, frame, pattern, n)
            continue

        if pattern.pattern in {"FVG", "IFVG"} and pattern.gap_low is not None and pattern.gap_high is not None:
            fill_color, line_color, alpha = _zone_colors(pattern)
            ax.axhspan(pattern.gap_low, pattern.gap_high, color=fill_color, alpha=alpha, zorder=1, linewidth=0)
            ax.axhline(pattern.gap_low, color=line_color, linestyle=":", linewidth=0.8, alpha=0.9)
            ax.axhline(pattern.gap_high, color=line_color, linestyle=":", linewidth=0.8, alpha=0.9)
            _zone_tag(ax, n, (pattern.gap_low + pattern.gap_high) / 2, pattern.pattern, line_color)
            continue

        if pattern.pattern in {"OB", "Breaker"} and pattern.ob_low is not None and pattern.ob_high is not None:
            fill_color, line_color, alpha = _zone_colors(pattern)
            ax.axhspan(pattern.ob_low, pattern.ob_high, color=fill_color, alpha=alpha, zorder=1, linewidth=0)
            ax.axhline(pattern.ob_low, color=line_color, linestyle=":", linewidth=0.8, alpha=0.9)
            ax.axhline(pattern.ob_high, color=line_color, linestyle=":", linewidth=0.8, alpha=0.9)
            _zone_tag(ax, n, (pattern.ob_low + pattern.ob_high) / 2, pattern.pattern, line_color)
            continue

        if pattern.level is None:
            continue
        line_color = _BULL_ZONE_LINE if _direction_is_bullish(pattern) else _BEAR_ZONE_LINE
        ax.axhline(pattern.level, color=line_color, linewidth=0.8, alpha=0.85, linestyle=":")
        _zone_tag(ax, n, pattern.level, pattern.pattern, line_color, va="bottom")


def _draw_setup(ax, frame: pd.DataFrame, pattern: AlertPayload, n: int) -> None:
    if pattern.entry_low is None or pattern.entry_high is None:
        return

    _draw_htf_zone(ax, pattern, n)
    fill_color, line_color, alpha = _zone_colors(pattern)
    ax.axhspan(pattern.entry_low, pattern.entry_high, color=fill_color, alpha=alpha, zorder=1, linewidth=0)
    ax.axhline(pattern.entry_low, color=line_color, linestyle=":", linewidth=0.9, alpha=0.95)
    ax.axhline(pattern.entry_high, color=line_color, linestyle=":", linewidth=0.9, alpha=0.95)
    _draw_entry_marker(ax, frame, pattern)

    if pattern.invalidation is not None:
        ax.axhline(pattern.invalidation, color=_INVALIDATION, linestyle="--", linewidth=0.8, alpha=0.9)
    if pattern.sweep_level is not None:
        ax.axhline(pattern.sweep_level, color=_BEAR_ZONE_LINE if _direction_is_bullish(pattern) else _BULL_ZONE_LINE, linestyle="-.", linewidth=0.7, alpha=0.7)
    if pattern.structure_level is not None:
        ax.axhline(pattern.structure_level, color=line_color, linestyle="-.", linewidth=0.7, alpha=0.75)


def _draw_entry_marker(ax, frame: pd.DataFrame, pattern: AlertPayload) -> None:
    index = _entry_index(frame, pattern)
    if index is None:
        return
    candle = frame.iloc[index]
    price_range = max(float(frame["High"].max() - frame["Low"].min()), 1e-9)
    offset = price_range * 0.025
    if _direction_is_bullish(pattern):
        ax.scatter(index, float(candle["Low"]) - offset, marker="^", s=42, color="#16a34a", edgecolors="white", linewidths=0.45, zorder=6)
    else:
        ax.scatter(index, float(candle["High"]) + offset, marker="v", s=42, color="#dc2626", edgecolors="white", linewidths=0.45, zorder=6)


def _entry_index(frame: pd.DataFrame, pattern: AlertPayload) -> int | None:
    entry_time = pattern.metadata.get("entry_time") or pattern.timestamp
    try:
        entry_ts = pd.to_datetime(int(entry_time), unit="ms", utc=True)
    except (TypeError, ValueError):
        return None
    matches = frame.index.get_indexer([entry_ts], method="nearest")
    if len(matches) == 0 or matches[0] < 0:
        return None
    return int(matches[0])


def _draw_htf_zone(ax, pattern: AlertPayload, n: int) -> None:
    low = pattern.metadata.get("htf_zone_low")
    high = pattern.metadata.get("htf_zone_high")
    zone_type = pattern.metadata.get("htf_zone_type")
    if low is None or high is None or zone_type in {None, "None"}:
        return
    try:
        low_f = float(low)
        high_f = float(high)
    except (TypeError, ValueError):
        return
    fill_color, line_color, _ = _zone_colors(pattern)
    ax.axhspan(low_f, high_f, color=fill_color, alpha=0.055, zorder=0, linewidth=0)
    ax.axhline(low_f, color=line_color, linestyle="-", linewidth=0.55, alpha=0.45)
    ax.axhline(high_f, color=line_color, linestyle="-", linewidth=0.55, alpha=0.45)
    _zone_tag(ax, n, (low_f + high_f) / 2, f"HTF {zone_type}", line_color)


def _zone_tag(ax, n: int, level: float, text: str, color: str, *, va: str = "center") -> None:
    ax.text(
        n - 0.8,
        level,
        f" {text} ",
        ha="right",
        va=va,
        color=color,
        fontsize=6.0,
        bbox={
            "boxstyle": "round,pad=0.18",
            "facecolor": (*matplotlib.colors.to_rgb(color), _LABEL_ALPHA),
            "edgecolor": color,
            "linewidth": 0.45,
        },
    )


def _draw_price_label(ax, frame: pd.DataFrame) -> None:
    last_close = frame["Close"].iloc[-1]
    ax.annotate(
        f" {last_close:,.1f} ",
        xy=(len(frame) - 0.45, last_close),
        ha="left",
        va="center",
        fontsize=8,
        color="white",
        bbox={"boxstyle": "round,pad=0.28", "facecolor": _PRICE_LABEL, "edgecolor": "none"},
    )


def _style_axes(price_ax, volume_ax) -> None:
    for axis in (price_ax, volume_ax):
        axis.set_facecolor(_BACKGROUND)
        axis.grid(True, linestyle=":", linewidth=0.5, color=_GRID)
        for spine in axis.spines.values():
            spine.set_visible(False)
        axis.tick_params(axis="both", colors=_TEXT, labelsize=8, length=0)


def _style_volume_bars(volume_ax, frame: pd.DataFrame) -> None:
    for patch, candle in zip(volume_ax.patches, frame.itertuples()):
        is_bull = candle.Close >= candle.Open
        patch.set_facecolor(_BULL_VOLUME if is_bull else _BEAR_VOLUME)
        patch.set_edgecolor(_BULL_VOLUME_EDGE if is_bull else _BEAR_VOLUME_EDGE)
        patch.set_linewidth(0.35)


def _render(frame: pd.DataFrame, patterns: list[AlertPayload], symbol: str, timeframe: str) -> io.BytesIO:
    fig, axes = mpf.plot(
        frame,
        type="candle",
        style=_STYLE,
        volume=True,
        volume_panel=1,
        panel_ratios=(5, 1),
        returnfig=True,
        figsize=(12.4, 6.1),
        tight_layout=True,
        xrotation=0,
        datetime_format=_datetime_format(timeframe),
        scale_padding={"left": 0.08, "right": 1.1, "top": 0.22, "bottom": 0.35},
    )
    price_ax = axes[0]
    volume_ax = axes[2]
    visible_patterns = visible_alerts_for_chart(
        [{"low": float(row["Low"]), "high": float(row["High"])} for _, row in frame.iterrows()],
        patterns,
    )
    if visible_patterns:
        _draw_patterns(price_ax, frame, visible_patterns, len(frame))
    _draw_price_label(price_ax, frame)
    _style_axes(price_ax, volume_ax)
    _style_volume_bars(volume_ax, frame)
    price_ax.set_title(f"{symbol}  {timeframe}", loc="left", fontsize=10, color=_TEXT, pad=8, fontweight="normal")
    price_ax.set_ylabel("")
    volume_ax.set_ylabel("")

    buffer = io.BytesIO()
    fig.patch.set_facecolor(_BACKGROUND)
    fig.savefig(buffer, format="png", dpi=130, bbox_inches="tight", facecolor=_BACKGROUND)
    buffer.seek(0)
    plt.close(fig)
    return buffer


async def generate_chart(candles: list[dict], patterns: list[AlertPayload], symbol: str, timeframe: str) -> io.BytesIO | None:
    if not candles:
        return None
    try:
        frame = _to_df(candles, timeframe)
        return await asyncio.to_thread(_render, frame, patterns or [], symbol, timeframe)
    except Exception as exc:
        logger.error("generate_chart %s %s: %s", symbol, timeframe, exc)
        return None


__all__ = ["generate_chart"]
