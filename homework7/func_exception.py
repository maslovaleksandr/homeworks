def exception_decorator(func):
    def inner(*args):
        try:
            func(*args)
        except Exception as e:
            print(e)
    return inner


@exception_decorator
def some_func(a, b):
    return a+b/0


some_func(4, 1)

