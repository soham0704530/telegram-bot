from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes

def send_typing_action(func):
    """Sends typing action while processing command."""
    @wraps(func)
    async def command_func(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        return await func(update, context, *args, **kwargs)
    return command_func
