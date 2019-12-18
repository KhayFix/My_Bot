Начало чего-то большего
====
Это бот для Telegram, созданый с целью сделать вашу жизнь лучше, присылает вам фотографии котиков.

Установка
----------
Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Положите картинки с котиками в папку images. Название файлов может начинаться с любого символа. Формат картинки jpg или jpeg.


Настройка
----------
Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    # Настройка прокси
    PROXY = {'proxy_url': 'socks5h://ВАШ_SOCKS5_ПРОСКИ:1080',
             'urllib3_proxy_kwargs': {
                 'username': 'ЛОГИН',
                 'password': 'ПАРОЛЬ',
             }
             }
    
    API_KEY = "API ключ, который вы получили у BotFather"
    
    # Смайлики можно вставить другие: 
    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:', ':leopard:', ':sun_with_face:']
    
Смайлики в USER_EMOJI можно добавить от сюда:
https://www.webfx.com/tools/emoji-cheat-sheet/

Запуск
----------
В активированном виртуальном окружении выполните:

.. code-block:: text

    python bot.py