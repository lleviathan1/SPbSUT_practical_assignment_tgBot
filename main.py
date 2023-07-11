import telebot
import unittest
import logging
import json

# Конфигурирование логов
logging.basicConfig(level=logging.INFO, filename="loging/info.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

# Вспомогательные функции
import source.config as config
import source.keyboard as keyboardd

# SL - Сервис логика
import source.meme as meme
import source.weather as weather
import source.translate as translate
import source.calc as calc

# Подключение по токену
bot = telebot.TeleBot(config.parse("config/config.json")["tg_api_token"])

# Состояния пользователей
usersState = {}
# В программе используется идея акторов,
# но без акторного фреймворка

# Данная фича нужна для того, чтобы пользователи
# друг друга не блокировали без использования ассинхронных функций

# Каждому пользователю соотвествуют состояния

# Обработка легко представима в виде конечного автомата

@bot.message_handler(commands=['start'])
def request_start(message):
    logging.info(f"Новое сообщение от пользователя id: {message.from_user.id} -> {message.text}")
    lastState = usersState.get(str(message.from_user.id))
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(
        f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, "Привет, выбери действие", reply_markup=keyboardd.getStartKeyboard())


@bot.message_handler(commands=['help'])
def request_help(message):
    logging.info(f"Новое сообщение от пользователя id: {message.from_user.id} -> {message.text}")
    lastState = usersState.get(str(message.from_user.id))
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(
        f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, "Что-то помогающее пользователю", reply_markup=keyboardd.getStartKeyboard())


# SLM - менеджер сервис логики
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    logging.info(f"Новое сообщение от пользователя id: {message.from_user.id} -> {message.text}")
    if usersState.get(str(message.from_user.id)) in ["functionSelection", None]:
        lastState = usersState.get(str(message.from_user.id))
        if message.text == "Переводчик":
            usersState[str(message.from_user.id)] = "translate"
            logging.info(
                f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
        elif message.text == "Калькулятор":
            usersState[str(message.from_user.id)] = "calc"
            logging.info(
                f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
            calc.calc_send_request(message, bot, usersState)
        elif message.text == "Прогноз погоды":
            usersState[str(message.from_user.id)] = "weather"
            logging.info(
                f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
        elif message.text == "Мем дня":
            usersState[str(message.from_user.id)] = "meme"
            logging.info(
                f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
            meme.send_meme(message, bot, usersState)
        else:
            logging.warning(f"Пользователь отправил некоректную команду {message.text}. Сообщение проигнорировано")
    elif usersState.get(str(message.from_user.id)) == "waitCalcResponse":
        calc.calc_send_responce(message, bot, usersState)
    else:
        logging.warning(
            f"Состояние пользователя {usersState.get(str(message.from_user.id))}. Сообщение проигнорировано")


def main():
    logging.info("Бот стартовал")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
