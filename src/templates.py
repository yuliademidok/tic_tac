interface_string = {
    "welcome": "Добро пожаловать в Игру Крестики Нолики",
    "game_type": "С кем желаешь играть {variants}",
    "enter_name": "Введите свое имя",
    "ask_step": "Введите координаты хода через пробел\n",
    "win": "победил {name}",
    "draw": "произвошла ничья",
    "new_game": "Желаете начать новую игру? {variants}",
    "invalid_step": "Ячейка не существует или занята",
    "bye": "До встречи",
    "help": """Игроки по очереди ставят на свободные клетки поля знаки. 
Введите режим ("-mode") и имена игроков ("-u1", "-u2")""",
}

template_variants = {
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    # "game_type": lambda template, **kwargs: template.format(variants=("C", "U")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    # "win": lambda template, **kwargs: template.format(**kwargs),
    # "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str.format(variants=template_variants[template_name]))
        return user_input
    else:
        print(interface_string[template_name])
