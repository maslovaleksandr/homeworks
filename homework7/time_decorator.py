import time


def time_result(func):
    def inner():
        start_time = time.time()
        func()
        return print(time.time() - start_time)
        # return print('job was done in {}'.format(time.strftime("%S",(end_time - start_time)))
    return inner



@time_result
def some_func():
    print('hello world')


some_func()

