from telegram.ext import ConversationHandler, CallbackContext

def add_handlers(dp):
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [MessageHandler(Filters.regex('^(Male|Female)$'), gender)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, age)],
            LOCATION: [MessageHandler(Filters.location, location)],
        },

        fallbacks=[CommandHandler('cancel', cancel)],
    ))

def start(update, context):
    # Отправка сообщения с приветствием
    update.message.reply_text('Привет! Отправьте мне свой пол, используя следующие ключевые слова: Male или Female')
    return GENDER

def gender(update, context):
    # Регистрация пола пользователя
    context.user_data['gender'] = update.message.text
    update.message.reply_text('Сколько вам лет?')
    return AGE

def age(update, context):
    # Регистрация возраста пользователя
    context.user_data['age'] = update.message.text
    update.message.reply_text('Отправьте мне свою текущую локацию')
    return LOCATION

def location(update, context):
    # Регистрация местоположения пользователя
    context.user_data