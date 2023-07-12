from telebot import types


def getStartKeyboard():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Переводчик', callback_data='Переводчик')
    btn2 = types.InlineKeyboardButton('Калькулятор', callback_data='Калькулятор')
    btn3 = types.InlineKeyboardButton('Прогноз погоды', callback_data='Прогноз погоды')
    btn4 = types.InlineKeyboardButton('Мем дня', callback_data='Мем дня')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup


def getCalcExamples():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('0.1 + 0.3 * e ** pi', callback_data='0.1 + 0.3 * e ** pi')
    btn2 = types.InlineKeyboardButton('6/(8-2**3)', callback_data='6/(8-2**3)')
    btn3 = types.InlineKeyboardButton('(((-6)(1)))**-pi', callback_data='(((-6)(1)))**-pi')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup

def getTranslateKeyboard():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('The dark came into the room from the little window that opened in the side of The Hill')
    btn3 = types.InlineKeyboardButton('Zweierlei geht aus dieser Tatsache hervor.')
    btn2 = types.InlineKeyboardButton('古池や')
    btn4 = types.InlineKeyboardButton('Неудивительно, что ехали они больше молча, неизменно пуская лошадок в галоп везде, где трава была пониже и земля поровнее')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup

def getWeatherKeyboard():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        'Санкт-Петербург')
    btn3 = types.InlineKeyboardButton('Москва')
    btn2 = types.InlineKeyboardButton('Париж')
    btn4 = types.InlineKeyboardButton('Веллингтон')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup