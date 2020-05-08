#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = list(a_dictionary.keys())
    {a_dictionary.pop(key) for key in new_dic if a_dictionary[key] == value}
    return (a_dictionary)
