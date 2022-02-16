## isOdd (проверяет нечетность числа)

# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))


## Progress (заполняет progress bar)

# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()

# ## emoji 
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize("Python is fun :red_heart:"))


# matplotlib (математические функции)
# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

# list = [1, 2, 3, 2, 7]
# plt.plot(list)

# plt.show()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None: # в момент когда пользователь пришлет "hello", будет выполнена эта команда
    update.message.reply_text(f'Hello {update.effective_user.first_name}') # печатаем Hello и забираем имя пользователя


updater = Updater('5261564788:AAGvVd04bSYxydwIlh4yQxH7VUxfgXGsUuw')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('server start')
updater.start_polling()
updater.idle()