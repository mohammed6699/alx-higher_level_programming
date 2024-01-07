#!/usr/bin/python3
"""Module for print '#' sign"""

def print_square(size):
    """Method foe printing '#' sign
    Args:
        size: int size of the square sign
    Raises:
        TypeError: if the size is not int
        ValueError: if the size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
print((('#' * size + "\n") * size), end="")

if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
