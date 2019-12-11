import random


def random_num():
    while True:
        yield random.randint(1, 10)


x = random_num()
print(next(x))


def range_gen(start, end, step):
    i = 0
    while start != end - 1:
        yield i
        i += step


g = range_gen(1, 10, 2)
print(next(g))



def map_gen(arg, func):
    for m in arg:
        yield func(m)


mas = ['wekm', 'w', 'eeee']
my_gen = map_gen(mas, len)
print(next(my_gen))



def numerate_gen(l):
    index = 0
    for el in l:
        yield index, el
        index += 1


num = numerate_gen(mas)
print(next(num))
print(next(num))
print(next(num))


def as_zip(a1, a2):
    for i in range(len(a1)):
        yield (a1[i], a2[i])


words = ['hello', 'hi', 'what']
numbers = [1, 2, 3, 4]
z = as_zip(words, numbers)
try:
    print(next(z))
    print(next(z))
    print(next(z))
    print(next(z))
except StopIteration:
    print("generator ended")

