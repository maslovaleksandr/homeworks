import time


def func_decorator(func):
    def inner(*args):
        print("{} is canceled".format(func.__name__))
    return inner


@func_decorator
def add(x, y):
    return x + y


@func_decorator
def power(x, y):
    return x**y


power()
add(3)
