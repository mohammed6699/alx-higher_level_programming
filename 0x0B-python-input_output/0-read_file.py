#!/usr/bin/python3
""" File function to read a file"""


def read_file(filename=""):
    """Read the file by using utf-8"""

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
