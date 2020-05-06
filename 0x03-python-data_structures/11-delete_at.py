#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length_list = len(my_list) - 1
    if idx < 0 or idx > length_list:
        return(my_list)
    else:
        del my_list[idx]
        return(my_list)
