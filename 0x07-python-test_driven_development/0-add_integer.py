#!/user/bin/python3
""" Function to add two numbers"""

def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: first int
        b: second int, default value 98
    Raises:
        TypeError: if a, b are not int, float
    Returns:
        The sum of two int
    """
    if type(a) not in (int, float):
        raise TypeError('a must be integer')
    if type(b) not in (int, float):
        raise TypeError('b must be integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
