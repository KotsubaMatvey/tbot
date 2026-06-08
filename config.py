import os
from dotenv import load_dotenv
from timeframes import EXECUTION_HTF_MAP, MODEL_3_HTF_MAP, MODEL_3_LTF_MAP, SUPPORTED_TIMEFRAMES

load_dotenv()


def _csv_env(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name)
    if not raw:
        return list(default)
    values = [item.strip() for item in raw.split(",") if item.strip()]
    return values or list(default)

# ── Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ── Binance Futures symbols
SYMBOLS = _csv_env("SYMBOLS", ["BTCUSDT", "ETHUSDT", "SOLUSDT"])

# ── Timeframes
TIMEFRAMES = [tf for tf in _csv_env("TIMEFRAMES", ["5m", "15m", "30m", "1h"]) if tf in SUPPORTED_TIMEFRAMES]
STRATEGY_TIMEFRAMES = [
    tf
    for tf in _csv_env("STRATEGY_TIMEFRAMES", ["1m", "3m", "5m", "15m", "30m", "1h", "4h"])
    if tf in SUPPORTED_TIMEFRAMES
]

# Entry model HTF/LTF behavior
REQUIRE_HTF_CONTEXT_FOR_ENTRY_MODELS = True
ENTRY_MODEL_HTF_MODE = os.getenv("ENTRY_MODEL_HTF_MODE", "strict")  # strict | soft | off
LIVE_MODEL_FILTER_CONFIG = os.getenv("LIVE_MODEL_FILTER_CONFIG", "configs/live_model_filters_2025.json")
DISPLACEMENT_MIN_BODY_RATIO = 0.55
DISPLACEMENT_MIN_RANGE_EXPANSION = 1.2
DISPLACEMENT_FVG_BONUS = 0.25
DISPLACEMENT_VALID_BODY_RATIO = 0.70
DISPLACEMENT_VALID_RANGE_EXPANSION = 1.5
DISPLACEMENT_STRONG_BODY_RATIO = 0.70
DISPLACEMENT_STRONG_RANGE_EXPANSION = 2.0
SWING_INTERMEDIATE_RANGE_MULT = 1.1
SWING_LONG_MIN_AGE_BARS = 20
EQ_TOLERANCE_BPS = 5
EQ_ATR_MULT = 0.10
MIN_EQ_TOUCHES = 2
MODEL3_FILL_THRESHOLD = 0.5
MODEL3_REACTION_BARS = 10
MODEL3_MIN_RR_TO_OBJECTIVE = 1.5
MIN_RISK_BPS = 5
STOP_BUFFER_BPS = 2
DEFAULT_STOP_MODE = "structural"
DEFAULT_MODEL3_STOP_MODE = "source_zone_extreme"
INVALIDATION_CONFIRMATION = "close"
MAX_SWEEP_TO_IFVG_BARS = 30
MIN_IFVG_RETEST_BARS = 1
MAX_IFVG_RETEST_BARS = 15
MAX_SETUP_AGE_BARS = 30
MAX_INVERSION_AGE_BARS = 40

# ── Candles to fetch
CANDLE_LIMIT = 500

# ── Scanner interval (seconds)
SCAN_INTERVAL = 60

# ── Digest interval (seconds) — 1 hour
DIGEST_INTERVAL = 3600

# ── CryptoBot
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN", "")

# ── Owner user IDs (permanent free access)
_owner_raw = os.getenv("OWNER_IDS", "")
OWNER_IDS = [int(x.strip()) for x in _owner_raw.split(",") if x.strip().isdigit()]

# ── Payment check interval (seconds)
PAYMENT_CHECK_INTERVAL = 30

# ── Insights channel
CHANNEL_ID = os.getenv("CHANNEL_ID", "")

# ── Welcome photo (absolute path; set env to "" to disable)
_default_photo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "welcome.jpg")
WELCOME_PHOTO = os.getenv("WELCOME_PHOTO", _default_photo)
