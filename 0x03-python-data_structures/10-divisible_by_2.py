#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return (None)

    divition = []
    for i in my_list:
        if (i % 2) == 0:
            divition.append(True)
        else:
            divition.append(False)
    return (divition)
