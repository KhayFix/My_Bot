from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

import settings

# Журнал событий
logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# обработка команды старт
def greet_user(bot, update, user_data):
    emo = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    user_data['emo'] = emo
    text = f'Привет {emo}'
    update.message.reply_text(text)


# Пишет в сообшение что было написанно. Пишет в логи кто, что писал.
def talk_to_me(bot, update, user_data):
    user_text = 'Привет {}{}! Ты написал: {}'.format(update.message.chat.first_name, user_data['emo'],
                                                     update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)
    update.message.reply_text(user_text)


def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


# Функция соединения с платформой Телеграмм
def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
