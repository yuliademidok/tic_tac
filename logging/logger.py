from pathlib import Path
import os
from datetime import datetime, date

"""
в логе должно присутсвовать: 
- Когда начата игра
- Номер игры в данной сессии игры
- В каком режиме начата игра
- Каждый ход игрока
- Кто победил и на каком шаге
- Выбран ли реванш
Для логирования данных записей, вам необходимо, разработать удобный способ хранения данных игры в файле. Можно 
воспользоваться схемой CSV
"""

delim = ','
columns = ('start_time', 'game_number', 'game_mode', 'game_steps', 'winner_name', 'win_step', 'revenge_requested')

count = 1

ROOT_DIR = Path(__file__).parent.parent
log_file_name = f'{date.today().strftime("%Y%m%d")}'
# file = os.path.join(ROOT_DIR, "logs", log_file_name)


def log_write(data):
    file = os.path.join(ROOT_DIR, "logs", log_file_name)
    with open(file, 'a', encoding="UTF-8") as f:
        f.writelines(data + delim)


def add_file_header():
    file = os.path.join(ROOT_DIR, "logs", log_file_name)
    with open(file, 'a+', encoding="UTF-8") as f:
        f.seek(0)
        data = f.read()
        if len(data) == 0:
            f.write(f"{delim.join(columns)}")


def log_game_start(mode):
    """Logs:
    - game init time
    - game number
    - game mode"""
    add_file_header()
    log_write('\n' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    global count
    log_write(str(count))
    count += 1

    log_write(mode)


def log_game_end(steps, winner, step_num):
    """Logs:
    - users' steps
    - winner name
    - win step"""
    log_write(str(steps))
    if winner:
        log_write(winner['name'])
    else:
        log_write("")
    log_write(str(step_num))


def log_revenge(user_answer):
    log_write('y' if user_answer else 'n')
