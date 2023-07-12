import logging


def sl_log_state(state ,id, usersState):
    lastState = usersState.get(str(id))
    usersState[str(id)] = state
    logging.info(
        f'Пользователь id {id} сменил состояние c {lastState} на {state}')