from telegram.ext import (Updater, CommandHandler, MessageHandler, RegexHandler, Filters)

from handlers import *
import settings

# Журнал событий
logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция соединения с платформой Телеграмм
def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))

    dp.add_handler(RegexHandler('^(БЕЗ КОТА\nи жизнь не та)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
