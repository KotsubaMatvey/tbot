from __future__ import annotations

import payment_flow
from database import get_user, is_subscribed, upsert_user
from keyboards import build_toggle_keyboard
from scanner import STRATEGY_PATTERNS

from .common import user_ready

TRADING_PREFIX = "trade_model"


def trading_keyboard(selected: set[str]):
    return build_toggle_keyboard(STRATEGY_PATTERNS, selected, TRADING_PREFIX)


async def trading_cmd(update, context) -> None:
    user_id = update.effective_user.id
    if not is_subscribed(user_id):
        await payment_flow.send_payment_screen(user_id, context, update, expired=True)
        return
    user = get_user(user_id)
    if not user_ready(user):
        await update.message.reply_text("Setup is not finished yet. Send /start or /reset.")
        return
    await update.message.reply_text(
        "Trading Strategies\n\nSelect strategy alerts:",
        reply_markup=trading_keyboard(set(user["entry_models"])),
    )


async def handle_trading_callback(user_id: int, data: str, query, context) -> bool:
    if not data.startswith(f"{TRADING_PREFIX}_"):
        return False
    if not is_subscribed(user_id):
        await query.answer("Subscription required", show_alert=True)
        return True
    user = get_user(user_id)
    if not user_ready(user):
        await query.answer("Finish setup first", show_alert=True)
        return True

    item = data[len(TRADING_PREFIX) + 1 :]
    selected = set(user["entry_models"])
    if item == "CONFIRM":
        await query.answer("Trading strategies saved")
        await query.edit_message_text("Trading strategies saved.")
        return True
    if item not in STRATEGY_PATTERNS:
        await query.answer("Unknown strategy", show_alert=True)
        return True

    if item in selected:
        if len(selected) <= 1:
            await query.answer("Select at least one strategy", show_alert=True)
            return True
        selected.remove(item)
    else:
        selected.add(item)
    upsert_user(user_id, entry_models=sorted(selected))
    await query.answer("Saved")
    await query.edit_message_reply_markup(trading_keyboard(selected))
    return True


__all__ = ["handle_trading_callback", "trading_cmd", "trading_keyboard"]
