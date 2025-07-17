import os
import telebot
from telebot import types
import firebase_admin
from firebase_admin import credentials, db
from keep_alive import keep_alive

# Token do bot
TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Inicializar Firebase
cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ngomany-eeec0-default-rtdb.firebaseio.com/'
})

def get_user_ref(user_id):
    return db.reference(f"users/{user_id}")

@bot.message_handler(commands=['start'])
def start(msg):
    uid = msg.from_user.id
    ref = get_user_ref(uid)
    if not ref.get():
        ref.set({
            'saldo_ango': 0.0,
            'saldo_dolar': 0.0
        })
    bot.reply_to(msg, "🎰 Bem-vindo ao Cassino ANGO!")

# Ativa webserver do keep_alive
keep_alive()

# Inicia o bot
bot.polling(non_stop=True)

