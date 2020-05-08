#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return([replace if number == search else number for number in my_list])
