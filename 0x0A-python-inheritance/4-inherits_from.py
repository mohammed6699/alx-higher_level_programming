#!/usr/bin/python3
"""Module for inherits_from"""
def inherits_from(obj, a_class):
    """ function to check if the object isinstance from the class,
        but not from the same type"""

    return isinstance(obj, a_class) and type(obj) != a_class
