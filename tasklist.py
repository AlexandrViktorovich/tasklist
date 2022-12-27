from datetime import datetime
import os
import psutil
import telebot
import OPi.GPIO as GPIO


key = ''

bot = telebot.TeleBot(key, parse_mode=None)

PORT=5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT,GPIO.out)
print('start input and output')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = telebot.types.KeyboardButton('Включить лампочку')
    item2 = telebot.types.KeyboardButton('Выключить лампочку')
    markup.add(item1,item2)
    
    bot.send_message(message.chat.id,f'Добро пожаловать',reply_markup = markup)
    
@bot.message_handler(content_types=['text'])
def message_bot(message):
    now = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    if message.text=='Включить лампочку':
        
        GPIO.output(PORT,GPIO.LOW)
        bot.send_message(message.chat.id, "Лампочка успешно включена")

    elif message.text == 'Выключить лампочку':

        GPIO.output(PORT,GPIO.HIGH)
        bot.send_message(message.chat.id, "Лампочка успешно выключена")


bot.infinity_polling(none_stop=True,interval=0)

