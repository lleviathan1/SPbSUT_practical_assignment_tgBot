import telebot
import source.config as config
import unittest
import json

cfg = config.parse("config/config.json")
bot = telebot.TeleBot(cfg["token"])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, великий потомок русов!!! Поговори с РУСОМ!!!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
