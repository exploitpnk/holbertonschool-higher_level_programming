#!/usr/bin/python3
for numbers in range(100):
    if (numbers == 99):
        print("{0:02}".format(numbers))
    else:
        print("{0:02}, ".format(numbers), end="")
