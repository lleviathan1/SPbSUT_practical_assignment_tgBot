from googletrans import Translator
import source.sl_log as log
import source.keyboard as keyboard

translator = Translator()


def request_phrase(message, bot, usersState):
    bot.reply_to(message, "Отправь мне фразу или выбери из предложенных", reply_markup=keyboard.getTranslateKeyboard())
    log.sl_log_state("waitPhraseToTranslate", message.from_user.id, usersState)


def response_translate_text(message, bot, usersState):
    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang

    # Если ввод по русски, то перевести на английский по умолчанию.
    if lang == 'ru':
        send = translator.translate(message.text)

    # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(message.text, dest='ru')

    bot.send_message(message.chat.id, send.text, reply_markup = keyboard.getStartKeyboard())
    log.sl_log_state("functionSelection", message.from_user.id, usersState)

