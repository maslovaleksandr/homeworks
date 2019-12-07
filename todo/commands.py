# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function


class BaseCommand(object):
    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


    @staticmethod
    def user_input_secure_wrap(func, *args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        from models import ToDoItem, ToBuyItem, ToReadUrl

        return {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
            'ToReadUrl': ToReadUrl
        }


    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('hello world')

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None
        selected_key = None

        def give_me_num():
            selection = int(input_function('Input number: '))
            selected_key = list(classes.keys())[selection]
            return selected_key

        selected_key = self.user_input_secure_wrap(give_me_num)

        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()
        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object.heading)))
        print()
        return new_object


class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        ListCommand().perform(objects)

        input_function = get_input_function()
        selection = None
        selected_key = None

        def give_me_num():
            selection = int(input_function('Input number: '))
            selected_key = objects[selection]
            return selected_key

        selected_key = self.user_input_secure_wrap(give_me_num)
        print('Selected: {}'.format(selected_key.heading))
        print()
        if selected_key.status == '[-]':
            selected_key.status = '[+]'
            print('Changed status of object {} to {}'.format(selected_key.heading, selected_key.status))
            print()


class UndoneCommand(DoneCommand):


    @staticmethod
    def label():
        return 'undone'

    # selected_key = self.user_input_secure_wrap(give_me_num)
    # print('Selected: {}'.format(selected_key.heading))
    # print()
    # if selected_key.status == '[-]':
    #     selected_key.status = '[+]'
    #     print('Changed status of object {} to {}'.format(selected_key.heading, selected_key.status))
    #     print()

    # def perform(self, objects, *args, **kwargs):
    #
    #     if len(objects) == 0:
    #         print('There are no items in storage.')
    #         return
    #
    #     for index, obj in enumerate(objects):
    #         print('{}: {}'.format(index, str(obj)))
    #
    #     input_function = get_input_function()
    #     selection = None
    #     selected_key = None
    #
    #     def give_me_num():
    #         selection = int(input_function('Input number: '))
    #         selected_key = objects[selection]
    #         return selected_key
    #
    #     selected_key = self.user_input_secure_wrap(give_me_num)
    #     print('Selected: {}'.format(selected_key.heading))
    #     print()
    #     if selected_key.status == '[+]':
    #         selected_key.status = '[-]'
    #         print('Changed status of object {} to {}'.format(selected_key.heading, selected_key.status))
    #         print()



class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')















