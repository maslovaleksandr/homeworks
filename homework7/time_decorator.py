import time


def time_result(func):
    def inner():
        start_time = time.time()
        func()
        return print("Function run time is: {}".format(time.time() - start_time))
    return inner



@time_result
def some_func():
    print('hello world')


some_func()

