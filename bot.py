from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '8336262442:AAEFGhSgf03ulR_lOBMAtNkxM1gR1G2SP58'
GROUP_CHAT_ID = -1002906668663  # <-- metti qui l'ID del gruppo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(
        f"Ciao {user}! 👋\n La sua foto verrà valutata dal nostro team di esperti."
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file_id = photo.file_id

    # Inoltra la foto al gruppo
    await context.bot.send_photo(chat_id=GROUP_CHAT_ID, photo=file_id)

    # Conferma all’utente
    await update.message.reply_text("📸 Foto inviata al nostro gruppo di esperti! Gloria al circolino!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

print("🤖 Bot avviato! Aspettando messaggi...")
app.run_polling()
