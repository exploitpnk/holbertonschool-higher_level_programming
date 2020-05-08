#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary, key=a_dictionary.get)
    else:
        max_value = None
    return(max_value)
