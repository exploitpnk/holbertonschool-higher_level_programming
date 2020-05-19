#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for item in range(0, x):
            print(my_list[item], end='')
        print('')
        return (x)
    except:
        print('')
        return (item)
