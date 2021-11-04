from itertools import cycle

from src.board import get_board, board_match, display_board
from src.steps import make_step, ask_new_game
from src.sys_args import sys_game_args
from src.templates import user_interface
from src.users import create_users, ask_mode
from logger import game_logger


def game_init() -> dict:
    user_interface("welcome")

    commands = sys_game_args()
    mode = commands.get("-mode") or ask_mode()
    name = (commands.get("-u1"), commands.get("-u2"))

    return {
        "users": create_users(mode, name),
        "board": get_board(3),
    }


def game_end(step_num, winner):
    result_str = f"победил {winner['name']}" if winner else "произвошла ничья"
    print(f"На ходу #{step_num}", result_str)
    user_answer = ask_new_game()

    # log revenge
    game_logger.log_revenge(user_answer)

    return user_answer


def game_cycle(users: list[dict, ...], board: list[list]):
    winner = None
    step_num = None
    steps = set()

    game_logger.log_game_start(users[1]['mode'])

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

    # log game steps, name and step
    game_logger.log_game_end(steps, winner, step_num)

    return step_num, winner
