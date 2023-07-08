import telebot
import unittest
import logging
import json

import source.config as config
import source.calc as calc
import source.meme as meme
import source.weather as weather
import source.translate as translate

bot = telebot.TeleBot(config.parse("config/config.json")["token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, великий потомок русов!!! Поговори с РУСОМ!!!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def main():
    logging.info("Бот стартовал")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
