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
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = [O.to_dictionary() for O in list_objs]
        with open("().json".format(cls.__name__), "w", encoding = "utf-8")as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding = "utf-8")as f:
            return (cls.create(**d) for d in cls.frmo_json_string(f.read()))
