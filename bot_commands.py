from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def hi_command(update: Update, context: CallbackContext): # в момент когда пользователь пришлет "hello", будет выполнена эта команда
    update.message.reply_text(f'Hi {update.effective_user.first_name}!') # печатаем Hello и забираем имя пользователя

def help_command(update: Update, context: CallbackContext): 
    update.message.reply_text(f'/hi\n/time\n/help\n/sum') #возвращает помощь

def time_command(update: Update, context: CallbackContext): 
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext): 
    msg = update.message.text
    print(msg)
    items = msg.split(' ') # /sum 123 5343532
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}') #возвращает помощь