from telegram import Update
from telegram.ext import CallbackContext
from core import config_state

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🔍 Bienvenido al Leaked Bot.\nUsa /setdomain y /settech para comenzar.")

def set_domain(update: Update, context: CallbackContext):
    if context.args:
        config_state.target_domain = context.args[0]
        update.message.reply_text(f"✅ Dominio establecido: {config_state.target_domain}")
    else:
        update.message.reply_text("Uso correcto: /setdomain <dominio>")

def set_tech(update: Update, context: CallbackContext):
    if context.args:
        techs = " ".join(context.args)
        config_state.tech_keywords = [t.strip() for t in techs.replace(";", ",").split(",") if t.strip()]
        update.message.reply_text(f"✅ Tecnologías configuradas: {', '.join(config_state.tech_keywords)}")
    else:
        update.message.reply_text("Uso correcto: /settech <tech1, tech2, ...>")

