# +3.Сделать менеджер контекста, который бы мог измерять время
# выполнения блока кода, пример использования:
#
# with TimeIt() as t:
#     some_long_function()
#
# print('Execution time was:', t.time)

from time import time, sleep


class timeit:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        self.result = self.end_time - self.start_time


def long_func():
    a = [i for i in range(0, 100)]
    print(a)


with timeit() as t:
    sleep(3)
    long_func()

print("Execution time was: ", t.result)


