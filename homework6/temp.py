from oop_task import Basket, Fruits


apple = Fruits('Apple', 15)
b = Basket()
b.add_fruit(apple, b.__class__.__name__)