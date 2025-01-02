from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv("7802166659:AAFTzQphGhKhimOHx_KoTT0NkskjwOedBck")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Halo, saya adalah bot Anda!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Kamu berkata: {update.message.text}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
