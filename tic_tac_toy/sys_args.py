import sys

from tic_tac_toy.constants import GAME_RULES, GAME_MODES


def sys_help() -> bool:
    if "help" in sys.argv:
        print(GAME_RULES)
        return True


def sys_game_args() -> tuple[str, list]:
    mode = None
    users = None
    try:
        argv_mode = sys.argv[1]
        if argv_mode.upper() in GAME_MODES:
            mode = argv_mode.upper()
            users = sys.argv[2:4]
    except IndexError:
        pass

    return mode, users
