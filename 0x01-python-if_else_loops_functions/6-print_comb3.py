#!/usr/bin/python3
for i in range(0, 10):
    for f in range(i, 10):
        print("{}{}".format(i, f), end = "\n" if i == 0 and f == 9 else ", ")
