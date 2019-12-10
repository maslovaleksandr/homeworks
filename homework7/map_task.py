from functools import reduce


def five_division(n):
    return n % 5


def func_str(n):
    return str(n)


k = [1, 4, 5, 30, 99]
print(list(map(five_division, k)))
print(list(map(func_str, k)))

n = ['some', 1, 'v', 40, '3a', str]
result = filter(lambda s: not isinstance(s, str), ['some', 1, 'v', 40, '3a', str])
print(list(result))





words = ['some', 'other', 'value']


result = reduce(lambda a, b: a+b, map(lambda word: len(word), words))
print(result)
