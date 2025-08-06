from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройки бота
TOKEN = "8461499184:AAHYdJpKjBkjvZC6A1LArP2f02Rmpepr7lQ"
ADMIN_ID = 6576936069

# Тексты команд (можно менять здесь)
START_TEXT = "Barev es @aseennq aliqi botnem"
IDEA_THANKS = "Mersi mtqi hamar🤍"
IDEA_NO_TEXT = "Пожалуйста, напиши идею после команды, например:\n/mtqer моя идея"
IDEA_FORWARD_PREFIX = "Новая идея от"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)

async def mtqer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        idea_text = " ".join(context.args)
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"{IDEA_FORWARD_PREFIX} @{update.effective_user.username}:\n{idea_text}"
        )
        await update.message.reply_text(IDEA_THANKS)
    else:
        await update.message.reply_text(IDEA_NO_TEXT)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("mtqer", mtqer))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
