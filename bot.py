import telebot
import threading
import time

# Bot tokenini shu joyga yoz
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

def reminder_thread(chat_id, delay, message):
    time.sleep(delay)
    bot.send_message(chat_id, f"🔔 Eslatma: {message}")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "👋 Salom! Men Detective Mafia uchun eslatma botman.\n"
                                      "Vaqt belgilash uchun quyidagini yozing:\n\n"
                                      "/remind <soniya> <xabar>\n\n"
                                      "Masalan: /remind 30 O'yin boshlanadi!")

@bot.message_handler(commands=['remind'])
def remind_message(message):
    try:
        parts = message.text.split(' ', 2)
        delay = int(parts[1])
        msg = parts[2]
        chat_id = message.chat.id
        bot.send_message(chat_id, f"⏳ {delay} soniyadan so‘ng eslatma yuboraman.")
        threading.Thread(target=reminder_thread, args=(chat_id, delay, msg)).start()
    except:
        bot.send_message(message.chat.id, "❌ Foydalanish: /remind <soniya> <xabar>")

bot.polling()
