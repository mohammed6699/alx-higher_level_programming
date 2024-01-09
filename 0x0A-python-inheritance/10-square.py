#!/usr/bin/python3
"""Module for Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Module for sub class square"""
    def __init__(self, size):
        """function for define the size"""

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """function for define the area"""
        return self.__size ** 2
