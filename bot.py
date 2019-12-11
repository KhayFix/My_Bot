from glob import glob
import logging
from random import choice

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

import settings



# Журнал событий
logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# обработка команды старт
def greet_user(bot, update):
    text = 'Вызван /start \nВведите название планеты, например "/planet Mars": ' \
           '\nМожно подсчитать колличество слов: "/wordcount Привет!":' \
           '\nМожно узнать ближайшее полнолуние: "/next_full_moon 2019-01-01"'
    logging.info(text)
    update.message.reply_text(text)

# Пишет в сообшение что было написанно. Пишет в логи кто, что писал.
def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)
    update.message.reply_text(user_text)


# Функция соединения с платформой Телеграмм
def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
