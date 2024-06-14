from telegram import Bot
from telegram.ext import Updater, MessageHandler, filters,Application
import asyncio

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = '7311342048:AAFvXN29Dabf9wX0BSxOh3kMfdv_M1mzm6U'

# Initialize the bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Define a function to handle incoming messages
async def handle_message(update, context):
    chat_id = update.message.chat_id
    print(f"Your Chat ID: {chat_id}")
    await update.message.reply_text(f"Your Chat ID: {chat_id}")

# Set up the Updater and Dispatcher
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Add a handler for messages
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Start the bot
application.run_polling()


