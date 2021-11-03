import random

from tic_tac_toy.templates import user_interface


def get_step() -> tuple:
    while True:
        result = []
        input_step = user_interface("ask_step")
        steps = input_step.split(" ")
        try:
            if len(steps) != 2:
                raise ValueError
            for itm in steps:
                result.append(int(itm))
        except ValueError:
            continue
        return tuple(result)


def chek_step(board: list[list], step: tuple) -> bool:
    if step[0] < 1 or step[1] < 1:
        return False
    try:
        cell = board[step[0] - 1][step[1] - 1]
        if not cell:
            return True
    except IndexError:
        pass
    return False


def user_step(user: dict, board: list[list]) -> tuple:
    while True:
        step = get_step()
        if chek_step(board, step):
            board[step[0] - 1][step[1] - 1] = user["symbol"]
            return step
        else:
            user_interface("invalid_step")
            continue


def computer_step(user: dict, board: list[list]) -> tuple:
    board_size = len(board)
    possible_steps = set((i, j) for i in range(1, board_size + 1) for j in range(1, board_size + 1))
    comp_step = random.choice(tuple(possible_steps.difference(user["all_steps"])))
    board[comp_step[0] - 1][comp_step[1] - 1] = user["symbol"]
    return tuple(comp_step)


def make_step(user: dict, board: list[list]):
    if user['mode'] == 'COMP':
        return computer_step(user, board)
    else:
        return user_step(user, board)


def ask_new_game() -> bool:
    variants = ('Y', 'N')

    while True:
        user_answer = input(f"Желаете начать новую игру? {'/'.join(variants)}").upper()
        if user_answer in variants:
            return user_answer == variants[0]
        print("Ошибка ввода, введите верное значение")
