from functools import wraps
from time import sleep


def slow_down(func):
    @wraps(func)
    def inner(*args, **kwargs):
        sleep(1)
        res = func(args)
        return res

    return inner


@slow_down
def example(*args):
    print(args)
    return "success"


example("my name is yaeli")
