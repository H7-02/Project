import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

from config import TOKEN  # Импортируйте токен бота из config.py

# Установите уровень логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание объекта бота
bot = telegram.Bot(token=TOKEN)

# Инициализация бота
updater = Updater(bot=bot, use_context=True)
dp = updater.dispatcher

# Здесь можно добавить обработчики команд и сообщений
# ...

if __name__ == '__main__':
    from handlers import add_handlers  # Импортируйте функцию, которая добавляет обработчики

    # Добавьте обработчики
    add_handlers(dp)

    # Запуск бота
    updater.start_polling()
    updater.idle()
