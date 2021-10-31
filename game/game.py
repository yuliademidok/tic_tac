from itertools import cycle

from game.board import get_board, board_match, display_board
from game.steps import make_step, ask_new_game
from game.users import ask_mode, create_users


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
    return user_answer


def game_cycle(users: list[dict, ...], board: list[list]):
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
    return step_num, winner
