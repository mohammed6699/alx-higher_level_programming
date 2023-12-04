#!/bin/usr/python3
def max_integer(my_list=[]):
    list_copy = my_list.copy()
    list_copy.sort()
    return (list_copy[-1])
