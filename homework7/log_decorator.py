import time


def add_log(func):
    def inner():
        print("{} started at: {}".format(func.__name__, time.strftime("%H:%M:%S", time.gmtime())))
        func()
        time.sleep(2)
        print("{} ended at: {}".format(func.__name__, time.strftime("%H:%M:%S", time.gmtime())))
    return inner


@add_log
def some_func():
    print('hello wolrd')


@add_log
def print_list():
    new_list = [i for i in range(1, 1000)]
    print(new_list)


some_func()
print_list()

