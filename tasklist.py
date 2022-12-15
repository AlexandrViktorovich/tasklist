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
    
@bot.message_handler(content_types=['text'])
def message_bot(message):
    now = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    if message.text=='Список процессов':
        process_data = [x.name() for x in psutil.process_iter()]
        global tmp
        tmp = ''

        for i in process_data:
            tmp = tmp + i + "\n"
        bot.send_message(message.chat.id, tmp)

    elif message.text == 'Проверка процессов':
        global new_proc
        new_proc = ''
        global l
        l = []

        for i in psutil.process_iter():
            if i.name() not in tmp and i.name() != 'sppsvc.exe':
                new_proc = i.name()
                l.append(new_proc)
                bot.send_message(message.chat.id,f'Запущен процесс {i.name()} в {datetime.today().strftime("%d/%m/%Y %H:%M:%S")}')

    elif message.text == 'Завершение процесса':

        print(l)
        for i in psutil.process_iter() :
            if i.name() in l:
                try:
                    i.kill()
                finally:
                    bot.send_message(message.chat.id, f'Завершен процесс {i.name()} в {datetime.today().strftime("%d/%m/%Y %H:%M:%S")}')

    elif message.text == 'Завершение работы':
        #os.system("shutdown /s /t 1")
        bot.send_message(message.chat.id,f'Завершение работы компьютера в {datetime.today().strftime("%d/%m/%Y %H:%M:%S")}')


bot.infinity_polling(none_stop=True,interval=0)

