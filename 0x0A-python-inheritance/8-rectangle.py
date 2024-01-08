#!/usr/bin/python3
'''Module for base_geometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """class for rectangle based on BaseGeometry class"""
    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.height = height
        self.width = width
