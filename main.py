import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from bot.handlers import setup_handlers

def main():
    # Load environment variables
    load_dotenv()
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN is missing in environment variables.")

    # Logging configuration
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Create application
    application = ApplicationBuilder().token(token).build()

    # Register handlers
    setup_handlers(application)

    # Start polling
    application.run_polling()
