#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        my_tuple = (len(sentence), None)
    my_tuple = (len(sentence), sentence[:1])
    return(my_tuple)
