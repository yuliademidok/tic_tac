from src.board import get_board
from src.game import game_init, game_cycle, game_end
from src.sys_args import sys_help


def main():
    sys_help()

    game_vars = game_init()
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game)
        if end_result:
            game_vars["board"] = get_board(3)


if __name__ == '__main__':
    main()
