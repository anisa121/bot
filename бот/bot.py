# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
import telebot
import constant
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1090577355:AAEDIL8jvU_CTM9CkZKCuE07-rYtZSO_JN0') # Токен API к Telegram
# dispatcher = updater.dispatcher
@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True  )
    user_markup.row('/stop')
    user_markup.row('Ресурсы', 'Deads')
    bot.send_message(message.from_user.id, 'Your Welcome!', reply_markup=user_markup)

# @bot.message_handler(commands=['stop'])
# def start_message(message):
#     directory = 'google.com'
#     # hide_makrup = telebot.types.
#     bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)


def ret_info():
    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find('div', {'class' : 'maincounter-number'}).text


def farm_data():
    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find('div', {'class' : 'content-inner'}, 'div', {'id' : 'maincounter-wrap'}).text

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'deads':
        bot.send_message(message.chat.id, farm_data())
    if message.text.lower() == 'ресурсы':
        bot.send_message(message.chat.id, ret_info())
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling(none_stop=True)

# Обработка команд
# def startCommand(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')

# Хендлеры
# start_command_handler = CommandHandler('start', startCommand)
# text_message_handler = MessageHandler(Filters.text, textMessage)
# # Добавляем хендлеры в диспетчер
# dispatcher.add_handler(start_command_handler)
# dispatcher.add_handler(text_message_handler)
# # Начинаем поиск обновлений
# updater.start_polling(clean=True)
# # Останавливаем бота, если были нажаты Ctrl + C
# updater.idle()