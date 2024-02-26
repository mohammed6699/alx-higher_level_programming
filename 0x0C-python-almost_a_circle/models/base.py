#!/usr/bin/python3
"""Models for the class attribute Base"""

from json imports dumps, loads
class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base. __nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        else
        return dumps(list_dictionaries)
