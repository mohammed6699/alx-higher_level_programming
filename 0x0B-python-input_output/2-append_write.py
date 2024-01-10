#!/usr/bin/python3
"""Define append mode"""

def append_write(filename="", text=""):
    """append text to the file"""
    with open(filename, 'a', encoding='utf-8')as file:
        return file.write(text)
