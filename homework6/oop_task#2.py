# *ЗАДАЧА 2:
# Пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.


class Sides:
    def __init__(self, *numbers):
        self.side = numbers


class square(Sides):
    def sq(self):
        return self.side[0]**2

    def perimetr(self):
        return side[0]*4



class rectangle(Sides):
    def sq(self):
        return self.side[0]*self.side[1]

    def perimetr(self):
        return (self.side[0]+self.side[1])*2


class triangle(Sides):
    def sq(self):
        return

    def perimetr(selfe):
        result = 0
        return sum(selfe.side)

class polygon:
    pass



