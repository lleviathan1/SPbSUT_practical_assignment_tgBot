import telebot
import json

bot = telebot.TeleBot("API-Token")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def main():
    print("Hello Telegram")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
