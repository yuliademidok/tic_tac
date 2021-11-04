import os
from datetime import datetime

from src.constants import FILES, ROOT_DIR, log_columns

delim = ';'


def log_write(data: str, handler: str, mode="a"):
    file = os.path.join(ROOT_DIR, "logs", FILES[handler])
    with open(file, mode, encoding="UTF-8") as f:
        f.writelines(data + delim)


def add_file_header(handler: str, header: tuple):
    file = os.path.join(ROOT_DIR, "logs", FILES[handler])
    with open(file, 'a+', encoding="UTF-8") as f:
        f.seek(0)
        data = f.read()
        if len(data) == 0:
            f.write(f"{delim.join(header)}")


def get_game_number() -> str:
    file = os.path.join(ROOT_DIR, "logs", FILES["GAME_INIT"])
    with open(file, 'r', encoding="UTF-8") as f:
        try:
            game_num = (f.readlines())[-1].split(delim)[0]
            if not game_num.isnumeric():
                return "0"
        except IndexError:
            return "0"

    return game_num


def log_game_start(init_data):
    """Logs:
    - game number
    - game init time
    - game mode
    - users names"""
    add_file_header("GAME_INIT", log_columns[0]["init_game"])
    game_num = str(int(get_game_number()) + 1)
    names = delim.join(_["name"] for _ in init_data["users"])
    log_write(
        f"\n{delim.join([game_num, str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')), init_data['mode'], names])}",
        "GAME_INIT")


def log_game(steps, winner):
    """Logs:
    - game number
    - winner name
    - users' steps"""
    add_file_header("GAME_LOG", log_columns[1]["game_log"])
    game_num = get_game_number()
    steps = delim.join(map(str, steps))
    winner = winner['name'] if winner else "draw"

    log_write(
        f"\n{delim.join([game_num, winner, steps])}",
        "GAME_LOG")
