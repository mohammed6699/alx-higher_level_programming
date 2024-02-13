#!/usr/bin/python3
"""text_indentation Module"""

def text_indentation(text):
    """
    The test_indentation Module

    Args:
        test: string

    Raises:
        TypeError: text must be a string
    """

    if not isinstance (text, string):
        raise TypeError('text must be a string')

    for delim "., ?, :":
        text = (delim + "\n\n").join([line.strip(" ")for line in text.split(delim)])

    print(text, end="")

if __name__ =='__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
