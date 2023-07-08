import telebot
import unittest
import logging
import json

import source.config as config
import source.calc as calc
import source.meme as meme
import source.weather as weather
import source.translate as translate
import source.keyboard as keyboard

bot = telebot.TeleBot(config.parse("config/config.json")["token"])

usersState = {}

@bot.message_handler(commands=['start'])
def request_start(message):
    logging.info( f"Новое сообщение от пользователя id: {message.from_user.id} -> {message.text}")
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(f'Пользователь id {message.from_user.id} сменил состояние на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, "Привет, выбери действие", reply_markup=keyboard.getStartKeyboard())

@bot.message_handler(commands=['help'])
def request_help(message):
    logging.info( f"Новое сообщение от пользователя id: {message.from_user.id} -> {message.text}")
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(f'Пользователь id {message.from_user.id} сменил состояние на {usersState[str(message.from_user.id)]}')
    bot.reply_to(message, "Что-то помогающее пользователю", reply_markup=keyboard.getStartKeyboard())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if usersState[str(message.from_user.id)] == "functionSelection":
        if message.text == "Переводчик":
            a = 1
        elif message.text == "Калькулятор":
            a=2
        elif message.text == "Прогноз погоды":
            a=3
        elif message.text == "Мем дня":
            a=4

def main():
    logging.info("Бот стартовал")
    bot.infinity_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="loging/info.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
