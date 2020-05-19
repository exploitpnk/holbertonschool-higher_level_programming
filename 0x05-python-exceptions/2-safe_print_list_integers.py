#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_values = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                printed_values += 1
        print()
        return (printed_values)
    except TypeError:
        print()
