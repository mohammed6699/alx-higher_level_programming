#!/usr/bin/python3
'''Module for base_geometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """class for rectangle based on BaseGeometry class"""

    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

        def area(self):
            return self.__width * self.__height

        def __str__(self):
            return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
