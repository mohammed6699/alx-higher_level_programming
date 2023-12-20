#!/user/bin/python3
"""square module"""

class Square:
    """Define a square"""

    def __init__(self, size = 0):
        """constructor

        Args:
            size: length os square side

        Raises:
            TypeError: If the size is not int
            ValueError: if the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
