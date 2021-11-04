from itertools import cycle

from logger.game_logger import log_game_start, log_game
from src.board import get_board, board_match, display_board
from src.steps import make_step, ask_new_game
from src.sys_args import sys_game_args
from src.templates import user_interface
from src.users import create_users, ask_mode


def game_init() -> dict:
    user_interface("welcome")

    commands = sys_game_args()
    mode = commands.get("-mode") or ask_mode()
    name = (commands.get("-u1"), commands.get("-u2"))

    init_data = {
        "users": create_users(mode, name),
        "board": get_board(3),
        "mode": mode,
    }

    # log game init
    log_game_start(init_data)
    return init_data


def game_end(step_num, winner):
    result_str = f"победил {winner['name']}" if winner else "произвошла ничья"
    print(f"На ходу #{step_num}", result_str)
    user_answer = ask_new_game()

    return user_answer


def game_cycle(users: list[dict, ...], board: list[list], mode):
    winner = None
    step_num = None
    steps = set()

    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = steps

        print(f"Ход {step_num} Игрока: {user['name']}")
        display_board(board)
        step = make_step(user, board)
        user['steps'].append(step)
        steps.add(step)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break

    # log game winner, steps
    log_game(steps, winner)

    return step_num, winner
