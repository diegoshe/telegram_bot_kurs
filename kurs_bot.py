import config
from main import format_data_list, format_data_str, creat_user_bd
from branch import *

import telebot
from telebot import TeleBot, types
from pprint import pformat, pprint

bot = TeleBot(config.TOKEN)



@bot.message_handler(comands=['/start'])
def welcome(message):
    user_name = message.from_user.first_name
    bot_name = bot.get_me().first_name
    creat_user_bd(message)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Курс всех банков')
    button2 = types.KeyboardButton('Выгодно продать')
    button3 = types.KeyboardButton('Выгодно купить')
    button4 = types.KeyboardButton('Контакты отделений')

    markup.add(button1)
    markup.add(button2, button3)
    markup.add(button4)

    bot.send_message(message.chat.id, f"Добро пожаловать, {user_name}!\nЯ - <b>{bot_name}</b>, бот следящий за курсом $ в Минске!",
    parse_mode='html', reply_markup=markup)

    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands = ['url'])
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Курс всех банков':
            data = format_data_list(message.text)
            result = format_data_str(data, message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        elif message.text == 'Выгодно продать':
            data = format_data_list(message.text)
            result = format_data_str(data, message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        elif message.text == 'Выгодно купить':
            data = format_data_list(message.text)
            result = format_data_str(data,message.text)
            bot.send_message(message.chat.id, f'{result}', parse_mode='html')
        elif message.text == 'Контакты отделений':

            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton('Абсолютбанк', URL_ABSOLUTBANK)
            button2 = types.InlineKeyboardButton('Альфа-Банк', URL_ALFA_BANK)
            button3 = types.InlineKeyboardButton('Банк Дабрабыт', URL_BANKDABRABYT)
            button4 = types.InlineKeyboardButton('Белагропромбанк', URL_BELAGROPROMBANK)
            button5 = types.InlineKeyboardButton('Беларусбанк', URL_BELARUSBANK)
            button6 = types.InlineKeyboardButton('Белинвестбанк', URL_BELINVESTBANK)
            button7 = types.InlineKeyboardButton('БНБ-Банк', URL_BNB_BANK)
            button8 = types.InlineKeyboardButton('БСБ Банк', URL_BSB_BANK)
            button9 = types.InlineKeyboardButton('Идеябанк', URL_IDEABANK)
            button10 = types.InlineKeyboardButton('МТБанк', URL_MTBANK)
            button11 = types.InlineKeyboardButton('Паритетбанк', URL_PARITETBANK)
            button12 = types.InlineKeyboardButton('Приорбанк', URL_PRIORBANK)
            button13 = types.InlineKeyboardButton('СтатусБанк', URL_STATUSBANK)
            button14 = types.InlineKeyboardButton('Технобанк', URL_TECHNOBANK)
            button15 = types.InlineKeyboardButton('ТК Банк', URL_TKBANK)
            button16 = types.InlineKeyboardButton('Франсбанк', URL_FRANSABANK)
            button17 = types.InlineKeyboardButton('Цептер Банк', URL_ZEPTERBANK)

            markup.add(button1, button2, button3)
            markup.add(button4,button5, button6)
            markup.add(button7, button8, button9)
            markup.add(button10,button11, button12)
            markup.add(button13, button14, button15)
            markup.add(button16,button17)

            bot.send_message(message.chat.id, 'При обмене крупных сумм рекомендую обратится в колл-цент выбранного банка', reply_markup=markup)
        else:
            welcome(message)


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'absolutbank':
#                 bot.send_message(call.message.chat.id, 'OKE')
#     except Exception as e:
#         print(repr(e))


# RUN
bot.polling(none_stop=True)