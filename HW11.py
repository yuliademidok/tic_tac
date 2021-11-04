# TODO: 3 вложенности это плохо
import random

from functools import partial


def retry(func=None, count=1):
    if func is None:
        return partial(retry, count=count)

    def wrapper(*args, **kwargs):
        nonlocal count
        while count:
            try:
                result = func(*args, **kwargs)
                return result
            except ValueError:
                count -= 1
        raise ValueError

    return wrapper


@retry(count=10)
def connect():
    a = random.randint(1, 100)
    if a % 3:
        return "ОТВЕТ"
    raise ValueError


print(connect())
print(connect())
print(connect())
