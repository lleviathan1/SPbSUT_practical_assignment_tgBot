import logging
import math
import requests

import source.config as config
import source.keyboard as keyboard
import source.sl_log as log


def request_city(message, bot, usersState):
    bot.reply_to(message, "Отправь мне город или выбери из предложенных", reply_markup=keyboard.getWeatherKeyboard())
    log.sl_log_state("waitCity", message.from_user.id, usersState)

def response_weather(message, bot, usersState):
    weather_api_key = config.parse("config/config.json")["weather_api_token"]
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&units=metric&appid={weather_api_key}")
        data = response.json()

        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        bot.send_message(message.chat.id,
                         f"Погода в городе: {city}\n"
                         f"Температура: {cur_temp}°C\n"
                         f"Влажность: {humidity}%\n"
                         f"Давление: {math.ceil(pressure / 1.333)} мм.рт.ст\n"
                         f"Ветер: {wind} м/с",
                         reply_markup = keyboard.getStartKeyboard())
        log.sl_log_state("functionSelection", message.from_user.id, usersState)
    except:
        logging.warning(data['message'])
        bot.send_message(message.chat.id, 'Город не найден, попробуйте снова',
                         reply_markup=keyboard.getWeatherKeyboard())
