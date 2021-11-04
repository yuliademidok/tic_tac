import random

from src.constants import USER_TEMPLATE, COMP_NAMES, SYMBOLS, GAME_MODES


def create_user(symbol, name) -> dict:
    user = {}
    for itm in USER_TEMPLATE:
        user[itm[0]] = itm[1](name=name, symbol=symbol, mode=GAME_MODES[0])
    return user


def create_comp(symbol, name) -> dict:
    return {
        "name": name or random.choice(COMP_NAMES),
        "symbol": symbol,
        "steps": [],
        "mode": GAME_MODES[1],
    }


MODES = {
    GAME_MODES[1]: {"creator": create_comp},
    GAME_MODES[0]: {"creator": create_user},
}


def get_user(mode, symbol, name) -> dict:
    return MODES[mode]["creator"](symbol=symbol, name=name)


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


def create_users(mode, name) -> list[dict]:
    users = []
    for symbol, mode, name in zip(SYMBOLS, (GAME_MODES[0], mode), name):
        user = get_user(mode, symbol, name)
        users.append(user)
    return users
