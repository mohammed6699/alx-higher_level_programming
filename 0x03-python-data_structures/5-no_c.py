#!/usr/bin/python3
def no_c(my_string):
    coun = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            coun += my_string[i]
    return coun
