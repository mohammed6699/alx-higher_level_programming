#!/usr/bin/python3
"""class task"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that retrieves a dictionary representation of a
            Student class"""
        return self.__dict__
