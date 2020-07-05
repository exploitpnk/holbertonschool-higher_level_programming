#!/usr/bin/python3
""" Class Base will be the 'base' of all other classes """


class Base:
    """ This class will be the 'base' of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
