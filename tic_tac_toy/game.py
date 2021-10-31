from itertools import cycle

from tic_tac_toy.board import get_board, board_match, display_board
from tic_tac_toy.steps import make_step, ask_new_game
from tic_tac_toy.users import ask_mode, create_users
from logging import logger


def game_init() -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    return {
        "users": create_users(ask_mode()),
        "board": get_board(3),
    }


def game_end(step_num, winner):
    result_str = f"победил {winner['name']}" if winner else "произвошла ничья"
    print(f"На ходу #{step_num}", result_str)
    user_answer = ask_new_game()

    # log revenge
    logger.log_revenge(user_answer)

    return user_answer


def game_cycle(users: list[dict, ...], board: list[list]):
    winner = None
    step_num = None
    steps = set()

    logger.log_game_start(users[1]['mode'])

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
    logger.log_game_end(steps, winner, step_num)

    return step_num, winner
