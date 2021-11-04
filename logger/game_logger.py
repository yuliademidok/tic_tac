import os
from datetime import datetime

from src.constants import FILES, ROOT_DIR, log_columns

delim = ';'
count = 1


def log_write(data: str, handler: str, mode="a"):
    file = os.path.join(ROOT_DIR, "logs", FILES[handler])
    with open(file, mode, encoding="UTF-8") as f:
        f.writelines(data + delim)


def add_file_header(handler: str):
    file = os.path.join(ROOT_DIR, "logs", FILES[handler])
    with open(file, 'a+', encoding="UTF-8") as f:
        f.seek(0)
        data = f.read()
        if len(data) == 0:
            f.write(f"{delim.join(log_columns)}")


def log_game_start(mode):
    """Logs:
    - game init time
    - game number
    - game mode"""
    add_file_header("GAME_INIT")
    log_write("\n" + str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')), "GAME_INIT")

    global count
    log_write(str(count), "GAME_INIT")
    count += 1

    log_write(mode, "GAME_INIT")


def log_game_end(steps, winner, step_num):
    """Logs:
    - users' steps
    - winner name
    - win step"""
    log_write(str(steps), "GAME_INIT")
    if winner:
        log_write(winner['name'], "GAME_INIT")
    else:
        log_write("draw", "GAME_INIT")
    log_write(str(step_num), "GAME_INIT")


def log_revenge(user_answer):
    log_write('y' if user_answer else 'n', "GAME_INIT")
