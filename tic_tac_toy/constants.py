SYMBOLS = ("X", "O")

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

GAME_MODES = ("USER", "COMP")

USER_TEMPLATE = (
    ("name", lambda name, *args, **kwargs: name),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("mode", lambda mode, *args, **kwargs: mode),
)

GAME_RULES = """Игра крестики - нолики. 
Игроки по очереди ставят на свободные клетки поля знаки. 
Первый, выстроивший в ряд своих фигуры по вертикали, горизонтали или диагонали, выигрывает. 
Введите режим (user/ comp) и имена игроков"""
