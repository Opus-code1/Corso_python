"""
Bot Telegram essenziale con tre comandi.

Dipendenza: pip install python-telegram-bot
Avvio (PowerShell): $env:TELEGRAM_BOT_TOKEN="token"; python ai.py
"""

import os
import random
from datetime import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	"""Prima funzione: presenta il bot e i suoi comandi."""
	await update.effective_message.reply_text(
		"Ciao! Sono il tuo bot. Prova /ora oppure /moneta."
	)

async def ora(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	"Seconda funzione: mostra l'ora locale."
	ora_locale = datetime.now().astimezone().strftime("%H:%M:%S")
	await update.effective_message.reply_text(f"Ora locale: {ora_locale}")

async def moneta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	"""Terza funzione: lancia una moneta."""
	await update.effective_message.reply_text(
		f"È uscito: {random.choice(('Testa', 'Croce'))}!"
	)

def main() -> None:
	token = os.getenv("TELEGRAM_BOT_TOKEN")
	if not token:
		raise SystemExit(
			"Token mancante: imposta la variabile TELEGRAM_BOT_TOKEN con il token di BotFather."
		)

	app = Application.builder().token(token).build()
	app.add_handler(CommandHandler("start", start))
	app.add_handler(CommandHandler("ora", ora))
	app.add_handler(CommandHandler("moneta", moneta))
	app.run_polling()


if __name__ == "__main__":
	main()
