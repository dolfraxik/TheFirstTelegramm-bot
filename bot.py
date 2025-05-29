import telebot
from telebot import types



bot = telebot.TeleBot("7452479396:AAEcCgB0J01ROZbK1E96Gu2cxTs9OBn_yDs")

@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <u>{message.from_user.first_name}</u> <b>{message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(func=lambda message: True)
def get_user_text(message):
    if message.text == '/привет':
        bot.send_message(message.chat.id, text="Приветствую", parse_mode='html')
    elif message.text == "id":
       bot.send_message(message.chat.id, text=f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('icon.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'video':
        video = open('Short.mp4', 'rb')
        bot.send_video(message.chat.id, video, timeout=60)
    else:
        bot.send_message(message.chat.id, text="Я тебя не понимаю", parse_mode='html')
@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://chatgpt.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

bot.polling(none_stop=True)