import logging
import source.keyboard as keyboard
import math
import cmath

def calc_from_string(string):
    for c in ['sin', 'cos', 'tan', 'pi', 'e']:
        string = string.replace(c, "math."+c)
    fix_string = str(string)
    for c in ['math.sin', 'math.cos', 'math.tan', 'math.pi', 'math.e']:
        fix_string = fix_string.replace(c, '')
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ']
    operations = ['+', '-', '*', '/', '(', ')']
    for c in fix_string:
        if (not c in nums) and (not c in operations):
            return "Сообщение некорректно"
    try:
        return eval(string)
    except TypeError:
        return "Ответ не в множестве натуральных чисел"
    except  ArithmeticError or NameError:
        return "Арифметическая ошибка"


def calc_send_request(message, bot, usersState):
    lastState = usersState.get(str(message.from_user.id))
    usersState[str(message.from_user.id)] = "waitCalcResponse"
    logging.info(
        f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, "Отправь мне операцию, например (0.2+0.4)-99*(-2), или выбери из предложенных", reply_markup=keyboard.getCalcExamples())


def calc_send_responce(message, bot, usersState):
    lastState = usersState.get(str(message.from_user.id))
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(
        f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, f"{calc_from_string(message.text)}", reply_markup=keyboard.getStartKeyboard())
