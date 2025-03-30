import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from handlers import config

#variables de entorno
load_dotenv()
TOKEN = os.getenv("TU_TELEGRAM_TOKEN")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", config.start))
dispatcher.add_handler(CommandHandler("setdomain", config.set_domain))
dispatcher.add_handler(CommandHandler("settech", config.set_tech))

print("🤖 Bot iniciado... Esperando comandos.")
updater.start_polling()
updater.idle()

