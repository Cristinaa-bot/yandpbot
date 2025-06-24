from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import logging

logging.basicConfig(level=logging.INFO)
TOKEN = "YOUR_TOKEN"

# Профили (в памяти)
profiles = []

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Benvenuto nel bot Y&P! Usa /newprofile per iniziare.")

async def new_profile(update: Update, context: CallbackContext):
    await update.message.reply_text("Invia le foto (max 5), poi manda descrizione in 7 linee:
Nome
Età
Città
Nazionalità
Date
Descrizione
WhatsApp")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newprofile", new_profile))
    app.run_polling()

if __name__ == "__main__":
    main()