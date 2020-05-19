from functools import wraps


def counter_calls(func):
    counter = 0

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        res = func(*args)
        if kwargs != {}:
            print(counter)
        if res is not None:
            return res

    return inner
@counter_calls
def count_func():
    print("hello")

count_func()
count_func()
count_func()
count_func()
count_func(finel="1")