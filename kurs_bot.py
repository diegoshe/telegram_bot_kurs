import config
from parser import get_data_sort, format_data_list, format_data_str, parse_website

import telebot
from telebot import TeleBot, types

bot = TeleBot(config.TOKEN)



@bot.message_handler(comands=['/start'])
def welcome(message):
    user_name = message.from_user.first_name
    bot_name = bot.get_me().first_name

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Курс всех банков')
    button2 = types.KeyboardButton('Выгодно продать')
    button3 = types.KeyboardButton('Выгодно купить')

    markup.add(button1)
    markup.add(button2, button3)

    bot.send_message(message.chat.id, f"Добро пожаловать, {user_name}!\nЯ - <b>{bot_name}</b>, бот следящий за курсом $ в Минске!",
    parse_mode='html', reply_markup=markup)

    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Курс всех банков':
            data = parse_website()
            result = format_data_str(data, message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        elif message.text == 'Выгодно продать':
            data = get_data_sort(message.text)
            result = format_data_str(data, message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        elif message.text == 'Выгодно купить':
            data = get_data_sort(message.text)
            result = format_data_str(data,message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        else:
            welcome(message)

# RUN
bot.polling(none_stop=True)