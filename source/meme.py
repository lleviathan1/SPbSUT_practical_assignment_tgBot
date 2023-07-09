import logging
import os
from random import randint

os.system("ls mems > mems/mems_list.txt")
with open("mems/mems_list.txt", "r") as read_file:
    meme = read_file.readlines()
    if len(meme) == 0:
        logging.critical("Мемы не добавлены")
        exit(1)
    try:
        meme.remove("mems_list.txt\n")
    except ValueError:
        None
meme = meme[randint(0, len(meme)-1)]
meme = meme.replace('\n', '')
logging.info(f"В качестве мема дня был выбран файл {meme}")
meme = open(f"mems/{meme}", 'rb')
meme_file_id = -1

def send_meme(message, bot, usersState):
    global meme_file_id
    lastState = usersState.get(str(message.from_user.id))
    usersState[str(message.from_user.id)] = "functionSelection"
    logging.info(
        f'Пользователь id {message.from_user.id} сменил состояние c {lastState} на {usersState[str(message.from_user.id)]}')
    if meme_file_id == -1:
        meme_file_id = bot.send_photo(message.from_user.id, meme).photo[0].file_id
    else:
        bot.send_photo(message.from_user.id, meme_file_id)


