#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_values = 0
    try:
        for item in range(0, x):
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end='')
                printed_values += 1
        print('')
        return(item)
    except TypeError:
        print('')
