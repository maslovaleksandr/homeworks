class Window:
    def __init__(self, glass_status):
        self.glass = glass_status

    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened
        print('Windows is now ', self.is_opened)


w1 = Window('broken')
w2 = Window('not broken')

print('Initial state w1: ', w1.glass, w2.glass)


class Table:
    def __init__(self, number_of_legs):
        print('New number of legs {} '.format(number_of_legs))


t1 = Table(3)
t2 = Table(4)


class Example:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
        print('{}, {}, {}'.format(self.a, self._b, self.__c))

    def call(self):
        print("called!")


e = Example()
print(e.a)
print(e._b)
print(e.__c)
