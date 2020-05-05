#!/usr/bin/python3
def element_at(my_list, idx):
    listlength = len(my_list) - 1
    if (idx < 0 or idx > listlength):
        return (None)
    else:
        return (my_list[idx])
