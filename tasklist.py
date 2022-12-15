from datetime import datetime
import os
import psutil
import telebot

key = '5812992790:AAGmAYiCh5ftUF5qBdeaLHc-clf3PhnYgmM'

bot = telebot.TeleBot(key, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = telebot.types.KeyboardButton('Список процессов')
    item2 = telebot.types.KeyboardButton('Проверка процессов')
    item3 = telebot.types.KeyboardButton('Завершение процесса')
    item4 = telebot.types.KeyboardButton('Завершение работы')
    markup.add(item1,item2,item3,item4)
    
    bot.send_message(message.chat.id,f'Добро пожаловать',reply_markup = markup)
    
   

