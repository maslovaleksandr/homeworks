def count_decorator(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner


@count_decorator
def print_some():
    print('hello world')


print_some()
print_some()
print_some()
print_some()

print(print_some.calls)
