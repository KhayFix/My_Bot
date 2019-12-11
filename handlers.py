from glob import glob
import logging
from random import choice

from utils import get_keyboard, get_user_emo


# обработка команды старт
def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = f'Привет {emo}'
    update.message.reply_text(text, reply_markup=get_keyboard())


# Пишет в сообшение что было написанно. Пишет в логи кто, что писал.
def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = 'Привет {}{}! Ты написал: {}'.format(update.message.chat.first_name, emo,
                                                     update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)
    update.message.reply_text(user_text, reply_markup=get_keyboard())

# функция берет из папки images рандомную картинку
def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))

# функция присваивает новый эмоджи, старый убирает
def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text(f'Готово: {emo}', reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text(f'Готово: {get_user_emo(user_data)}', reply_markup=get_keyboard())


def get_location(bot, update, user_data):
    print(update.message.locarion)
    update.message.reply_text(f'Готово: {get_user_emo(user_data)}', reply_markup=get_keyboard())
