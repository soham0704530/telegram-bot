from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application

from bot.utils import send_typing_action

@send_typing_action
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the bot! Use /help to see available commands."
    )

@send_typing_action
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Available commands:\n"
        "/start - Welcome message\n"
        "/help - List commands"
    )

def setup_handlers(application: Application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
