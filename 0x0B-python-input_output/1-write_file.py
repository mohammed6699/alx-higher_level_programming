#!/usr/bin/python3
""" Write and print the file content"""

def write_file(filename="", text=""):
    """write and read the file content"""
    with open(filename, 'w',  encoding='utf-8')as file:
        return (file.write(text))
