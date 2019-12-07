# -*- coding: utf-8 -*-

from utils import get_input_function


class Storage(object):  # storage = Storage()
    obj = None

    items = None



    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.status = '[-]'

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __init__(self, heading, status):
        super(ToDoItem, self).__init__(heading)
        self.status = status

    def __str__(self):
        return '{} ToDo: {}'.format(
            self.status,
            self.heading
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        status = '[-]'
        heading = input_function('Input heading: ')
        return ToDoItem(heading, status)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price, status):
        super(ToBuyItem, self).__init__(heading)
        self.price = price
        self.status = status

    def __str__(self):
        return '{} ToBuy: {} for {}'.format(
            self.status,
            self.heading,
            self.price
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        status = '[-]'
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price, status)


class ToReadUrl(BaseItem):
    def __init__(self, heading, url, status):
        super(ToReadUrl, self).__init__(heading)
        self.url = url
        self.status = status

    def __str__(self):
        return '{} ToRead: {} on {}'.format(
            self.status,
            self.heading,
            self.url
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        status = '[-]'
        heading = input_function('Input heading: ')
        url = input_function('Input url or: ')
        return ToReadUrl(heading, url, status)




