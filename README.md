<h1 align="center">Practical assignment tgBot</h1>

## Телеграм бот на Python 3

### Используются следующие технологии:
+ pyTelegramBotAPI
+ SQLite
+ unittest
+ logger
+ googletrans

## Оглавление

+ [Оглавление](#оглавление)
+ [Описание](#описание)
+ [Зависимости](#зависимости)
+ [Запуск тестов](#запуск_тестов)
+ [Запуск](#запуск)

## Описание

Бот реализует следующие функции:
+ Переводчик
+ Прогноз погоды
+ Калькулятор
+ Мем дня

## Зависимости
Бот работает исключительно на **Linux**. 

Для запуска понадобится много зависимостей, но основные представлены тут.

### Ubuntu/Debian

```bash
sudo apt update && sudo apt install python3 -y
pip install googletrans==4.0.0-rc1 pyTelegramBotAPI
```

## Запуск тестов

Для бота предусмотрены UNIT тесты.

Запуск происходит следующим образом:
```commandline
python3 startBot.py test
```
Ожидаемый результат:

![Ожидаемый_результат](https://github.com/happyT1024/SPbSUT_practical_assignment_tgBot/blob/master/photos/testsOK.png)

## Запуск
Когда настроили зависимости, можно переходить к настройке конфигурации.

В файле **_config/config.json_** надо установить параметры токена бота - **tg_api_token**, и токена сайта openweathermap.org - **weather_api_token**

Далее следует создать дирректорию logging - в нее будут писаться логи программы.

Пример логов:
![Логи](https://github.com/happyT1024/SPbSUT_practical_assignment_tgBot/blob/master/photos/logging.png)

Далее следует создать папку **memes**, в которую следует поместить несколько мемов.

Во время загрузки программы мем дня автоматически выберется.

Теперь можно запускать бота
```bash
python3 startBot.py
```
Если что-то не получилось, читайте логи в файле **logging/info.log**

