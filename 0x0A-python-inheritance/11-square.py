#!/usr/bin/python3
"""Module for square class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """super class Square"""

    def __init__(self, size):
        """function to define the size"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """function to define the area of square"""
        return self.__size ** 2

    def __str__(self):
        """function to print the string"""
        return "[Square] " + str(self.__size) + "/" +str(self.__size)
