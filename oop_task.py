# 1. Создать класс корзина у которого можно выставить разную вместительность для разных объектов
# 2. Создать класс пакет, в который тоже можно помещать предметы у него тоже есть вместимость
# 3. Созать любой класс объекты которогом можно помещать в корзину и в пакет.
# 4. Если вместимость корзины или пакета недостаточна, сообщить, что объект поместить нельзя


class Basket:
    def __init__(self):
        self.max_items = 10
        self.status = 0

    def add_fruit(self, fruit, name):
        if self.status + fruit.fruit_weight > self.max_items:
            return print('use basket')
        self.status = self.status + fruit.fruit_weight
        print('Adding {} to {}....'.format(fruit.fruit_name, name))
        return self.status

    def print_status(self, name):
        print('current status of {} is {}'.format(name, self.status))


class Pocket(Basket):
    def __init__(self):
        super().__init__()
        self.max_items = 5
        self.status = 0


class Fruits:
    def __init__(self, fruit_name, weight):
        self.fruit_name = fruit_name
        self.fruit_weight = weight


# apple = fruits('apple', 2)
# new_pocket = pocket()
# new_pocket.add_fruit(apple, new_pocket.__class__.__name__)
# new_pocket.add_fruit(apple, new_pocket.__class__.__name__)
# new_pocket.print_status(new_pocket.__class__.__name__)

# my_basket = basket()
# my_basket.add_fruit(my_fruit)
