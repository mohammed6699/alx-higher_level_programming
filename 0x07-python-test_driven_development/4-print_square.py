#!/usr/bin/python3

"""The 4-print_square.py Module"""

def print_square(size):
    """ The print_square Module
        
        Args:
            size: length of the square (int)

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: size must be an integer
        """
        if not isinstance (size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')

        print(('#' * size + '\n') * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt')
