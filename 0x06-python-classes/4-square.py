#!/usr/bin/python3
"""Square model"""

class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size: length of a side of square
        """
        self.size = size

    @property
    def size(self):
        """property to determine the size of square

        Raises:
            TypeError: if the size is not int
            ValueError: if the size is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area of square
        Return:
            area of a square
        """
        return self.__size ** 2
