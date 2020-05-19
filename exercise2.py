from functools import wraps


def my_decorator(my_func):
    @wraps(my_func)
    def inner(*args, **kwargs):
        print(f"Calling: {my_func.__name__} ( {args} )")
        res = my_func(args[0],args[1])
        if res is not None:
            print(f"Return: {type(res)} : {res}")
        return res

    return inner


@my_decorator
def my_yaeli(name, age):
    print(f"my name is {name} and my age is {age}")
    return 1


my_yaeli("yaeli", "20")
