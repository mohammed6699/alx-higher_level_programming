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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        else
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = [O.to_dictionary() for O in list_objs]
        with open("().json".format(cls.__name__), "w", encoding = "utf-8")as f:
            f.write(cls.to_json_string(list_objs))
