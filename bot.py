"""Application entrypoint."""
from __future__ import annotations

import atexit
import logging
import os
import time
from pathlib import Path

from telegram import Update
from telegram.error import NetworkError, TimedOut
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters

from config import TELEGRAM_BOT_TOKEN
from database import init_db
from handlers import (
    callback_handler,
    chart_cmd,
    charts_cmd,
    help_cmd,
    menu_button_handler,
    reset,
    resume_cmd,
    session_status_cmd,
    sessions_cmd,
    start,
    status_cmd,
    stop_cmd,
    zones_cmd,
)
from payment_flow import pay_cmd
from scheduler import post_init, validate_config

APP_DIR = Path(__file__).resolve().parent
PID_FILE = APP_DIR / "logs" / "bot.pid"


class _SensitiveTokenFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        token = TELEGRAM_BOT_TOKEN
        if token:
            message = record.getMessage()
            if token in message:
                record.msg = message.replace(token, "<telegram-token>")
                record.args = ()
        return True


def _configure_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger().addFilter(_SensitiveTokenFilter())
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def _write_pid_file() -> None:
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()), encoding="utf-8")
    atexit.register(lambda: PID_FILE.unlink(missing_ok=True))


_configure_logging()
logger = logging.getLogger(__name__)


def _build_application() -> Application:
    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    app.add_handler(CommandHandler("start",      start))
    app.add_handler(CommandHandler("pay",        pay_cmd))
    app.add_handler(CommandHandler("reset",      reset))
    app.add_handler(CommandHandler("stop",       stop_cmd))
    app.add_handler(CommandHandler("resume",     resume_cmd))
    app.add_handler(CommandHandler("status",     status_cmd))
    app.add_handler(CommandHandler("zones",      zones_cmd))
    app.add_handler(CommandHandler("help",       help_cmd))
    app.add_handler(CommandHandler("session",    session_status_cmd))
    app.add_handler(CommandHandler("chart",      chart_cmd))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_button_handler))
    return app


def main():
    init_db()
    validate_config()
    _write_pid_file()
    while True:
        app = _build_application()
        try:
            logger.info("Bot started")
            app.run_polling(allowed_updates=Update.ALL_TYPES)
            return
        except (TimedOut, NetworkError) as exc:
            logger.warning("Telegram polling startup/network error: %s. Retrying in 15s", exc)
            time.sleep(15)


if __name__ == "__main__":
    main()
