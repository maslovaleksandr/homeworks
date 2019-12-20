from contextlib import contextmanager


class Lock(object):
    def __init__(self):
        self.lock = False


@contextmanager
def set_status(value):
    value.lock = True
    yield value


k = Lock()

with set_status(k) as s:
    print(s.lock)

print(k.lock)
