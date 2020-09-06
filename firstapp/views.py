"""
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot

TOKEN = '1065354171:AAFvOKsypLWgbe_y02FD9FOyVjRJ-V-8S24'
tbot = telebot.TeleBot(TOKEN)


# For free PythonAnywhere accounts
# tbot = telebot.TeleBot(TOKEN, threaded=False)

@csrf_exempt
def index(request):
    if request.META['CONTENT_TYPE'] == 'application/json':

        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tbot.process_new_updates([update])

        return HttpResponse("")

    else:
        raise PermissionDenied


@tbot.message_handler(content_types=["text"])
def get_okn(message):
    tbot.send_message(message.chat.id, "Hello, bot!")




"""


from django.shortcuts import render

# Create your views here.

import telebot
from telebot import types

from django.http import HttpResponse


def index(request):

    bot = telebot.TeleBot("1065354171:AAFvOKsypLWgbe_y02FD9FOyVjRJ-V-8S24")

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, hooo...")
        chat_id = message.chat.id

        markup = types.ReplyKeyboardMarkup()
        itembtna = types.KeyboardButton('a')
        itembtnv = types.KeyboardButton('v')
        itembtnc = types.KeyboardButton('c')
        itembtnd = types.KeyboardButton('d')
        itembtne = types.KeyboardButton('e')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)






    bot.remove_webhook()

    bot.polling()
    return HttpResponse('Done')

