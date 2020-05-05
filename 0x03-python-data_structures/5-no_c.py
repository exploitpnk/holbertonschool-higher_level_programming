#!/usr/bin/python3
def no_c(my_string):
    listofchars = list(my_string)
    for char in listofchars:
        if char == 'c' or char == 'C':
            listofchars.remove(char)
    return("".join(listofchars))
