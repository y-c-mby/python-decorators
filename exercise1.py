import datetime
from time import sleep
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def inner():
        start = datetime.datetime.now()
        func()
        print("the program ran " + str(datetime.datetime.now() - start))

    return inner()


@my_decorator
def sleeping_function():
    sleep(2)
    print("hi i'm sleeping")


#sleeping_function()
