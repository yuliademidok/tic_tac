import random

from tic_tac_toy.constants import USER_TEMPLATE, COMP_NAMES, SYMBOLS, GAME_MODES
from tic_tac_toy.sys_args import sys_game_args
from tic_tac_toy.templates import user_interface

users = sys_game_args()[1]


def create_user(symbol) -> dict:
    user = {}

    if users:
        name = users.pop(0)
    else:
        name = user_interface("enter_name")

    for itm in USER_TEMPLATE:
        user[itm[0]] = itm[1](name=name, symbol=symbol, mode=GAME_MODES[0])
    return user


def create_comp(symbol) -> dict:
    return {
        "name": random.choice(COMP_NAMES),
        "symbol": symbol,
        "steps": [],
        "mode": GAME_MODES[1],
    }


MODES = {
    GAME_MODES[1]: {"creator": create_comp},
    GAME_MODES[0]: {"creator": create_user},
}


def get_user(mode, symbol) -> dict:
    return MODES[mode]["creator"](symbol=symbol)


def ask_mode() -> str:
    user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}

    modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
    modes_string = f"Выберите номер режима игры\n{modes_str}"

    while True:
        try:
            mode_input = int(input(modes_string))
            return user_modes[mode_input]
        except ValueError:
            print("Недопустимый ввод, введите только число")
        except KeyError:
            print("Недопустимое значение, повторите ввод")
        continue


def create_users() -> list[dict]:
    mode = sys_game_args()[0]
    if not mode:
        mode = ask_mode()

    users = []
    for symbol, mode in zip(SYMBOLS, (GAME_MODES[0], mode)):
        user = get_user(mode, symbol)
        users.append(user)
    return users
