# +2.Сделать менеджер контекста, который бы проглатывал все исключения вызванные
# в теле и писал их в консоль, пример использования:
#
# with no_exceptions():
#     1 / 0  # => logs: ZeroDivisionError
#
# print('Done!')  # => continues execution

from contextlib import contextmanager


@contextmanager
def no_exceptions():
    try:
        print('hello world')
        yield
    except Exception as e:
        print("Log:", e)


with no_exceptions():
    sdfsdf

print('done')