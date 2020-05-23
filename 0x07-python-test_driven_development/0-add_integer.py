#!/usr/bin/python3
""" Return two integers """

def add_integer(a, b=98):
    """ add_integer adds two integers """
    if a is None or (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    try:
        return(int(a) + int(b))
    except Exception as e:
        raise e
