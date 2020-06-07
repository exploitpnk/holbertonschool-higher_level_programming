#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if type(attrs) == list:
            new_dic = {}
            for attribute in attrs:
                if attribute in self.__dict__:
                    new_dic[attribute] = self.__dict__[attribute]
            return new_dic
        else:
            return self.__dict__
