from pathlib import Path

from src.templates import user_interface

SYMBOLS = ("X", "O")

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

GAME_MODES = ("USER", "COMP")

USER_TEMPLATE = (
    ("name", lambda name, *args, **kwargs: name or user_interface("enter_name")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("mode", lambda mode, *args, **kwargs: mode),
)

FILES = {
    "GAME_INIT": "game_init",
}

COMMANDS = (
    "-mode",
    "-u1",
    "-u2",
)

ROOT_DIR = Path(__file__).parent.parent

log_columns = (
    'start_time',
    'game_number',
    'game_mode',
    'game_steps',
    'winner_name',
    'win_step',
    'revenge_requested'
)
