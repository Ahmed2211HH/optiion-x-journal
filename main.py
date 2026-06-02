from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 أهلاً بك في OPTION X Journal\n\n"
        "استخدم /help لمعرفة الأوامر."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n/help\n/stats"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 لا توجد صفقات مسجلة حالياً."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("stats", stats))

print("OPTION X Journal Running...")

app.run_polling()
