#!/usr/bin/python3
"""Module for Text_indentation"""

def text_indentation(text):
    """
    Method for add 2 lines between sentences

    Args:
        text: string

    Raises:
        TypeError: when text is not str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ")
                for line in text.split(delim)])

    print(text, end="")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/5-text_indentation.py")
