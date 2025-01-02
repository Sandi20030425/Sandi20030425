from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7802166659:AAFTzQphGhKhimOHx_KoTT0NkskjwOedBck"

# Fungsi yang akan dijalankan ketika bot menerima perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Halo, saya bot! Ada yang bisa saya bantu?")

# Fungsi utama untuk menjalankan bot
def main():
    # Membuat aplikasi bot menggunakan token
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Mulai bot
    application.run_polling()

if __name__ == "__main__":
    main()
