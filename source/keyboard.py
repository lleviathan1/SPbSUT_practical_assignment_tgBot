from telebot import types

def getStartKeyboard():
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Переводчик')
    itembtn2 = types.KeyboardButton('Калькулятор')
    itembtn3 = types.KeyboardButton('Прогноз погоды')
    itembtn4 = types.KeyboardButton('Мем дня')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup