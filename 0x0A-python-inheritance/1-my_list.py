#!/usr/bin/python3
"""Module for My list class"""

class MyList(list):
    "MyList class"""
    def print_sorted(self):
        """bublic instance method,print sorted list"""
        print(sorted(self))
