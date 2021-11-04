import sys

from src.constants import GAME_MODES, COMMANDS
from src.templates import user_interface


def sys_help() -> bool:
    if "help" in sys.argv:
        user_interface("help")
        return sys.exit(0)


def sys_game_args() -> dict:
    init_commands = {}
    try:
        command_input = sys.argv[1:]
        for i in COMMANDS:
            if i in command_input:
                init_commands[i] = command_input[command_input.index(i) + 1]

        if init_commands.get("-mode").upper() in GAME_MODES:
            init_commands["-mode"] = init_commands.get("-mode").upper()
        else:
            del init_commands["-mode"]
    except IndexError:
        pass
    except AttributeError:
        pass

    return init_commands

